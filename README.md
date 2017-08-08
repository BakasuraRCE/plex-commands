Plex Commands
=============

Plex channel to provide useful commands 

Features
--------

* Works on Linux, Mac OS X and Windows
* Commands can be executed from any client
* Ability to shutdown, restart, hibernate or suspend server
* Shortcut to refresh all libraries

Requirements
------------

* Plex Media Server 0.9 or higher

Install
-------

Download and extract the folder *Commands.bundle* to:

* **Linux**: /var/lib/plexmediaserver/Library/Application Support/Plex Media Server/Plug-ins
* **Mac OS X**: /Applications/Plex Media Server.app/Contents/Resources/Plug-ins

The user that runs Plex Media Server need rights to execute this commands. The easiest method in Linux and Mac OS X is [manager permissions with sudo](https://wiki.archlinux.org/index.php/pm-utils#User_permission_method):
 
```plex ALL = NOPASSWD: /sbin/shutdown -h now,/sbin/shutdown -r -h now,/usr/sbin/pm-hibernate,/usr/sbin/pm-suspend```

The user and group in Linux are *plex:plex* (daemon) but in Mac OS X the user is the one that is validated.

TO-DO
-----

* Add support for Windows
