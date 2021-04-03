@echo off

echo.
echo  ###################################
echo  # Welcome to ip2e installer 1.3.2 #
echo  ###################################
echo.
echo  - This installer simply creates a shortcut to the 
echo    application on your desktop. We recommend that 
echo    before continuing, make sure you have left the 
echo    application folder in a place where no one can 
echo    delete it.
echo.
echo    Examples: 
echo        - C:\ip2e
echo        - C:\Program Files\ip2e
echo.
echo  * Press ENTER to continue or Ctrl+C to exit
pause > nul
echo.
echo  * Creating shortchut (%USERPROFILE%\Desktop\ip2e (daemon).lnk)
set SCRIPT="%TEMP%\%RANDOM%-%RANDOM%.vbs"
echo Set oWS = WScript.CreateObject("WScript.Shell") >> %SCRIPT%
echo sLinkFile = "%USERPROFILE%\Desktop\ip2e (daemon).lnk" >> %SCRIPT%
echo Set oLink = oWS.CreateShortcut(sLinkFile) >> %SCRIPT%
echo oLink.TargetPath = "%~d0%~p0\src\ip2e-daemon.py" >> %SCRIPT%
echo oLink.WorkingDirectory = "%~d0%~p0" >> %SCRIPT%
echo oLink.IconLocation = "%~d0%~p0\icon\ip2e.ico" >> %SCRIPT%
echo oLink.Save >> %SCRIPT%
cscript /nologo %SCRIPT%
del %SCRIPT%
echo  * Creating shortchut (%USERPROFILE%\Desktop\ip2e (config).lnk)
set SCRIPT="%TEMP%\%RANDOM%-%RANDOM%.vbs"
echo Set oWS = WScript.CreateObject("WScript.Shell") >> %SCRIPT%
echo sLinkFile = "%USERPROFILE%\Desktop\ip2e (config).lnk" >> %SCRIPT%
echo Set oLink = oWS.CreateShortcut(sLinkFile) >> %SCRIPT%
echo oLink.TargetPath = "%~d0%~p0\src\ip2e-config.py" >> %SCRIPT%
echo oLink.WorkingDirectory = "%~d0%~p0" >> %SCRIPT%
echo oLink.IconLocation = "%~d0%~p0\icon\ip2e.ico" >> %SCRIPT%
echo oLink.Save >> %SCRIPT%
cscript /nologo %SCRIPT%
del %SCRIPT%
echo  * Creating shortchut (%USERPROFILE%\Desktop\ip2e (background).lnk)
copy /Y src\ip2e-daemon.vbs ip2e-daemon.vbs
set SCRIPT="%TEMP%\%RANDOM%-%RANDOM%.vbs"
echo Set oWS = WScript.CreateObject("WScript.Shell") >> %SCRIPT%
echo sLinkFile = "%USERPROFILE%\Desktop\ip2e (background).lnk" >> %SCRIPT%
echo Set oLink = oWS.CreateShortcut(sLinkFile) >> %SCRIPT%
echo oLink.TargetPath = "%~d0%~p0\src\ip2e-daemon.vbs" >> %SCRIPT%
echo oLink.WorkingDirectory = "%~d0%~p0" >> %SCRIPT%
echo oLink.IconLocation = "%~d0%~p0\icon\ip2e.ico" >> %SCRIPT%
echo oLink.Save >> %SCRIPT%
cscript /nologo %SCRIPT%
del %SCRIPT%
echo * Shortcuts created!
echo Press ENTER to exit 
pause > nul
