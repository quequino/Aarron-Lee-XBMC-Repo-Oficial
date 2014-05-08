#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Developed by: enen92 

import urllib,urllib2,re,xbmcplugin,xbmcgui,sys,xbmc,xbmcaddon,xbmcvfs,os,json,datetime
from t0mm0.common.addon import Addon

##############Pasta de Imagens####################
addon_id = 'script.sportsdevilfixes'
selfAddon = xbmcaddon.Addon(id=addon_id)
addonfolder = selfAddon.getAddonInfo('path')
addon = Addon(addon_id)
datapath = addon.get_profile()
print datapath
################################################## 
#DIALOGS
mensagemok = xbmcgui.Dialog().ok
progresso = xbmcgui.DialogProgress()
#
#SPORTSDEVIL FOLDER
sportsdeviladdon = xbmcaddon.Addon(id="plugin.video.SportsDevil")
sportsdevilfolder = sportsdeviladdon.getAddonInfo('path')
sd_os_folder = xbmc.translatePath(os.path.join('special://home/addons','plugin.video.SportsDevil'))
#
zipurl="https://github.com/al101/SportsDevil-Fixes/archive/master.zip"
path = xbmc.translatePath('special://temp')
lib=os.path.join(path, 'master.zip')
clonefile = os.path.join(datapath, 'lastclone.txt')
shafile = os.path.join(datapath, 'lastcommit.txt')
timesdatefile = os.path.join(datapath, 'timesdate.txt')

def init():
	if not xbmcvfs.exists(datapath): xbmcvfs.mkdirs(datapath)
	for filename in (clonefile, shafile,timesdatefile):
   		if not xbmcvfs.exists(filename):
        		save(filename,"0")
	lastcommit()

def lastcommit():
	try:
		returndata = json_get("https://api.github.com/repos/al101/SportsDevil-Fixes/commits?per_page=1&sha=master")
		last_commit = returndata[0]["sha"]		
	except: mensagemok('SportsDevil Fixes','Could not obtain open last commit information. Please try again.');sys.exit(0)
	if returndata: checker(last_commit)

def checker(last_commit):
	week_days = weekdays()
	sha_hash = readfile(shafile)
	datelast = readfile(clonefile)
	times_clone_date = readfile(timesdatefile)
	if sha_hash != last_commit and sha_hash != "0":
		print datelast, week_days
		if datelast in week_days and int(times_clone_date) < 2: initold("There are new fixes!",last_commit)
		elif datelast not in week_days: initold("There are new fixes!",last_commit)
		else: mensagemok('SportsDevil Fixes','There are new fixes.','However this script only allows 2 clones per week','Try again next week or do it mannualy');sportsdevil_launch_yesno()	
	elif sha_hash != last_commit and sha_hash == "0": initold("This is your first run!",last_commit)
	else: mensagemok('SportsDevil Fixes','There are no new fixes.');sportsdevil_launch_yesno()		

def initold(string,last_commit):
	yes= xbmcgui.Dialog().yesno("SportsDevil Fixes",string, 'Do you want to clone al101 SportsDevil-fixes master?')
	if yes: download_and_launch(last_commit)
	else: sys.exit(0)



def download_and_launch(last_commit):
	success = xbmcvfs.exists(sd_os_folder)
	if success:
		downloader(zipurl,last_commit)
	else: mensagemok('SportsDevil Fixes','SportsDevil addon is not instaled on your system!','Please install it from Max repo first');sys.exit(0)   



def downloader(urlzip,last_commit):
	progresso.create('SportsDevil-Fixes', "master.zip" ,'Trying to get server response...please wait.')
	try:
		request = urllib2.Request(urlzip)
		u = urllib2.urlopen(request,timeout=2000)
	except: 
		progresso.close()
		mensagemok('SportsDevil-Fixes',"Could not obtain server's response.")
	if u:
		f = open(lib, 'wb')
		meta = u.info()
		file_size = int(meta.getheaders("Content-Length")[0])
		file_size_dl = 0
		block_sz = 8192
		while True:
			if progresso.iscanceled() == 0:	
				buffer = u.read(block_sz)
				if not buffer:
 					break
					progresso.close()
					print "Download stopped!"
				file_size_dl += len(buffer)
				f.write(buffer)
				progresso.update(int(file_size_dl * 100. / file_size),"master.zip","Downloading...")
			elif progresso.iscanceled() == 1:
				f.close()
				progresso.close()
				print "Progress dialog closed"
				break
		f.close()
		progresso.close()
		print "Downloader finished."
		unziper(addonfolder + "master.zip",last_commit)
	else:pass

def unziper(zipfile,last_commit):
	progresso.create('SportsDevil-Fixes', "Unziping git master" ,'Please wait...')
        
        
    	import extract
        extract.all(lib,path)
	progresso.update(25,"Unziping git master","Done.")
	progresso.update(30,"Copying to addons dir","Please wait...")
	copy(last_commit)

def copy(last_commit):
	import distutils.core
	masterfolder=os.path.join(path, 'SportsDevil-Fixes-master')
	masteraddonfolder=os.path.join(masterfolder, 'plugin.video.SportsDevil')
	fromDirectory = masteraddonfolder
	toDirectory = sportsdevilfolder
	distutils.dir_util.copy_tree(fromDirectory, toDirectory)
	progresso.update(35,"Copying to addons dir","Done.")
	removepackages(masterfolder,last_commit)
	

def removepackages(masterfolder,last_commit):
	datelast = readfile(clonefile)
	times_clone_date = readfile(timesdatefile)
	save(shafile,last_commit)
	save(clonefile,datetime.datetime.now().strftime("%m/%d/%Y"))
	week_days = weekdays()
	if datelast in week_days:
		save(timesdatefile,str(int(times_clone_date)+1))
	else: save(timesdatefile,str(1))
	sportsdevil_launch_yesno()

def sportsdevil_launch_yesno():
	yes= xbmcgui.Dialog().yesno("SportsDevil Fixes", 'Do you want to run SportsDevil?')
	if yes: launchsportsdevil()
	else: sys.exit(0)

def weekdays():
	import datetime
	now = datetime.datetime.now()
	now_day_1 = now - datetime.timedelta(days=now.weekday())
	dates = {}
	for n_week in range(3):
    		dates[n_week] = [(now_day_1 + datetime.timedelta(days=d+n_week*7)).strftime("%m/%d/%Y") for d in range(7)]
	return dates[0]
	

def launchsportsdevil():
	try:
		progresso.update(90,"Lanching SportsDevil...","Please wait...")
		progresso.update(100,"Lanching SportsDevil...","Done")
		progresso.close()
	except:pass
	xbmc.executebuiltin("RunAddon(plugin.video.SportsDevil)")

def json_post(data,url):
	data = json.dumps(data)
	req = urllib2.Request(url, data, {'Content-Type': 'application/json'})
	f = urllib2.urlopen(req)
	response = f.read()
	f.close()

def json_get(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
    data = json.load(urllib2.urlopen(req))
    return data

def save(filename,contents):  
	fh = open(filename, 'w+')
	fh.write(contents)  
	fh.close()
	return

def readfile(filename):
	f = open(filename, "r")
	string = f.read()
	return string
	
	
             
def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param




def addDir(name,url,mode,iconimage,checker,fanart):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&checker="+urllib.quote_plus(checker)+"&iconimage="+urllib.quote_plus(iconimage)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
	liz.setProperty('fanart_image', 'http://wakpaper.com/large/Theater_wallpapers_163.jpg')
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": checker } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok
        
############################################################################################################
          
params=get_params()
url=None
name=None
mode=None
iconimage=None
fanart=None

try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        mode=int(params["mode"])
except:
        pass
try:        
        iconimage=urllib.unquote_plus(params["iconimage"])
except:
        pass
try:        
        fanart=urllib.unquote_plus(params["fanart"])
except:
        pass

print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "Iconimage: "+str(iconimage)

if mode==None or url==None or len(url)<1:
        print ""
        init()



   



xbmcplugin.endOfDirectory(int(sys.argv[1]))
