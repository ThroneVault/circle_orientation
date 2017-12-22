import numpy as np
import time
from datetime import datetime
startTime = datetime.now()

#do something

gelen_veri=[12.1,12.2,12.1,12.4,12.0,10.2,12.1,12.3,12.2,12.3,12.1,12.3,12.2,12.3,12.1,12.3,12.2,12.3,12.1,12.3,12.2,12.3,12.1,12.3,12.2,12.3,12.1,12.3,12.2,12.3]
#gelen_veri=[1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]
yeni=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]
t=0
ctr=0
tot=0
x=0
std=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]


for c in gelen_veri:
    z=gelen_veri[x]
    if(yeni[8]==0 and yeni[9]==0):
        for c in yeni:
            yeni[ctr]=z
            ctr += 1
    x=x+1

    #shifting
    ctr=13
    while ctr>=0:
        tot = yeni[ctr] + tot
        yeni[ctr]=yeni[ctr-1]
        ctr-=1
    yeni[0]=z
    n=14
    ort=tot/n


    ctr=0

    std=float(np.sqrt(float(pow((yeni[ctr]-ort),2)/n)))
    if std>0.2:
        print "!!!!!!!!!!!!!",ctr
        yeni[0]=ort

    print yeni[0]
    ctr=0
    ort=0
    tot=0

    ctr=0
    time.sleep(0.001)
    #print tot

print datetime.now()-startTime

