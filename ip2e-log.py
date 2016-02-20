#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# --------------------------------------------------------------
# ip2e (IP to email) - See the log file.                       |
# Created by clamsawd (clamsawd@openmailbox.org)               |
# Licensed by GPL v.3                                          |
# Last update: 20-02-2016                                      |
#                                                              |
# Compatible with Python 3.x                                   |
# --------------------------------------------------------------
version="1.3.2"

#Import python-modules
import os
import sys

#Check if your system use Python 3.x
if sys.version_info<(3,0):
	print ("")
	print ("You need python 3.x to run this program.")
	print ("")
	exit()

#Function to clear screen
def ClearScreen():
	if sys.platform == "cygwin":
		print (300 * "\n")
	elif os.name == "posix":
		os.system("clear")
	elif os.name == "nt":
		os.system("cls")
	else:
		print ("Error: Unable clear screen")
		
#Detect system & PATH of user folder
if os.path.exists("/storage/sdcard0"):
	HOMESCARD0="/storage/sdcard0/Android/data"
	os.chdir(HOMESCARD0)
	print ("Android (Posix) detected")
elif os.name == "posix":
	os.chdir(os.environ["HOME"])
	print ("Unix (Posix) detected")
elif os.name == "nt":
	os.chdir(os.environ["USERPROFILE"])
	print ("Windows detected")

if not os.path.exists(".ip2e"):
	os.makedirs(".ip2e")
	os.chdir(".ip2e")
if os.path.exists(".ip2e"):
	os.chdir(".ip2e")

#See the log file
if os.path.isfile("ip2e.log"):
	print ("ip2e.log exists")
	ClearScreen()
	readfile=open('ip2e.log', 'r')
	print(readfile.read())
	readfile.close()
else:
	ClearScreen()
	print ("")
	print ("* ip2e.log doesn't exist.")
	print ("")
