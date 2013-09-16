import sys
import dbhash
db = dbhash.open(sys.argv[1], 'r')
print db.first()
for i in xrange(1, len(db)):
    print db.next()
db.close()

