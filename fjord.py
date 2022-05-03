import tkinter as tk
from turtle import home
import webbrowser
from tkinter import *
from tkinter import filedialog, ttk
import os
import time



# GUI window
root = tk.Tk()
root.title("Fjord")
root.geometry('800x450')
icon=PhotoImage(file="assets\\logo.png")
root.iconphoto(False, icon)
root.resizable(0,0)
Tab_Control = ttk.Notebook(root)

#------ Tab Style -------#
style = ttk.Style()

style.theme_create('hi', settings={
    ".": {
        "configure": {
            "background": '#ffffff', # All except tabs
            "foreground": '#000000'     
        }
    },
    "TNotebook": {
        "configure": {
            "background":'#ffffff', # Your margin color
        }
    },
})
 
style.theme_use('hi')
#------ End -------#

#----TABS-----#

#start tab
Start = Frame(Tab_Control, width=800, height=450, bg='white')
Tab_Control.add(Start, text='Start')

#Tweaks Tab
Tweaks = Frame(Tab_Control, width=800, height=450, bg='white')
#bg='white'
Tab_Control.add(Tweaks, text='Tweaks')

#Extras Tab
Extra = Frame(Tab_Control, width=800, height=450, bg='white')
Tab_Control.add(Extra, text='Extra')
Tab_Control.pack(expand=3, fill="both")

#Security Tab
Security = Frame(Tab_Control, width=800, height=450, bg='white')
Tab_Control.add(Security, text='Security')

#Cleanup Tab
Cleanup = Frame(Tab_Control, width=800, height=450, bg='white')
Tab_Control.add(Cleanup, text='Cleanup')
Tab_Control.pack(expand=3, fill="both")

#Programs Tab
Programs = Frame(Tab_Control, width=800, height=450, bg='white')
Tab_Control.add(Programs, text='Programs')
Tab_Control.pack(expand=3, fill="both")

#Tab Name Labels
ttk.Label(Tweaks, text="").grid(column=0, row=0, padx=10, pady=10)
ttk.Label(Security, text="").grid(column=0, row=0, padx=10, pady=10)


#------- Scrollbar --------#

#Start_Canvas = Canvas(Start)
#Start_Canvas.pack(side=LEFT, fill=BOTH, expand=1)

#Start_Scrollbar = ttk.Scrollbar(Start, orient=VERTICAL, command=Start_Canvas.yview)
#Start_Scrollbar.pack(side=RIGHT, fill=Y)

#Start_Canvas.configure(yscrollcommand=Start_Scrollbar.set)
#Start_Canvas.bind('<Configure>', lambda e: Start_Canvas.configure(scrollregion = Start_Canvas.bbox("all")))

#second_frame = Frame(Start_Canvas)

#Start_Canvas.create_window((0,0), window = second_frame)

#----- Scrollbar -----#


#----BUTTON FUNCTIONS-----#


#Start Button Function
def ApplyNDrestart():
    os.system("shutdown /r /t 1")

def dkmd():
    Start.config(bg='black')
    Tweaks.config(bg='black')
    Security.config(bg='black')
    Cleanup.config(bg='black')
    Programs.config(bg='black')
    Extra.config(bg='black')

def lkmd():
    Start.config(bg='white')
    Tweaks.config(bg='white')
    Security.config(bg='white')
    Cleanup.config(bg='white')
    Programs.config(bg='white')
    Extra.config(bg='white')

def UndoTweaks():
    os.startfile('lib\\links\\Create A Restore Point.lnk')
    input('Press ENTER to exit')

def readDocs():
    webbrowser.open('https://github.com/x1comp/Fjord/blob/main/README.md')

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

def DisableOneDrive():
    os.system(r''' Powershell -Command "& { Start-Process \"lib\\bat\\OneDrive Uninstaller v0.4.cmd\" -ArgumentList @("\"lib\\bat\\OneDrive Uninstaller v0.4.cmd\"") -Verb RunAs } " ''')
    input('Press ENTER to exit')

def msimodetool():
   os.system(r''' Powershell -Command "& { Start-Process \"lib\\3 MSI Mode Tool.exe\" -ArgumentList @(\"lib\\3 MSI Mode Tool.exe\"") -Verb RunAs } " ''')

def winprivdash():
     os.startfile('lib\\Windows Privacy Dashboard.exe')

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

def disableautoruns():
   os.startfile('lib\\4 AutoRuns.exe')
   input('Press ENTER to exit')
    
def networkTweaks():
    os.system(r''' Powershell -Command "& { Start-Process \"lib\\bat\\IPConfig.bat\" -ArgumentList @(\"lib\\bat\\IPConfig.bat\") -Verb RunAs } " ''')
    input('Press ENTER to exit')
    time.sleep(1)
    os.system(r''' Powershell -Command "& { Start-Process \"lib\\bat\\Network Latency Optimizations.cmd\" -ArgumentList @(\"lib\\bat\\Network Latency Optimizations.cmd\") -Verb RunAs } " ''')
    input('Press ENTER to exit')
    
def DisableDriverSearching():
    os.startfile('lib\\reg\\Disable Automatic Driver Updates.reg')
    input('Press ENTER to exit')

def DisableWinUpdate():
    os.system(r''' Powershell -Command "& { Start-Process \"lib\\bat\\Turn Off Auto Windows Updates.cmd\" -ArgumentList @(\"lib\\bat\\Turn Off Auto Windows Updates.cmd\") -Verb RunAs } " ''')

def disablePOWT():
    os.startfile('lib\\reg\\PowerThrottling.reg')
    #os.system(r''' Powershell -Command "& { Start-Process \"lib\\reg\\Disable Power Throttling.reg\" -ArgumentList @(\"lib\\reg\\Disable Power Throttling.reg\") -Verb RunAs } " ''')

def disableSPECNDMELT():
    os.startfile('lib\\reg\\Disable Spectre Meltdown Protection.reg')
    #os.system(r''' Powershell -Command "& { Start-Process \"lib\\reg\\Disable Spectre Meltdown Protection.reg\" -ArgumentList @(\"lib\\reg\\Disable Spectre Meltdown Protection.reg\") -Verb RunAs } " ''')

def disableAMSE():
    os.system(r''' Powershell -Command "& { Start-Process \"lib\\dControl.exe\" -ArgumentList @(\"lib\\bat\\dControl.exe\") -Verb RunAs } " ''')
    input('Press ENTER to exit')

def kydataqsize():
    os.startfile('lib\\reg\\KeyboardDataQueueSize.reg')
    #os.system(r''' Powershell -Command "& { Start-Process \"lib\\reg\\KeyboardDataQueueSize.reg\" -ArgumentList @(\"lib\\reg\\KeyboardDataQueueSize.reg\") -Verb RunAs } " ''')

def Mousedataqsize():
    os.startfile('lib\\reg\\MouseDataQueueSize.reg')
    #os.system(r''' Powershell -Command "& { Start-Process \"lib\\reg\\MouseDataQueueSize.reg\" -ArgumentList @(\"lib\\reg\\MouseDataQueueSize.reg\") -Verb RunAs } " ''')

def DisableMit():
    os.startfile('lib\\reg\\Disable Mitigations.reg')
    input('Press ENTER to exit')

#Extra Button Functions

def DisableMouseacc():
    os.startfile('lib\\reg\\M2 MarkC Windows 10 Mouse Fix.reg')

def DisableDrivUpdate():
  os.system(r''' Powershell -Command "& { Start-Process \"lib\\bat\\6 Disable Memory Compression.cmd\" -ArgumentList @(\"lib\\bat\\6 Disable Memory Compression.cmd\") -Verb RunAs } " ''') 

def DisableFSO():
    os.startfile('lib\\reg\\Disable FSO.reg')

def DisableTransparency():
    os.startfile('lib\\reg\\Disable Transparency.reg')

def DisableGameDVR():
    os.startfile('lib\\reg\\Disable Game DVR.reg')

def filesys():
    os.startfile('lib\\reg\\File System.reg')

def photoviewer():
    os.startfile('lib\\reg\\Windows Photo Viewer.reg')

def Disablebluetooth():
    os.startfile('lib\\reg\\OPTIONAL Disable Bluetooth Services.reg')

def DisableMaps():
    os.startfile('lib\\reg\\OPTIONAL Disable Download Maps Manager.reg')

def DisablePrint():
    os.startfile('lib\\reg\\OPTIONAL Disable Printer Services.reg')

def LargeFilesysCache():
    os.startfile('lib\\reg\\LargeSystemCache.reg')

def DELPOW():
    os.startfiLE('lib\\bat\\Delete Other Power Plans.cmd')

def ImportPOW():
    os.startfile('lib\\bat\\Snowy POW.cmd')


# Security Button Functions
def dism():
    os.system(r''' Powershell -Command "& { Start-Process \"lib\\bat\\dism.cmd\" -ArgumentList @(\"lib\\bat\\dism.cmd\") -Verb RunAs } " ''')
    input('Press ENTER to exit')

def RoundedTB():
    webbrowser.open('https://github.com/torchgm/RoundedTB/releases/tag/R3.1')

def sfc():
    os.system(r''' Powershell -Command "& { Start-Process \"lib\\bat\\sfc.cmd\" -ArgumentList @(\"lib\\bat\\sfc.cmd\") -Verb RunAs } " ''')
    input('Press ENTER to exit')
    
def MalwareBytes():
    webbrowser.open('https://www.malwarebytes.com/mwb-download')
    input('Press ENTER to exit')
    
def disableAMSES():
    os.system(r''' Powershell -Command "& { Start-Process \"lib\\dControl.exe\" -ArgumentList @(\"lib\\bat\\dControl.exe\") -Verb RunAs } " ''')
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

#Programs

def DS4WIN():
    webbrowser.open('https://github.com/Ryochan7/DS4Windows/releases')

def TIMRES():
    webbrowser.open('https://timerresolution.net/')

def KEY2X():
    webbrowser.open('https://www.embenco.nl/keys2xinput/download/')

def MSI():
    webbrowser.open('https://www.msi.com/Landing/afterburner/graphics-cards')

def throttlestop():
    webbrowser.open('https://www.techpowerup.com/download/techpowerup-throttlestop/')

#right click button functions
def help():
    webbrowser.open('https://github.com/x1comp/Fjordio/blob/main/README.md')

def credits():
	webbrowser.open('https://github.com/x1comp/Fjord/README.md')

def my_popup(e):
	my_menu.tk_popup(e.x_root, e.y_root)

def browseFiles():
    filedialog.askopenfilename(initialdir = "lib", title = "Select a File", filetypes = (("all files","*.*"), ("Text files", "*.txt*"),))
 #----TAB BUTTONS----#   


#Start
img=PhotoImage(file='assets\\logo.png')
Label(Start,image=img, width=50, height=60). place(relx=0.5, rely=0.2, anchor=CENTER)

ApplyNDrestart = tk.Button(Start, text="Apply And Restart", padx=20, pady=10, fg="white", bg="#263D42", command=ApplyNDrestart)
ApplyNDrestart.place(relx=0.5, rely=0.9, anchor=CENTER)

UndoTweaks = tk.Button(Start, text="Undo Tweaks", padx=20, pady=10, fg="white", bg="#263D42", command=UndoTweaks)
UndoTweaks.place(relx=0.5, rely=0.75, anchor=CENTER)

dkmd = tk.Button(Start, text="Enable Dark Mode", padx=15, pady=10, fg="white", bg="#263D42", command=dkmd)
dkmd.place(relx=0.215, rely=0.9, anchor=CENTER)

lkmd = tk.Button(Start, text="Enable Light Mode", padx=15, pady=10, fg="white", bg="#263D42", command=lkmd)
lkmd.place(relx=0.815, rely=0.9, anchor=CENTER)

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

DisableWinDefender = tk.Button(Tweaks, text="Disable Windows Defender", padx=1, pady=12, fg="white", bg="#263D42", command=DisableWinDefender)
DisableWinDefender.place(relx=0.16, rely=0.14, anchor=CENTER)

DisableWinUpdate = tk.Button(Tweaks, text="Disable Windows Updates", padx=2, pady=12, fg="white", bg="#263D42", command=DisableWinUpdate)
DisableWinUpdate.place(relx=0.16, rely=0.3, anchor=CENTER)

winTweaks = tk.Button(Tweaks, text="Windows Tweaks", padx=24, pady=11, fg="white", bg="#263D42", command=winTweaks)
winTweaks.place(relx=0.16, rely=0.46, anchor=CENTER)

networkTweaks = tk.Button(Tweaks, text="Network Tweaks", padx=25.15, pady=10, fg="white", bg="#263D42", command=networkTweaks)
networkTweaks.place(relx=0.16, rely=0.62, anchor=CENTER)

AudioTweaks = tk.Button(Tweaks, text="Audio Tweaks", padx=31.225, pady=10, fg="white", bg="#263D42", command=AudioTweaks)
AudioTweaks.place(relx=0.16, rely=0.78, anchor=CENTER)

disableautoruns = tk.Button(Tweaks, text="Disable autoruns", padx=20, pady=11, fg="white", bg="#263D42", command=disableautoruns)
disableautoruns.place(relx=0.38, rely=0.143, anchor=CENTER)

DisableOneDrive = tk.Button(Tweaks, text="Disable OneDrive", padx=20, pady=10, fg="white", bg="#263D42", command=DisableOneDrive)
DisableOneDrive.place(relx=0.38, rely=0.3, anchor=CENTER)

regTweaks = tk.Button(Tweaks, text="Registry Tweaks", padx=24, pady=10, fg="white", bg="#263D42", command=regTweaks)
regTweaks.place(relx=0.38, rely=0.46, anchor=CENTER)

AdvancedDebloat = tk.Button(Tweaks, text="Advanced Debloat", padx=16, pady=10, fg="white", bg="#263D42", command=AdvancedDebloat )
AdvancedDebloat.place(relx=0.38, rely=0.62, anchor=CENTER)

xbxTweaks = tk.Button(Tweaks, text="Disable Xbox Game Bar", padx=10, pady=10, fg="white", bg="#263D42", command=xbxTweaks)
xbxTweaks.place(relx=0.6, rely=0.14, anchor=CENTER)

latencyTweaks = tk.Button(Tweaks, text="Latency & BCD Tweaks", padx=10, pady=10, fg="white", bg="#263D42", command=latencyTweaks)
latencyTweaks.place(relx=0.6, rely=0.3, anchor=CENTER)

msimodetool = tk.Button(Tweaks, text="MSI Mode Tool", padx=26, pady=10, fg="white", bg="#263D42", command=msimodetool)
msimodetool.place(relx=0.38, rely=0.78, anchor=CENTER)

winprivdash = tk.Button(Tweaks, text="Windows Privacy Dashboard", padx=10, pady=10, fg="white", bg="#263D42", command=winprivdash)
winprivdash.place(relx=0.6, rely=0.78, anchor=CENTER)

DisableDriverSearching = tk.Button(Tweaks, text="Disable Driver Searching", padx=2, pady=10, fg="white", bg="#263D42", command=DisableDriverSearching)
DisableDriverSearching.place(relx=0.6, rely=0.46, anchor=CENTER)

DisableMit = tk.Button(Tweaks, text="Disable Mitigations", padx=20, pady=10, fg="white", bg="#263D42", command=DisableMit)
DisableMit.place(relx=0.6, rely=0.62, anchor=CENTER)

disableAMSE = tk.Button(Tweaks, text="Disable AMSE", padx=34, pady=10, fg="white", bg="#263D42", command=disableAMSE)
disableAMSE.place(relx=0.84, rely=0.14, anchor=CENTER)

disablePOWT = tk.Button(Tweaks, text="Disable Power Throttling", padx=10, pady=10, fg="white", bg="#263D42", command=disablePOWT)
disablePOWT.place(relx=0.84, rely=0.3, anchor=CENTER)

disableSPECNDMELT = tk.Button(Tweaks, text="Disable Spectre & Meltdown", padx=10, pady=10, fg="white", bg="#263D42", command=disableSPECNDMELT)
disableSPECNDMELT.place(relx=0.84, rely=0.46, anchor=CENTER)

kydataqsize = tk.Button(Tweaks, text="Keyboard Data Queue Size", padx=4, pady=10, fg="white", bg="#263D42", command=kydataqsize)
kydataqsize.place(relx=0.84, rely=0.62, anchor=CENTER)

Mousedataqsize = tk.Button(Tweaks, text="Mouse Data Queue Size", padx=4, pady=10, fg="white", bg="#263D42", command=Mousedataqsize)
Mousedataqsize.place(relx=0.84, rely=0.78, anchor=CENTER)

#Extras

DisablePrint = tk.Button(Extra, text="Disable Print Services", padx=10, pady=10, fg="white", bg="#263D42", command=DisablePrint)
DisablePrint.place(relx=0.16, rely=0.14, anchor=CENTER)

Disablebluetooth = tk.Button(Extra, text="Disable Bluetooth Services", padx=10, pady=10, fg="white", bg="#263D42", command=Disablebluetooth)
Disablebluetooth.place(relx=0.38, rely=0.143, anchor=CENTER)

DisableMaps = tk.Button(Extra, text="Disable Maps Services", padx=10, pady=10, fg="white", bg="#263D42", command=DisableMaps)
DisableMaps.place(relx=0.6, rely=0.14, anchor=CENTER)

DisableMouseacc = tk.Button(Extra, text="Disable Mouse accelaration", padx=1, pady=10, fg="white", bg="#263D42", command=DisableMouseacc)
DisableMouseacc.place(relx=0.84, rely=0.14, anchor=CENTER)

DisableDrivUpdate = tk.Button(Extra, text="Disable Memory Compression", padx=1, pady=10, fg="white", bg="#263D42", command=DisableDrivUpdate)
DisableDrivUpdate.place(relx=0.16, rely=0.3, anchor=CENTER)

DisableFSO = tk.Button(Extra, text="Disable FSO", padx=40, pady=10, fg="white", bg="#263D42", command=DisableFSO)
DisableFSO.place(relx=0.38, rely=0.3, anchor=CENTER)

filesys = tk.Button(Extra, text="Windows File System Tweaks", padx=10, pady=10, fg="white", bg="#263D42", command=filesys)
filesys.place(relx=0.6, rely=0.3, anchor=CENTER)

photoviewer = tk.Button(Extra, text="Windows Photo Viewer Tweaks", padx=10, pady=10, fg="white", bg="#263D42", command=photoviewer)
photoviewer.place(relx=0.84, rely=0.3, anchor=CENTER)

DisableGameDVR = tk.Button(Extra, text="Disable Game DVR", padx=300, pady=10, fg="white", bg="#263D42", command=DisableGameDVR)
DisableGameDVR.place(relx=0.5, rely=0.45, anchor=CENTER)

LargeFilesysCache = tk.Button(Extra, text="Large File system Cache Tweaks", padx=265, pady=10, fg="white", bg="#263D42", command=LargeFilesysCache)
LargeFilesysCache.place(relx=0.5, rely=0.575, anchor=CENTER)

DELPOW = tk.Button(Extra, text="Delete Power Plans", padx=300, pady=10, fg="white", bg="#263D42", command=DELPOW)
DELPOW.place(relx=0.5, rely=0.7, anchor=CENTER)

ImportPOW = tk.Button(Extra, text="Import Performance POW", padx=285, pady=10, fg="white", bg="#263D42", command=ImportPOW)
ImportPOW.place(relx=0.5, rely=0.825, anchor=CENTER)



#Security
dism = tk.Button(Security, text="Dism scan", padx=94, pady=10, fg="white", bg="#263D42", command=dism)
dism.place(relx=0.5, rely=0.35, anchor=CENTER)

#RoundedTB = tk.Button(Security, text="Install RoundedTB", padx=28, pady=10, fg="white", bg="#263D42", command=RoundedTB)
#RoundedTB.place(relx=0.21, rely=0.55, anchor=CENTER)

sfc = tk.Button(Security, text="sfc scan", padx=100, pady=10, fg="white", bg="#263D42", command=sfc)
sfc.place(relx=0.5, rely=0.2, anchor=CENTER)

MalwareBytes = tk.Button(Security, text="Install MalwareBytes", padx=72, pady=10, fg="white", bg="#263D42", command=MalwareBytes)
MalwareBytes.place(relx=0.5, rely=0.5, anchor=CENTER)

disableAMSES = tk.Button(Security, text="Disable AMSE", padx=90, pady=10, fg="white", bg="#263D42", command=disableAMSES)
disableAMSES.place(relx=0.5, rely=0.65, anchor=CENTER)

#CustStart = tk.Button(Security, text="Start Customization", padx=28, pady=12, fg="white", bg="#263D42", command=CustStart)
#CustStart.place(relx=0.810, rely=0.55, anchor=CENTER)

#cleanup
TempFilesCleanup = tk.Button(Cleanup, text="Temp File Cleanup", padx=100, pady=10, fg="white", bg="#263D42", command=TempFilesCleanup)
TempFilesCleanup.place(relx=0.5, rely=0.35, anchor=CENTER)

diskcleanup = tk.Button(Cleanup, text="Disk Cleanup", padx=140, pady=10, fg="white", bg="#263D42", command=diskcleanup)
diskcleanup.place(relx=0.5, rely=0.8, anchor=CENTER)

OldRestorePointCleanup = tk.Button(Cleanup, text="Delete Old Restore Points", padx=100, pady=10, fg="white", bg="#263D42", command=OldRestorePointCleanup )
OldRestorePointCleanup.place(relx=0.5, rely=0.65, anchor=CENTER)

WindowsUpdateCleanup = tk.Button(Cleanup, text="Windows Update cache Cleanup", padx=75, pady=10, fg="white", bg="#263D42", command=WindowsUpdateCleanup)
WindowsUpdateCleanup.place(relx=0.5, rely=0.5, anchor=CENTER)

LogFilesCleanup = tk.Button(Cleanup, text="Log File Cleanup", padx=100, pady=10, fg="white", bg="#263D42", command=LogFilesCleanup)
LogFilesCleanup.place(relx=0.5, rely=0.2, anchor=CENTER)

#Debloat
MSI = tk.Button(Programs, text="Install MSI Afterburner", padx=85, pady=10, fg="white", bg="#263D42", command=MSI)
MSI.place(relx=0.5, rely=0.15, anchor=CENTER)

throttlestop = tk.Button(Programs, text="Install Throttlestop", padx=100, pady=10, fg="white", bg="#263D42", command=throttlestop)
throttlestop.place(relx=0.5, rely=0.3, anchor=CENTER)

DS4WIN = tk.Button(Programs, text="Install DS4Windows", padx=100, pady=10, fg="white", bg="#263D42", command=DS4WIN)
DS4WIN.place(relx=0.5, rely=0.45, anchor=CENTER)

TIMRES = tk.Button(Programs, text="Install Windows Timer Resolution", padx=65, pady=10, fg="white", bg="#263D42", command=TIMRES)
TIMRES.place(relx=0.5, rely=0.6, anchor=CENTER)

KEY2X = tk.Button(Programs, text="Install Keys2x", padx=120, pady=10, fg="white", bg="#263D42", command=KEY2X)
KEY2X.place(relx=0.5, rely=0.75, anchor=CENTER)

# right click
my_menu = Menu(root, tearoff=False)
my_menu.add_command(label="Show Credits", command=credits)
my_menu.add_command(label="Get Help", command=help)
my_menu.add_command(label="Edit Filter Options", command=browseFiles)
my_menu.add_separator()
my_menu.add_command(label="Exit", command=root.quit)

root.bind("<Button-3>", my_popup)
root.mainloop()
