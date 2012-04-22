#strings.py
#encoding: utf-8
"""
List of strings for application, enables multilanguage support, strings.py
is for English language verision of app, other languages should store same 
string in files named 'string_(Langcode).py', debug output is hardcoded in 
English
"""
userAgent = "GRoange"
welcome = u"""\n\n\n\nWelcome to GRoange, the Reddit Notification Manager for OS X and Growl
----------------------------------------------------------------------"""
newMsgNot = "%s has new %i messages on Reddit."
cantLogin = "Can't login to %s, because: %s" 
redditUnavail = "Cannot connect to reddit."
timeoutclose = "I can't seem to reach reddit now, try again later."
timeoutretry = "Couldn't reach reddit %i retries left."
nousers = 'Sorry, I cannot connect any of your accounts to Reddit. Closing...'

