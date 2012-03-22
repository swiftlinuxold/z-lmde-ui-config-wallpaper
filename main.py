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

def install_pkg_antix (name1, name2, url):
    # First check for package
    # Credit: http://stackoverflow.com/questions/3387961/check-if-a-package-is-installed
    devnull = open (os.devnull,"w")
    retval = subprocess.call(["dpkg","-s",name1],stdout=devnull,stderr=subprocess.STDOUT)
    devnull.close()
    if retval == 0:
        print (name1 + ' is already installed')
    else:
        print 'DOWNLOADING ' + name1 + ' FROM ' + url
        wget_command = 'wget -nv -nd -nH -r -l1 --wait=1 -erobots=off --no-parent -A '
        deb_file = name1 + '_*' + name2
        wget_command = wget_command + chr(39) + deb_file + chr(39) + ' '
        wget_command = wget_command + url
        print wget_command
        os.system (wget_command)
        os.system ('dpkg -i ' + deb_file)
        os.system ('rm ' + deb_file)

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
src = dir_develop + '/wallpaper/usr_share_backgrounds_swift/*'
dest = '/usr/share/backgrounds/swift'
os.system ('cp ' + src + ' ' + dest)

# Install yad
# install_pkg_antix ('yad', chr(45) + '1_i386.deb', 'http://debs.slavino.sk/pool/main/y/yad/')

# Install feh
# os.system ('apt-get install -y feh')


print 'FINISHED ADDING WALLPAPER WIZARD'
print '================================'
