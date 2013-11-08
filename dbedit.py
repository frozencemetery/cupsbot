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
  # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
  # GNU General Public License for more details.

  # You should have received a copy of the GNU General Public License
  # along with cupsbot. If not, see <http://www.gnu.org/licenses/>.

import sys

import cPickle as P

from cupsbot import TestBot as C

with open(C.dblocat, 'r') as f:
  db = P.load(f)
  pass

while True:
  sys.stdout.write("\\>> "); sys.stdout.flush()

  cur = sys.stdin.read(2)
  if cur[0] == 'q':
    print "May the cups be with you!"
    sys.exit()
    pass
  elif cur[0] == 'w':
    with open(C.dblocat, 'w') as f:
      P.dump(db, f)
      pass
    print "Core dumped!"
    pass
  elif cur[0] == 'd':
    print "Contents:"
    for i in range(len(db)):
      print (i, db[i])
      pass
    print "EOF"
    pass
  elif cur[0] == 'D':
    cur = cur[1:] # del(cur[0]) # kill the 'D'
    while cur[-1] != '\n':
      cur += sys.stdin.read(1)
      pass
    cur = int(cur)
    del(db[cur])
    print "Deleted quote number " + str(cur)
  else:
    print "Usage:"
    print " - q: exit the program"
    print " - w: write the database out to disk"
    print " - d: display the database with line numbers"
    print " - D <num>: delete quote number <num>"
    print ""
    pass
  pass
