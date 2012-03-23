#!/usr/bin/env python
# Dependencies: feh, rox (pinboard), randwallpaper.sh, login_background.sh,
#               gtk, pygtk
# File Name: wallpaper.py
# Version: 1.5.0
# Purpose: allows the user to select a meathod for setting the wallpaper, 
#          as well as a wallpaper / color / default folder based on their
#          choice of options
# Authors: Dave

# Copyright (C) antiXCommunity http://antix.freeforums.org
# License: gplv2
# This file is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
################################################################################
#################################################################
import pygtk, gtk
pygtk.require('2.0')
import os

#Set variables
HELPFILE = os.path.expanduser("~/.wallpaper/help.txt")
DEFAULT = "/usr/share/wallpaper-antix/wallpaper-none.png"
USERFOLDER = os.path.expanduser("~/.wallpaper")
SAVED = os.path.expanduser("~/.wallpaper/saved")
SAVEDSESSION = os.path.expanduser("~/.wallpaper/session")
SETTYPE = os.path.expanduser("~/.wallpaper/set-type")
COLOR = os.path.expanduser("~/.wallpaper/color")
BACKFOLDER = os.path.expanduser("~/.wallpaper/background_folder")
SAVEDCHECK = os.path.isfile(SAVED)

if (SAVEDCHECK) == (False):
  os.system("cp -r /usr/share/wallpaper-antix/SKEL $HOME/.wallpaper;")
  
text = open((SAVED), "r")
LINES = text.readline()
IMAGE = LINES.split('\n', 1)[0]
text.close()

text = open((SAVEDSESSION), "r")
LINES = text.readline()
SESSION = LINES.split('\n', 1)[0]
text.close

text = open((HELPFILE), "r")
HELPTEXT = text.read()
text.close

class Base:

    def set (self, widget):
      if SESSION == "rox-icewm":
        model = self.combo.get_model()
        index = self.combo.get_active()
        if index:
          TAPPLY = model[index][0]
          if TAPPLY == "Random Wallpaper":
            pic = file((SAVED), "w")
            pic.write (DEFAULT) 
            pic.close()
            pic = file((SETTYPE), "w")
            pic.write ("random") 
            pic.close()
            os.system("echo 'random' > $HOME/.wallpaper/set-type && randwallpaper.sh")
          elif TAPPLY == "Random Wallpaper Timed":
            pic = file((SAVED), "w")
            pic.write (DEFAULT) 
            pic.close()
            pic = file((SETTYPE), "w")
            pic.write ("random-time") 
            pic.close()
            os.system("login_background.sh &")
          elif TAPPLY == "No Wallpaper":
            pic = file((SAVED), "w")
            pic.write (DEFAULT) 
            pic.close()
            pic = file((SETTYPE), "w")
            pic.write ("color")
            pic.close()
            os.system("xsetroot -solid \"`cat $HOME/.wallpaper/color`\" && echo 'color' > $HOME/.wallpaper/set-type  && xrefresh")
          elif TAPPLY == "Scale":
            pic = file((SAVED), "w")
            pic.write (IMAGE) 
            pic.close()
            pic = file((SETTYPE), "w")
            pic.write ("static" )
            pic.close()
            os.system("Rox-Wallpaper `cat $HOME/.wallpaper/saved` && feh --bg-scale `cat $HOME/.wallpaper/saved` && cp ~/.fehbg ~/.wallpaper/feh-bg.rox-ice && xrefresh")
          elif TAPPLY == "Center":
            pic = file((SAVED), "w")
            pic.write (IMAGE) 
            pic.close()
            pic = file((SETTYPE), "w")
            pic.write ("static" )
            pic.close()
            os.system("Rox-Wallpaper `cat $HOME/.wallpaper/saved` && feh --bg-center `cat $HOME/.wallpaper/saved` && cp ~/.fehbg ~/.wallpaper/feh-bg.rox-ice && xrefresh") 
          elif TAPPLY == "Fill":
            pic = file((SAVED), "w")
            pic.write (IMAGE) 
            pic.close()
            pic = file((SETTYPE), "w")
            pic.write ("static" )
            pic.close()
            os.system("Rox-Wallpaper `cat $HOME/.wallpaper/saved` && feh --bg-fill `cat $HOME/.wallpaper/saved` && cp ~/.fehbg ~/.wallpaper/feh-bg.rox-ice && xrefresh")
      elif SESSION == "rox-fluxbox":
        model = self.combo.get_model()
        index = self.combo.get_active()			
        if index:
          TAPPLY = model[index][0] 
          if TAPPLY == "Random Wallpaper":
            pic = file((SAVED), "w")
            pic.write (DEFAULT) 
            pic.close()
            pic = file((SETTYPE), "w")
            pic.write ("random") 
            pic.close()
            os.system("echo 'random' > $HOME/.wallpaper/set-type && randwallpaper.sh")
          elif TAPPLY == "Random Wallpaper Timed":
            pic = file((SAVED), "w")
            pic.write (DEFAULT) 
            pic.close()
            pic = file((SETTYPE), "w")
            pic.write ("random-time") 
            pic.close()
            os.system("login_background.sh &")
          elif TAPPLY == "No Wallpaper":
            pic = file((SAVED), "w")
            pic.write (DEFAULT) 
            pic.close()
            pic = file((SETTYPE), "w")
            pic.write ("color")
            pic.close()
            os.system("xsetroot -solid \"`cat $HOME/.wallpaper/color`\" && echo 'color' > $HOME/.wallpaper/set-type  && xrefresh")
          elif TAPPLY == "Scale": 
            pic = file((SAVED), "w")
            pic.write (IMAGE) 
            pic.close()
            pic = file((SETTYPE), "w")
            pic.write ("static" )
            pic.close()
            os.system("Rox-Wallpaper `cat $HOME/.wallpaper/saved` && feh --bg-scale `cat $HOME/.wallpaper/saved` && cp ~/.fehbg ~/.wallpaper/feh-bg.rox-fb && xrefresh")
          elif TAPPLY == "Center":
            pic = file((SAVED), "w")
            pic.write (IMAGE) 
            pic.close()
            pic = file((SETTYPE), "w")
            pic.write ("static" )
            pic.close()
            os.system("Rox-Wallpaper `cat $HOME/.wallpaper/saved` && feh --bg-center `cat $HOME/.wallpaper/saved` && cp ~/.fehbg ~/.wallpaper/feh-bg.rox-fb && xrefresh")
          elif TAPPLY == "Fill":
            pic = file((SAVED), "w")
            pic.write (IMAGE) 
            pic.close()
            pic = file((SETTYPE), "w")
            pic.write ("static" )
            pic.close()
            os.system("Rox-Wallpaper `cat $HOME/.wallpaper/saved` && feh --bg-fill `cat $HOME/.wallpaper/saved` && cp ~/.fehbg ~/.wallpaper/feh-bg.rox-fb && xrefresh")
      elif SESSION == "rox-jwm":
        model = self.combo.get_model()
        index = self.combo.get_active()			
        if index:
          TAPPLY = model[index][0] 
          if TAPPLY == "Random Wallpaper":
            pic = file((SAVED), "w")
            pic.write (DEFAULT) 
            pic.close()
            pic = file((SETTYPE), "w")
            pic.write ("random") 
            pic.close()
            os.system("echo 'random' > $HOME/.wallpaper/set-type && randwallpaper.sh")
          elif TAPPLY == "Random Wallpaper Timed":
            pic = file((SAVED), "w")
            pic.write (DEFAULT) 
            pic.close()
            pic = file((SETTYPE), "w")
            pic.write ("random-time") 
            pic.close()
            os.system("login_background.sh &")
          elif TAPPLY == "No Wallpaper":
            pic = file((SAVED), "w")
            pic.write (DEFAULT) 
            pic.close()
            pic = file((SETTYPE), "w")
            pic.write ("color")
            pic.close()
            os.system("xsetroot -solid \"`cat $HOME/.wallpaper/color`\" && echo 'color' > $HOME/.wallpaper/set-type  && xrefresh")
          elif TAPPLY == "Scale": 
            pic = file((SAVED), "w")
            pic.write (IMAGE) 
            pic.close()
            pic = file((SETTYPE), "w")
            pic.write ("static" )
            pic.close()
            os.system("Rox-Wallpaper `cat $HOME/.wallpaper/saved` && feh --bg-scale `cat $HOME/.wallpaper/saved` && cp ~/.fehbg ~/.wallpaper/feh-bg.rox-jwm && xrefresh")
          elif TAPPLY == "Center":
            pic = file((SAVED), "w")
            pic.write (IMAGE) 
            pic.close()
            pic = file((SETTYPE), "w")
            pic.write ("static" )
            pic.close()
            os.system("Rox-Wallpaper `cat $HOME/.wallpaper/saved` && feh --bg-center `cat $HOME/.wallpaper/saved` && cp ~/.fehbg ~/.wallpaper/feh-bg.rox-jwm && xrefresh")
          elif TAPPLY == "Fill":
            pic = file((SAVED), "w")
            pic.write (IMAGE) 
            pic.close()
            pic = file((SETTYPE), "w")
            pic.write ("static" )
            pic.close()
            os.system("Rox-Wallpaper `cat $HOME/.wallpaper/saved` && feh --bg-fill `cat $HOME/.wallpaper/saved` && cp ~/.fehbg ~/.wallpaper/feh-bg.rox-jwm && xrefresh")
      elif SESSION == "icewm":
        model = self.combo.get_model()
        index = self.combo.get_active()
        if index:
          TAPPLY = model[index][0]
          if TAPPLY == "Random Wallpaper":
            pic = file((SAVED), "w")
            pic.write (DEFAULT) 
            pic.close()
            pic = file((SETTYPE), "w")
            pic.write ("random") 
            pic.close()
            os.system("echo 'random' > $HOME/.wallpaper/set-type && randwallpaper.sh")
          elif TAPPLY == "Random Wallpaper Timed":
            pic = file((SAVED), "w")
            pic.write (DEFAULT) 
            pic.close()
            pic = file((SETTYPE), "w")
            pic.write ("random-time") 
            pic.close()
            os.system("login_background.sh &")
          elif TAPPLY == "No Wallpaper":
            pic = file((SAVED), "w")
            pic.write (DEFAULT) 
            pic.close()
            pic = file((SETTYPE), "w")
            pic.write ("color")
            pic.close()
            os.system("xsetroot -solid \"`cat $HOME/.wallpaper/color`\" && echo 'color' > $HOME/.wallpaper/set-type  && xrefresh")
          elif TAPPLY == "Scale":
            pic = file((SAVED), "w")
            pic.write (IMAGE) 
            pic.close()
            pic = file((SETTYPE), "w")
            pic.write ("static" )
            pic.close()
            os.system("feh --bg-scale `cat $HOME/.wallpaper/saved` && cp ~/.fehbg ~/.wallpaper/feh-bg.ice && xrefresh")
          elif TAPPLY == "Center":
            pic = file((SAVED), "w")
            pic.write (IMAGE) 
            pic.close()
            pic = file((SETTYPE), "w")
            pic.write ("static" )
            pic.close()
            os.system("feh --bg-center `cat $HOME/.wallpaper/saved` && cp ~/.fehbg ~/.wallpaper/feh-bg.ice && xrefresh")
          elif TAPPLY == "Fill":
            pic = file((SAVED), "w")
            pic.write (IMAGE) 
            pic.close()
            pic = file((SETTYPE), "w")
            pic.write ("static" )
            pic.close()
            os.system("feh --bg-fill `cat $HOME/.wallpaper/saved` && cp ~/.fehbg ~/.wallpaper/feh-bg.ice && xrefresh")
      elif SESSION == "fluxbox":
        model = self.combo.get_model()
        index = self.combo.get_active()
        if index:
          TAPPLY = model[index][0]
          if TAPPLY == "Random Wallpaper":
            pic = file((SAVED), "w")
            pic.write (DEFAULT) 
            pic.close()
            pic = file((SETTYPE), "w")
            pic.write ("random") 
            pic.close()
            os.system("echo 'random' > $HOME/.wallpaper/set-type && randwallpaper.sh")
          elif TAPPLY == "Random Wallpaper Timed":
            pic = file((SAVED), "w")
            pic.write (DEFAULT) 
            pic.close()
            pic = file((SETTYPE), "w")
            pic.write ("random-time") 
            pic.close()
            os.system("login_background.sh &")
          elif TAPPLY == "No Wallpaper":
            pic = file((SAVED), "w")
            pic.write (DEFAULT) 
            pic.close()
            pic = file((SETTYPE), "w")
            pic.write ("color")
            pic.close()
            os.system("xsetroot -solid \"`cat $HOME/.wallpaper/color`\" && echo 'color' > $HOME/.wallpaper/set-type  && xrefresh")
          elif TAPPLY == "Scale":
            pic = file((SAVED), "w")
            pic.write (IMAGE) 
            pic.close()
            pic = file((SETTYPE), "w")
            pic.write ("static" )
            pic.close()
            os.system("feh --bg-scale `cat $HOME/.wallpaper/saved` && cp ~/.fehbg ~/.wallpaper/feh-bg.fb && xrefresh")
          elif TAPPLY == "Center":
            pic = file((SAVED), "w")
            pic.write (IMAGE) 
            pic.close()
            pic = file((SETTYPE), "w")
            pic.write ("static" )
            pic.close()
            os.system("feh --bg-center `cat $HOME/.wallpaper/saved` && cp ~/.fehbg ~/.wallpaper/feh-bg.fb && xrefresh")
          elif TAPPLY == "Fill":
            pic = file((SAVED), "w")
            pic.write (IMAGE) 
            pic.close()
            pic = file((SETTYPE), "w")
            pic.write ("static" )
            pic.close()
            os.system("feh --bg-fill `cat $HOME/.wallpaper/saved` && cp ~/.fehbg ~/.wallpaper/feh-bg.fb && xrefresh")
      elif SESSION == "jwm":
        model = self.combo.get_model()
        index = self.combo.get_active()
        if index:
          TAPPLY = model[index][0]
          if TAPPLY == "Random Wallpaper":
            pic = file((SAVED), "w")
            pic.write (DEFAULT) 
            pic.close()
            pic = file((SETTYPE), "w")
            pic.write ("random") 
            pic.close()
            os.system("echo 'random' > $HOME/.wallpaper/set-type && randwallpaper.sh")
          elif TAPPLY == "Random Wallpaper Timed":
            pic = file((SAVED), "w")
            pic.write (DEFAULT) 
            pic.close()
            pic = file((SETTYPE), "w")
            pic.write ("random-time") 
            pic.close()
            os.system("login_background.sh &")
          elif TAPPLY == "No Wallpaper":
            pic = file((SAVED), "w")
            pic.write (DEFAULT) 
            pic.close()
            pic = file((SETTYPE), "w")
            pic.write ("color")
            pic.close()
            os.system("xsetroot -solid \"`cat $HOME/.wallpaper/color`\" && echo 'color' > $HOME/.wallpaper/set-type  && xrefresh")
          elif TAPPLY == "Scale":
            pic = file((SAVED), "w")
            pic.write (IMAGE) 
            pic.close()
            pic = file((SETTYPE), "w")
            pic.write ("static" )
            pic.close()
            os.system("feh --bg-scale `cat $HOME/.wallpaper/saved` && cp ~/.fehbg ~/.wallpaper/feh-bg.jwm && xrefresh")
          elif TAPPLY == "Center":
            pic = file((SAVED), "w")
            pic.write (IMAGE) 
            pic.close()
            pic = file((SETTYPE), "w")
            pic.write ("static" )
            pic.close()
            os.system("feh --bg-center `cat $HOME/.wallpaper/saved` && cp ~/.fehbg ~/.wallpaper/feh-bg.jwm && xrefresh")
          elif TAPPLY == "Fill":
            pic = file((SAVED), "w")
            pic.write (IMAGE) 
            pic.close()
            pic = file((SETTYPE), "w")
            pic.write ("static" )
            pic.close()
            os.system("feh --bg-fill `cat $HOME/.wallpaper/saved` && cp ~/.fehbg ~/.wallpaper/feh-bg.jwm && xrefresh")
         	
    def combochange (self, widget):
      model = self.combo.get_model()
      index = self.combo.get_active()
      if index:
          SELECT = model[index][0]
          if SELECT == "No Wallpaper":
            self.picturebutton.hide()
            self.folderbutton.hide()
            self.colorbutton.show()
            self.imagebox.remove(self.image)
            self.pix = gtk.gdk.pixbuf_new_from_file((DEFAULT))
            self.pix = self.pix.scale_simple(300, 200, gtk.gdk.INTERP_BILINEAR)
            self.image = gtk.image_new_from_pixbuf(self.pix)
            self.imagebox.pack_start(self.image)
            self.image.show()
          elif SELECT == "Random Wallpaper":
            self.colorbutton.hide()
            self.picturebutton.hide()
            self.folderbutton.show()
            self.imagebox.remove(self.image)
            self.pix = gtk.gdk.pixbuf_new_from_file((DEFAULT))
            self.pix = self.pix.scale_simple(300, 200, gtk.gdk.INTERP_BILINEAR)
            self.image = gtk.image_new_from_pixbuf(self.pix)
            self.imagebox.pack_start(self.image)
            self.image.show()
          elif SELECT == "Random Wallpaper Timed":
            self.colorbutton.hide()
            self.picturebutton.hide()
            self.folderbutton.show()
            self.imagebox.remove(self.image)
            self.pix = gtk.gdk.pixbuf_new_from_file((DEFAULT))
            self.pix = self.pix.scale_simple(300, 200, gtk.gdk.INTERP_BILINEAR)
            self.image = gtk.image_new_from_pixbuf(self.pix)
            self.imagebox.pack_start(self.image)
            self.image.show()
          else:
            self.colorbutton.hide()
            self.folderbutton.hide()
            self.picturebutton.show()
            self.imagebox.remove(self.image)
            self.pix = gtk.gdk.pixbuf_new_from_file((IMAGE))
            self.pix = self.pix.scale_simple(300, 200, gtk.gdk.INTERP_BILINEAR)
            self.image = gtk.image_new_from_pixbuf(self.pix)
            self.imagebox.pack_start(self.image)
            self.image.show()

    def colorselect(self, widget):
      cdia = gtk.ColorSelectionDialog("Select color")
      response = cdia.run()          

      
      if response == gtk.RESPONSE_OK:
        colorsel = cdia.colorsel
        color = colorsel.get_current_color()
        print color.to_string()
        cf = file((COLOR), "w")
        cf.write (color.to_string())
        cf.close()

      cdia.destroy()
 
    def folder (self, widget):
      backfolder = file((BACKFOLDER), "r")
      FOLDER = backfolder.readline()
      backfolder.close()
      dialog = gtk.FileChooserDialog("Open...", None, gtk.FILE_CHOOSER_ACTION_SELECT_FOLDER,(gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL, gtk.STOCK_OPEN, gtk.RESPONSE_OK))
      dialog.set_current_folder(os.path.expanduser(FOLDER))
      dialog.set_default_response(gtk.RESPONSE_OK)
      
      filter = gtk.FileFilter()
      filter.set_name("All Files")
      filter.add_pattern("*")
      dialog.add_filter(filter)
      
      response = dialog.run()
      if response == gtk.RESPONSE_OK:
        FOLDER = dialog.get_filename()
        backfolder = file((BACKFOLDER), "w")
        backfolder.write (FOLDER) 
        backfolder.close()
      elif response == gtk.RESPONSE_CANCEL:
		print "No file selected"  
      dialog.destroy()

    def update_preview(self, dialog, preview):
        filename = dialog.get_preview_filename()
        try:
            pixbuf = gtk.gdk.pixbuf_new_from_file_at_size(filename, 200,200)
            preview.set_from_pixbuf(pixbuf)
            have_preview = True
        except:
            have_preview = False
        dialog.set_preview_widget_active(have_preview)
        return


    def pictureselect(self, widget):
      backfolder = file((BACKFOLDER), "r")
      FOLDER = backfolder.readline()
      backfolder.close()
      dialog = gtk.FileChooserDialog("Open...", None, gtk.FILE_CHOOSER_ACTION_OPEN,(gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL, gtk.STOCK_OPEN, gtk.RESPONSE_OK))
      dialog.set_current_folder(os.path.expanduser(FOLDER))
      dialog.set_default_response(gtk.RESPONSE_OK)
      
      filter = gtk.FileFilter()
      filter.set_name("Images")
      filter.add_mime_type("image/png")
      filter.add_mime_type("image/jpeg")
      filter.add_mime_type("image/gif")
      filter.add_mime_type("image/tiff")
      filter.add_pattern("*.png")
      filter.add_pattern("*.jpg")
      filter.add_pattern("*.gif")
      filter.add_pattern("*.jpeg")
      filter.add_pattern("*.tiff")
      filter.add_pattern("*.tif")
      dialog.add_filter(filter)

      previewImage = gtk.Image()
      dialog.set_preview_widget(previewImage)
      dialog.set_use_preview_label(False)
      dialog.set_transient_for(self.window)
      dialog.connect("update-preview", self.update_preview, previewImage)

      response = dialog.run()
      if response == gtk.RESPONSE_OK:
        global IMAGE
        IMAGE = dialog.get_filename()
        self.imagebox.remove(self.image)
        self.pix = gtk.gdk.pixbuf_new_from_file(dialog.get_filename())
        self.pix = self.pix.scale_simple(300, 200, gtk.gdk.INTERP_BILINEAR)
        self.image = gtk.image_new_from_pixbuf(self.pix)
        self.imagebox.pack_start(self.image)
        self.image.show()
      elif response == gtk.RESPONSE_CANCEL:
		print "No file selected"  
      dialog.destroy()
      
    def about(self, widget):
      about = gtk.AboutDialog()
      about.set_program_name("antiX Wallpaper")
      about.set_version("1.0.0")
      about.set_copyright("(c)the antiX community")
      about.set_comments("This is an antiX application for setting the wallpaper on the preinstalled window managers")
      about.set_website("http://antix.freeforums.org")
      about.run()
      about.destroy()

    def help(self, widget):
      help = gtk.Dialog()
      help.set_position(gtk.WIN_POS_CENTER)
      help.set_size_request(350, 350)
      help.set_resizable(False)
      help.set_title("antiX Wallpaper - help")

      helptext = gtk.TextBuffer()
      helptext.set_text(HELPTEXT)

      view = gtk.TextView();
      view.set_buffer(helptext)
      view.set_editable(False)
      setting =view.get_buffer()
      view.set_wrap_mode(gtk.WRAP_WORD)
      view.show()

      textsw = gtk.ScrolledWindow()
      textsw.set_policy(gtk.POLICY_AUTOMATIC,gtk.POLICY_AUTOMATIC)
      textsw.add(view)
      textsw.set_size_request(350,300)
      textsw.show()

      help.vbox.pack_start(textsw, True, True, 0)
      help.add_button(gtk.STOCK_CLOSE, gtk.RESPONSE_CLOSE)
      
      help.run()
      help.destroy()
      
    def main(self):
      gtk.main()
    
    def destroy(self, widget, data=None):
      gtk.main_quit()
      
    def __init__(self):
      self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
      self.window.set_position(gtk.WIN_POS_CENTER)
      self.window.set_size_request(350,350)
      self.window.set_title("antiX Wallpaper")

      self.menubar = gtk.MenuBar()

      self.menu = gtk.Menu()
      self.filemenu = gtk.MenuItem("Options")
      self.filemenu.set_submenu(self.menu)
      self.filemenu.show()
      
      self.helpmenu = gtk.ImageMenuItem(gtk.STOCK_HELP)
      self.helpmenu.connect("activate", self.help)
      self.helpmenu.show()
      self.menu.append(self.helpmenu)

      self.aboutmenu = gtk.ImageMenuItem(gtk.STOCK_ABOUT)
      self.aboutmenu.connect("activate", self.about)
      self.aboutmenu.show()
      self.menu.append(self.aboutmenu)

      self.foldermenu = gtk.ImageMenuItem(gtk.STOCK_OPEN)
      self.foldermenu.set_label("Default Folder")
      self.foldermenu.connect("activate", self.folder)
      self.foldermenu.show()
      self.menu.append(self.foldermenu)

      self.imagemenu = gtk.ImageMenuItem(gtk.STOCK_OPEN)
      self.imagemenu.set_label("Open Image")
      self.imagemenu.connect("activate", self.pictureselect)
      self.imagemenu.show()
      self.menu.append(self.imagemenu)

      self.colormenu = gtk.ImageMenuItem(gtk.STOCK_OPEN)
      self.colormenu.set_label("Default Color")
      self.colormenu.connect("activate", self.colorselect)
      self.colormenu.show()
      self.menu.append(self.colormenu)

      self.exit = gtk.ImageMenuItem(gtk.STOCK_QUIT)
      self.exit.connect("activate", self.destroy)
      self.exit.show()
      self.menu.append(self.exit)
      self.menu.show()

      self.menubar.append(self.filemenu)
      self.menubar.show()

      self.pix = gtk.gdk.pixbuf_new_from_file(IMAGE)
      self.pix = self.pix.scale_simple(300, 200, gtk.gdk.INTERP_BILINEAR)
      self.image = gtk.image_new_from_pixbuf(self.pix)
      self.image.show()

      self.combo = gtk.combo_box_new_text()
      self.combo.append_text("Choose how to apply:")
      self.combo.append_text("Center")
      self.combo.append_text("Fill")
      self.combo.append_text("Scale")
      self.combo.append_text("No Wallpaper")
      self.combo.append_text("Random Wallpaper")
      self.combo.append_text("Random Wallpaper Timed")
      self.combo.set_active(0)
      self.combo.connect("changed", self.combochange)
      self.combo.show()
      
      self.folderbutton = gtk.Button(stock=gtk.STOCK_OPEN)
      self.folderbutton.connect("clicked", self.folder)
      self.folderbutton.set_size_request(0,50)
      self.folderbutton.hide()

      self.picturebutton = gtk.Button(stock=gtk.STOCK_OPEN)
      self.picturebutton.connect("clicked", self.pictureselect)
      self.picturebutton.set_size_request(0,50)
      self.picturebutton.show()

      self.colorbutton = gtk.Button(stock=gtk.STOCK_OPEN)
      self.colorbutton.connect("clicked", self.colorselect)
      self.colorbutton.set_size_request(0,50)
      self.colorbutton.hide()
      
      self.closebutton = gtk.Button(stock=gtk.STOCK_CLOSE)
      self.closebutton.connect("clicked", self.destroy)
      self.closebutton.set_size_request(0,50)
      self.closebutton.show()
      
      self.okbutton = gtk.Button(stock=gtk.STOCK_OK)
      self.okbutton.connect("clicked", self.set)
      self.okbutton.set_size_request(0,50)
      self.okbutton.show()
      
      self.buttonbox = gtk.HButtonBox()
      self.buttonbox.pack_start(self.folderbutton)
      self.buttonbox.pack_start(self.colorbutton)
      self.buttonbox.pack_start(self.picturebutton)
      self.buttonbox.pack_start(self.closebutton)
      self.buttonbox.pack_start(self.okbutton)
      self.buttonbox.show()
      
      self.imagebox = gtk.HBox()
      self.imagebox.pack_start(self.image)
      self.imagebox.show()

      self.topbox = gtk.VBox()
      self.topbox.pack_start(self.menubar)
      self.topbox.pack_start(self.imagebox)
      self.topbox.pack_start(self.combo)
      self.topbox.show()
      
      self.mainbox = gtk.VBox()
      self.mainbox.pack_start(self.topbox)
      self.mainbox.pack_start(self.buttonbox)
      self.mainbox.show()
      
      self.window.show()
      self.window.add(self.mainbox)
      self.window.connect("destroy", self.destroy)
      
    def main(self):
      gtk.main()
      

if __name__ == "__main__":
 base = Base()
 base.main()
