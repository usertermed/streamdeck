# streamdeck
# installs steamtinkerlaunch (locally) and obs studio


import os

# variables
STL_GIT_REPO = "https://github.com/sonic2kk/SteamTinkerLaunch.git"
FLATHUB_REMOTE_URL = "https://flathub.org/repo/flathub.flatpakrepo"
OBS_STUDIO_FLATPAK = "org.obsproject.Studio"

print("Streamdeck ...")

print("Moving to home directory ...")
os.system("cd ~")
print("OK")

print("Cloning SteamTinkerLaunch from GitHub ...")
os.system("git clone " + STL_GIT_REPO)
print("OK")

print("Move into repository ...")
os.system("cd SteamTinkerLaunch")
print("OK")

print("Setting permissions for SteamTinkerLaunch ...")
os.system("chmod +rwx ./SteamTinkerLaunch")
print("OK")

print("SteamTinkerLaunch ready. Moving out ...")
os.system("cd ~")
print("OK")

print("Adding Flathub remote ...")
os.system("flatpak remote-add --if-not-exists flathub " + FLATHUB_REMOTE_URL)
print("OK")

print("Installing OBS Studio ...")
os.system("flatpak install flathub " + OBS_STUDIO_FLATPAK)
print("OK")

print("Cloning streamdeck repo for grids ...")
os.system("cd ~")
os.system("git clone https://github.com/usertermed/streamdeck")

print("OBS Studio ready. Adding to Steam ...")
os.system("cd ~/SteamTinkerLaunch")
os.system('./SteamTinkerLaunch ansg -an="OBS Studio" -ep="/usr/bin/flatpak" -sd="/usr/bin" -ip="~/streamdeck/grids/obs/icon.png" -lo="run com.obsproject.Studio" -hr="~/streamdeck/grids/obs/hero.png" -lg="~/streamdeck/grids/obs/logo.png" -ba="~/streamdeck/grids/obs/grid-small.png" -tf="~/streamdeck/grids/obs/grid-large.png"')

print("OBS Studio added to Steam.")