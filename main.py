#! /usr/bin/env python

# Check for root user login
import os, sys
if not os.geteuid()==0:
    sys.exit("\nOnly root can run this script\n")

# Get your username (not root)
import pwd
uname=pwd.getpwuid(1000)[0]

# The remastering process uses chroot mode.
# Check to see if this script is operating in chroot mode.
# /home/mint directory only exists in chroot mode
is_chroot = os.path.exists('/home/mint')
dir_develop=''
if (is_chroot):
	dir_develop='/usr/local/bin/develop'
	dir_user = '/home/mint'
else:
	dir_develop='/home/' + uname + '/develop'
	dir_user = '/home/' + uname

# Everything up to this point is common to all Python scripts called by shared-*.sh
# =================================================================================

# THIS IS THE SCRIPT FOR ADDING THE SWIFT LINUX CONFIGURATION SCRIPTS

print '============================='
print 'BEGIN ADDING WALLPAPER WIZARD'

import shutil, subprocess

def purge_packages (packages):
    os.system ('echo PURGING ' + packages)
    os.system ('apt-get purge -y ' + packages)

def create_dir (dir_to_create):
    if not (os.path.exists(dir_to_create)):
        os.mkdir (dir_to_create)

# Remove original Linux Mint wallpaper to save space
print "REMOVING EXCESS WALLPAPERS"
purge_packages ('mint-artwork-debian mint-backgrounds-debian mint-meta-debian')
purge_packages ('mint-backgrounds-katya mint-backgrounds-katya-extra')

print "ADDING SWIFT LINUX WALLPAPER"
# Create directory for Swift Linux wallpaper
dir_wallpaper='/usr/share/backgrounds/swift'
create_dir ('/usr/share/backgrounds')
create_dir ('/usr/share/backgrounds/swift')

# Copy the wallpaper images to the Swift Linux wallpaper directory
src = dir_develop + '/ui-config-wallpaper/usr_share_backgrounds_swift/*'
dest = '/usr/share/backgrounds/swift'
os.system ('cp ' + src + ' ' + dest)

# Create the /home/(username)/.wallpaper directory
create_dir (dir_user + '/.wallpaper')
create_dir ('/etc/skel/.wallpaper')

# Put the essential files in the /home/(username)/.wallpaper directory
os.system ('cp ' + dir_develop + '/ui-config-wallpaper/home_user_dotwallpaper/* ' + dir_user + '/.wallpaper')
os.system ('cp ' + dir_develop + '/ui-config-wallpaper/home_user_dotwallpaper/* ' + '/etc/skel/.wallpaper')

src = dir_develop + '/ui-config-wallpaper/usr_local_bin/config-wallpaper-rox.py'
dest = '/usr/local/bin/config-wallpaper-rox.py'
os.system ('cp ' + src + ' ' + dest)
os.system ('chmod a+rwx ' + dest)

src = dir_develop + '/ui-config-wallpaper/usr_local_bin/config-wallpaper-lightdm.py'
dest = '/usr/local/bin/config-wallpaper-lightdm.py'
os.system ('cp ' + src + ' ' + dest)
os.system ('chmod a+rwx ' + dest)

src = dir_develop + '/ui-config-wallpaper/usr_local_bin/config-wallpaper.py'
dest = '/usr/local/bin/config-wallpaper.py'
os.system ('cp ' + src + ' ' + dest)
os.system ('chmod a+rwx ' + dest)

src = dir_develop + '/ui-config-wallpaper/usr_local_bin/Rox-Wallpaper'
dest = '/usr/local/bin/Rox-Wallpaper'
os.system ('cp ' + src + ' ' + dest)
os.system ('chmod a+rwx ' + dest)

# Install yad
install_pkg_antix ('yad', chr(45) + '1_i386.deb', 'http://debs.slavino.sk/pool/main/y/yad/')

# Install feh
os.system ('apt-get install -qq feh')

src = dir_develop + '/ui-config-wallpaper/home_user/dot_fehbg'
dest = dir_user + '/.fehbg'
os.system ('cp ' + src + ' ' + dest)

if (is_chroot):
    os.system ('chown -R mint:users ' + dir_user)
else:
    os.system ('chown -R ' + uname + ':users ' + dir_user)

print 'FINISHED ADDING WALLPAPER WIZARD'
print '================================'
