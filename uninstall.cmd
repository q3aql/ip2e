@echo off

echo Removing desktop shortcuts....

del %USERPROFILE%\Desktop\"ip2e (daemon).lnk"
del %USERPROFILE%\Desktop\"ip2e (config).lnk"
del %USERPROFILE%\Desktop\"ip2e (background).lnk"

echo Removed!
echo Press ENTER to exit 
pause > nul