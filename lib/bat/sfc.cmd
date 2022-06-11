echo off && title sfc scan && mode con: cols=100 lines=25 && color 02 && cls
echo sfc scan script by Snowy && timeout /t 2 >nul && cls

echo off
cls
sfc /SCANNOW
exit