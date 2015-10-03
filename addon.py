import sys
import xbmcgui
import xbmcplugin
addon_handle = int(sys.argv[1])
xbmcplugin.setContent(addon_handle, 'audio')
url = 'http://swrdasding-lh.akamaihd.net/i/dasdingvisual_live@6416/master.m3u8'
li = xbmcgui.ListItem(label='DASDING Visual Radio Stream')
url = 'http://swr3visual-lh.akamaihd.net/i/swr3visual_live@6410/master.m3u8'
li = xbmcgui.ListItem(label='SWR3 Visual Radio Stream')
url = 'http://swr_event01_uni-lh.akamaihd.net/i/swr_event01@112805/master.m3u8'
li = xbmcgui.ListItem(label='Event Stream 01')
url = 'http://swr_event02_uni-lh.akamaihd.net/i/swr_event02@112806/master.m3u8'
li = xbmcgui.ListItem(label='Event Stream 02')
url = 'http://swr_event03_uni-lh.akamaihd.net/i/swr_event03@198168/master.m3u8'
li = xbmcgui.ListItem(label='Event Stream 03')
url = 'http://swr_event04_uni-lh.akamaihd.net/i/swr_event04@198169/master.m3u8'
li = xbmcgui.ListItem(label='Event Stream 04')
li.setIconImage('DefaultVideo.png')
li.setThumbnailImage('icon.png')
li.setProperty('fanart_image', 'visualradio.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
xbmcplugin.endOfDirectory(addon_handle)
