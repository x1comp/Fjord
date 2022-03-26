import tkinter as tk
import webbrowser
from tkinter import *
from tkinter import filedialog, ttk
import os
import time


# GUI window
root = tk.Tk()
root.title("Fjord")
root.geometry('750x450')
root.resizable(0,0)
Tab_Control = ttk.Notebook(root)

#----TABS-----#

#Start Tab
Start = ttk.Frame(Tab_Control)
Tab_Control.add(Start, text='Start')

#Tweaks Tab
Tweaks = ttk.Frame(Tab_Control)
Tab_Control.add(Tweaks, text='Tweaks')
Tab_Control.pack(expand=1, fill="both")

#Apperance Tab
Apperance = ttk.Frame(Tab_Control)
Tab_Control.add(Apperance, text='Apperance')
Tab_Control.pack(expand=2, fill="both")

#Cleanup Tab
Cleanup = ttk.Frame(Tab_Control)
Tab_Control.add(Cleanup, text='Cleanup')
Tab_Control.pack(expand=3, fill="both")

#Debloat Tab
Advanced_Tweaks = ttk.Frame(Tab_Control)
Tab_Control.add(Advanced_Tweaks, text='Programs')
Tab_Control.pack(expand=3, fill="both")

#Tab Name Labels
ttk.Label(Tweaks, text="").grid(column=0, row=0, padx=10, pady=10)
ttk.Label(Apperance, text="").grid(column=0, row=0, padx=10, pady=10)

icon=PhotoImage(file="assets\\logo.png")
root.iconphoto(False, icon)

#----BUTTON FUNCTIONS-----#


#Start Button Function
def readDocs():
    webbrowser.open('https://github.com/x1comp/Tweaking-Utility/blob/main/README.md')

def restorePoint():
    os.startfile('lib\\links\\Create A Restore Point.lnk')
    input('Press ENTER to exit')

def DeleteUnusedApps():
    os.startfile('lib\\links\\Uninstall Apps You Don_t Need.lnk')
    input('Press ENTER to exit')

def Perfopt():
    os.startfile('lib\\links\\Performance Options.lnk')
    input('Press ENTER to exit')

def startup():
    os.startfile('lib\\links\\Startup Apps.lnk')
    input('Press ENTER to exit')

def disableUAC():
    os.startfile('lib\\reg\\5 Disable UAC.reg')
    input('Press ENTER to exit')

# Tweak Button Functions
def regTweaks():
    os.startfile('lib\\reg\\Registry Tweaks.reg')
    input('Press ENTER to exit')

def xbxTweaks():
    os.startfile('lib\\reg\\OPTIONAL Disable Xbox Services.reg')
    input('Press ENTER to exit')

def AudioTweaks():
    os.startfile('lib\\links\\Change Sound Settings.lnk')
    input('Press ENTER to exit')

def winTweaks():
    os.startfile('lib\\reg\\Optimize ALL Windows Settings.reg')
    input('Press ENTER to exit')
    
def latencyTweaks():
    os.system(r''' Powershell -Command "& { Start-Process \"lib\\bat\\Latency BCD Tweaks.cmd\" -ArgumentList @(\"lib\\bat\\Latency BCD Tweaks.cmd\") -Verb RunAs } " ''')
    input('Press ENTER to exit')

def DisableWinDefender():
    os.startfile('lib\\reg\\Disable Windows Defender.reg')
    input('Press ENTER to exit')
    
def networkTweaks():
    os.system(r''' Powershell -Command "& { Start-Process \"lib\\bat\\IPConfig.bat\" -ArgumentList @(\"lib\\bat\\IPConfig.bat\") -Verb RunAs } " ''')
    input('Press ENTER to exit')
    time.sleep(1)
    os.system(r''' Powershell -Command "& { Start-Process \"lib\\bat\\Network Latency Optimizations.cmd\" -ArgumentList @(\"lib\\bat\\Network Latency Optimizations.cmd\") -Verb RunAs } " ''')
    input('Press ENTER to exit')

def UndoTweaks():
    os.startfile('lib\\links\\Create A Restore Point.lnk')
    input('Press ENTER to exit')
    
def DisableDriverSearching():
    os.startfile('lib\\reg\\Disable Automatic Driver Updates.reg')
    input('Press ENTER to exit')

def DisableWinUpdate():
    os.system(r''' Powershell -Command "& { Start-Process \"lib\\bat\\Turn Off Auto Windows Updates.cmd\" -ArgumentList @(\"lib\\bat\\Turn Off Auto Windows Updates.cmd\") -Verb RunAs } " ''')

def DisableMit():
    os.startfile('lib\\reg\\Disable Mitigations.reg')
    input('Press ENTER to exit')

# Apperance Button Functions
def ApplyNDrestartA():
     os.system("shutdown /r /t 1")

def TaskBar():
    os.startfile('lib\\links\\tasbar.lnk')
    input('Press ENTER to exit')

def RoundedTB():
    webbrowser.open('https://github.com/torchgm/RoundedTB/releases/tag/R3.1')

def Themes():
    os.startfile('lib\\links\\themes.lnk')
    input('Press ENTER to exit')
    
def darkMode():
    os.startfile('lib\\links\\colors.lnk')
    input('Press ENTER to exit')
    
def lightMode():
    os.startfile('lib\\links\\colors.lnk')
    input('Press ENTER to exit')

def CustStart():
    os.startfile('lib\\links\\start.lnk')
    input('Press ENTER to exit')

#Cleanup
def diskcleanup():
    os.startfile('lib\\links\\4 Disk Clean-Up.lnk')
    input('Press ENTER to exit')

def AdvancedDebloat():
    os.system(r''' Powershell -Command "& { Start-Process \"lib\\bat\\Debloat Script.cmd\" -ArgumentList @(\"lib\\bat\\Debloat Script.cmd\") -Verb RunAs } " ''')
    input('Press ENTER to exit')
    
def disableautoruns():
    os.startfile('lib\\4 AutoRuns.exe')
    input('Press ENTER to exit')
    

def TempFilesCleanup():
    os.system(r''' Powershell -Command "& { Start-Process \"lib\\bat\\Delete Temporary Files.cmd\" -ArgumentList @(\"lib\\bat\\Delete Temporary Files.cmd\") -Verb RunAs } " ''')
    input('Press ENTER to exit')

def flushdns():
    os.system(r''' Powershell -Command "& { Start-Process \"lib\\bat\\IPConfig.bat\" -ArgumentList @(\"lib\\bat\\IPConfig.bat\") -Verb RunAs } " ''')

def OldRestorePointCleanup():
    os.startfile('lib\\links\\Create A Restore Point.lnk')
    input('Press ENTER to exit')
    
def WindowsUpdateCleanup():
    os.system(r''' Powershell -Command "& { Start-Process \"lib\\bat\\Delete Windows Update Cache.cmd\" -ArgumentList @(\"lib\\bat\\Delete Windows Update Cache.cmd\") -Verb RunAs } " ''')
    input('Press ENTER to exit')
    
def LogFilesCleanup():
    os.system(r''' Powershell -Command "& { Start-Process \"lib\\bat\\Delete Log Files.cmd\" -ArgumentList @(\"lib\\bat\\Delete Log Files.cmd\") -Verb RunAs } " ''')
    input('Press ENTER to exit')

#Debloat
def DisableOneDrive():
    os.system(r''' Powershell -Command "& { Start-Process \"lib\\bat\\OneDrive Uninstaller v0.4.cmd\" -ArgumentList @("\"lib\\bat\\OneDrive Uninstaller v0.4.cmd\"") -Verb RunAs } " ''')
    input('Press ENTER to exit')

def MSI():
    webbrowser.open('https://www.msi.com/Landing/afterburner/graphics-cards')

def msimodetool():
   os.system(r''' Powershell -Command "& { Start-Process \"lib\\3 MSI Mode Tool.exe\" -ArgumentList @(\"lib\\3 MSI Mode Tool.exe\"") -Verb RunAs } " ''')

def throttlestop():
    webbrowser.open('https://www.techpowerup.com/download/techpowerup-throttlestop/')

def winprivdash():
     os.startfile('lib\\Windows Privacy Dashboard.exe')

def ApplyNDrestart():
     os.system("shutdown /r /t 1")

#right click button functions
def help():
    webbrowser.open('https://github.com/x1comp/Tweaking-Utility/blob/main/README.md')

def credits():
	webbrowser.open('https://github.com/x1comp/Tweaking-Utility/README.md')

def my_popup(e):
	my_menu.tk_popup(e.x_root, e.y_root)

def browseFiles():
     filedialog.askopenfilename(initialdir = "lib", title = "Select a File", filetypes = (("all files","*.*"), ("Text files", "*.txt*"),))
 #----TAB BUTTONS----#   

 #Start
DeleteUnusedApps = tk.Button(Start, text="Delete Unused Apps", padx=18, pady=12, fg="white", bg="#263D42", command=DeleteUnusedApps)
DeleteUnusedApps.place(relx=0.21, rely=0.55, anchor=CENTER)

restorePoint = tk.Button(Start, text="Create Restore Point", padx=23, pady=12, fg="white", bg="#263D42", command=restorePoint)
restorePoint.place(relx=0.21, rely=0.225, anchor=CENTER)

disableUAC = tk.Button(Start, text="Disable UAC", padx=40, pady=12, fg="white", bg="#263D42", command=disableUAC)
disableUAC.place(relx=0.21, rely=0.387, anchor=CENTER)

startup = tk.Button(Start, text="Disable Startup Apps", padx=23, pady=12, fg="white", bg="#263D42", command=startup)
startup.place(relx=0.81, rely=0.387, anchor=CENTER)

Perfopt = tk.Button(Start, text="Performance Options", padx=23, pady=12, fg="white", bg="#263D42", command=Perfopt)
Perfopt.place(relx=0.81, rely=0.225, anchor=CENTER)

readDocs = tk.Button(Start, text="Read Documentation", padx=15, pady=11, fg="white", bg="#263D42", command=readDocs)
readDocs.place(relx=0.81, rely=0.55, anchor=CENTER)

# Tweaks
regTweaks = tk.Button(Tweaks, text="Registry Tweaks", padx=27, pady=10, fg="white", bg="#263D42", command=regTweaks)
regTweaks.place(relx=0.81, rely=0.36, anchor=CENTER)

xbxTweaks = tk.Button(Tweaks, text="Disable Xbox Game Bar", padx=10, pady=12, fg="white", bg="#263D42", command=xbxTweaks)
xbxTweaks.place(relx=0.81, rely=0.2, anchor=CENTER)

DisableWinDefender = tk.Button(Tweaks, text="Disable Windows Defender", padx=1, pady=12, fg="white", bg="#263D42", command=DisableWinDefender)
DisableWinDefender.place(relx=0.21, rely=0.2, anchor=CENTER)

winTweaks = tk.Button(Tweaks, text="Windows Tweaks", padx=24, pady=11, fg="white", bg="#263D42", command=winTweaks)
winTweaks.place(relx=0.21, rely=0.525, anchor=CENTER)

networkTweaks = tk.Button(Tweaks, text="Network Tweaks", padx=25.15, pady=12, fg="white", bg="#263D42", command=networkTweaks)
networkTweaks.place(relx=0.21, rely=0.675, anchor=CENTER)

latencyTweaks = tk.Button(Tweaks, text="Latency & BCD Tweaks", padx=10, pady=12, fg="white", bg="#263D42", command=latencyTweaks)
latencyTweaks.place(relx=0.810, rely=0.525, anchor=CENTER)

UndoTweaks = tk.Button(root, text="Undo Tweaks", padx=16, pady=11, fg="white", bg="#263D42", command=UndoTweaks)
UndoTweaks.place(relx=0.520, rely=0.8, anchor=CENTER)

ApplyNDrestart = tk.Button(root, text="Apply And Restart", padx=16, pady=11, fg="white", bg="#263D42", command=ApplyNDrestart)
ApplyNDrestart.place(relx=0.520, rely=0.925, anchor=CENTER)

AudioTweaks = tk.Button(Tweaks, text="Audio Tweaks", padx=31.225, pady=12, fg="white", bg="#263D42", command=AudioTweaks)
AudioTweaks.place(relx=0.21, rely=0.825, anchor=CENTER)

DisableDriverSearching = tk.Button(Tweaks, text="Disable Driver Searching", padx=2, pady=12, fg="white", bg="#263D42", command=DisableDriverSearching)
DisableDriverSearching.place(relx=0.81, rely=0.675, anchor=CENTER)

DisableWinUpdate = tk.Button(Tweaks, text="Disable Windows Updates", padx=2, pady=12, fg="white", bg="#263D42", command=DisableWinUpdate)
DisableWinUpdate.place(relx=0.21, rely=0.36, anchor=CENTER)

DisableMit = tk.Button(Tweaks, text="Disable Mitigations", padx=20, pady=12, fg="white", bg="#263D42", command=DisableMit)
DisableMit.place(relx=0.81, rely=0.825, anchor=CENTER)

#Apperance
TaskBar = tk.Button(Apperance, text="Taskbar customization", padx=20, pady=12, fg="white", bg="#263D42", command=TaskBar)
TaskBar.place(relx=0.81, rely=0.387, anchor=CENTER)

RoundedTB = tk.Button(Apperance, text="Install RoundedTB", padx=28, pady=12, fg="white", bg="#263D42", command=RoundedTB)
RoundedTB.place(relx=0.21, rely=0.55, anchor=CENTER)

Themes = tk.Button(Apperance, text="Themes customization", padx=20, pady=12, fg="white", bg="#263D42", command=Themes)
Themes.place(relx=0.21, rely=0.225, anchor=CENTER)

darkMode = tk.Button(Apperance, text="Enable Dark Mode", padx=30, pady=12, fg="white", bg="#263D42", command=darkMode)
darkMode.place(relx=0.21, rely=0.387, anchor=CENTER)

lightMode = tk.Button(Apperance, text="Enable Light Mode", padx=29, pady=12, fg="white", bg="#263D42", command=lightMode)
lightMode.place(relx=0.81, rely=0.225, anchor=CENTER)

CustStart = tk.Button(Apperance, text="Start Customization", padx=28, pady=12, fg="white", bg="#263D42", command=CustStart)
CustStart.place(relx=0.810, rely=0.55, anchor=CENTER)

ApplyNDrestartA = tk.Button(Apperance, text="Apply And Restart", padx=16, pady=11, fg="white", bg="#263D42", command=ApplyNDrestartA)
ApplyNDrestartA.place(relx=0.520, rely=0.925, anchor=CENTER)


#cleanup
TempFilesCleanup = tk.Button(Cleanup, text="Temp File Cleanup", padx=28, pady=12, fg="white", bg="#263D42", command=TempFilesCleanup)
TempFilesCleanup.place(relx=0.81, rely=0.387, anchor=CENTER)

diskcleanup = tk.Button(Cleanup, text="Disk Cleanup", padx=40, pady=12, fg="white", bg="#263D42", command=diskcleanup)
diskcleanup.place(relx=0.810, rely=0.55, anchor=CENTER)

disableautoruns = tk.Button(Cleanup, text="Disable autoruns", padx=20, pady=11, fg="white", bg="#263D42", command=disableautoruns)
disableautoruns.place(relx=0.810, rely=0.7, anchor=CENTER)

DisableOneDrive = tk.Button(Cleanup, text="Disable OneDrive", padx=35, pady=12, fg="white", bg="#263D42", command=DisableOneDrive)
DisableOneDrive.place(relx=0.21, rely=0.55, anchor=CENTER)

OldRestorePointCleanup = tk.Button(Cleanup, text="Delete Old Restore Points", padx=20, pady=12, fg="white", bg="#263D42", command=OldRestorePointCleanup )
OldRestorePointCleanup.place(relx=0.21, rely=0.225, anchor=CENTER)

WindowsUpdateCleanup = tk.Button(Cleanup, text="Windows Update cache Cleanup", padx=1, pady=12, fg="white", bg="#263D42", command=WindowsUpdateCleanup)
WindowsUpdateCleanup.place(relx=0.21, rely=0.375, anchor=CENTER)

LogFilesCleanup = tk.Button(Cleanup, text="Log File Cleanup", padx=38, pady=12, fg="white", bg="#263D42", command=LogFilesCleanup)
LogFilesCleanup.place(relx=0.81, rely=0.225, anchor=CENTER)

AdvancedDebloat = tk.Button(Cleanup, text="Advanced Debloat", padx=30, pady=12, fg="white", bg="#263D42", command=AdvancedDebloat )
AdvancedDebloat.place(relx=0.21, rely=0.7, anchor=CENTER)

ApplyNDrestart = tk.Button(Cleanup, text="Apply And Restart", padx=16, pady=11, fg="white", bg="#263D42", command=ApplyNDrestart)
ApplyNDrestart.place(relx=0.520, rely=0.925, anchor=CENTER)

#Debloat
msi = tk.Button(Advanced_Tweaks, text="Install MSI Afterburner", padx=8, pady=12, fg="white", bg="#263D42", command=MSI)
msi.place(relx=0.21, rely=0.2, anchor=CENTER)

msimodetool = tk.Button(Advanced_Tweaks, text="MSI Mode Tool", padx=42, pady=12, fg="white", bg="#263D42", command=msimodetool)
msimodetool.place(relx=0.81, rely=0.2, anchor=CENTER)

throttlestop = tk.Button(Advanced_Tweaks, text="Install Throttlestop", padx=15, pady=12, fg="white", bg="#263D42", command=throttlestop)
throttlestop.place(relx=0.21, rely=0.36, anchor=CENTER)

winprivdash = tk.Button(Advanced_Tweaks, text="Windows Privacy Dashboard", padx=20, pady=10, fg="white", bg="#263D42", command=winprivdash)
winprivdash.place(relx=0.81, rely=0.36, anchor=CENTER)

# right click
my_menu = Menu(root, tearoff=False)
my_menu.add_command(label="Show Credits", command=credits)
my_menu.add_command(label="Get Help", command=help)
my_menu.add_command(label="Edit Filter Options", command=browseFiles)
my_menu.add_separator()
my_menu.add_command(label="Exit", command=root.quit)

root.bind("<Button-3>", my_popup)
root.mainloop()
