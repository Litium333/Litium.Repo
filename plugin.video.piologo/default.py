# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Irmãos Piologo
#------------------------------------------------------------
# Licença: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Baseado no código do addon youtube
#------------------------------------------------------------

import xbmc, xbmcaddon, xbmcplugin, os, sys, plugintools
from addon.common.addon import Addon

addonID = 'plugin.video.piologo'
addon   = Addon(addonID, sys.argv)
local   = xbmcaddon.Addon(id=addonID)
icon    = local.getAddonInfo('icon')
base    = 'plugin://plugin.video.youtube/'

fan01 = 'special://home/addons/plugin.video.piologo/resources/fan01.png'
icon = 'special://home/addons/plugin.video.piologo/resources/icon.png'
icon00 = 'special://home/addons/plugin.video.piologo/resources/icon00.png'
icon01 = 'special://home/addons/plugin.video.piologo/resources/icon01.png'
icon02 = 'special://home/addons/plugin.video.piologo/resources/icon02.png'
icon03 = 'special://home/addons/plugin.video.piologo/resources/icon03.png'
icon04 = 'special://home/addons/plugin.video.piologo/resources/icon04.png'
icon05 = 'special://home/addons/plugin.video.piologo/resources/icon05.png'
icon06 = 'special://home/addons/plugin.video.piologo/resources/icon06.png'
icon07 = 'special://home/addons/plugin.video.piologo/resources/icon07.png'
icon08 = 'special://home/addons/plugin.video.piologo/resources/icon08.png'
icon09 = 'special://home/addons/plugin.video.piologo/resources/icon09.png'
icon10 = 'special://home/addons/plugin.video.piologo/resources/icon10.png'
icon11 = 'special://home/addons/plugin.video.piologo/resources/icon11.png'
icon12 = 'special://home/addons/plugin.video.piologo/resources/icon12.png'
icon13 = 'special://home/addons/plugin.video.piologo/resources/icon13.png'


def run():
    plugintools.log("piologo.run")
    params = plugintools.get_params()
    if params.get("action") is None: main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    plugintools.close_item_list()

def main_list(params):
	plugintools.log("piologo ===> " + repr(params))
	
	
	plugintools.add_item(title = "DESTAQUES-O MELHOR E O PIOR", url =  base + "playlist/PLW8JWj0QilvWqmdhDeHv7f7fxtUGxqMmN/", thumbnail = icon01, fanart = fan01, folder = True)
	plugintools.add_item(title = "PARTOBA", url = base + "playlist/PLW8JWj0QilvVaUcT_P3py2DPb_rGCWAB9/", thumbnail = icon02, fanart = fan01, folder = True)
	plugintools.add_item(title = "AS PESSOAS MAIS INTELIGENTEMENTE BURRAS DA TERRA!", url = base + "playlist/PLW8JWj0QilvUxDnlRGcyt3RoBlYfPSzd3/", thumbnail = icon03, fanart = fan01, folder = True)
	plugintools.add_item(title = "PASTOR METRELHADORA", url = base + "playlist/PLW8JWj0QilvXcnyiBtizPuxmAndJ2dkDq/", thumbnail = icon04, fanart = fan01, folder = True)
	plugintools.add_item(title = "THUG LIFE IRMÃOS PIOLOGO", url = base + "playlist/PLW8JWj0QilvUsVb1-iZ-_8Uh2Gen9aVIG/", thumbnail = icon05, fanart = fan01, folder = True)
	plugintools.add_item(title = "PIORES MOMENTOS DO BRASIL NAS COPAS!!!", url = base + "playlist/PLW8JWj0QilvVH-5oZyZ6Sm9d8vRbIHuzd/", thumbnail = icon06, fanart = fan01, folder = True)
	plugintools.add_item(title = "DESAFIOS E DICAS", url = base + "playlist/PLW8JWj0QilvUaI-b-21Yh9c5d-JjXtoKH/", thumbnail = icon07, fanart = fan01, folder = True)
	plugintools.add_item(title = "IRMÃOS PIOLOGO FILMES", url = base + "playlist/PLW8JWj0QilvWGE1le0VogUQwiyJbe9iSm/", thumbnail = icon08, fanart = fan01, folder = True)
	plugintools.add_item(title = "XINGANDO MUITO E COMENTARALHO COM OS IRMÃOS PIOLOGO", url = base + "playlist/PLW8JWj0QilvX8EQ_KSD6jTiXLlhX-mPtm/", thumbnail = icon09, fanart = fan01, folder = True)
	plugintools.add_item(title = "ENTREVISTAS", url = base + "playlist/PLW8JWj0QilvXzJ8nuqWnnauP4Q1DgzNQd/", thumbnail = icon10, fanart = fan01, folder = True)
	plugintools.add_item(title = "TRIP LOKA", url = base + "playlist/PLW8JWj0QilvW1hWk3JQ1Kztu7ga7WTs7y/", thumbnail = icon11, fanart = fan01, folder = True)
	plugintools.add_item(title = "RETARDA NEWS", url = base + "playlist/PLlBrtqz6Ki1x3rkncSjduyp-oZwohcwJw/", thumbnail = icon12, fanart = fan01, folder = True)
	plugintools.add_item(title = "MIX PIOLOGO", url = base + "playlist/PL19gknxbuyZojroqNcZUGZ618APul2YNk/", thumbnail = icon13, fanart = fan01, folder = True)
	
	



	

	xbmcplugin.setContent(int(sys.argv[1]), 'movies')
	xbmc.executebuiltin('Container.SetViewMode(500)')
	
run()
