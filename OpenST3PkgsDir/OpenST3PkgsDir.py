#!C:\Python27\python.exe

import sublime, sublime_plugin, random, types, re, os, sys, imp, subprocess
ST3_PKGs_PATH = os.path.expandvars('%AppData%') + "\\Sublime Text 3\\Packages"

class OpenST3PkgsDirCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        subprocess.Popen('explorer '+ST3_PKGs_PATH+'\\User')
        subprocess.Popen('explorer '+ST3_PKGs_PATH)