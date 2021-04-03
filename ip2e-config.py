#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# --------------------------------------------------------------
# ip2e (IP to email) - Create the configuration file.          |
# Created by q3aql (q3aql@protonmail.ch)                       |
# Licensed by GPL v.3                                          |
# Last update: 03-04-2021                                      |
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
  print ("* You need python 3.x to run this program.")
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
    print ("* Error: Unable clear screen")
		
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

if os.path.isfile("ip2e.conf"):
  ClearScreen()
  print ("")
  print ("** ip2e-config v"+version+" **")
  print ("")
  print (" - Detected a previous configuration file.")
  print (" - Do you want to overwrite or check the current configuration?")
  print ("")
  print (" * (o) - overwrite (create new configuration)")
  print (" * (c) - check and test the current configuration")
  print ("")
  OverWriteOrCheck=input("- [Default: check and test] Choose an option; ")
  if OverWriteOrCheck == "o" or OverWriteOrCheck == "O":
    print ("Create new configuration")
  else:
    exec(open("ip2e.conf").read())
    #Import smtplib
    import smtplib
    try:
      server = smtplib.SMTP(SmtpFromEmail)
      server.ehlo()
      server.starttls()
      server.ehlo()
      server.login(FromEmailUser,FromEmailPass)
      server.quit()
      print ("")
      print ("* Test OK")
      print ("")
      PauseExit=input("+ Press ENTER to exit ")
    except:
      print ("")
      print ("* Failed to connect ("+SmtpFromEmail+")")
      print ("")
      PauseExit=input("+ Press ENTER to exit ")
      exit()

#Set variables of 'ip2e.conf'
ClearScreen()
print ("")
print ("** ip2e-config v"+version+" - Create config.file **")
print ("")
FromEmail=input("- Type the email sender: ")
FromEmailUser=input("- Type the user of email sender: ")
FromEmailPass=input("- Type the pass of email sender: ")
SmtpFromEmail=input("- Type the server STMP (STARTTLS) of email sender: ")
ToEmail=input("- Type the email receiver: ")

#Create 'ip2e.conf'
if os.path.isfile("ip2e.conf"):
  os.remove("ip2e.conf")
ip2ecf=open('ip2e.conf','w')
ip2ecf.close()
ip2ecf=open('ip2e.conf','a')
ip2ecf.write('# sample configuration file of ip2e\n')
ip2ecf.write('\n')
ip2ecf.write('FromEmail="'+FromEmail+'"\n')
ip2ecf.write('FromEmailUser="'+FromEmailUser+'"\n')
ip2ecf.write('FromEmailPass="'+FromEmailPass+'"\n')
ip2ecf.write('SmtpFromEmail="'+SmtpFromEmail+'"\n')
ip2ecf.write('ToEmail="'+ToEmail+'"\n')
ip2ecf.close()

#Show the configuration
ClearScreen()
print ("")
print ("** ip2e-config v"+version+" - Current config.file **")
print ("")
readfile=open('ip2e.conf', 'r')
print(readfile.read())
readfile.close()

#Test connection with your configuration
print ("")
TestConnection=input("- [Default: y] Test connection with your configuration (y/n): ")
if TestConnection == "n":
  print ("Exiting...")
  exit()
else:
  exec(open("ip2e.conf").read())
  #Import smtplib
  import smtplib
  try:
    server = smtplib.SMTP(SmtpFromEmail)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(FromEmailUser,FromEmailPass)
    server.quit()
    print ("")
    print ("* Test OK")
    print ("")
    PauseExit=input("+ Press ENTER to exit ")
  except:
    print ("")
    print ("* Failed to connect ("+SmtpFromEmail+")")
    print ("")
    PauseExit=input("+ Press ENTER to exit ")
