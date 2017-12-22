import cv2
import numpy as np


def f(x): return x


img = cv2.imread('gri2.jpg',1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
filt=0
lowh = 0
high = 114
lows = 168
higs = 255
lowv = 157
higv = 255

cv2.namedWindow('Control')
cv2.createTrackbar("LowH", "Control",0,255, f)
cv2.createTrackbar("HighH", "Control",0,255,  f)

cv2.createTrackbar("LowS", "Control",0,255,  f)
cv2.createTrackbar("HighS", "Control",0,255,  f)

cv2.createTrackbar("LowV", "Control",0,255,  f)
cv2.createTrackbar("HighV", "Control",0,255,  f)
while 1:


    lowh = cv2.getTrackbarPos('LowH', 'Control')
    high = cv2.getTrackbarPos('HighH', 'Control')
    lows = cv2.getTrackbarPos('LowS', 'Control')
    higs=cv2.getTrackbarPos('HighS', 'Control')
    lowv=cv2.getTrackbarPos('LowV', 'Control')
    higv=cv2.getTrackbarPos('HighV', 'Control')




    d=np.array([lowh,lows,lowv])
    t=np.array([high,higs,higv])
    filt=cv2.inRange(img, d, t)

    print "lowh=",lowh
    print "high",high
    print "lows=",lows
    print "higs=",higs
    print"lowv=",lowv
    print "higv=",higv
    cv2.imshow('detected circles',filt)
    cv2.waitKey(30)

cv2.destroyAllWindows()