@echo off && title Latency and BCD Tweaks && mode con: cols=100 lines=25 && color 02 && cls
echo Batch File By Snowy
@echo
bcdedit /set disabledynamictick yes
bcdedit /deletevalue useplatformclock
bcdedit /set useplatformtick yes
pause