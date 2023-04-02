from TouchPortalAPI import tppbuild
from sys import platform
import TPPEntry

PLUGIN_MAIN = "main.py"

PLUGIN_EXE_NAME = "firebot_plugin"

PLUGIN_EXE_ICON = r"firebot_plugin.png"

PLUGIN_ENTRY = "TPPEntry.py"


PLUGIN_ENTRY_INDENT = 2


PLUGIN_ROOT = "Firebot_Plugin"
""" This is the root folder name that will be inside of .tpp """

PLUGIN_ICON = r"firebot_plugin.png"
""" Path to icon file used in entry.tp for category `imagepath`, if any. If left blank, TP will use a default icon. """

OUTPUT_PATH = r"./"
""" This tells tppbuild where you want finished build tpp to be saved at. Default "./" meaning current dir where tppbuild is running from. """

""" PLUGIN_VERSION: A version string for the generated .tpp file name. This example reads the `__version__` from the example plugin's code. """
PLUGIN_VERSION = TPPEntry.__version__
# If you only wants to use TP entry.tp version you can use the code blow this code will read entry.tp and grab its version.
"""
import json
import os
entry = os.path.join(os.path.split(__file__)[0], PLUGIN_ENTRY)
with open(entry, "r") as f:
    PLUGIN_VERSION = str(json.load(f)['version'])
"""
# Or just set the PLUGIN_VERSION manually.
# PLUGIN_VERSION = "1.0.0-beta1"

"""
If you have any required file(s) that your plugin needs, put them in this list.
"""
ADDITIONAL_FILES = []

"""
start.sh file is not needed for Windows machine. as it can execute the exe itself where as
Mac and Linux requires to run `chmod +x program` in order to run it.
"""
# if platform != "win32":
#     ADDITIONAL_FILES.append("start.sh")

"""
Any additional arguments to be passed to Pyinstaller. Optional.
"""
ADDITIONAL_PYINSTALLER_ARGS = [
    "--log-level=WARN"
]

"""
Any additional TPPSDK Arguments can be passed here
"""
ADDITINAL_TPPSDK_ARGS = []
# validateBuild()

if __name__ == "__main__":
    tppbuild.runBuild()
