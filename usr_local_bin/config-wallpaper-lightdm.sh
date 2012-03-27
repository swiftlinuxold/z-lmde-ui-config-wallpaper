# File Name: slimbackground.sh
# Purpose: allow user to set slim login background
# Authors: OU812 for antiX
# Latest Change: 20 August 2008
# latest Change: 02 January 2009 and renamed antixccslim.sh
# latest Change: 06 April 2009 changed cd directory
##########################################################################

#!/bin/bash

[ "$(whoami)" != "root" ] && exec gksu bash $0

TEXTDOMAINDIR=/usr/share/locale
TEXTDOMAIN=antixccslim.sh

cd /usr/share/backgrounds

export SLIMBACKGROUND=$(cat <<End_of_Text 

<window title="Slim Background" icon="gnome-control-center" window-position="1">

<vbox>
  <chooser>
    <height>500</height><width>600</width>
    <variable>BACKGROUND</variable>
  </chooser>

  <hbox>
    <button>
     <label>"`gettext $"View"`"</label>
	<input file>"/usr/share/icons/gTangish-2.0a1/16x16/actions/dialog-ok.png"</input>
        <action>feh -g 320x240 "$BACKGROUND" </action>
    </button>

    <button>
    <label>"`gettext $"Commit"`"</label>
	<input file>"/usr/share/icons/gTangish-2.0a1/16x16/actions/dialog-ok.png"</input>
        <action>cp -bv "$BACKGROUND" /usr/share/slim/themes/antiX/background.jpg</action>
	<action>EXIT:close</action>
    </button>
    
    <button>
    <label>"`gettext $"Cancel"`"</label>
	<input file>"/usr/share/icons/gTangish-2.0a1/16x16/actions/dialog-cancel.png"</input>
	<action>EXIT:close</action>
    </button>
  </hbox>
</vbox>

</window>
End_of_Text
)

gtkdialog --program=SLIMBACKGROUND
