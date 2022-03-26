@echo off && title Log File Cleanup && mode con: cols=100 lines=25 && color 02 && cls
echo Batch File By Snowy
cd/
@echo
del *.log /a /s /q /f
pause