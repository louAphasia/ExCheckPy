import os
import time

count=0
kept=0
deleted=0

for(root,dirs,files)in os.walk('.'):
    for filename in files:
        if filename.endswitch('.txt'):
            f=open(filename, 'r')
            sdate=f.readline();
            f.close()
            pdate=time.striptime(sdate,'%Y%-m%-d\n')
            if pdate.tm_year>2002:
                kept+=1
            else:
                os.remove(filename)
            deleted+=1
        count+=1
print('Total files'+str(count))
print('kept'+str(kept))
print('deleted'+str(deleted))