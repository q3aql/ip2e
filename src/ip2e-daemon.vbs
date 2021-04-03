Set WshShell = CreateObject("WScript.Shell")
WshShell.Run chr(34) & "ip2e-daemon.py" & Chr(34), 0 
Set WshShell = Nothing