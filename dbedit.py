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
