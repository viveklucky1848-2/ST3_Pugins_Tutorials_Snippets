#!C:\Python27\python.exe

import sublime, sublime_plugin, random, types, re, os, sys, imp, subprocess
# Set Base Path to Plugin's directory
PLUGIN_BASE_PATH = BASE_PATH = os.path.abspath(os.path.dirname(__file__))
# Get Windows User folder
WIN_USER_PATH = BASE_PATH.split('\AppData', 1)[0]
# Get ST3 Packages path
ST3_PKG_PATH = BASE_PATH.rsplit('\\',1)[0]
# Expand Windows Environment Variables
# sublime.message_dialog(os.path.expandvars('%Appdata%'))
TEST_WIN_PATH = os.path.expandvars('%Appdata%')
ST_PROJ_PATH = os.path.expandvars('%Userprofile%') + '\\Projects\\simple'
# subprocess.Popen('explorer '+TEST_WIN_PATH)

class TestSublimeTextPluginCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        filePath = self.view.file_name()
        dirPath = os.path.dirname(filePath)
        fileName = os.path.basename(self.view.file_name())
        fileNamePrefix = fileName.rsplit('.')[0]
        fileNameExt = fileName.rsplit('.')[1]
        sublimeFuncs = dir(sublime)
        output = '\n'.join(sublimeFuncs)
        # sublime.message_dialog("Vivek")
        # sublime.status_message('Shah')
        # sublime.set_clipboard(output)
        subprocess.Popen('explorer '+ST_PROJ_PATH)
