#!/usr/bin/env python

# Copyright (C) 2013 Robbie Harwood (frozencemetery)
# Based on code from the python irclib python-irclib.sourceforge.net (GPL)

  # This file is part of cupsbot, based on lurker.

  # cupsbot is free software: you can redistribute it and/or modify
  # it under the terms of the GNU General Public License as published by
  # the Free Software Foundation, either version 3 of the License, or
  # (at your option) any later version.

  # cupsbot is distributed in the hope that it will be useful,
  # but WITHOUT ANY WARRANTY; without even the implied warranty of
  # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  # GNU General Public License for more details.

  # You should have received a copy of the GNU General Public License
  # along with cupsbot.  If not, see <http://www.gnu.org/licenses/>.

import cPickle
import random
import re
import time

from irc.bot import SingleServerIRCBot
from irc.client import nm_to_n, nm_to_h, irc_lower, ip_numstr_to_quad, ip_quad_to_numstr

class TestBot(SingleServerIRCBot):
  db = [] # response database
  dblocat = "cups.db"

  def __init__(self, channel, nickname, server, port=6667):
    SingleServerIRCBot.__init__(self, [(server, port)], nickname, nickname)
    self.channel = channel
    pass

  def on_nicknameinuse(self, c, e):
    c.nick(c.get_nickname() + "_")
    return

  def on_join(self, c, e):
    channel = e._target
    return

  def on_welcome(self, c, e):
    c.privmsg("NickServ", "IDENTIFY ********")
    c.join(self.channel)
    return

  def on_kick(self, c, e):
    return
  
  def on_nick(self, c, e):
    return

  def on_part(self, c, e):
    return

  def on_topic(self, c, e):
    return

  def on_mode(self, c, e):
    return

  def on_quit(self, c, e):
    return

  def load_db(self): # exception on error
    with open(self.dblocat, 'r') as f:
      self.db = cPickle.load(f)
      pass
    return

  def do_command(self, e):
    cmd = e.arguments()[0].strip()
    c = self.connection
    nick = nm_to_n(e.source())

    if "cups" in nick.toLower():
      return

    channel = e.target() # note that this might be a private query
    if channel[:1] not in ['#', '&', '+', '!']:
      channel = nick
      pass

    if re.search("c+u+p", cmd.lower()) == None:
      return
    print '(' + channel + ')' + "< " + nick + "> " + cmd

    if len(cmd) > 1 and cmd[0] == '!':
      self.load_db()
      if cmd[1:].upper() not in self.db:
        with open(self.dblocat, 'w') as f:
          self.db.append(cmd[1:].upper())
          cPickle.dump(self.db, f)
          pass
        c.privmsg(channel, nick + ": reply added!")
        pass
      else:
        c.privmsg(channel,
                  nick + ": your cups-foo is strong.  BUT MINE IS STRONGER!")
        pass
      return
    else:
      if len(self.db) == 0: # db is not loaded
        self.load_db()
        pass

      c.privmsg(channel, random.choice(self.db))
      return
    pass

  def on_action(self, c, e):
    self.do_command(e)
    return

  def on_privmsg(self, c, e):
    self.do_command(e)
    return

  def on_pubmsg(self, c, e):
    self.do_command(e)
    return

def main():
  import sys
  if len(sys.argv) != 4 and len(sys.argv) != 5:
    print "Syntax is: \"python cupsbot.py <server[:port]> <nick> <chan> [<pass>]\""
    sys.exit(1)
    pass
  
  s = sys.argv[1].split(":", 1)
  server = s[0]
  if len(s) == 2:
    try:
      port = int(s[1])
      pass
    except ValueError:
      print "PORT IS TOO WEIRD!"
      sys.exit(1)
      pass
    pass
  else:
    port = 6667
    pass

  nickname = sys.argv[2]
  
  channel = sys.argv[3]
  
  try:
    channel = channel + " " + sys.argv[4]
    pass
  except:
    pass
  
  bot = TestBot(channel, nickname, server, port)
  bot.start()
  pass

if __name__ == "__main__":
  main()
  pass
