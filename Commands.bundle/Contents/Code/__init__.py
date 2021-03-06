import commands
import platform
import os

APPLICATIONS_PREFIX = "/applications/commands"

NAME = L('Title')

ART  = 'art-default.jpg'
ICON = 'icon-default.png'

OS = platform.system()

####################################################################################################

def Start():
    ##  http://dev.plexapp.com/docs/mod_Plugin.html
    Plugin.AddPrefixHandler(APPLICATIONS_PREFIX, ApplicationsMainMenu, NAME, ICON, ART)

    Plugin.AddViewGroup("InfoList", viewMode="InfoList", mediaType="items")
    Plugin.AddViewGroup("List", viewMode="List", mediaType="items")

    MediaContainer.title1 = NAME
    MediaContainer.viewGroup = "List"
    MediaContainer.art = R(ART)
    DirectoryItem.thumb = R(ICON)
    VideoItem.thumb = R(ICON)
    
    HTTP.CacheTime = CACHE_1HOUR

def ApplicationsMainMenu():
    dir = MediaContainer(viewGroup="InfoList")

    dir.Append(
        Function(
            DirectoryItem(
                Shutdown,
                L('MenuShutdown'),
                subtitle="shutdown",
                thumb=R(ICON),
                art=R(ART)
            )
        )
    )

    dir.Append(
        Function(
            DirectoryItem(
                Reboot,
                L('MenuReboot'),
                subtitle="reboot",
                thumb=R(ICON),
                art=R(ART)
            )
        )
    )

    dir.Append(
        Function(
            DirectoryItem(
                Hibernate,
                L('MenuHibernate'),
                subtitle="hibernate",
                thumb=R(ICON),
                art=R(ART)
            )
        )
    )

    dir.Append(
        Function(
            DirectoryItem(
                Suspend,
                L('MenuSuspend'),
                subtitle="suspend",
                thumb=R(ICON),
                art=R(ART)
            )
        )
    )

    dir.Append(
        Function(
            DirectoryItem(
                ForceRefresh,
                L('MenuForceRefresh'),
                subtitle="forcerefresh",
                thumb=R(ICON),
                art=R(ART)
            )
        )
    )

    return dir

def Shutdown(sender):
	if OS == 'Windows':
		Log(os.system('shutdown -s'))
	else:
		Log(commands.getoutput('sudo shutdown -h now'))
	return MessageContainer("Shutdown", L('LogShutdown'))

def Reboot(sender):
	if OS == 'Windows':
		Log(os.system('shutdown -r'))
	else:
		Log(commands.getoutput('sudo shutdown -r -h now'))
		
	return MessageContainer("Reboot", L('LogReboot'))

def Hibernate(sender):
	if OS == 'Windows':
		Log(os.system('shutdown -h'))
	else:
		Log(commands.getoutput('sudo pm-hibernate'))

	return MessageContainer("Hibernate", L('LogHibernate'))

def Suspend(sender):
	if OS == 'Windows':
		Log(os.system('shutdown -h'))
	else:
		Log(commands.getoutput('sudo pm-suspend'))

	return MessageContainer("Suspend", L('LogSuspend'))

def ForceRefresh(sender):
    return MessageContainer("ForceRefresh", L('LogForceRefresh'))

