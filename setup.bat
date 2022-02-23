@echo off

@REM Create Folder
md C:\Program Files\Glush

@REM Move Files Into The New Folder
move glush.exe, config.json c:\Program Files\Glush

@REM Making sure that the task scheduler is enabled.
net start "task scheduler"

@REM Configure Windows Task Scheduler
SCHTASKS /CREATE /SC MINUTE /TN "Glush\Glush for Windows" /TR "C:\Program Files\Glush\glush.exe"

pause