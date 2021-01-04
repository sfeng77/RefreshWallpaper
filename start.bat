@echo off
cd  /d  C:\Users\sfeng\Projects\RefreshWallpaper
set Log=C:\Users\sfeng\Projects\RefreshWallpaper\Log.txt
echo Script launched on %date% at %time% under %UserName% > %Log%
c:\python\python39\python.exe  C:\Users\sfeng\Projects\RefreshWallpaper\downloadandsetwallpaper.py  1>>%Log%  2>>&1
echo Script ended on %date% at %time% >> %Log%

