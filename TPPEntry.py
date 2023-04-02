__version__ = "1.1"

PLUGIN_ID = "firebot.plugin"


TP_PLUGIN_INFO = {
    "sdk": 6,
    "version": int(float(__version__) * 100),  # TP only recognizes integer version numbers
    "name": "Firebot Plugin",
    "id": PLUGIN_ID,
    # Startup command, with default logging options read from configuration file (see main() for details)
    "plugin_start_cmd": r"%TP_PLUGIN_FOLDER%Firebot_Plugin\\firebot_plugin.exe @plugin_config.txt",
    "configuration": {
        "colorDark": "#25274c",
        "colorLight": "#707ab5"
    },
 #   "doc": {
 #       "repository": "Your-Rep-Name",
 #       "Install": "example install instruction",
 #       "description": "example description"
 #   }
}


TP_PLUGIN_SETTINGS = {
   # "example": {
   #     "name": "Example Setting",
   #     # "text" is the default type and could be omitted here
   #     "type": "text",
   #     "default": "Example value",
   #     "readOnly": False,  # this is also the default
   #     "doc": "example doc for example setting",
   #     "value": None  # we can optionally use the settings struct to hold the current value
   # },
}


TP_PLUGIN_CATEGORIES = {
    "main": {
        "id": PLUGIN_ID + ".main",
        "name" : "FireBot",
         "imagepath" : "%TP_PLUGIN_FOLDER%Firebot_Plugin\\firebot_plugin.png"
    }
}


TP_PLUGIN_ACTIONS = {
    "Retrieve All Variables": {
        "category": "main",
        "id": PLUGIN_ID + ".act.GetAllVariables",
        "name": "Retrieve All Variables",
        "prefix": TP_PLUGIN_CATEGORIES["main"]["name"],
        "type": "communicate",
        "tryInline": True,
        "doc": "Retrieve all of variables stored in firebots database",
       # "description": "Returns all variables stored in firebots database",
        "format": "Returns all variables stored in firebots database - Creates States for each variable",
        "data": {  }
    },
    
    "Get Variable Value": {
        "category": "main",
        "id": PLUGIN_ID + ".act.GetVariableValue",
        "name": "Get Value for Variable",
        "prefix": TP_PLUGIN_CATEGORIES["main"]["name"],
        "type": "communicate",
        "tryInline": True,
        "doc": "Retrieve the value of a variable stored in firebots database",
        "description": "Returns the value of a variable stored in firebots database",
        "format": "Get value for the variable $[1] and store it in $[2]",
        "data": {
            "Variable Name": {
                "id": PLUGIN_ID + ".act.GetVariableValue.name",
                "type": "text",
                "label": "Text",
                "default": ""
            },
            "Variable TP State": {
                "id": PLUGIN_ID + ".act.GetVariableValue.state",
                "type": "text",
                "label": "Text",
                "default": ""
            }
        }
    },
        
    "Set Variable Value": {
        "category": "main",
        "id": PLUGIN_ID + ".act.SetVariableValue",
        "name": "Set Value for Variable",
        "prefix": TP_PLUGIN_CATEGORIES["main"]["name"],
        "type": "communicate",
        "tryInline": True,
        "doc": "Set the value of a variable stored in firebots database",
        "description": "Sets the value of a variable stored in firebots database",
        "format": "Set value for the variable $[1] to $[2]",
        "data": {
            "SetVariableValue name": {
                "id": PLUGIN_ID + ".act.SetVariableValue.name",
                "type": "text",
                "label": "Text",
                "default": ""
            },
            "SetVariableValue Value": {
                "id": PLUGIN_ID + ".act.SetVariableValue.value",
                "type": "text",
                "label": "Text",
                "default": ""
            }
        }
    },
    
    "Get Top Currency": {
        "category": "main",
        "id": PLUGIN_ID + ".act.Currency.GetTop",
        "name": "Get Top Currency",
        "prefix": TP_PLUGIN_CATEGORIES["main"]["name"],
        "type": "communicate",
        "tryInline": True,
        "doc": "Gets Top Currency",
        "description": "Gets Top Currency for User",
        "format": "Get Currency for $[1] from top $[2]",
        "data": {
            "Currency Name": {
                "id": PLUGIN_ID + ".act.Currency.GetTop.name",
                "type": "text",
                "label": "Text",
                "default": ""
            },
            "Amount": {
                "id": PLUGIN_ID + ".act.Currency.GetTop.amount",
                "type": "text",
                "label": "Text",
                "default": ""
            }
        }
    },
    
    "Get User Currency": {
        "category": "main",
        "id": PLUGIN_ID + ".act.Currency.GetUser",
        "name": "Get Currency from User",
        "prefix": TP_PLUGIN_CATEGORIES["main"]["name"],
        "type": "communicate",
        "tryInline": True,
        "doc": "Gets Currency from a User",
        "description": "Gets Currency from a User",
        "format": "Get Currency for User:$[2] and Currency:$[1]",
        "data": {
            "Currency Name": {
                "id": PLUGIN_ID + ".act.Currency.Get.name",
                "type": "text",
                "label": "Text",
                "default": ""
            },
            "User Name": {
                "id": PLUGIN_ID + ".act.Currency.Get.username",
                "type": "text",
                "label": "Text",
                "default": ""
            }
        }
    },
    
    
    "Set Currency": {
        "category": "main",
        "id": PLUGIN_ID + ".act.Currency.Set",
        "name": "Set Currency for User",
        "prefix": TP_PLUGIN_CATEGORIES["main"]["name"],
        "type": "communicate",
        "tryInline": True,
        "doc": "Sets Currency for a User",
        "description": "Sets Currency for a User",
        "format": "Set Currency for User:$[3] and Currency:$[1] to $[2]",
        "data": {
            "Currency Name": {
                "id": PLUGIN_ID + ".act.Currency.Set.name",
                "type": "text",
                "label": "Text",
                "default": ""
            },
            "Amount": {
                "id": PLUGIN_ID + ".act.Currency.Set.amount",
                "type": "text",
                "label": "Text",
                "default": ""
            },
            "User Name": {
                "id": PLUGIN_ID + ".act.Currency.Set.username",
                "type": "text",
                "label": "Text",
                "default": ""
            }
        }
    },
    
    "Subtract Currency": {
        "category": "main",
        "id": PLUGIN_ID + ".act.Currency.Subtract",
        "name": "Subtract Currency from User",
        "prefix": TP_PLUGIN_CATEGORIES["main"]["name"],
        "type": "communicate",
        "tryInline": True,
        "doc": "Subtracts Currency from a User",
        "description": "Subtracts Currency from a User",
        "format": "Subtract Currency for User:$[3] and Currency:$[1] by $[2]",
        "data": {
            "Currency Name": {
                "id": PLUGIN_ID + ".act.Currency.Subtract.name",
                "type": "text",
                "label": "Text",
                "default": ""
            },
            "Amount": {
                "id": PLUGIN_ID + ".act.Currency.Subtract.amount",
                "type": "text",
                "label": "Text",
                "default": ""
            },
            "User Name": {
                "id": PLUGIN_ID + ".act.Currency.Subtract.username",
                "type": "text",
                "label": "Text",
                "default": ""
            }
        }
    },
    
    "Add Currency": {
        "category": "main",
        "id": PLUGIN_ID + ".act.Currency.Add",
        "name": "Add Currency to User",
        "prefix": TP_PLUGIN_CATEGORIES["main"]["name"],
        "type": "communicate",
        "tryInline": True,
        "doc": "Adds Currency to a User",
        "description": "Adds Currency to a User",
        "format": "Add Currency for User:$[3] and Currency:$[1] by $[2]",
        "data": {
            "Currency Name": {
                "id": PLUGIN_ID + ".act.Currency.Add.name",
                "type": "text",
                "label": "Text",
                "default": ""
            },
            "Amount": {
                "id": PLUGIN_ID + ".act.Currency.Add.amount",
                "type": "text",
                "label": "Text",
                "default": ""
            },
            "User Name": {
                "id": PLUGIN_ID + ".act.Currency.Add.username",
                "type": "text",
                "label": "Text",
                "default": ""
            }
        }
    },
    
    "Add Currency Online": {
        "category": "main",
        "id": PLUGIN_ID + ".act.Currency.AddOnline",
        "name": "Add Currency to Online Users",
        "prefix": TP_PLUGIN_CATEGORIES["main"]["name"],
        "type": "communicate",
        "tryInline": True,
        "doc": "Adds Currency to Online Users",
        "description": "Adds Currency to Online Users",
        "format": "Add Currency for all Online Users:Currency:$[1] by $[2]",
        "data": {
            "Currency Name": {
                "id": PLUGIN_ID + ".act.Currency.AddOnline.name",
                "type": "text",
                "label": "Text",
                "default": ""
            },
            "Amount": {
                "id": PLUGIN_ID + ".act.Currency.AddOnline.amount",
                "type": "text",
                "label": "Text",
                "default": ""
            }
        }
    },
    
    "Remove Currency Online": {
        "category": "main",
        "id": PLUGIN_ID + ".act.Currency.RemoveOnline",
        "name": "Remove Currency from Online Users",
        "prefix": TP_PLUGIN_CATEGORIES["main"]["name"],
        "type": "communicate",
        "tryInline": True,
        "doc": "Removes Currency from Online Users",
        "description": "Removes Currency from Online Users",
        "format": "Remove Currency for all Online Users:Currency:$[1] by $[2]",
        "data": {
            "Currency Name": {
                "id": PLUGIN_ID + ".act.Currency.RemoveOnline.name",
                "type": "text",
                "label": "Text",
                "default": ""
            },
            "Amount": {
                "id": PLUGIN_ID + ".act.Currency.RemoveOnline.amount",
                "type": "text",
                "label": "Text",
                "default": ""
            }
        }
    },
    
    "Counter Increase/Decrease/Set": {
        "category": "main",
        "id": PLUGIN_ID + ".act.Counters",
        "name": "Increase/Decrease/Set a Counter",
        "prefix": TP_PLUGIN_CATEGORIES["main"]["name"],
        "type": "communicate",
        "tryInline": True,
        "doc": "Allows you to manipulate a counter for a specific variable",
        "format": "$[1] Counter:$[2] by $[3]",
        "data": {
            "Choice": {
                "id": PLUGIN_ID + ".act.Counters.Choice",
                "type": "choice",
                "label": "Text",
                "default": "",
                "valueChoices": [
                    "Increase",
                    "Decrease",
                    "Set"
                ]
            },
            "CounterName": {
                "id": PLUGIN_ID + ".act.Counters.name",
                "type": "text",
                "label": "Text",
                "default": "5"
            },
            "Amount to Set/Increase/Decrease": {
                "id": PLUGIN_ID + ".act.Counters.amount",
                "type": "text",
                "label": "Text",
                "default": "5"
            }
        }
    },
    
    "Get Counter Value": {
        "category": "main",
        "id": PLUGIN_ID + ".act.GetCounterValue",
        "name": "Get Counter Value",
        "prefix": TP_PLUGIN_CATEGORIES["main"]["name"],
        "type": "communicate",
        "tryInline": True,
        "doc": "Retrieve a Counter Value",
        "description": "Counter Name will be used to make a variable within TouchPortal to store",
        "format": "Get Value for $[1]",
        "data": {
            "CounterValue Name": {
                "id": PLUGIN_ID + ".act.GetCounterValue.name",
                "type": "text",
                "label": "Text",
                "default": ""
            }
        }
    },
 # "Get Counter ID": {
 #     "category": "main",
 #     "id": PLUGIN_ID + ".act.GetCounterID",
 #     "name": "Get Counter ID",
 #     "prefix": TP_PLUGIN_CATEGORIES["main"]["name"],
 #     "type": "communicate",
 #     "tryInline": True,
 #     "doc": "Retrieve a Counter ID",
 #     "description": "Counter Name will be used to make a variable within TouchPortal to store",
 #     "format": "Get Counter ID for $[1] and store it in $[2]",
 #     "data": {
 #         "CounterValue Name": {
 #             "id": PLUGIN_ID + ".act.GetCounterID.name",
 #             "type": "text",
 #             "label": "Text",
 #             "default": ""
 #         },
 #         "CounterValue Name": {
 #             "id": PLUGIN_ID + ".act.GetCounterID.varname",
 #             "type": "text",
 #             "label": "Text",
 #             "default": ""
 #         }
 #         
 #     }
 # },
    "Firworks / Confetti": {
        "category": "main",
        "id": PLUGIN_ID + ".act.effects",
        "name": "Activate Confetti / Fireworks",
        "prefix": TP_PLUGIN_CATEGORIES["main"]["name"],
        "type": "communicate",
        "tryInline": True,
        "doc": "Activate Confetti / Fireworks",
        "description": "Default duration is 6 seconds",
        "format": "Activate $[1] for $[2] seconds",
        "data": {
            "Choice": {
                "id": PLUGIN_ID + ".act.effects.Choice",
                "type": "choice",
                "label": "Text",
                "default": "",
                "valueChoices": [
                    "Confetti",
                    "Fireworks",
                ]
            },
            "Effect Duration": {
                "id": PLUGIN_ID + ".act.effects.duration",
                "type": "text",
                "label": "Text",
                "default": "5"
            }
        }
    },
    
    "Text to Speech": {
        "category": "main",
        "id": PLUGIN_ID + ".act.TTS",
        "name": "Text to Speech",
        "prefix": TP_PLUGIN_CATEGORIES["main"]["name"],
        "type": "communicate",
        "tryInline": True,
        "doc": "Text to Speech",
        "description": "Convert Text to Speech",
        "format": "Text to Speech: $[1]",
        "data": {
            "TTS Text": {
                "id": PLUGIN_ID + ".act.TTS.text",
                "type": "text",
                "label": "Text",
                "default": "Hello World!"
            }
        }
    },
    
    "Disable / Enable / Reset Timer": {
        "category": "main",
        "id": PLUGIN_ID + ".act.timer",
        "name": "Disable / Enable / Reset Timer",
        "prefix": TP_PLUGIN_CATEGORIES["main"]["name"],
        "type": "communicate",
        "tryInline": True,
        "doc": "Disable / Enable / Reset Timer",
        "description": "Manage a Timer",
        "format": "$[1] the timer for Timer-Name:$[2] ",
        "data": {
            "Choice": {
                "id": PLUGIN_ID + ".act.timer.Choice",
                "type": "choice",
                "label": "Text",
                "default": "",
                "valueChoices": [
                    "Enable",
                    "Disable",
                    "Reset"
                ]
            },
            "Timer Name": {
                "id": PLUGIN_ID + ".act.timer.Name",
                "type": "text",
                "label": "Text",
                "default": ""
            }
        }
    },
    
    
    
}

TP_PLUGIN_CONNECTORS = {}

# Plugin static state(s). These are listed in the entry.tp file,
# vs. dynamic states which would be created/removed at runtime.
TP_PLUGIN_STATES = {
 #  "text": {
 #      # "category" is optional, if omitted then this state will be added to all, or the only, category(ies)
 #      "category": "main",
 #      "id": PLUGIN_ID + ".state.text",
 #      # "text" is the default type and could be omitted here
 #      "type": "text",
 #      "desc": "Example State Text",
 #      "doc": "example doc",
 #      # we can conveniently use a value here which we already defined above
 #      "default": TP_PLUGIN_ACTIONS["example"]["data"]["text"]["default"]
 #  },
 #  "color": {
 #      "id": PLUGIN_ID + ".state.color",
 #      "desc": "Example State Color",
 #      "default": TP_PLUGIN_ACTIONS["example"]["data"]["color"]["default"]
 #  },
}

# Plugin Event(s).
TP_PLUGIN_EVENTS = {}