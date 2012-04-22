# encoding: utf-8
"""
user.py
class for reddit user, handles reddit API calls
Created by Mark Lubin on 2012-04-19.
"""
#Reddit user class

import reddit
import strings
import errors

class User:
  __username = ''
  __password = ''
  __newMsgs = False
  __shouldNotify = False
  __newMsgCnt = 0
  __msgsReported = 0
  __red = ''
  
  def __init__(self,username,password):
    self.__username = username
    self.__password = password
    self.__newMsgs = False
    self.__shouldNotify = True
    self.__newMsgCnt == 0
    self.__msgsReported == 0
    self.__red = reddit.Reddit(user_agent = strings.userAgent)
    try:
      self.__red.login(self.__username,self.__password)
    except Exception as e:
      raise errors.GRorangeCantAuthenticate(str(e))
    
  def getShouldNotify(self):
    return self.__shouldNotify
 
  def setShouldNotify(self,should):
    self.__shouldNotify = should
  
  
  def getUsername(self):
    return self.__username
  
  def hasNewMsgs(self):
    self.__newMsgCnt = len(list(self.__red.user.get_unread(limit=None)))
    #print "Found %i messages." % self.__newMsgCnt
    #print "Have reported %i messages" % self.__msgsReported
    if self.__newMsgCnt > self.__msgsReported:
      self.__msgsReported += self.__newMsgCnt
      return self.__newMsgCnt
    else: return 0
      