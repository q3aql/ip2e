#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# --------------------------------------------------------------
# ip2e (IP to email) - Run ip2e daemon.                        |
# Created by clamsawd (clamsawd@openmailbox.org)               |
# Licensed by GPL v.3                                          |
# Last update: 01-11-2015                                      |
#                                                              |
# Compatible with Python 3.x                                   |
# --------------------------------------------------------------
version="1.0"

#Import python-modules
import urllib
import urllib.request
import os
import sys
import time
import smtplib

#Check if your system use Python 3.x
if sys.version_info<(3,0):
	print ("")
	print ("You need python 3.x to run this program.")
	print ("")
	exit(1)

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
if os.path.isfile("ip2e-conf.py"):
	print ("ip2e-conf.py exists")
else:
	print ("ip2e-conf.py created")
	ip2ecf=open('ip2e-conf.py','w')
	ip2ecf.close()
	ip2ecf=open('ip2e-conf.py','a')
	ip2ecf.write('# sample configuration file of ip2e\n')
	ip2ecf.write('\n')
	ip2ecf.write('FromEmail="ip2e@daemon"\n')
	ip2ecf.write('FromEmailUser="unknown"\n')
	ip2ecf.write('FromEmailPass="password-here"\n')
	ip2ecf.write('SmtpFromEmail="smtp.email.com"\n')
	ip2ecf.write('ToEmail="unknown@email.com"\n')
	ip2ecf.close()

#Check if exists 'current-ip.py'
if os.path.isfile("current-ip.py"):
	print ("current-ip.py exists")
else:
	print ("current-ip.py created")
	ip2eIPcf=open('current-ip.py','w')
	ip2eIPcf.close()
	ip2eIPcf=open('current-ip.py','a')
	ip2eIPcf.write('CurrentIP="0.0.0.0"\n')
	ip2eIPcf.close()

#Import variables from ip2e-conf.py
exec(open("ip2e-conf.py").read())

#Import native OS color scheme
try:
	def GreenColor():
		if os.name == "posix":
			GreenColor = (chr(27)+"[1;32m")
			print (GreenColor+"", end="")
		elif os.name == "nt":
			os.system("color 2")
	def RedColor():
		if os.name == "posix":
			RedColor = (chr(27)+"[1;31m")
			print (RedColor+"", end="")
		elif os.name == "nt":
			os.system("color 4")
	def OrangeColor():
		if os.name == "posix":
			OrangeColor = (chr(27)+"[1;33m")
			print (OrangeColor+"", end="")
		elif os.name == "nt":
			os.system("color 6")
except:
	print ("Error importing native color scheme")
	exit(1)

#Check if exists a previous log.file.
if os.path.isfile("ip2e.log"):
	os.remove("ip2e.log")
createlog=open('ip2e.log','w')
createlog.close()

#Run ip2e daemon
ClearScreen()
editlog=open('ip2e.log','a')
CurrentTime = time.strftime("%H:%M")
GreenColor()
print ("[ip2e-daemon] ["+CurrentTime+"] Initialized ip2e-daemon v"+version+" (Ctrl+C to stop)")
if os.name == "posix":
	print ("[ip2e-daemon] ["+CurrentTime+"] Log in "+os.environ["HOME"]+"/.ip2e/ip2e.log")
elif os.name == "nt":
	print ("[ip2e-daemon] ["+CurrentTime+"] Log in "+os.environ["USERPROFILE"]+"\.ip2e\\ip2e.log")
editlog.write("[ip2e-daemon] ["+CurrentTime+"] Initialized ip2e-daemon v"+version+"\n")
OrangeColor()
print ("[ip2e-daemon] ["+CurrentTime+"] Waiting 60 seconds...")
editlog.write("[ip2e-daemon] ["+CurrentTime+"] Waiting 60 seconds...\n")
editlog.close()
time.sleep(60)

PublicIP = 1

while PublicIP <= 2:
	GetCurrentIP = 1
	while GetCurrentIP <= 2:
		CurrentTime = time.strftime("%H:%M")
		OrangeColor()
		print ("[ip2e-daemon] ["+CurrentTime+"] IP Updating...")
		editlog=open('ip2e.log','a')
		editlog.write("[ip2e-daemon] ["+CurrentTime+"] IP Updating...\n")
		try:
			response = urllib.request.urlopen('http://icanhazip.com')
			#response = urllib.request.urlopen('http://ip.appspot.com/')
			#response = urllib.request.urlopen('http://ident.me')
			NewIPRaw = response.read()
			NewIP = NewIPRaw.strip().decode('utf-8')
			GetCurrentIP += 2
		except:
			CurrentTime = time.strftime("%H:%M")
			RedColor()
			print ("[ip2e-daemon] ["+CurrentTime+"] Error getting IP")
			print ("[ip2e-daemon] ["+CurrentTime+"] Retrying in 10 seconds...")
			editlog.write("[ip2e-daemon] ["+CurrentTime+"] Error getting IP\n")
			editlog.write("[ip2e-daemon] ["+CurrentTime+"] Retrying in 10 seconds...\n")
			time.sleep(10)
	exec(open("current-ip.py").read())
	if CurrentIP == NewIP:
		CurrentTime = time.strftime("%H:%M")
		GreenColor()
		print ("[ip2e-daemon] ["+CurrentTime+"] IP has not changed")
		editlog.write("[ip2e-daemon] ["+CurrentTime+"] IP has not changed\n")
	else:
		CurrentTime = time.strftime("%H:%M")
		GreenColor()
		print ("[ip2e-daemon] ["+CurrentTime+"] New IP - From "+CurrentIP+" to "+NewIP)
		editlog.write("[ip2e-daemon] ["+CurrentTime+"] New IP - From "+CurrentIP+" to "+NewIP+"\n")
		SendEmailOK = 1
		while SendEmailOK <= 2:
			CurrentTime = time.strftime("%H:%M")
			#Sending email using smtplib
			SmtpSubject = "[ip2e-daemon] ["+CurrentTime+"] IP has changed"
			SmtpHeader = "From: "+FromEmail+"\n"+"To: "+ToEmail+"\n"+"Subject: "+SmtpSubject+"\n"
			SmtpBodyMessage = SmtpHeader+"\n"+"[ip2e] New IP is "+NewIP+"\n\n"
			#Check sending errors
			try:
				server = smtplib.SMTP(SmtpFromEmail)
				server.ehlo()
				server.starttls()
				server.ehlo()
				server.login(FromEmailUser,FromEmailPass)
				server.sendmail(FromEmail, ToEmail, SmtpBodyMessage)
				server.quit()
				CurrentTime = time.strftime("%H:%M")
				MailMessage="[ip2e-daemon] ["+CurrentTime+"] Email was sent successfully"
				GreenColor()
				print (MailMessage+" ("+ToEmail+")")
				editlog.write(MailMessage+" ("+ToEmail+")\n")
				SendEmailOK += 2
			except:
				CurrentTime = time.strftime("%H:%M")
				RedColor()
				print ("[ip2e-daemon] ["+CurrentTime+"] Failed to connect ("+SmtpFromEmail+")")
				print ("[ip2e-daemon] ["+CurrentTime+"] Check your settings or your connection")
				editlog.write("[ip2e-daemon] ["+CurrentTime+"] Failed to connect ("+SmtpFromEmail+")\n")
				editlog.write("[ip2e-daemon] ["+CurrentTime+"] Check your settings or your connection\n")
				MailMessage="[ip2e-daemon] ["+CurrentTime+"] Failed to send email"
				print (MailMessage+" ("+ToEmail+")")
				print ("[ip2e-daemon] ["+CurrentTime+"] Retrying in 10 seconds...")
				editlog.write(MailMessage+" ("+ToEmail+")\n")
				editlog.write("[ip2e-daemon] ["+CurrentTime+"] Retrying in 10 seconds...\n")
				time.sleep(10)
		os.remove("current-ip.py")
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
	GreenColor()
	print ("[ip2e-daemon] ["+CurrentTime+"] Next update in 10 minutes...")
	editlog.write("[ip2e-daemon] ["+CurrentTime+"] Next update in 10 minutes...\n")
	editlog.close()
	time.sleep(600)
