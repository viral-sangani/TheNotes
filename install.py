#!/usr/bin/python3
import os
import subprocess

os.system("sudo snap install mdless")
os.system("echo '<<<<<<<<<<<<<< mdless installed >>>>>>>>>>>>>>>' ")

alias = "alias hint=\'python ~/TheNotes/.hint.py\'"
s = subprocess.check_output("echo $SHELL", shell = True)
if 'zsh' in str(s):
	os.system("echo \"" + alias + "\" >> ~/.zshrc")
	os.system("echo \"Please run \'source ~/.zshrc\'\"")

else:
	os.system("echo \"" + alias + "\" >> ~/.bashrc")
	os.system("bash source_bash.sh")
