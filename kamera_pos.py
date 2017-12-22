import cv2
import numpy as np


def close(a,b,thr):
    if abs(a-b)<thr:
        return 1
    return 0
diz = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
old_diz =  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
print "BASLANGIC"
cap=cv2.VideoCapture(1)
thr=5

fr=0
while 1:

    circles=0
    print "detecting"
    while 1:
        ret, frame = cap.read()
        imgOriginal = frame
        img = frame


        img = cv2.medianBlur(img, 5)
        cimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        hsv = cv2.cvtColor(imgOriginal, cv2.COLOR_BGR2HSV)

        circles = cv2.HoughCircles(cimg, cv2.HOUGH_GRADIENT, 1.1, 85, param1=30, param2=70, minRadius=55, maxRadius=75)  # 90

        # Param 1 will set the sensitivity; how strong the edges of the circles need to be. Too high and it won't detect anything, too low and it will find too much clutter.
        # Param 2 will set how many edge points it needs to find to declare that it's found a circle. Again, too high will detect nothing, too low will declare anything to be a circle.
        # The ideal value of param 2 will be related to the circumference of the circles.

        if (circles is None)!=1:
            break

    c = 0
    sayac=0
    sayac2=0
    for i in circles[0, :]:
        # draw the outer circle
        cv2.circle(imgOriginal, (i[0], i[1]), i[2], (0, 255, 0), 2)
        # draw the center of the circle
        cv2.circle(imgOriginal, (i[0], i[1]), 2, (0, 0, 255), 3)
        diz[c] = i
        if fr == 0:
            print "only once"
            old_diz[c] = i

        print diz[c]

        c += 1
    sayac=0
    fr = 1
    print "Eski dizi"
    while (sayac < c):
        print old_diz[sayac]

        sayac += 1

    print " "
    sayac=0
    sayac2=0
    while sayac < c:
        while sayac2<c:
            print ""
            print old_diz[sayac2][0]
            print "vs"
            print diz[sayac][0]
            if close(old_diz[sayac2][0], diz[sayac][0], 10) and close(old_diz[sayac2][1], diz[sayac][1], 10) and (diz[sayac2][2]>old_diz[sayac][2]):
                # update
                diz[sayac2][0]=old_diz[sayac][0]
                diz[sayac2][1] = old_diz[sayac][1]
                diz[sayac2][2] = old_diz[sayac][2]
                print "update",sayac2,sayac

            sayac2 += 1
        sayac+=1
        sayac2=0

    sayac = 0
    sayac2=0
    while (sayac < c):
        old_diz[sayac] = diz[sayac]

        sayac += 1
    sayac=0
    print "Yenilenen dizi"
    while (sayac < c):
        print diz[sayac]
        sayac += 1

    print " "
    font = cv2.FONT_HERSHEY_SIMPLEX
    yenicount = 0
    while yenicount<c:
        cv2.putText(imgOriginal, str(int(diz[yenicount][0]))+","+str(int(diz[yenicount][1]))+","+str(int(diz[yenicount][2])), (diz[yenicount][0], diz[yenicount][1]), font, 2,
                    (255, 255, 255), 2, cv2.LINE_AA)
        yenicount += 1

    cv2.imshow('detected circles', imgOriginal)
    cv2.waitKey(30)

cv2.destroyAllWindows()