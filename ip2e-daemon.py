#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# --------------------------------------------------------------
# ip2e (IP to email) - Run ip2e daemon.                        |
# Created by clamsawd (clamsawd@openmailbox.org)               |
# Licensed by GPL v.3                                          |
# Last update: 16-02-2016                                      |
#                                                              |
# Compatible with Python 3.x                                   |
# --------------------------------------------------------------
version="1.3.1"

#Import python-modules
import urllib
import urllib.request
import os
import sys
import time
import smtplib
import random

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
	LogFile=HOMESCARD0+"/ip2e/ip2e.log"
	LockFile=HOMESCARD0+"/ip2e/ip2e.lock"
	print ("Android (Posix) detected")
elif os.name == "posix":
	os.chdir(os.environ["HOME"])
	LogFile=os.environ["HOME"]+"/.ip2e/ip2e.log"
	LockFile=os.environ["HOME"]+"/.ip2e/ip2e.lock"
	print ("Unix (Posix) detected")
elif os.name == "nt":
	os.chdir(os.environ["USERPROFILE"])
	LogFile=os.environ["USERPROFILE"]+"\\.ip2e\\ip2e.log"
	LockFile=os.environ["USERPROFILE"]+"\\.ip2e\\ip2e.lock"
	print ("Windows detected")

if not os.path.exists(".ip2e"):
	os.makedirs(".ip2e")
	os.chdir(".ip2e")
if os.path.exists(".ip2e"):
	os.chdir(".ip2e")

#Check if exists 'ip2e.conf'
if os.path.isfile("ip2e.conf"):
	print ("ip2e.conf exists")
else:
	ClearScreen()
	print ("")
	print ("* The configuration file doesn't exist")
	print ("")
	print ("* You can create it if you run 'ip2e-config.py'")
	print ("")
	PauseExit=input("+ Press ENTER to exit ")
	exit()

#Check if exists 'IP.log'
if os.path.isfile("IP.log"):
	print ("IP.log exists")
else:
	print ("IP.log created")
	ip2eIPcf=open('IP.log','w')
	ip2eIPcf.close()
	ip2eIPcf=open('IP.log','a')
	ip2eIPcf.write('0.0.0.0')
	ip2eIPcf.close()

#Import variables from ip2e.conf
exec(open("ip2e.conf").read())

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
	def EndColor():
		if os.name == "posix":
			EndColor = (chr(27)+"[0m")
			print (EndColor+"", end="")
		elif os.name == "nt":
			print ("", end="")		
except:
	print ("")
	print ("* Error importing native color scheme")
	print ("")
	PauseExit=input("+ Press ENTER to exit ")
	exit()

#Check if ip2e-daemon is running.
if os.path.isfile("ip2e.lock"):
	readLock=open('ip2e.lock', 'r')
	LockN=readLock.read()
	readLock.close()
	ClearScreen()
	print ("Checking "+LockFile+"...")
	time.sleep(4)
	readLock2=open('ip2e.lock', 'r')
	LockN2=readLock2.read()
	readLock2.close()
	if LockN != LockN2:
		ClearScreen()
		print ("")
		print ("* ip2e-daemon is already running.")
		print ("")
		PauseExit=input("+ Press ENTER to exit ")
		exit()
if not os.path.isfile("ip2e.lock"):
	createLock=open('ip2e.lock','w')
	createLock.write(str(random.randrange(135790)))
	createLock.close()

#Function to lock process.
def LockProcess():
	createLock=open('ip2e.lock','w')
	createLock.write(str(random.randrange(135790)))
	createLock.close()

#Function to sleep 'N' seconds.
def TimeSleep(N):
	Time=1
	while Time < N:
		createLock=open('ip2e.lock','w')
		createLock.write(str(random.randrange(135790)))
		createLock.close()
		time.sleep(1)
		Time=Time + 1		

#Check if exists a previous log.file
if os.path.isfile("ip2e.log"):
	createlog=open('ip2e.log','w')
	createlog.close()

#Run ip2e daemon
ClearScreen()
LockProcess()
editlog=open('ip2e.log','a')
CurrentTime = time.strftime("%H:%M")
GreenColor()
print ("[ip2e-daemon] ["+CurrentTime+"] Initialized ip2e-daemon v"+version+" (Ctrl+C to stop)")
print ("[ip2e-daemon] ["+CurrentTime+"] Log in "+LogFile)
EndColor()
editlog.write("[ip2e-daemon] ["+CurrentTime+"] Initialized ip2e-daemon v"+version+"\n")
OrangeColor()
print ("[ip2e-daemon] ["+CurrentTime+"] Waiting 60 seconds...")
EndColor()
editlog.write("[ip2e-daemon] ["+CurrentTime+"] Waiting 60 seconds...\n")
editlog.close()
TimeSleep(60)

PublicIP = 1
while PublicIP <= 2:
	GetCurrentIP = 1
	while GetCurrentIP <= 2:
		CurrentTime = time.strftime("%H:%M")
		LockProcess()
		OrangeColor()
		print ("[ip2e-daemon] ["+CurrentTime+"] IP Updating...")
		EndColor()
		editlog=open('ip2e.log','a')
		editlog.write("[ip2e-daemon] ["+CurrentTime+"] IP Updating...\n")
		#Check & get the new IP
		try:
			LockProcess()
			response = urllib.request.urlopen('http://icanhazip.com')
			#response = urllib.request.urlopen('http://ip.appspot.com/')
			#response = urllib.request.urlopen('http://ident.me')
			NewIPRaw = response.read()
			NewIP = NewIPRaw.strip().decode('utf-8')
			GetCurrentIP += 2
		except:
			CurrentTime = time.strftime("%H:%M")
			LockProcess()
			RedColor()
			print ("[ip2e-daemon] ["+CurrentTime+"] Error getting IP")
			print ("[ip2e-daemon] ["+CurrentTime+"] Retrying in 10 seconds...")
			EndColor()
			editlog.write("[ip2e-daemon] ["+CurrentTime+"] Error getting IP\n")
			editlog.write("[ip2e-daemon] ["+CurrentTime+"] Retrying in 10 seconds...\n")
			TimeSleep(10)
	#Read IP log file & get the current IP
	readfileIP=open('IP.log', 'r')
	CurrentIPRaw=readfileIP.read()
	CurrentIP=CurrentIPRaw.strip()
	readfileIP.close()
	LockProcess()
	#Check if the IP has been renewed
	if CurrentIP == NewIP:
		CurrentTime = time.strftime("%H:%M")
		LockProcess()
		GreenColor()
		print ("[ip2e-daemon] ["+CurrentTime+"] IP has not changed")
		EndColor()
		editlog.write("[ip2e-daemon] ["+CurrentTime+"] IP has not changed\n")
	else:
		CurrentTime = time.strftime("%H:%M")
		LockProcess()
		GreenColor()
		print ("[ip2e-daemon] ["+CurrentTime+"] New IP - From "+CurrentIP+" to "+NewIP)
		EndColor()
		editlog.write("[ip2e-daemon] ["+CurrentTime+"] New IP - From "+CurrentIP+" to "+NewIP+"\n")
		SendEmailOK = 1
		while SendEmailOK <= 2:
			LockProcess()
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
				LockProcess()
				GreenColor()
				print (MailMessage+" ("+ToEmail+")")
				EndColor()
				editlog.write(MailMessage+" ("+ToEmail+")\n")
				SendEmailOK += 2
			except:
				CurrentTime = time.strftime("%H:%M")
				LockProcess()
				RedColor()
				print ("[ip2e-daemon] ["+CurrentTime+"] Failed to connect ("+SmtpFromEmail+")")
				print ("[ip2e-daemon] ["+CurrentTime+"] Check your settings or your connection")
				EndColor()
				editlog.write("[ip2e-daemon] ["+CurrentTime+"] Failed to connect ("+SmtpFromEmail+")\n")
				editlog.write("[ip2e-daemon] ["+CurrentTime+"] Check your settings or your connection\n")
				MailMessage="[ip2e-daemon] ["+CurrentTime+"] Failed to send email"
				RedColor()
				print (MailMessage+" ("+ToEmail+")")
				print ("[ip2e-daemon] ["+CurrentTime+"] Retrying in 10 seconds...")
				EndColor()
				editlog.write(MailMessage+" ("+ToEmail+")\n")
				editlog.write("[ip2e-daemon] ["+CurrentTime+"] Retrying in 10 seconds...\n")
				TimeSleep(10)
		#Remove the previous IP log file & create a new.
		ip2eIPcf=open('IP.log','w')
		ip2eIPcf.write(NewIP)
		ip2eIPcf.close()
	#Wait 10 minutes until the next checking
	CurrentTime = time.strftime("%H:%M")
	LockProcess()
	GreenColor()
	print ("[ip2e-daemon] ["+CurrentTime+"] Next update in 10 minutes...")
	EndColor()
	editlog.write("[ip2e-daemon] ["+CurrentTime+"] Next update in 10 minutes...\n")
	editlog.close()
	TimeSleep(600)
