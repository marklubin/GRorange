# encoding: utf-8
"""
terminal.py

Created by Mark Lubin on 2012-04-19.
"""
from notification import Notification
import strings
import errors

class Terminal(Notification):
  
  def __init__(self):
    pass
  
  def notify(self,user,n):
    print strings.newMsgNot % (user,n)
 
    
  