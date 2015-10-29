#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# --------------------------------------------------------------
# ip2e (IP to email) - See the log file.                       |
# Created by clamsawd (clamsawd@openmailbox.org)               |
# Licensed by GPL v.3                                          |
# Last update: 29-10-2015                                      |
#                                                              |
# Dependences: curl, wget, sendEmail, libio-socket-ssl-perl    |
# Compatible with Python 3.x                                   |
# --------------------------------------------------------------
version="0.7-beta"

#Import python-modules
import os
import sys

#Check if your system use Python 3.x
if sys.version_info<(3,0):
	print ("")
	print ("You need python 3.x to run this program.")
	print ("")
	exit(1)

#Function to clear screen
def ClearScreen():
	if os.name == "posix":
		os.system("clear")
	elif os.name == "nt":
		os.system("cls")
	else:
		print ("Error: Unable clear screen")
		
#Detect system & PATH of user folder
if os.name == "posix":
	os.chdir(os.environ["HOME"])
	print ("POSIX detected")
elif os.name == "nt":
	os.chdir(os.environ["USERPROFILE"])
	print ("Windows detected")

if not os.path.exists(".ip2e"):
	os.makedirs(".ip2e")
	os.chdir(".ip2e")
if os.path.exists(".ip2e"):
	os.chdir(".ip2e")

#Check if exists 'ip2e-conf.py'
def createip2ecf():
	ip2ecf=open('ip2e-conf.py','w')
	ip2ecf.close()
def writeip2ecf():
	ip2ecf=open('ip2e-conf.py','a')
	ip2ecf.write('# sample configuration file of ip2e\n')
	ip2ecf.write('\n')
	ip2ecf.write('FromEmail="ip2e@daemon"\n')
	ip2ecf.write('FromEmailUser="unknown"\n')
	ip2ecf.write('FromEmailPass="password-here"\n')
	ip2ecf.write('SmtpFromEmail="smtp.email.com"\n')
	ip2ecf.write('ToEmail="unknown@email.com"\n')
	ip2ecf.close()

if os.path.isfile("ip2e-conf.py"):
	print ("ip2e-conf.py exists")
else:
	print ("ip2e-conf.py created")
	createip2ecf()
	writeip2ecf()

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
	print ("ip2e.log doesn't exist.")
	print ("")
