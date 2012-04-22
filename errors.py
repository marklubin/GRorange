# encoding: utf-8
"""
growl.py

Created by Mark Lubin on 2012-04-19.
"""
import urllib2
import strings

class GRorangeCantAuthenticate(Exception):
  value = ''
  def __init__(self,value):
    self.value = value
  def __str__(self):
    return repr(self.value)
    
class GRorangeCantConnectToReddit(Exception):
  value = ''
  def __init__(self,value):
    self.value = value
  def __str__(self):
    return strings.redditUnavail
    