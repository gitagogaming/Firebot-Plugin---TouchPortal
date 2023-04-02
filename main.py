"""
Firebot TouchPortal Plugin
"""


## pyinstaller --add-data "plugin_config.txt;." --onefile main.py --name firebot_plugin.exe


import TPPEntry
import TouchPortalAPI
from TouchPortalAPI import TYPES
from TouchPortalAPI.logger import Logger

import os
from threading import Thread
from sys import exit
import configparser

import firebotpy
from TPPEntry import PLUGIN_ID
from update_check import plugin_update_check, GITHUB_PLUGIN_NAME, GITHUB_USER_NAME, PLUGIN_NAME
import webbrowser


class ClientInterface(TouchPortalAPI.Client):
    def __init__(self):
        super().__init__(self)
        
        self.pluginId = TPPEntry.PLUGIN_ID
        self.configFile = self.ParseConfig("plugin_config.txt")
        
        # TP connection settings - These can be left at default
        self.TPHOST = self.configFile["TP CONFIG"]["tphost"]
        self.TPPORT = int(self.configFile["TP CONFIG"]["tpport"])

        self.RCV_BUFFER_SZ = int(self.configFile["TP CONFIG"]["rcv_buffer_sz"]) # Incoming data buffer size
        self.SND_BUFFER_SZ = int(self.configFile["TP CONFIG"]["snd_buffer_sz"]) # maximum size of send data buffer ( 1MB )

        # Log settings
        self.logLevel = self.configFile["LOGGING"]["loglevel"]
        self.setLogFile(self.configFile["LOGGING"]["logname"])
    

        # Register events
        self.add_listener(TYPES.onConnect, self.onConnect)
        self.add_listener(TYPES.onAction, self.onAction)
        self.add_listener(TYPES.onShutdown, self.onShutdown)
        self.add_listener(TYPES.onListChange, self.onListChange)
        self.add_listener(TYPES.onNotificationOptionClicked, self.onNoticationClicked)
        
    
    """
    Custom Method/Functions
    """
    def settingsToDict(self, settings):
        # Converts from [{"setting1": "value"}, {"setting1": "value"}] to {"Setting1": "value", "Setting2": "value"}
        return { list(settings[i])[0] : list(settings[i].values())[0] for i in range(len(settings)) }


    def ParseConfig(self, file):
        config = configparser.ConfigParser()
        config.read(os.path.join(os.path.dirname(os.path.realpath(__file__)), file))
        return {s:dict(config.items(s)) for s in config.sections()}

    def onNoticationClicked(data):
        if data['optionId'] == f'{PLUGIN_ID}.tp.update.download':
            github_check = TouchPortalAPI.Tools.updateCheck(GITHUB_USER_NAME, GITHUB_PLUGIN_NAME)
            url = f"https://github.com/{GITHUB_USER_NAME}/{GITHUB_PLUGIN_NAME}/releases/tag/{github_check}"
            webbrowser.open(url, new=0, autoraise=True)

    """
    Events
    """
    def onConnect(self, data):
        self.log.info(f"Connected to TP v{data.get('tpVersionString', '?')}, plugin v{data.get('pluginVersion', '?')}.")
        self.log.debug(f"Connection: {data}")
        print(self.ParseConfig("config.ini"))
        
        
                ## Checking for Updates
        try:
            github_check, message = plugin_update_check(str(data['pluginVersion']))
            if github_check == True:
                plugin.showNotification(
                    notificationId= f"{PLUGIN_ID}.TP.Plugins.Update_Check",
                    title=f"{PLUGIN_NAME} {github_check} is available",
                    msg=f"A new version of {PLUGIN_NAME} is available and ready to Download.\nThis may include Bug Fixes and or New Features\n\nPatch Notes\n{message} ",
                    options= [{
                    "id":f"{PLUGIN_ID}.tp.update.download",
                    "title":"Click to Update!"
                }])
        except:
            print("Error Checking for Updates")


    def onSettings(self, data):
        self.log.debug(f"Connection: {data}")


    def onAction(self, data):
        self.log.debug(f"Connection: {data}")
        
        if not (action_data := data.get('data')) or not (aid := data.get('actionId')):
            return
        
        print(aid)
        ### Counters
        if aid == PLUGIN_ID + '.act.Counters':
            if data['data'][0]['value'] == "Increase":
                fire.increaseCounter(data['data'][1]['value'], data['data'][2]['value'])
            if data['data'][0]['value'] == "Decrease":
                fire.increaseCounter(data['data'][1]['value'], f"-{data['data'][2]['value']}")
            if data['data'][0]['value'] == "Set":
                fire.setCounter(data['data'][1]['value'], data['data'][2]['value'])
            
            ## Fetch new Counter value
            counter_value = fire.getCounterValue(data['data'][2]['value'])
            plugin.createState(f"{PLUGIN_ID}.state.counter.{data['data'][1]['value']}", f"FireBot | Counter Value {data['data'][0]['value']}", str(counter_value), f"Counter Values")
        
        
        if aid == PLUGIN_ID + '.act.GetCounterValue':
            counter_value = fire.getCounterValue(data['data'][0]['value'])
                            
            plugin.createState(stateId=f"{PLUGIN_ID}.state.CounterValue.{data['data'][0]['value']}", 
                                description= f"FireBot | Counter Value {data['data'][0]['value']}",
                                value = str(counter_value),
                                parentGroup = f"Counter Values")
           # print(counter_value)
        
        
        
        ### Currency Actions
        if aid == PLUGIN_ID + '.act.Currency.GetTop':
            #Top_Currency_Users
            tcu = fire.getTopCurrency(data['data'][0]['value'], data['data'][1]['value'])
            
            for indx, x in enumerate(tcu, 1):
                plugin.createState(f"{PLUGIN_ID}.state.Current.Top{data['data'][1]['value']}.{indx}.username", 
                                   f"FireBot | Top Currency {indx} - Username", 
                                   str(x['username']),
                                   f"Top Currency: {indx}")
                
                plugin.createState(stateId=f"{PLUGIN_ID}.state.Current.Top{data['data'][1]['value']}.{indx}.amount", 
                                   description= f"FireBot | Top Currency {indx} - Amount",
                                   value = str(x['amount']),
                                   parentGroup = f"Top Currency: {indx}")
                indx += 1
            
        if aid == PLUGIN_ID + '.act.Currency.Add':
            fire.addCurrency(data['data'][0]['value'], data['data'][1]['value'], data['data'][2]['value'])
            
        if aid == PLUGIN_ID + '.act.Currency.Subtract':
            fire.subtractCurrency(data['data'][0]['value'], data['data'][1]['value'], data['data'][2]['value'])
            
        if aid == PLUGIN_ID + ".act.Currency.Set":
            fire.setUserCurrency(data['data'][0]['value'], data['data'][1]['value'], data['data'][2]['value'])
            
        if aid == PLUGIN_ID + '.act.Currency.Get':
            user_currency = fire.getUserCurrency(user = data['data'][1]['value'], currency=data['data'][0]['value'])                
            plugin.createState(stateId=f"{PLUGIN_ID}.state.GetUserCurrency.amount", 
                             description= f"FireBot | Get User Currency - Amount ",
                             value = f"{data['data'][1]['value']}: {str(user_currency)}")
                             #arentGroup = f"Top Currency: {indx}")
            
        if aid == PLUGIN_ID + '.act.Currency.AddOnline':
            fire.addCurrencyOnline(data['data'][0]['value'], data['data'][1]['value'])
            
        if aid == PLUGIN_ID + '.act.Currency.RemoveOnline':
            fire.removeCurrencyOnline(data['data'][0]['value'], f"-{data['data'][1]['value']}")
            
            
        if aid == PLUGIN_ID + '.act.effects':
            if data['data'][0]['value'] == "Fireworks":
                fire.fireworks(data['data'][1]['value'])
                
            if data['data'][0]['value'] == "Confetti":
                fire.confetti(data['data'][1]['value'])
            
            
        if aid == PLUGIN_ID + '.act.timer':
            if data['data'][0]['value'] == "Enable":
                fire.enableTimer(data['data'][1]['value'])
            if data['data'][0]['value'] == "Disable":
                fire.disableTimer(data['data'][1]['value'])
            if data['data'][0]['value'] == "Reset":
                fire.resetTimer(data['data'][1]['value'])
            
       # if aid == PLUGIN_ID + '.act.TTS':
       #     fire.textToSpeech(data['data'][0]['value'])
            
        if aid == PLUGIN_ID + '.act.GetVariableValue':
            answer = fire.getVariable(data['data'][0]['value'])
            plugin.createState(stateId=f"{PLUGIN_ID}.state.GetVariableValue", description= f"Variable Value: {data['data'][0]['value']} ", value= str(answer), parentGroup = f"Variable Values")
            
        if aid == PLUGIN_ID + '.act.SetVariableValue':
            fire.customVariable(data['data'][0]['value'], data['data'][1]['value'])
            plugin.createState(stateId=f"{PLUGIN_ID}.state.GetVariableValue", description= f"Variable Value: {data['data'][0]['value']} ", value= str(data['data'][1]['value']), parentGroup = f"Variable Values")
            
        if  aid == PLUGIN_ID + '.act.GetAllVariables':
            answer = fire.getAllVariables()
            ## example response = {'TestVar1': {'t': 0, 'v': 'Data Test'}, 'TestVar12': {'t': 0, 'v': 'Data Test'}}
            for x in answer:
                plugin.createState(stateId=f"{PLUGIN_ID}.state.GetVariableValue", description= f"Variable Value: {x}", value= str(answer[x]['v']), parentGroup = "Variable Values")

           #answer = fire.getAllVariables()
           #print(answer)

    ## When a Choice List is Changed in a Button Action
    def onListChange(self, data):
        self.log.debug(f"Connection: {data}")


    def onShutdown(self, data):
        self.log.info('Received shutdown event from TP Client.')
        self.disconnect()
        


 #   def onError(self, data):
 #       self.error(f'Error in TP Client event handler: {repr(data)}')





plugin = ClientInterface()
ret = 0
try:
    fire = firebotpy.Firebot()
    plugin.connect()
except KeyboardInterrupt:
    plugin.log.warning("Caught keyboard interrupt, exiting.")
except Exception:
    from traceback import format_exc
    plugin.log.error(f"Exception in TP Client:\n{format_exc()}")
    ret = -1
finally:
    plugin.disconnect()
    del plugin
    exit(ret)

