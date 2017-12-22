import cv2
import numpy as np

imgOriginal = cv2.imread('pembe.jpg', 1)
img = cv2.imread('pembe.jpg', 0)
img = cv2.medianBlur(img, 5)
cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
hsv = cv2.cvtColor(imgOriginal, cv2.COLOR_BGR2HSV)

print "detecting"
circles1 = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1.1, 200,50,90,60,80)
circles2 = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1.1, 200,50,90,60,120)

c = 0

for i in circles1[0, :]:
    # draw the outer circle
    cv2.circle(imgOriginal, (i[0], i[1]), i[2], (0, 255, 0), 2)
    # draw the center of the circle
    cv2.circle(imgOriginal, (i[0], i[1]), 2, (0, 0, 255), 3)

for i in circles2[0, :]:
    # draw the outer circle
    cv2.circle(imgOriginal, (i[0], i[1]), i[2], (0, 255, 0), 2)
    # draw the center of the circle
    cv2.circle(imgOriginal, (i[0], i[1]), 2, (0, 0, 255), 3)

c=0
counter=0
t=0
yenicount=0
egim=[0,0,0,0,0,0,0]


edges = cv2.Canny(img,50,150,apertureSize = 3)

ctr=0
minLineLength = 20
maxLineGap = 10
lines = cv2.HoughLinesP(edges,1,np.pi/180,50,minLineLength,maxLineGap)
for x in range(0, len(lines)):
    for x1,y1,x2,y2 in lines[x]:
        cv2.line(imgOriginal,(x1,y1),(x2,y2),(255,255,0),2)
        print lines
print "values"

cv2.circle(hsv, (int(circles1[0][0][0]),int(circles1[0][0][1])), int(circles1[0][0][2]), [0,0,0], -1)  # fills inside of the little circle

lowh = 0
high = 255
lows = 0
higs = 38
lowv = 92
higv = 255
font = cv2.FONT_HERSHEY_SIMPLEX

d = np.array([lowh, lows, lowv])
t = np.array([high, higs, higv])
filt = cv2.inRange(hsv, d, t)
im1 = np.zeros(filt.shape, np.uint8)
cv2.circle(im1, (int(circles2[0][0][0]),int(circles2[0][0][1])), int(circles2[0][0][2]), [255,255,255], -1)
res = np.zeros(filt.shape, np.uint8)

cv2.bitwise_and(filt,im1,res)
rows,cols=res.shape
print rows,cols
i=0
j=0
d=0

#dikey arama, dikeyde ilk gelen pikseli secer
while (j < cols-10 )&(d==0):
    while (i < rows-10 ):
        if (res[i,j] > 5)and (res[i+5,j+5]>5):
            renk_i = i
            renk_j = j
            cv2.putText(imgOriginal, ".", (renk_j,renk_i+20), font, 5, (0, 255, 255), 5,
                        cv2.LINE_AA)
            print i,j
            d=1
        i += 1
    j += 1
    i = 0
renk_i=renk_i+20
cv2.line(imgOriginal, (renk_j,renk_i), (circles2[0][0][0],circles2[0][0][1]), (255, 255, 255))

egimust=-float(renk_i - circles2[0][0][1])
egimalt = -float(renk_j - circles2[0][0][0])
print "egimust:",egimust
print "egimalt:",egimalt

egim[yenicount]=(np.arctan(egimust / egimalt))*(180/np.pi)
print "egim=", egim[yenicount]

print renk_i
print renk_j

cv2.imshow('detected circles',imgOriginal)
cv2.imshow('map',res)
cv2.waitKey(0)
cv2.destroyAllWindows()