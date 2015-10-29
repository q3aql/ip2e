#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# --------------------------------------------------------------
# ip2e (IP to email) - Run ip2e daemon.                        |
# Created by clamsawd (clamsawd@openmailbox.org)               |
# Licensed by GPL v.3                                          |
# Last update: 29-10-2015                                      |
#                                                              |
# Dependences: curl, wget, sendEmail, libio-socket-ssl-perl    |
# Compatible with Python 3.x                                   |
# --------------------------------------------------------------
version="0.6-alpha"

#Import python-modules
import subprocess
import os
import sys
import time

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

#Function to pause screen
def PauseScreen():
	if os.name == "posix":
		os.system("read pause")
	elif os.name == "nt":
		os.system("pause > nul")
				
#Function to wait ten minutes
def WaitTenMinutes():
	if os.name == "posix":
		os.system("sleep 600")
	elif os.name == "nt":
		os.system("ping -n 600 localhost>nul")
	else:
		print ("Error waiting 10 minutes")
		
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

#Check if exists 'current-ip.py'
def createip2eIPcf():
	ip2eIPcf=open('current-ip.py','w')
	ip2eIPcf.close()
def writeip2eIPcf():
	ip2eIPcf=open('current-ip.py','a')
	ip2eIPcf.write('CurrentIP="0.0.0.0"\n')
	ip2eIPcf.close()
	
if os.path.isfile("current-ip.py"):
	print ("current-ip.py exists")
else:
	print ("current-ip.py created")
	createip2eIPcf()
	writeip2eIPcf()

#Check if sendEmail is installed
from subprocess import PIPE, Popen
try:
	sendEmailCheck = Popen(['sendEmail', '-q'], stdout=PIPE, stderr=PIPE)
	sendEmailCheck.stderr.close()
except:
	ClearScreen()
	print ("")
	print ("Error: 'sendEmail' is not installed!")
	print ("")
	print ("Help:")
	print ("  * http://caspian.dotconf.net/menu/Software/SendEmail/")
	print ("")
	print ("Press ENTER to exit")
	PauseScreen()
	exit(1)

#Check if curl is installed
try:
	curlCheck = Popen(['curl', '--version'], stdout=PIPE, stderr=PIPE)
	curlCheck.stderr.close()
except:
	ClearScreen()
	print ("")
	print ("Error: 'curl' is not installed!")
	print ("")
	print ("Help:")
	print ("  * http://curl.haxx.se/download.html")
	print ("  * http://www.paehl.com/open_source/?CURL_7.45.0")
	print ("")
	print ("Press ENTER to exit")
	PauseScreen()
	exit(1)

#Import variables from ip2e-conf.py
exec(open("ip2e-conf.py").read())

#Import Windows colors scheme
def GreenColor():
	os.system("color 2")
def RedColor():
	os.system("color 4")
def OrangeColor():
	os.system("color 6")

#Run ip2e daemon
ClearScreen()
CurrentTime = time.strftime("%H:%M")
if os.name == "posix":
	print (chr(27)+"[1;32m"+"[ip2e-daemon] ["+CurrentTime+"] Initialized ip2e-daemon v"+version+" (Ctrl+C to stop)")
elif os.name == "nt":
	GreenColor()
	print ("[ip2e-daemon] ["+CurrentTime+"] Initialized ip2e-daemon v"+version+" (Ctrl+C to stop)")
if os.name == "posix":
	print (chr(27)+"[1;32m"+"[ip2e-daemon] ["+CurrentTime+"] Log in "+os.environ["HOME"]+"/.ip2e/ip2e.log")
elif os.name == "nt":
	GreenColor()
	print ("[ip2e-daemon] ["+CurrentTime+"] Log in "+os.environ["USERPROFILE"]+"\.ip2e\\ip2e.log")
os.system("echo [ip2e-daemon] ["+CurrentTime+"] Initialized ip2e-daemon v"+version+" > ip2e.log")
if os.name == "posix":
	print (chr(27)+"[1;33m"+"[ip2e-daemon] ["+CurrentTime+"] Waiting 60 seconds...")
elif os.name == "nt":
	OrangeColor()
	print ("[ip2e-daemon] ["+CurrentTime+"] Waiting 60 seconds...")
os.system("echo [ip2e-daemon] ["+CurrentTime+"] Waiting 60 seconds... >> ip2e.log")
if os.name == "posix":
	os.system("sleep 60")
elif os.name == "nt":
	os.system("ping -n 60 localhost>nul")

PublicIP = 1

while PublicIP <= 2:
	GetCurrentIP = 1
	while GetCurrentIP <= 2:
		CurrentTime = time.strftime("%H:%M")
		if os.name == "posix":
			print (chr(27)+"[1;33m"+"[ip2e-daemon] ["+CurrentTime+"] IP Updating...")
		elif os.name == "nt":
			OrangeColor()
			print ("[ip2e-daemon] ["+CurrentTime+"] IP Updating...")
		os.system("echo [ip2e-daemon] ["+CurrentTime+"] IP Updating... >> ip2e.log")
		NewIPRaw = os.popen('curl -s icanhazip.com').read()
		NewIP = NewIPRaw.strip()
		#NewIP = os.popen('curl -s http://ip.appspot.com/').read()
		#NewIP = os.popen('curl -s ident.me').read()
		#NewIPRaw = os.popen('curl -s ifconfig.me').read()
		#NewIP = NewIPRaw.strip()
		if NewIP != "":
			GetCurrentIP += 2
		else:
			CurrentTime = time.strftime("%H:%M")
			if os.name == "posix":
				print (chr(27)+"[1;31m"+"[ip2e-daemon] ["+CurrentTime+"] Error getting IP")
				print (chr(27)+"[1;33m"+"[ip2e-daemon] ["+CurrentTime+"] Retrying in 5 seconds...")
			elif os.name == "nt":
				RedColor()
				print ("[ip2e-daemon] ["+CurrentTime+"] Error getting IP")
				print ("[ip2e-daemon] ["+CurrentTime+"] Retrying in 5 seconds...")
			os.system("echo [ip2e-daemon] ["+CurrentTime+"] Error getting IP >> ip2e.log")
			os.system("echo [ip2e-daemon] ["+CurrentTime+"] Retrying in 5 seconds... >> ip2e.log")
			if os.name == "posix":
				os.system("sleep 5")
			elif os.name == "nt":
				os.system("ping -n 5 localhost>nul")
	exec(open("current-ip.py").read())
	if CurrentIP == NewIP:
		CurrentTime = time.strftime("%H:%M")
		if os.name == "posix":
			print (chr(27)+"[1;32m"+"[ip2e-daemon] ["+CurrentTime+"] IP has not changed")
		elif os.name == "nt":
			GreenColor()
			print ("[ip2e-daemon] ["+CurrentTime+"] IP has not changed")
		os.system("echo [ip2e-daemon] ["+CurrentTime+"] IP has not changed >> ip2e.log")
	else:
		CurrentTime = time.strftime("%H:%M")
		if os.name == "posix":
			print (chr(27)+"[1;32m"+"[ip2e-daemon] ["+CurrentTime+"] New IP - From "+CurrentIP+" to "+NewIP)
		elif os.name == "nt":
			GreenColor()
			print ("[ip2e-daemon] ["+CurrentTime+"] New IP - From "+CurrentIP+" to "+NewIP)
		os.system("echo [ip2e-daemon] ["+CurrentTime+"] New IP - From "+CurrentIP+" to "+NewIP+" >> ip2e.log")
		SendEmailOK = 1
		while SendEmailOK <= 2:
			CurrentTime = time.strftime("%H:%M")
			if os.name == "posix":
				ErrorSendEmail = os.system("sendEmail -q -f "+FromEmail+" -t "+ToEmail+" -u '[ip2e-daemon] ["+CurrentTime+"] IP has changed' -m '[ip2e] New IP is '"+NewIP+" -s "+SmtpFromEmail+" -xu "+FromEmailUser+" -xp "+FromEmailPass)
			elif os.name == "nt":
				ErrorSendEmail = os.system("sendEmail -q -f "+FromEmail+" -t "+ToEmail+" -u [ip2e-daemon] ["+CurrentTime+"] IP has changed -m [ip2e] New IP is "+NewIP+" -s "+SmtpFromEmail+" -xu "+FromEmailUser+" -xp "+FromEmailPass)
			if ErrorSendEmail == 0:
				CurrentTime = time.strftime("%H:%M")
				MailMessage="[ip2e-daemon] ["+CurrentTime+"] Email was sent successfully"
				if os.name == "posix":
					print (chr(27)+"[1;32m"+MailMessage+" ("+ToEmail+")")
				elif os.name == "nt":
					GreenColor()
					print (MailMessage+" ("+ToEmail+")")
				os.system("echo "+MailMessage+" to "+ToEmail+" >> ip2e.log")
				SendEmailOK += 2
			else:
				CurrentTime = time.strftime("%H:%M")
				MailMessage="[ip2e-daemon] ["+CurrentTime+"] Fail to send email"
				if os.name == "posix":
					print (chr(27)+"[1;31m"+MailMessage+" ("+ToEmail+")")
					print (chr(27)+"[1;33m"+"[ip2e-daemon] ["+CurrentTime+"] Retrying in 5 seconds...")
				elif os.name == "nt":
					RedColor()
					print (MailMessage+" ("+ToEmail+")")
					print ("[ip2e-daemon] ["+CurrentTime+"] Retrying in 5 seconds...")
				os.system("echo "+MailMessage+" to "+ToEmail+" >> ip2e.log")
				os.system("echo [ip2e-daemon] ["+CurrentTime+"] Retrying in 5 seconds... >> ip2e.log")
				if os.name == "posix":
					os.system("sleep 5")
				elif os.name == "nt":
					os.system("ping -n 5 localhost>nul")
		if os.name == "posix":
			os.system("rm current-ip.py")
		elif os.name == "nt":
			os.system("del current-ip.py")
		def createNewip2eIPcf():
			ip2eIPcf=open('current-ip.py','w')
			ip2eIPcf.close()
		def writeNewip2eIPcf():
			ip2eIPcf=open('current-ip.py','a')
			ip2eIPcf.write('CurrentIP="'+NewIP+'"\n')
			ip2eIPcf.close()
		createNewip2eIPcf()
		writeNewip2eIPcf()
	CurrentTime = time.strftime("%H:%M")
	if os.name == "posix":
		print (chr(27)+"[1;33m"+"[ip2e-daemon] ["+CurrentTime+"] Next update in 10 minutes...")
	elif os.name == "nt":
		GreenColor()
		print ("[ip2e-daemon] ["+CurrentTime+"] Next update in 10 minutes...")
	os.system("echo [ip2e-daemon] ["+CurrentTime+"] Next update in 10 minutes... >> ip2e.log")
	WaitTenMinutes()
