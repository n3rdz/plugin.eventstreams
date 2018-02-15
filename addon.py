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

url = 'http://wdr_ardevent1-lh.akamaihd.net/i/wdrardevent1_weltweit@112049/master.m3u8'
li = xbmcgui.ListItem('EDR Event1')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://wdr_event2-lh.akamaihd.net/i/wdrevent2_weltweit@112052/master.m3u8'
li = xbmcgui.ListItem('EDR Event2')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://wdr_event3-lh.akamaihd.net/i/wdrevent3_weltweit@112053/master.m3u8'
li = xbmcgui.ListItem('EDR Event3')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://wdr_event4-lh.akamaihd.net/i/wdrevent4_weltweit@112054/master.m3u8'
li = xbmcgui.ListItem('EDR Event4')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://brevent1hds-lh.akamaihd.net/i/br_event01isma@86390/master.m3u8'
li = xbmcgui.ListItem('BR Event3')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
  
url = 'http://brevent1hds-lh.akamaihd.net/i/br_event02isma@111248/master.m3u8'
li = xbmcgui.ListItem('BR Event2')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://brevent1hds-lh.akamaihd.net/i/br_event03isma@111249/master.m3u8'
li = xbmcgui.ListItem('BR Event3')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://brevent1hds-lh.akamaihd.net/i/br_event04isma@111250/master.m3u8'
li = xbmcgui.ListItem('BR Event3')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://hrevent-lh.akamaihd.net/i/hr_event@309239/master.m3u8'
li = xbmcgui.ListItem('HR Event1')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://hrevent2-lh.akamaihd.net/i/hr_event2@309240/master.m3u8'
li = xbmcgui.ListItem('HR Event2')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://ndr_events-lh.akamaihd.net/i/ndrevent_1@119220/master.m3u8'
li = xbmcgui.ListItem('NDR Event1')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://ndr_events-lh.akamaihd.net/i/ndrevent_2@119221/master.m3u8'
li = xbmcgui.ListItem('NDR Event2')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://ndr_events-lh.akamaihd.net/i/ndrevent_3@119222/master.m3u8'
li = xbmcgui.ListItem('NDR Event3')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://ndr_spezial-lh.akamaihd.net/i/spezial_1@119227/master.m3u8'
li = xbmcgui.ListItem('NDR Spezial1')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://ndr_spezial-lh.akamaihd.net/i/spezial_2@119228/master.m3u8'
li = xbmcgui.ListItem('NDR Spezial2')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

 url = 'http://ndr_spezial-lh.akamaihd.net/i/spezial_3@119229/master.m3u8'
li = xbmcgui.ListItem('NDR Spezial3')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://ndr_spezial-lh.akamaihd.net/i/spezial_4@119230/master.m3u8'
li = xbmcgui.ListItem('NDR Spezial4')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://ndr_spezial-lh.akamaihd.net/i/spezial_5@384495/master.m3u8'
li = xbmcgui.ListItem('NDR Spezial5')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://ndr_spezial-lh.akamaihd.net/i/spezial_6@364638/master.m3u8'
li = xbmcgui.ListItem('NDR Spezial6')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://rbb_event-lh.akamaihd.net/i/rbbevent_nongeo@107643/master.m3u8'
li = xbmcgui.ListItem('RBB Event')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'https://arteevent01-lh.akamaihd.net/i/arte_event01@395110/master.m3u8'
li = xbmcgui.ListItem('arte Event1')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://arteevent02lh.akamaihd.net/i/arteevent02@308866/master.m3u8'
li = xbmcgui.ListItem('arte Event2')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://arteevent03lh.akamaihd.net/i/arteevent03@305298/master.m3u8'
li = xbmcgui.ListItem('arte Event3')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://liveevent1.mdr.de/i/livetvmdrevent1_ww@106904/master.m3u8'
li = xbmcgui.ListItem('MDR Event1')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
  
url = 'http://liveevent2.mdr.de/i/livetvmdrevent2_ww@106905/master.m3u8'
li = xbmcgui.ListItem('MDR Event2')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://liveevent2.mdr.de/i/livetvmdrevent3_ww@106905/master.m3u8'
li = xbmcgui.ListItem('MDR Event3')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://zdf0304-lh.akamaihd.net/i/de03_v1@392855/master.m3u8'
li = xbmcgui.ListItem('ZDF Event1')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://zdf0304-lh.akamaihd.net/i/de04_v1@392856/master.m3u8'
li = xbmcgui.ListItem('ZDF Event2')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://zdf0506-lh.akamaihd.net/i/de05_v1@392857/master.m3u8'
li = xbmcgui.ListItem('ZDF Event3')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://zdf0506-lh.akamaihd.net/i/de06_v1@392858/master.m3u8'
li = xbmcgui.ListItem('ZDF Event4')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://zdf0708-lh.akamaihd.net/i/de07_v1@392868/master.m3u8'
li = xbmcgui.ListItem('ZDF Event5')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://zdf0708-lh.akamaihd.net/i/de08_v1@392869/master.m3u8'
li = xbmcgui.ListItem('ZDF Event6')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://gl_event2_uni-lh.akamaihd.net/i/redcarpet_live@179589/master.m3u8'
li = xbmcgui.ListItem('Redcarpet Berlin Event2')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

xbmcplugin.endOfDirectory(addon_handle)
