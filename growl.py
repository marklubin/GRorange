# encoding: utf-8
"""
growl.py

Created by Mark Lubin on 2012-04-19.
"""
from notification import Notification
import errors
import strings
import gntp.notifier
import strings

class Growl(Notification):
  __growl = None
  
  def __init__(self):
    self.__growl = gntp.notifier.GrowlNotifier(
        applicationName = strings.userAgent,
        notifications = ["New Messages"],
        defaultNotifications = ["New Messages"],
    )
    self.__growl.register()
  
  def notify(self,user,n):
    self.__growl.notify(
        noteType = "New Messages",
        title = strings.userAgent,
        description = strings.newMsgNot % (user,n),
        icon = r"http://upload.wikimedia.org/wikipedia/fr/f/fc/Reddit-alien.png",
        sticky = False,
        priority = 1,
    )
    



