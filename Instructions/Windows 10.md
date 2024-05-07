#todo 
after installation:

activate windows
disable uac
nextvpn \#connect
update windows
disable defender: gpedit.msc -> administrative templates/windows components/windows defender antivirus

\#restart to firmware options
firmware:turn off fastboot
firmware:turn legacy mode from enabled to auto
(??) turn cmw off (??)

turn windows fast startup off

install applications:
winrar
chrome
nvidia driver
drivers
RuntimePack.20. (soft98)

\#restart

idm
idmbackup \#restore
poweriso
adobe reader
clover
FxSound enhancer
mbc-be
spotify
telegram
windirstat

\#restart

microsoft office 2019: word, excel, powerpoint

\#airplane mode, install, add to to firewall
lightroom
photoshop
premiere
after effects
audition
audacity

git
python
slack
postgres
pycharm

oxford
longman

\#restart

elCapitan cursor
setting:
 system:
  display:
   set scale to 117
  notification:
   edit quick actions:
    network bluetooth night-light airplane-mode
   disable "show me the window..."
   disable "suggest ways i can fini..."
   disable "get tips, tricks, and ..."
  focus assist:
   off
  power & sleep:
   all on never
  clipboard:
   history -> on
 devices:
  touchpad:
   threefinger-swipes: switch desktops and show desktop
   threefinger-taps: action center
   fourfinger-swipes: change audio and volumes
   fourfinger-taps: play/pause
  typing:
   disable spelling-autocorrect_misspelled_words
   enable multilingual_text_suggestion
  autoplay:
   set all to take_no_action
 personalization:
  background
  colors:
   set to \#32522A
   enable transparency
   enable start, taskbar and action center
   enable title bars and window borders
  lock screen
  start:
   turn off all
   choose which folders apear... -> only enable settings
  taskbar:
   automatically hide the taskbar
   use small buttons
   use peek to preview
   select which icons appear on the taskbar:
    speedvpn power netword volume telegram slack bluetooth windows_explorer(safely...)
 apps:
  apps&features:
   removed candy crush
   cortana -> advanced options -> app permissions -> disable background apps
   removed farm heroes saga
   removed feedback hub
   get help -> advanced options -> app permissions -> disable background apps
   removed groove music
   maps -> advanced options -> app permissions -> disable background apps
   removed onedrive
   removed solitaire collection
   removed mixed reality portal
   removed movies&tv
   removed office
   removed onenote
   sticky notes -> advanced options -> app permissions -> disable background apps
   removed weather
   removed xbox
   removed xbox live
  default apps:
   email: mail
   music: mbc
   video: mbc
   photo: photos
   web: chrome
  startup:
   disable poweriso
   disable spotify
 Accounts:
  your info: signed in
  email&accounts: fix sync settings
  sign-in: setup pin
 Time & language:
  date & time:
   set time automatically
   time zone: tehran
 Gaming:
  Xbox Game Bar: DISABLE
  game mode: off
 Ease of Access:
  keyboard:
   enable "use the PrtScn button to open..."
 Search:
  Permissions & history:
   safesearch: off
  Searching Windows:
   Find my files: enhanced
 Privacy:
  General:
   only enable "Let windows track app launches to improve start ..."
  Diagnostics & Feedback: 
   Feedback frequency:
    NEVER
  Background Apps:
   only enable:
    Alarms & Clock
    Mail & Calendar
    People
    Settings
    Snip & Sketch
    Spotify
    Voice Recorder
    Windows Security

disable windows update: 
	services.msc -> Windows update -> Startup type (Disabled) -> Apply -> ok
	gpedit.msc -> administrative templates -> windows components -> windows update -> configure automatic update (disable)
	meter your network connection
	regedit -> HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU -> create new DWORD(32bit) named AUOptions -> set value to 2

\#restart