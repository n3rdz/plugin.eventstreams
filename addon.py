import sys
import xbmcgui
import xbmcplugin

addon_handle = int(sys.argv[1])

xbmcplugin.setContent(addon_handle, 'movies')

url = 'http://swrdasding-lh.akamaihd.net/i/dasdingvisual_live@6416/master.m3u8'
li = xbmcgui.ListItem('DASDING Visual Radio')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://swr3visual-lh.akamaihd.net/i/swr3visual_live@6410/master.m3u8'
li = xbmcgui.ListItem('SWR3 Visual Radio')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://swr_event01_uni-lh.akamaihd.net/i/swr_event01@112805/master.m3u8'
li = xbmcgui.ListItem('SWR Event1')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://swr_event02_uni-lh.akamaihd.net/i/swr_event02@112806/master.m3u8'
li = xbmcgui.ListItem('SWR Event2')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://swr_event03_uni-lh.akamaihd.net/i/swr_event03@198168/master.m3u8'
li = xbmcgui.ListItem('SWR Event3')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://swr_event04_uni-lh.akamaihd.net/i/swr_event04@198169/master.m3u8'
li = xbmcgui.ListItem('SWR Event4')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://ndr_events-lh.akamaihd.net/i/ndrevent_1@119220/master.m3u8'
li = xbmcgui.ListItem('NDR Event1')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://brevent1hds-lh.akamaihd.net/i/br_event02isma@111248/master.m3u8'
li = xbmcgui.ListItem('BR Event2')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

xbmcplugin.endOfDirectory(addon_handle)
