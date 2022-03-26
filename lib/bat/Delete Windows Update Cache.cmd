@echo off
echo off && title Windows Update Disabler && mode con: cols=100 lines=25 && color 02 && cls
echo Batch File By Snowy
net stop wuauserv
net stop UsoSvc
rd /s /q C:\Windows\SoftwareDistribution
md C:\Windows\SoftwareDistribution
pause