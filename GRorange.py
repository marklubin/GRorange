#!/usr/bin/env python
# encoding: utf-8
"""
GRorange.py
Created by Mark Lubin on 2012-04-19.
"""

import sys
import os
import time




def main():
  import user
  import terminal
  import growl
  import errors
  
  #initialize vars
  isTerminal = True
  isConfigFile = True
  isDebug = False
  lang = 'EN'
  delay = 10
  timeoutlimit = 5
  redditUsers = []
  notificationReceivers = []
  
  #initialize language and import correct strings
  if lang == 'EN':
    exec("import strings")
    
  
  """
  Read command line argruments
  -----------------------------
  -c = use configuration file conf.ini for username,password,delahy
  -t = display notification in termial
  -g = display notification in Growl
  -i = use GUI interface for user configuration
  -d = use debug mode, print debug statments to terminal
  """
  for arg in sys.argv:
    if arg == '-t':
      isTerminal = True
    elif arg == '-c':
      isConfigFile = True
    elif arg == '-d':
      isDebug = True
      
  if isDebug: print """Running with:
  isDebug = %s
  isTerm = %s
  isConfigFile %s \n""" % (isDebug,isTerminal,isConfigFile)
  
  if isTerminal: print strings.welcome
    
  if isConfigFile:
    import conf
    delay = conf.delay
    timeoutlimit = conf.timeoutlimit
    if isDebug: 
      print "Delay set to %i by conf.py" % delay
      print "Timeout limit set to %i by conf.py" % timeoutlimit
    
    for x in conf.users:
      #construct new user and append to redditUsers
      if isDebug: print "Trying to login: %s" % x['username']
      try:
        redditUsers.append(user.User(x['username'],x['password']))
      except errors.GRorangeCantAuthenticate as e:
        print strings.cantLogin % (x['username'],str(e))
        if isDebug: print "Password: %s" % x['password']
        continue
    
  if isDebug: 
    for user in redditUsers:
      print "Added user account for: %s" % user.getUsername()
      
      
  #initialize IO object GROWL/CMDLINE/ETC
  if isTerminal:
    notificationReceivers.append(terminal.Terminal())
    if isDebug: print "Initialized terminal as Notification Receiver"
  
  #main loop for message checking
  timeout = 0
  if not len(redditUsers):
    print strings.nousers
    sys.exit()
  while True:
    for user in redditUsers:
      if isDebug: print "Checking messages for %s" % user.getUsername()
      try:
        num = user.hasNewMsgs()
      except errors.GRorangeCantConnectToReddit as e:
        timeout += 1
        if timeout == timeoutlimit:
          print strings.timeoutclose
          sys.exit()
        else:
          print strings.timeoutretry % (timeoutlimit-timeout)
      else:
        timeout = 0
        
      if num:
        for notifier in notificationReceivers:
          notifier.notify(user.getUsername(),num)
          if isDebug: print "Found new messages!"
      else:
        if isDebug: print "No new messages."
    if isDebug: print "Waiting %i seconds." % delay
    time.sleep(delay) #wait for delay seconds
      
  


if __name__ == '__main__':
  main()

