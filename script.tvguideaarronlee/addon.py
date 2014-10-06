#
#      Copyright (C) 2012 Tommy Winther
#      http://tommy.winther.nu
#
#  This Program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2, or (at your option)
#  any later version.
#
#  This Program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details
#
#  You should have received a copy of the GNU General Public License
#  along with this Program; see the file LICENSE.txt.  If not, write to
#  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.
#  http://www.gnu.org/copyleft/gpl.html

import xbmc
import xbmcaddon
import urllib
import socket 
import os
import shutil
xbmc.Player().stop


ADDON       = xbmcaddon.Addon(id = 'script.tvguideaarronlee')
HOME        = ADDON.getAddonInfo('path')
TITLE       = 'TV Guide AarronLee Premium'
VERSION     = '5.1.11'
addon       = xbmcaddon.Addon()
addonid     = addon.getAddonInfo('id')
versioninfo = addon.getAddonInfo('version')
datapath    = xbmc.translatePath(ADDON.getAddonInfo('profile'))
addonpath   = os.path.join(ADDON.getAddonInfo('path'), 'resources')
profilepath = os.path.join(xbmc.translatePath('special://profile'), '')
default_ini = os.path.join(addonpath, 'addons.ini')
local_ini   = os.path.join(addonpath, 'local.ini')
current_ini = os.path.join(datapath, 'addons.ini')
fav_xml     = os.path.join(profilepath,'favourites-aarronlee.xml')
cats        = ADDON.getSetting('categories')
oss         = 'OffSide Streams'
stvb        = 'StreamTVBox'

print '****** TV GUIDE AARRONLEE INFORMATION ******'
print addonid, versioninfo


def CheckVersion():
    prev = ADDON.getSetting('VERSION')
    curr = VERSION

    if prev == curr:
        return

    if prev == '4.1':
        d = xbmcgui.Dialog()
        d.ok(TITLE + ' - ' + VERSION, 'Si necesitas ayuda, actualizaciones y/o mas informacion...' , '[COLOR FF00FF00]www.tvguideaarronlee.com[/COLOR]',  'Gracias por usar la version premium.')

    ADDON.setSetting('VERSION', curr)

if oss or stvb in cats:
    cats = cats.replace(oss, '').replace(stvb, '')
    while '||' in cats:
        cats = cats.replace('||', '|')
    ADDON.setSetting('categories', cats)


if not os.path.exists(current_ini):
    try: os.makedirs(datapath)
    except: pass
    shutil.copy(default_ini, datapath)
    shutil.copy(local_ini, datapath)


ooOOOoo = ''
def ttTTtt(i, t1, t2=[]):
    t = ooOOOoo
    for c in t1:
      t += chr(c)
      i += 1
      if i > 1:
       t = t[:-1]
       i = 0  
    for c in t2:
      t += chr(c)
      i += 1
      if i > 1:
       t = t[:-1]
       i = 0
    return t


path = current_ini
try:
    url = 'https://dl.dropboxusercontent.com/u/108091935/addons.ini'
    urllib.urlretrieve(url, path)
except:
    pass

path = fav_xml
try:
    url = 'http://www.tvguideaarronlee.com/pluginfiles/favourites-aarronlee.xml'
    urllib.urlretrieve(url, path)
except:
    pass
	
	
busy = None
try:
    import xbmcgui
    busy = xbmcgui.WindowXMLDialog('DialogBusy.xml', '')
    busy.show()

    try:    busy.getControl(10).setVisible(False)
    except: pass

except:
    busy = None

import buggalo
import gui


buggalo.GMAIL_RECIPIENT = 'tvguideaarronlee@gmail.com'


try:
    CheckVersion()
    w = gui.TVGuide()

    if busy:
        busy.close()
        busy = None

    w.doModal()
    del w

except Exception:
    buggalo.onExceptionRaised()