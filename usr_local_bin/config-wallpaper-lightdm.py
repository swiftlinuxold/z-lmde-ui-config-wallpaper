#! /usr/bin/env python

# This is the Python script for changing the wallpaper file specified in
# /etc/lightdm/lightdm-gtk-greeter.conf

def change_image (image_path):
    import fileinput
    for line in fileinput.input(dest,inplace =1):
        line = line.strip()
        if line.startswith ('background='):
            line = 'background='+image_path
        print line 

