## Github Update Checker
import TouchPortalAPI
import requests
import base64
from TPPEntry import PLUGIN_ID


PLUGIN_NAME = "Firebot Plugin"
GITHUB_USER_NAME = "GitagoGaming"
GITHUB_PLUGIN_NAME = "Firebot-Plugin---TouchPortal"

def plugin_update_check(plugin_version:str):
    """ Checks Github for the latest version of the plugin
    - Returns patchnotes on notification if there is a new version 
    """
    try:
        github_check = TouchPortalAPI.Tools.updateCheck(GITHUB_USER_NAME, GITHUB_PLUGIN_NAME)
      
        if github_check.replace('v','').replace(".","") > plugin_version:
            ### Pulling Patch Notes for Notification
            try:
                r = requests.get(f"https://api.github.com/repos/{GITHUB_USER_NAME}/{GITHUB_PLUGIN_NAME}/contents/recent_patchnotes.txt")
                
                if r.status_code == 404:
                    print("No Patch Notes Found")
                    message = ""
                else:
                    base64_bytes = r.json()['content'].encode('ascii')
                    message_bytes = base64.b64decode(base64_bytes)
                    message = message_bytes.decode('ascii')
            except Exception as e:
                message = ""
                print("Error Plugin Update Check: ", e)
            return github_check, message
        else:
            return False, False
        
    except Exception as e:
        print("Something went wrong checking update", e)
        
        
        
        
        
################################ FOR FUTURE REFERENCE ################################
        
### MAIN.PY would include this

#   and in onConnect you would have
#         ## Checking for Updates
#        github_check, message = plugin_update_check()
#        if github_check == True:
#            plugin.showNotification(
#                notificationId= f"{PLUGIN_ID}.TP.Plugins.Update_Check",
#                title=f"{PLUGIN_NAME} {github_check} is available",
#                msg=f"A new version of {PLUGIN_NAME} is available and ready to Download. This may include Bug Fixes and or New Features\n\nPatch Notes\n{message} ",
#                options= [{
#                "id":f"{PLUGIN_ID}.tp.update.download",
#                "title":"Click to Update!"
#            }])


#   def onNoticationClicked(data):
#       if data['optionId'] == f'{PLUGIN_ID}.tp.update.download':
#           github_check = TouchPortalAPI.Tools.updateCheck(GITHUB_USER_NAME, GITHUB_PLUGIN_NAME)
#           url = f"https://github.com/{GITHUB_USER_NAME}/{GITHUB_PLUGIN_NAME}/releases/tag/{github_check}"
#           webbrowser.open(url, new=0, autoraise=True)
