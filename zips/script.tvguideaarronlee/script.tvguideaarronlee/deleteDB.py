
import os
import xbmc
import xbmcgui
import xbmcaddon

def deleteDB():
    try:
        xbmc.log("[script.tvguideaarronlee] Deleting database...", xbmc.LOGDEBUG)
        dbPath = xbmc.translatePath(xbmcaddon.Addon(id = 'script.tvguideaarronlee').getAddonInfo('profile'))
        dbPath = os.path.join(dbPath, 'source.db')

        delete_file(dbPath)
        
        passed = not os.path.exists(dbPath)

        if passed: 
            xbmc.log("[script.tvguideaarronlee] Deleting database...PASSED", xbmc.LOGDEBUG)
        else:
            xbmc.log("[script.tvguideaarronlee] Deleting database...FAILED", xbmc.LOGDEBUG)

        return passed

    except Exception, e:
        xbmc.log('[script.tvguideaarronlee] Deleting database...EXCEPTION', xbmc.LOGDEBUG)
        return False

def delete_file(filename):
    tries = 10
    while os.path.exists(filename) and tries > 0: 
        try:             
            os.remove(filename) 
            break 
        except: 
            tries -= 1 

if __name__ == '__main__':
    if deleteDB():
        d = xbmcgui.Dialog()
        d.ok('DigiTele TV', 'Base de Datos borrado.', 'Reinicia el plugin')    
    else:
        d = xbmcgui.Dialog()
        d.ok('DigiTele TV', 'Error en borrar base de datos.', 'Database may be locked,', 'please restart XBMC and try again')    


