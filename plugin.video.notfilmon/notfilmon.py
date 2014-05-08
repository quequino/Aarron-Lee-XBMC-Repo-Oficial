import urllib , sys , re , xbmcplugin , xbmcgui , xbmcaddon , xbmc , os
import settings
import json
from t0mm0 . common . net import Net
from t0mm0 . common . addon import Addon
if 64 - 64: i11iIiiIii
import datetime
import time
OO0o = Net ( )
if 81 - 81: Iii1I1 + OO0O0O % iiiii % ii1I - ooO0OO000o
ii11i = 'plugin.video.notfilmon'
oOooOoO0Oo0O = xbmcaddon . Addon ( id = ii11i )
if 10 - 10: IIiI1I11i11
#Global Constants
ooOO00oOo = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
OOOo0 = 'http://www.filmon.com/channel/'
Oooo000o = 'http://dl.dropbox.com/u/129714017/hubmaintenance/'
IiIi11iIIi1Ii = 'http://static.filmon.com/couch/channels/'
Oo0O = settings . res ( )
IiI = Addon ( 'plugin.video.notfilmon' , sys . argv )
ooOo = IiI . get_profile ( )
Oo = os . path . join ( ooOo , 'cookies' )
OO0o = Net ( )
o0O = 'http://www.filmon.com/ajax/login'
IiiIII111iI = oOooOoO0Oo0O . getSetting ( 'user' )
IiII = oOooOoO0Oo0O . getSetting ( 'pass' )
iI1Ii11111iIi = { 'password' : IiII ,
 'email' : IiiIII111iI ,
 'remember' : 1 }
i1i1II = { 'Host' : 'www.filmon.com' ,
 'Origin' : 'http://www.filmon.com' ,
 'Referer' : 'http://www.filmon.com/user/login' ,
 'X-Requested-With' : 'XMLHttpRequest' }
O0oo0OO0 = OO0o . http_POST ( o0O , iI1Ii11111iIi , i1i1II )
I1i1iiI1 = os . path . join ( Oo , "FilmOn.lwp" )
if os . path . exists ( Oo ) == False :
 os . makedirs ( Oo )
OO0o . save_cookies ( I1i1iiI1 )
if 24 - 24: oOOOO0o0o
if oOooOoO0Oo0O . getSetting ( 'visitor_ga' ) == '' :
 from random import randint
 oOooOoO0Oo0O . setSetting ( 'visitor_ga' , str ( randint ( 0 , 0x7fffffff ) ) )
 if 40 - 40: II / oo00 * i1I1Ii1iI1ii * o0oOoO00o . i1
oOOoo00O0O = "4.6.1"
i1111 = "FilmOn"
i11 = "UA-3174686-20"
if 41 - 41: O00o0o0000o0o . oOo0oooo00o * I1i1i1ii - IIIII
if 26 - 26: O00OoOoo00 . iiiI11 / oooOOOOO * oo00 / iiiI11
def oOO ( ) :
 if oOooOoO0Oo0O . getSetting ( 'filmon' ) == 'true' :
  I1iiiiI1iII ( 'My Recordings' , 'http://www.filmon.com/my/recordings' , 5 , 'http://a3.mzstatic.com/us/r1000/065/Purple/a8/0d/f0/mzl.otgnsovy.png' , '' , 'My Recordings' )
 I1iiiiI1iII ( 'Live Now Epg Main Channels' , 'http://www.filmon.com/tvguide/' , 1 , 'http://www.filmon.com/tv/themes/filmontv/img/mobile/filmon-logo-stb.png' , '' , 'TV Guide' )
 IiIi11i = 'http://www.filmon.com'
 OO0o . set_cookies ( I1i1iiI1 )
 O0oo0OO0 = OO0o . http_GET ( IiIi11i ) . content
 iIii1I111I11I = O0oo0OO0 . encode ( 'ascii' , 'ignore' )
 OO00OooO0OO = re . compile ( '"original_name":"(.+?)".+?"logo_148x148_uri":"(.+?)"' , re . DOTALL ) . findall ( iIii1I111I11I )
 for IiIi11i , iiiIi in OO00OooO0OO :
  IiIIIiI1I1 = iiiIi . replace ( '\/' , '/' )
  OoO000 = IiIi11i . encode ( "utf-8" )
  I1iiiiI1iII ( OoO000 , 'url' , 3 , IiIIIiI1I1 , '' , OoO000 )
  if 42 - 42: i1 - ii1I / i11iIiiIii + O00o0o0000o0o + II
 iIi ( 'movies' , 'default' )
 if 40 - 40: i1 . oo00 . oOOOO0o0o . ii1I
def I11iii ( url , name , group ) :
 OO0O00 = ':"(.+?)".+?"title":"(.+?)".+?"alias":"(.+?)"'
 OO0o . set_cookies ( I1i1iiI1 )
 O0oo0OO0 = OO0o . http_GET ( 'http://www.filmon.com' ) . content . encode ( 'ascii' , 'ignore' )
 iIii1I111I11I = O0oo0OO0 . split ( '"big_logo"' )
 ii1 = '"%s"' % str ( group )
 o0oO0o00oo = [ ]
 for II1i1Ii11Ii11 in iIii1I111I11I :
  if ii1 in II1i1Ii11Ii11 :
   OO00OooO0OO = re . compile ( OO0O00 , re . DOTALL ) . findall ( II1i1Ii11Ii11 )
   iiiIi = OO00OooO0OO [ 0 ] [ 0 ]
   name = OO00OooO0OO [ 0 ] [ 1 ]
   iII11i = OO00OooO0OO [ 0 ] [ 2 ]
   url = 'http://www.filmon.com/channel/' + str ( iII11i )
   if 97 - 97: oOo0oooo00o % oOo0oooo00o + ooO0OO000o * IIIII
   if name not in o0oO0o00oo :
    o0oO0o00oo . append ( name )
    name = name . encode ( "utf-8" )
    IiIIIiI1I1 = iiiIi . replace ( '\/' , '/' )
    I1iiiiI1iII ( name , url , 2 , IiIIIiI1I1 , '' , group )
 xbmcplugin . addSortMethod ( int ( sys . argv [ 1 ] ) , xbmcplugin . SORT_METHOD_VIDEO_TITLE )
 iIi ( 'movies' , 'default' )
 o0o00o0 ( 'None' , group )
 if 25 - 25: oOOOO0o0o - O00OoOoo00 . iiiii
 if 22 - 22: O00OoOoo00 + ooO0OO000o % iiiI11 . oOo0oooo00o . oo00
def OO0oo0oOO ( url , group ) :
 oo0oooooO0 = 'http://www.filmon.com/tvguide/'
 O0oo0OO0 = OO0o . http_GET ( oo0oooooO0 ) . content
 i11Iiii = O0oo0OO0 . encode ( 'ascii' , 'ignore' )
 iIii1I111I11I = str ( i11Iiii ) . replace ( '\n' , '' )
 OO00OooO0OO = re . compile ( 'bottom">(.+?)</h3>.+?href="(.+?)" >                <img src="(.+?)".+?.+?div class="title">.+?</div>.+?h4>(.+?)/h4>.+?"description">(.+?)/div>' ) . findall ( iIii1I111I11I )
 for OoO000 , oo0oooooO0 , IiIIIiI1I1 , iI , I1i1I1II in OO00OooO0OO :
  i1IiIiiI = str ( I1i1I1II ) . replace ( '",' , '' ) . replace ( '                ' , '' ) . replace ( '<a class="read-more" href="/tvguide/' , '' ) . replace ( '">Read more... &rarr;</a>' , '' ) . replace ( '\xc3' , '' ) . replace ( '\xa2' , '' ) . replace ( '\xe2' , '' ) . replace ( '\x82' , '' ) . replace ( '\xac' , '' ) . replace ( '\x84' , '' ) . replace ( '\xa2s' , '' ) . replace ( '\xc2' , '' ) . replace ( '\x9d' , '' ) . replace ( '<' , '' )
  iI = str ( iI ) . replace ( '<' , '' )
  I1i1I1II = '[B]%s [/B]\n\n%s' % ( iI , i1IiIiiI )
  url = 'http://www.filmon.com' + str ( oo0oooooO0 )
  I1iiiiI1iII ( OoO000 , url , 2 , IiIIIiI1I1 , I1i1I1II , 'TV Guide' )
  xbmcplugin . addSortMethod ( int ( sys . argv [ 1 ] ) , xbmcplugin . SORT_METHOD_VIDEO_TITLE )
  iIi ( 'movies' , 'epg' )
  if 31 - 31: I1i1i1ii . I1i1i1ii - i1I1Ii1iI1ii / II + oooOOOOO * IIiI1I11i11
  if 63 - 63: iiiI11 % ii1I / iiiii - iiiii
  if 8 - 8: oo00
def o00O ( name , url , iconimage , description , group ) :
 o0o00o0 ( group , name )
 OOO0OOO00oo = str ( url )
 OO0o . set_cookies ( I1i1iiI1 )
 O0oo0OO0 = OO0o . http_GET ( url ) . content
 i11Iiii = O0oo0OO0 . encode ( 'ascii' , 'ignore' )
 iIii1I111I11I = str ( i11Iiii ) . replace ( '\n' , '' )
 iIii1I111I11I = str ( i11Iiii ) . replace ( '\n' , '' )
 if oOooOoO0Oo0O . getSetting ( 'res' ) == '0' :
  OO00OooO0OO = re . compile ( '"name":"(.+?)".+?"quality":"(.+?)".+?"url":"(.+?)}' ) . findall ( iIii1I111I11I )
  for Iii111II , iiii11I , Ooo0OO0oOO in OO00OooO0OO :
   try :
    Ooo0OO0oOO = OO00OooO0OO [ 1 ] [ 2 ]
   except :
    pass
   if 'mp4' in Iii111II :
    if not 'promo' in Iii111II :
     oo0oooooO0 = str ( Ooo0OO0oOO ) . replace ( '\\' , '' )
     ii11i1 = str ( Ooo0OO0oOO ) . replace ( '\\' , '' ) . replace ( '"' , '' )
     IIIii1II1II = re . compile ( 'rtmp://(.+?)/(.+?)/(.+?)/"' )
     i1I1iI = IIIii1II1II . search ( oo0oooooO0 )
     oo0OooOOo0 = '%s/%s/' % ( i1I1iI . group ( 2 ) , i1I1iI . group ( 3 ) )
     o0OO00oO = 'http://www.filmon.com/tv/modules/FilmOnTV/files/flashapp/filmon/FilmonPlayer.swf?v=28'
     ii11i1 = str ( ii11i1 ) + str ( Iii111II )
   elif 'm4v' in Iii111II :
    oo0oooooO0 = str ( Ooo0OO0oOO ) . replace ( '\\' , '' )
    ii11i1 = str ( Ooo0OO0oOO ) . replace ( '\\' , '' ) . replace ( '"' , '' )
    oo0OooOOo0 = 'vodlast'
    o0OO00oO = 'http://www.filmon.com/tv/modules/FilmOnTV/files/flashapp/filmon/FilmonPlayer.swf'
    ii11i1 = str ( ii11i1 ) + '/' + str ( Iii111II )
   else :
    try :
     oo0oooooO0 = str ( Ooo0OO0oOO ) . replace ( '\\' , '' )
     ii11i1 = str ( Ooo0OO0oOO ) . replace ( '\\' , '' ) . replace ( '"' , '' )
     IIIii1II1II = re . compile ( 'rtmp://(.+?)/(.+?)id=(.+?)"' )
     i1I1iI = IIIii1II1II . search ( oo0oooooO0 )
     oo0OooOOo0 = '%sid=%s' % ( i1I1iI . group ( 2 ) , i1I1iI . group ( 3 ) )
     o0OO00oO = 'http://www.filmon.com/tv/modules/FilmOnTV/files/flashapp/filmon/FilmonPlayer.swf?v=28'
     ii11i1 = str ( ii11i1 ) + '/' + str ( Iii111II )
    except :
     pass
    try :
     oo0oooooO0 = str ( Ooo0OO0oOO ) . replace ( '\\' , '' )
     ii11i1 = str ( Ooo0OO0oOO ) . replace ( '\\' , '' ) . replace ( '"' , '' )
     IIIii1II1II = re . compile ( 'rtmp://(.+?)/(.+?)/(.+?)id=(.+?)"' )
     i1I1iI = IIIii1II1II . search ( oo0oooooO0 )
     oo0OooOOo0 = '%s/%sid=%s' % ( i1I1iI . group ( 2 ) , i1I1iI . group ( 3 ) , i1I1iI . group ( 4 ) )
     o0OO00oO = 'http://www.filmon.com/tv/modules/FilmOnTV/files/flashapp/filmon/FilmonPlayer.swf'
    except :
     pass
   if 'mp4' in ii11i1 :
    url = str ( ii11i1 ) + '/' + str ( Iii111II ) + ' playpath=' + str ( Iii111II ) + ' app=' + str ( oo0OooOOo0 ) + ' swfUrl=' + str ( o0OO00oO ) + ' pageurl=' + str ( url ) + ' live=true'
   else :
    iconimage = str ( iconimage )
    I11i1I1I = str ( ii11i1 )
    oO0Oo = OOO0OOO00oo
    url = str ( ii11i1 ) + '/' + str ( Iii111II ) + ' playpath=' + str ( Iii111II ) + ' app=' + str ( oo0OooOOo0 ) + ' swfUrl=' + str ( o0OO00oO ) + ' tcUrl=' + str ( I11i1I1I ) + ' pageurl=' + str ( oO0Oo ) + ' live=true'
   iiii11I = iiii11I . replace ( '480p' , 'HIGH' ) . replace ( '360p' , 'LOW' )
   oOOoo0Oo ( iiii11I , url , iconimage , name , '' , '' , '' , '' , '' )
 else :
  OO00OooO0OO = re . compile ( '"name":"(.+?)".+?"quality":".+?".+?"url":"(.+?)}' ) . findall ( iIii1I111I11I )
  if 'promo' in OO00OooO0OO [ 0 ] [ 0 ] :
   Iii111II = OO00OooO0OO [ 1 ] [ 0 ]
  else :
   Iii111II = OO00OooO0OO [ 0 ] [ 0 ]
  if oOooOoO0Oo0O . getSetting ( 'res' ) == '1' :
   Iii111II = str ( Iii111II ) . replace ( 'high' , 'low' )
  elif oOooOoO0Oo0O . getSetting ( 'res' ) == '2' :
   Iii111II = str ( Iii111II ) . replace ( 'low' , 'high' )
  Ooo0OO0oOO = OO00OooO0OO [ 1 ] [ 1 ]
  if 'mp4:' in Iii111II :
   oo0oooooO0 = str ( Ooo0OO0oOO ) . replace ( '\\' , '' )
   ii11i1 = str ( Ooo0OO0oOO ) . replace ( '\\' , '' ) . replace ( '"' , '' )
   IIIii1II1II = re . compile ( 'rtmp://(.+?)/(.+?)/(.+?)/"' )
   i1I1iI = IIIii1II1II . search ( oo0oooooO0 )
   oo0OooOOo0 = '%s/%s/' % ( i1I1iI . group ( 2 ) , i1I1iI . group ( 3 ) )
   o0OO00oO = 'http://www.filmon.com/tv/modules/FilmOnTV/files/flashapp/filmon/FilmonPlayer.swf?v=28'
   ii11i1 = str ( ii11i1 ) + str ( Iii111II )
  elif 'm4v' in Iii111II :
   oo0oooooO0 = str ( Ooo0OO0oOO ) . replace ( '\\' , '' )
   ii11i1 = str ( Ooo0OO0oOO ) . replace ( '\\' , '' ) . replace ( '"' , '' )
   oo0OooOOo0 = 'vodlast'
   o0OO00oO = 'http://www.filmon.com/tv/modules/FilmOnTV/files/flashapp/filmon/FilmonPlayer.swf'
   ii11i1 = str ( ii11i1 ) + '/' + str ( Iii111II )
  else :
   try :
    oo0oooooO0 = str ( Ooo0OO0oOO ) . replace ( '\\' , '' )
    ii11i1 = str ( Ooo0OO0oOO ) . replace ( '\\' , '' ) . replace ( '"' , '' )
    IIIii1II1II = re . compile ( 'rtmp://(.+?)/(.+?)id=(.+?)"' )
    i1I1iI = IIIii1II1II . search ( oo0oooooO0 )
    oo0OooOOo0 = '%sid=%s' % ( i1I1iI . group ( 2 ) , i1I1iI . group ( 3 ) )
    o0OO00oO = 'http://www.filmon.com/tv/modules/FilmOnTV/files/flashapp/filmon/FilmonPlayer.swf?v=28'
    ii11i1 = str ( ii11i1 ) + '/' + str ( Iii111II )
   except :
    pass
   try :
    oo0oooooO0 = str ( Ooo0OO0oOO ) . replace ( '\\' , '' )
    ii11i1 = str ( Ooo0OO0oOO ) . replace ( '\\' , '' ) . replace ( '"' , '' )
    IIIii1II1II = re . compile ( 'rtmp://(.+?)/(.+?)/(.+?)id=(.+?)"' )
    i1I1iI = IIIii1II1II . search ( oo0oooooO0 )
    oo0OooOOo0 = '%s/%sid=%s' % ( i1I1iI . group ( 2 ) , i1I1iI . group ( 3 ) , i1I1iI . group ( 4 ) )
    o0OO00oO = 'http://www.filmon.com/tv/modules/FilmOnTV/files/flashapp/filmon/FilmonPlayer.swf'
   except :
    pass
  if 'mp4' in ii11i1 :
   o00OO00OoO = str ( ii11i1 ) + '/' + str ( Iii111II ) + ' playpath=' + str ( Iii111II ) + ' app=' + str ( oo0OooOOo0 ) + ' swfUrl=' + str ( o0OO00oO ) + ' pageurl=' + str ( url ) + ' live=true'
   OOOO0OOoO0O0 ( name , o00OO00OoO , iconimage )
  else :
   iconimage = str ( iconimage )
   I11i1I1I = str ( ii11i1 )
   oO0Oo = OOO0OOO00oo
   url = str ( ii11i1 ) + '/' + str ( Iii111II ) + ' playpath=' + str ( Iii111II ) + ' app=' + str ( oo0OooOOo0 ) + ' swfUrl=' + str ( o0OO00oO ) + ' tcUrl=' + str ( I11i1I1I ) + ' pageurl=' + str ( oO0Oo ) + ' live=true'
   OOOO0OOoO0O0 ( name , url , iconimage )
   if 65 - 65: O00OoOoo00 * IIiI1I11i11 + I1i1i1ii % i11iIiiIii * i1 . iiiI11
def OoO0O00 ( url , group ) :
 OO0o . set_cookies ( I1i1iiI1 )
 url = 'http://www.filmon.com/my/recordings'
 O0oo0OO0 = OO0o . http_GET ( url ) . content
 iIii1I111I11I = O0oo0OO0 . encode ( 'ascii' , 'ignore' )
 OO00OooO0OO = re . compile ( '"stream_url":"(.+?),"stream_name":"(.+?)","id":".+?","title":"(.+?)","description":"(.+?)","channel_id":"(.+?)"' ) . findall ( iIii1I111I11I )
 for Ooo0OO0oOO , Iii111II , OoO000 , I1i1I1II , OOOo0 in OO00OooO0OO :
  oo0oooooO0 = str ( Ooo0OO0oOO ) . replace ( '\/' , '/' )
  ii11i1 = str ( Ooo0OO0oOO ) . replace ( '\/' , '/' ) . replace ( '"' , '' )
  IIIii1II1II = re . compile ( 'rtmp://(.+?)/(.+?)/(.+?)/(.+?)/(.+?)/(.+?)/(.+?)"' )
  i1I1iI = IIIii1II1II . search ( oo0oooooO0 )
  try :
   oo0OooOOo0 = '%s/%s/%s/%s/%s/%s' % ( i1I1iI . group ( 2 ) , i1I1iI . group ( 3 ) , i1I1iI . group ( 4 ) , i1I1iI . group ( 5 ) , i1I1iI . group ( 6 ) , i1I1iI . group ( 7 ) )
  except :
   oo0OooOOo0 = ''
  I11i1I1I = str ( ii11i1 )
  IiIIIiI1I1 = 'https://static.filmon.com/couch/channels/%s/big_logo.png' % str ( OOOo0 )
  o0OO00oO = 'http://www.filmon.com/tv/modules/FilmOnTV/files/flashapp/filmon/FilmonPlayer.swf'
  oO0Oo = 'http://www.filmon.com/my/recordings'
  url = str ( ii11i1 ) + '/' + str ( Iii111II ) + ' playpath=' + str ( Iii111II ) + ' app=' + str ( oo0OooOOo0 ) + ' swfUrl=' + str ( o0OO00oO ) + ' tcUrl=' + str ( I11i1I1I ) + ' pageurl=' + str ( oO0Oo )
  xbmcplugin . addSortMethod ( int ( sys . argv [ 1 ] ) , xbmcplugin . SORT_METHOD_VIDEO_TITLE )
  oOOoo0Oo ( OoO000 , url , IiIIIiI1I1 , Iii111II , oo0OooOOo0 , oO0Oo , o0OO00oO , I11i1I1I , I1i1I1II )
  iIi ( 'movies' , 'epg' )
  if 5 - 5: oOOOO0o0o / i1I1Ii1iI1ii . I1i1i1ii - Iii1I1 / O00OoOoo00
def ooOooo000oOO ( dateString ) :
 try :
  return datetime . datetime . fromtimestamp ( time . mktime ( time . strptime ( dateString . encode ( 'utf-8' , 'replace' ) , "%Y-%m-%d %H:%M:%S" ) ) )
 except :
  return datetime . datetime . today ( ) - datetime . timedelta ( days = 1 )
  if 59 - 59: ooO0OO000o + iiiii * oo00 + ii1I
  if 58 - 58: ooO0OO000o * O00o0o0000o0o * o0oOoO00o / O00o0o0000o0o
def oO0o0OOOO ( ) :
 if 68 - 68: IIIII - iiiI11 - IIiI1I11i11 - o0oOoO00o + oOo0oooo00o
 iiiI1I11i1 = 60 * 60
 IIi1i11111 = 2 * iiiI1I11i1
 if 81 - 81: i11iIiiIii % oo00 - O00o0o0000o0o
 O0ooo0O0oo0 = datetime . datetime . today ( )
 oo0oOo = ooOooo000oOO ( oOooOoO0Oo0O . getSetting ( 'ga_time' ) )
 o000O0o = O0ooo0O0oo0 - oo0oOo
 iI1iII1 = o000O0o . days
 oO0OOoo0OO = o000O0o . seconds
 if 65 - 65: I1i1i1ii . OO0O0O / Iii1I1 - I1i1i1ii
 iii1i1iiiiIi = ( iI1iII1 > 0 ) or ( oO0OOoo0OO > IIi1i11111 )
 if not iii1i1iiiiIi :
  return
  if 2 - 2: IIiI1I11i11 / Iii1I1 / i1I1Ii1iI1ii % oo00 % I1i1i1ii
 oOooOoO0Oo0O . setSetting ( 'ga_time' , str ( O0ooo0O0oo0 ) . split ( '.' ) [ 0 ] )
 o0o00OO0 ( )
 if 7 - 7: O00o0o0000o0o + iiiI11 + Iii1I1
 if 9 - 9: ooO0OO000o . i1I1Ii1iI1ii - oooOOOOO / i1I1Ii1iI1ii
 if 46 - 46: oOo0oooo00o . O00o0o0000o0o * oOo0oooo00o % ii1I
 if 46 - 46: oo00 + II
def iIi1i1ii1 ( utm_url ) :
 OOooOO000 = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
 import urllib2
 try :
  OOoOoo = urllib2 . Request ( utm_url , None ,
 { 'User-Agent' : OOooOO000 }
 )
  oO0000OOo00 = urllib2 . urlopen ( OOoOoo ) . read ( )
 except :
  print ( "GA fail: %s" % utm_url )
 return oO0000OOo00
 if 27 - 27: IIiI1I11i11 % IIiI1I11i11
def IIiIi1iI ( group , name ) :
 try :
  try :
   from hashlib import md5
  except :
   from md5 import md5
  from random import randint
  import time
  from urllib import unquote , quote
  from os import environ
  from hashlib import sha1
  i1IiiiI1iI = oOooOoO0Oo0O . getSetting ( 'visitor_ga' )
  i1iIi = "http://www.google-analytics.com/__utm.gif"
  if not group == 'None' :
   ooOOoooooo = i1iIi + "?" + "utmwv=" + oOOoo00O0O + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmt=" + "event" + "&utme=" + quote ( "5(channel*click*" + group + ':' + name + ")" ) + "&utmac=" + i11 + "&utmcc=__utma=%s" % "." . join ( [ "1" , i1IiiiI1iI , i1IiiiI1iI , i1IiiiI1iI , i1IiiiI1iI , "2" ] )
   if 1 - 1: oOOOO0o0o / i1I1Ii1iI1ii % IIIII * O00OoOoo00 . i11iIiiIii
   if 2 - 2: o0oOoO00o * oOo0oooo00o - OO0O0O + IIiI1I11i11 . i1 % IIIII
   if 92 - 92: IIIII
   if 25 - 25: oOOOO0o0o - IIiI1I11i11 / iiiii / i1I1Ii1iI1ii
   if 12 - 12: IIiI1I11i11 * IIIII % ii1I % OO0O0O
   if 20 - 20: O00o0o0000o0o % I1i1i1ii / I1i1i1ii + I1i1i1ii
   try :
    print "============================ POSTING TRACK EVENT ============================"
    iIi1i1ii1 ( ooOOoooooo )
   except :
    print "============================  CANNOT POST TRACK EVENT ============================"
 except :
  print "================  CANNOT POST TRACK EVENT ANALYTICS  ================"
  if 45 - 45: i1 - O00OoOoo00 - iiiii - II . ooO0OO000o / Iii1I1
def o0o00o0 ( group , name ) :
 try :
  try :
   from hashlib import md5
  except :
   from md5 import md5
  from random import randint
  import time
  from urllib import unquote , quote
  from os import environ
  from hashlib import sha1
  i1IiiiI1iI = oOooOoO0Oo0O . getSetting ( 'visitor_ga' )
  i1iIi = "http://www.google-analytics.com/__utm.gif"
  if name == "None" :
   oo0o00O = i1iIi + "?" + "utmwv=" + oOOoo00O0O + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( i1111 ) + "&utmac=" + i11 + "&utmcc=__utma=%s" % "." . join ( [ "1" , i1IiiiI1iI , i1IiiiI1iI , i1IiiiI1iI , i1IiiiI1iI , "2" ] )
   if 51 - 51: I1i1i1ii - II * IIIII
   if 66 - 66: iiiii + Iii1I1
   if 11 - 11: oOo0oooo00o + iiiii - II / i1I1Ii1iI1ii + oOOOO0o0o . ooO0OO000o
   if 41 - 41: I1i1i1ii - Iii1I1 - Iii1I1
   if 68 - 68: O00o0o0000o0o % iiiI11
  else :
   if group == "None" :
    oo0o00O = i1iIi + "?" + "utmwv=" + oOOoo00O0O + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( i1111 + "/" + name ) + "&utmac=" + i11 + "&utmcc=__utma=%s" % "." . join ( [ "1" , i1IiiiI1iI , i1IiiiI1iI , i1IiiiI1iI , i1IiiiI1iI , "2" ] )
    if 88 - 88: OO0O0O - oooOOOOO + O00o0o0000o0o
    if 40 - 40: IIiI1I11i11 * I1i1i1ii + O00o0o0000o0o % IIIII
    if 74 - 74: i1 - oOOOO0o0o + iiiii + iiiI11 / oo00
    if 23 - 23: Iii1I1
    if 85 - 85: I1i1i1ii
   else :
    oo0o00O = i1iIi + "?" + "utmwv=" + oOOoo00O0O + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( i1111 + "/" + group + "/" + name ) + "&utmac=" + i11 + "&utmcc=__utma=%s" % "." . join ( [ "1" , i1IiiiI1iI , i1IiiiI1iI , i1IiiiI1iI , i1IiiiI1iI , "2" ] )
    if 84 - 84: IIiI1I11i11 . OO0O0O % iiiii + I1i1i1ii % iiiii % II
    if 42 - 42: II / oOo0oooo00o / i1I1Ii1iI1ii + IIIII / oo00
    if 84 - 84: oooOOOOO * ooO0OO000o + oOOOO0o0o
    if 53 - 53: IIIII % ooO0OO000o . O00OoOoo00 - OO0O0O - O00OoOoo00 * ooO0OO000o
    if 77 - 77: OO0O0O * II
    if 95 - 95: IIiI1I11i11 + i11iIiiIii
  print "============================ POSTING ANALYTICS ============================"
  iIi1i1ii1 ( oo0o00O )
  if 6 - 6: oooOOOOO / i11iIiiIii + IIIII * i1
 except :
  print "================  CANNOT POST TO ANALYTICS  ================"
  if 80 - 80: ooO0OO000o
  if 83 - 83: oOo0oooo00o . i11iIiiIii + ooO0OO000o . i1I1Ii1iI1ii * oOo0oooo00o
def o0o00OO0 ( ) :
 try :
  oooO0 = xbmc . translatePath ( 'special://logpath' )
  iIiIiiIIiIIi = os . path . join ( oooO0 , 'xbmc.log' )
  oO0OOOO0 = open ( iIiIiiIIiIIi , 'r' ) . read ( )
  OO00OooO0OO = re . compile ( 'Platform: (.+?)\. Built.+?' ) . findall ( oO0OOOO0 )
 except :
  oO0OOOO0 = 'Starting XBMC (Unknown Git:.+?Platform: Unknown. Built.+?'
  OO00OooO0OO = re . compile ( 'Platform: (.+?)\. Built.+?' ) . findall ( oO0OOOO0 )
 print '==========================   ' + i1111 + ' ' + oOOoo00O0O + '   =========================='
 try :
  from hashlib import md5
 except :
  from md5 import md5
 from random import randint
 import time
 from urllib import unquote , quote
 from os import environ
 from hashlib import sha1
 import platform
 i1IiiiI1iI = oOooOoO0Oo0O . getSetting ( 'visitor_ga' )
 OO00OooO0OO = re . compile ( 'Platform: (.+?)\. Built.+?' ) . findall ( oO0OOOO0 )
 for iI1I11iiI1i in OO00OooO0OO :
  print iI1I11iiI1i
  i1iIi = "http://www.google-analytics.com/__utm.gif"
  ooOOoooooo = i1iIi + "?" + "utmwv=" + oOOoo00O0O + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmt=" + "event" + "&utme=" + quote ( "5(app*launch*" + iI1I11iiI1i + ")" ) + "&utmac=" + i11 + "&utmcc=__utma=%s" % "." . join ( [ "1" , i1IiiiI1iI , i1IiiiI1iI , i1IiiiI1iI , i1IiiiI1iI , "2" ] )
  if 78 - 78: i1 % Iii1I1 % I1i1i1ii
  if 46 - 46: iiiii . i11iIiiIii
  if 94 - 94: i1I1Ii1iI1ii * I1i1i1ii / oOOOO0o0o / I1i1i1ii
  if 87 - 87: oOOOO0o0o . O00OoOoo00
  if 75 - 75: oooOOOOO + oo00 + i1I1Ii1iI1ii * oOo0oooo00o % i1 . IIIII
  if 55 - 55: O00o0o0000o0o . IIiI1I11i11
  try :
   print "============================ POSTING APP LAUNCH TRACK EVENT ============================"
   iIi1i1ii1 ( ooOOoooooo )
  except :
   print "============================  CANNOT POST APP LAUNCH TRACK EVENT ============================"
   if 61 - 61: oOOOO0o0o % O00OoOoo00 . oOOOO0o0o
class o0oOO000oO0oo ( xbmcgui . WindowXMLDialog ) :
 def __init__ ( self , * args , ** kwargs ) :
  self . shut = kwargs [ 'close_time' ]
  xbmc . executebuiltin ( "Skin.Reset(AnimeWindowXMLDialogClose)" )
  xbmc . executebuiltin ( "Skin.SetBool(AnimeWindowXMLDialogClose)" )
  if 78 - 78: o0oOoO00o + O00o0o0000o0o - iiiI11
 def onInit ( self ) :
  xbmc . Player ( ) . play ( '%s/resources/skins/DefaultSkin/media/xbmchub.mp3' % oOooOoO0Oo0O . getAddonInfo ( 'path' ) )
  while self . shut > 0 :
   xbmc . sleep ( 1000 )
   self . shut -= 1
  xbmc . Player ( ) . stop ( )
  self . _close_dialog ( )
  if 38 - 38: i1I1Ii1iI1ii - i1 + OO0O0O / oo00 % oOOOO0o0o
 def onFocus ( self , controlID ) : pass
 if 57 - 57: II / oooOOOOO
 def onClick ( self , controlID ) :
  if controlID == 12 :
   xbmc . Player ( ) . stop ( )
   self . _close_dialog ( )
  if controlID == 7 :
   xbmc . Player ( ) . stop ( )
   self . _close_dialog ( )
   if 29 - 29: OO0O0O + oo00 * II * O00o0o0000o0o . IIiI1I11i11 * IIiI1I11i11
 def onAction ( self , action ) :
  if action in [ 5 , 6 , 7 , 9 , 10 , 92 , 117 ] or action . getButtonCode ( ) in [ 275 , 257 , 261 ] :
   xbmc . Player ( ) . stop ( )
   self . _close_dialog ( )
   if 7 - 7: O00OoOoo00 * iiiI11 % I1i1i1ii - i1I1Ii1iI1ii
 def _close_dialog ( self ) :
  xbmc . executebuiltin ( "Skin.Reset(AnimeWindowXMLDialogClose)" )
  time . sleep ( .4 )
  self . close ( )
  if 13 - 13: I1i1i1ii . i11iIiiIii
  if 56 - 56: o0oOoO00o % Iii1I1 - IIiI1I11i11
from xbmcads import ads
ads . ADDON_ADVERTISE ( ii11i )
if 100 - 100: I1i1i1ii - Iii1I1 % i1 * O00o0o0000o0o + IIiI1I11i11
if 88 - 88: iiiii - II * Iii1I1 * iiiii . iiiii
if 33 - 33: iiiI11 + IIIII * i1 / OO0O0O - IIiI1I11i11
if 54 - 54: iiiI11 / O00o0o0000o0o . i1 % IIIII
def OoO0OOOOo0O ( ) :
 if xbmc . getCondVisibility ( 'system.platform.ios' ) :
  if not xbmc . getCondVisibility ( 'system.platform.atv' ) :
   OooOO = o0oOO000oO0oo ( 'hub1.xml' , oOooOoO0Oo0O . getAddonInfo ( 'path' ) , 'DefaultSkin' , close_time = 34 , logo_path = '%s/resources/skins/DefaultSkin/media/Logo/' % oOooOoO0Oo0O . getAddonInfo ( 'path' ) )
 elif xbmc . getCondVisibility ( 'system.platform.android' ) :
  OooOO = o0oOO000oO0oo ( 'hub1.xml' , oOooOoO0Oo0O . getAddonInfo ( 'path' ) , 'DefaultSkin' , close_time = 34 , logo_path = '%s/resources/skins/DefaultSkin/media/Logo/' % oOooOoO0Oo0O . getAddonInfo ( 'path' ) )
 else :
  OooOO = o0oOO000oO0oo ( 'hub.xml' , oOooOoO0Oo0O . getAddonInfo ( 'path' ) , 'DefaultSkin' , close_time = 34 , logo_path = '%s/resources/skins/DefaultSkin/media/Logo/' % oOooOoO0Oo0O . getAddonInfo ( 'path' ) )
  if 21 - 21: oOo0oooo00o / O00OoOoo00 % OO0O0O * oOOOO0o0o
 OooOO . doModal ( )
 del OooOO
 if 57 - 57: ooO0OO000o + ii1I
def iIi1ii ( dateString ) :
 try :
  return datetime . datetime . fromtimestamp ( time . mktime ( time . strptime ( dateString . encode ( 'utf-8' , 'replace' ) , "%Y-%m-%d %H:%M:%S" ) ) )
 except :
  return datetime . datetime . today ( ) - datetime . timedelta ( days = 1000 )
  if 58 - 58: oo00 % i1I1Ii1iI1ii
  if 50 - 50: iiiI11 . i1I1Ii1iI1ii
def ooO0OO ( ) :
 if 54 - 54: O00OoOoo00 + I1i1i1ii % II + iiiii - Iii1I1 - i1I1Ii1iI1ii
 IIi1i11111 = 120
 if 77 - 77: O00o0o0000o0o * OO0O0O
 O0ooo0O0oo0 = datetime . datetime . today ( )
 oo0oOo = iIi1ii ( oOooOoO0Oo0O . getSetting ( 'pop_time' ) )
 o000O0o = O0ooo0O0oo0 - oo0oOo
 iI1iII1 = o000O0o . days
 if 98 - 98: IIiI1I11i11 % I1i1i1ii * iiiii
 iii1i1iiiiIi = ( iI1iII1 > IIi1i11111 )
 if not iii1i1iiiiIi :
  return
  if 51 - 51: OO0O0O . oo00 / i1 + i1I1Ii1iI1ii
 oOooOoO0Oo0O . setSetting ( 'pop_time' , str ( O0ooo0O0oo0 ) . split ( '.' ) [ 0 ] )
 OoO0OOOOo0O ( )
 if 33 - 33: oooOOOOO . ooO0OO000o % IIIII + i1I1Ii1iI1ii
oO0o0OOOO ( )
if 71 - 71: oOOOO0o0o % O00o0o0000o0o
if 98 - 98: oOo0oooo00o % i11iIiiIii % oooOOOOO + I1i1i1ii
def OOoOO0o0o0 ( ) :
 ii1I1 = [ ]
 OooooOOoo0 = sys . argv [ 2 ]
 if len ( OooooOOoo0 ) >= 2 :
  i1I1IiiIi1i = sys . argv [ 2 ]
  iiI11ii1I1 = i1I1IiiIi1i . replace ( '?' , '' )
  if ( i1I1IiiIi1i [ len ( i1I1IiiIi1i ) - 1 ] == '/' ) :
   i1I1IiiIi1i = i1I1IiiIi1i [ 0 : len ( i1I1IiiIi1i ) - 2 ]
  Ooo0OOoOoO0 = iiI11ii1I1 . split ( '&' )
  ii1I1 = { }
  for oOo0OOoO0 in range ( len ( Ooo0OOoOoO0 ) ) :
   IIo0Oo0oO0oOO00 = { }
   IIo0Oo0oO0oOO00 = Ooo0OOoOoO0 [ oOo0OOoO0 ] . split ( '=' )
   if ( len ( IIo0Oo0oO0oOO00 ) ) == 2 :
    ii1I1 [ IIo0Oo0oO0oOO00 [ 0 ] ] = IIo0Oo0oO0oOO00 [ 1 ]
    if 92 - 92: iiiii * iiiI11
 return ii1I1
 if 100 - 100: iiiI11 + iiiI11 * O00OoOoo00
 if 1 - 1: oooOOOOO . oooOOOOO / oo00 - iiiI11
def I1iiiiI1iII ( name , url , mode , iconimage , description , group ) :
 oooO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&description=" + urllib . quote_plus ( description ) + "&group=" + urllib . quote_plus ( group )
 i1I1i111Ii = True
 ooo = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 ooo . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 if not mode == 2 and not mode == 2000 :
  i1I1i111Ii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oooO , listitem = ooo , isFolder = True )
  if 27 - 27: oooOOOOO % IIiI1I11i11
 else :
  i1I1i111Ii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oooO , listitem = ooo , isFolder = False )
  if oOooOoO0Oo0O . getSetting ( 'res' ) == '0' :
   i1I1i111Ii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oooO , listitem = ooo , isFolder = True )
 return i1I1i111Ii
 if 73 - 73: O00o0o0000o0o
def oOOoo0Oo ( name , url , iconimage , playPath , app , pageUrl , swfUrl , tcUrl , description ) :
 i1I1i111Ii = True
 ooo = xbmcgui . ListItem ( name , iconImage = "DefaultVideo.png" , thumbnailImage = iconimage )
 ooo . setInfo ( type = "Video" , infoLabels = { "Title" : playPath , "Plot" : description } )
 ooo . setProperty ( "IsPlayable" , "true" )
 i1I1i111Ii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = url , listitem = ooo , isFolder = False )
 return i1I1i111Ii
 if 70 - 70: OO0O0O
def OOOO0OOoO0O0 ( name , url , iconimage ) :
 i11ii1iI = xbmcgui . DialogProgress ( )
 OO0O00 = '    Please Wait While We Load [COLOR yellow][B]%s[/B][/COLOR]' % ( name )
 i11ii1iI . create ( "NotFilmOn" , '' , OO0O00 , '' )
 i1I = str ( iconimage ) . replace ( 'http://static.filmon.com/couch/channels/' , '' ) . replace ( '/big_logo.png' , '' )
 IIiIi1iI ( i1I , name )
 ooo = xbmcgui . ListItem ( name , iconImage = "DefaultVideo.png" , thumbnailImage = iconimage )
 ooo . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 ooo . setProperty ( "IsPlayable" , "true" )
 IIIii11 = xbmc . PlayList ( xbmc . PLAYLIST_VIDEO )
 IIIii11 . clear ( )
 IIIii11 . add ( url , ooo )
 xbmc . Player ( xbmc . PLAYER_CORE_MPLAYER ) . play ( IIIii11 )
 i11ii1iI . close ( )
 if 9 - 9: Iii1I1 % Iii1I1 - i1I1Ii1iI1ii
 if 51 - 51: IIiI1I11i11 . OO0O0O - o0oOoO00o / Iii1I1
def iIi ( content , viewType ) :
 if 52 - 52: i1I1Ii1iI1ii + Iii1I1 + IIIII + oOOOO0o0o % IIIII
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if oOooOoO0Oo0O . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % oOooOoO0Oo0O . getSetting ( viewType ) )
  if 75 - 75: IIiI1I11i11 . oooOOOOO . Iii1I1 * iiiI11
  if 4 - 4: I1i1i1ii % i1 * II
  if 100 - 100: iiiI11 * O00o0o0000o0o + O00o0o0000o0o
  if 54 - 54: iiiii + i1I1Ii1iI1ii - ii1I % i11iIiiIii
i1I1IiiIi1i = OOoOO0o0o0 ( )
IiIi11i = None
OoO000 = None
iII1iIi11i = None
IiIIIiI1I1 = None
I1i1I1II = None
o0ooooO0o0O = None
if 24 - 24: Iii1I1 * i1I1Ii1iI1ii
try :
 IiIi11i = urllib . unquote_plus ( i1I1IiiIi1i [ "url" ] )
except :
 pass
try :
 OoO000 = urllib . unquote_plus ( i1I1IiiIi1i [ "name" ] )
except :
 pass
try :
 IiIIIiI1I1 = urllib . unquote_plus ( i1I1IiiIi1i [ "iconimage" ] )
except :
 pass
try :
 iII1iIi11i = int ( i1I1IiiIi1i [ "mode" ] )
except :
 pass
try :
 I1i1I1II = urllib . unquote_plus ( i1I1IiiIi1i [ "description" ] )
except :
 pass
try :
 o0ooooO0o0O = urllib . unquote_plus ( i1I1IiiIi1i [ "group" ] )
except :
 pass
 if 29 - 29: IIiI1I11i11 % O00o0o0000o0o - IIiI1I11i11 / O00o0o0000o0o . ii1I
 if 31 - 31: iiiI11
print "Mode: " + str ( iII1iIi11i )
print "URL: " + str ( IiIi11i )
print "Name: " + str ( OoO000 )
print "IconImage: " + str ( IiIIIiI1I1 )
print "Group: " + str ( o0ooooO0o0O )
if 88 - 88: II - oooOOOOO + O00o0o0000o0o * IIiI1I11i11 % OO0O0O + oOOOO0o0o
if iII1iIi11i == None or IiIi11i == None or len ( IiIi11i ) < 1 :
 print ""
 oOO ( )
 if 76 - 76: IIiI1I11i11 * IIIII % iiiI11
elif iII1iIi11i == 1 :
 print "" + IiIi11i
 OO0oo0oOO ( IiIi11i , o0ooooO0o0O )
 if 57 - 57: OO0O0O - ii1I / iiiI11 - Iii1I1 * iiiii % ooO0OO000o
elif iII1iIi11i == 2 :
 print "" + IiIi11i
 o00O ( OoO000 , IiIi11i , IiIIIiI1I1 , I1i1I1II , o0ooooO0o0O )
 if 68 - 68: iiiii * oOo0oooo00o % oo00 - O00OoOoo00
elif iII1iIi11i == 3 :
 print "" + IiIi11i
 I11iii ( IiIi11i , OoO000 , o0ooooO0o0O )
 if 34 - 34: iiiI11 . OO0O0O * oo00 * i1 / iiiI11 / o0oOoO00o
elif iII1iIi11i == 4 :
 print "" + IiIi11i
 Channel_Lists ( IiIi11i )
 if 78 - 78: oOOOO0o0o - i1I1Ii1iI1ii / oo00
 if 10 - 10: IIIII + oOOOO0o0o * o0oOoO00o + OO0O0O / iiiI11 / o0oOoO00o
 if 42 - 42: IIiI1I11i11
elif iII1iIi11i == 5 :
 print "" + IiIi11i
 OoO0O00 ( IiIi11i , o0ooooO0o0O )
 if 38 - 38: O00o0o0000o0o + ooO0OO000o % oooOOOOO % oo00 - I1i1i1ii / iiiii
elif iII1iIi11i == 2000 :
 OoO0OOOOo0O ( )
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
if 73 - 73: i1I1Ii1iI1ii * Iii1I1 - i11iIiiIii
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
