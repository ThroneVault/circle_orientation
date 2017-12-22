<<<<<<< HEAD
import cv2
import numpy as np
cap=cv2.VideoCapture(1)
while 1:



    circles=0
    print "detecting"
    while 1:
        print "d1"

        ret, frame = cap.read()
        imgOriginal = frame
        img = frame


        img = cv2.medianBlur(img, 5)
        cimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        hsv = cv2.cvtColor(imgOriginal, cv2.COLOR_BGR2HSV)

        circles = cv2.HoughCircles(cimg, cv2.HOUGH_GRADIENT,1.1,15,
                            param1=10,param2=80,minRadius=30,maxRadius=90)
        if (circles is None)!=1:
            break
    lowh = 0
    high = 114
    lows = 168
    higs = 255
    lowv = 157
    higv = 255

    d = np.array([lowh, lows, lowv])
    t = np.array([high, higs, higv])
    filt = cv2.inRange(hsv, d, t)

    c = 0
    diz = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    roi = diz





    for i in circles[0, :]:


        # draw the outer circle
        cv2.circle(imgOriginal, (i[0], i[1]), i[2], (0, 255, 0), 2)
        # draw the center of the circle
        cv2.circle(imgOriginal, (i[0], i[1]), 2, (0, 0, 255), 3)
        diz[c] = i
        diz[c][0] = int(diz[c][0])
        diz[c][1] = int(diz[c][1])
        diz[c][2] = int(diz[c][2])
        roi[c] = [diz[c][0] - diz[c][2], diz[c][1] - diz[c][2], diz[c][2], diz[c][2]]
        c += 1

    cou = c
    res = [0, 0, 0, 0, 0, 0]
    cir = 0
    cropped = [0, 0, 0, 0]

    print roi[0]
    while (cir < cou):
        print cir
        cv2.rectangle(imgOriginal, (roi[cir][0], roi[cir][1]),
                      (roi[cir][0] + roi[cir][2] + roi[cir][2], roi[cir][1] + roi[cir][2] + roi[cir][2]), (255, 0, 0),
                      2)
        res[cir] = filt[int(roi[cir][1]):int(roi[cir][1] + roi[cir][2] + roi[cir][2]),
                   int(roi[cir][0]):int(roi[cir][0]) + int(roi[cir][2] + roi[cir][2])]
        print [int(roi[cir][0]), int(roi[cir][0]) + int(roi[cir][2] + roi[cir][2]), int(roi[cir][1]),
               int(roi[cir][1] + roi[cir][2] + roi[cir][2])]
        cir += 1

    last_i = 0
    renk_i = 0
    renk_j = 0
    last_j = 0
    buli = [0, 0, 0, 0]
    bulj = [0, 0, 0, 0, 0]
    sayas = 0
    j = 0
    c = 0
    i = 0
    counter = 0
    t = 0
    yenicount = 0
    egim = [0, 0, 0, 0, 0, 0, 0]
    while (yenicount < cir):
        print "counter: ", yenicount
        isl = res[yenicount]
        rows, cols = isl.shape
        while (i < rows - 3):
            while (j < cols - 3):
                if (res[yenicount][i, j] > 5):
                    renk_i = i + renk_i
                    renk_j = j + renk_j
                    counter += 1
                j += 1
            i += 1
            j = 0

        i = 0
        j = 0
        if counter==0:
            counter=1
        buli[yenicount] = renk_i / counter
        bulj[yenicount] = renk_j / counter
        renk_i = 0
        renk_j = 0

        print "i j", buli[yenicount], bulj[yenicount]
        print "row col", rows / 2, cols / 2
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.line(res[yenicount], (bulj[yenicount], buli[yenicount]), (rows / 2, cols / 2), (255, 255, 255))
        counter = 0

        egimust = -float((buli[yenicount] - (rows / 2)))
        egimalt = float((bulj[yenicount] - (cols / 2)))
        print "egimust:", egimust
        print "egimalt:", egimalt
        if egimalt==0:
            egimalt=0.00001

        egim[yenicount] = (np.arctan(egimust / egimalt)) * (180 / np.pi)
        print "egim=", egim[yenicount]
        if egim[yenicount] < 0:
            egim[yenicount] = egim[yenicount] + 360
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(imgOriginal, str(int(egim[yenicount])), (diz[yenicount][0], diz[yenicount][1]), font, 2,
                    (255, 255, 255), 2, cv2.LINE_AA)
        yenicount += 1

    cv2.imshow('detected circles', imgOriginal)
    cv2.waitKey(30)

=======
import cv2
import numpy as np
cap=cv2.VideoCapture(1)
while 1:



    circles=0
    print "detecting"
    while 1:
        print "d1"

        ret, frame = cap.read()
        imgOriginal = frame
        img = frame


        img = cv2.medianBlur(img, 5)
        cimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        hsv = cv2.cvtColor(imgOriginal, cv2.COLOR_BGR2HSV)

        circles = cv2.HoughCircles(cimg, cv2.HOUGH_GRADIENT,1.1,15,
                            param1=10,param2=80,minRadius=30,maxRadius=90)
        if (circles is None)!=1:
            break
    lowh = 0
    high = 114
    lows = 168
    higs = 255
    lowv = 157
    higv = 255

    d = np.array([lowh, lows, lowv])
    t = np.array([high, higs, higv])
    filt = cv2.inRange(hsv, d, t)

    c = 0
    diz = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    roi = diz





    for i in circles[0, :]:


        # draw the outer circle
        cv2.circle(imgOriginal, (i[0], i[1]), i[2], (0, 255, 0), 2)
        # draw the center of the circle
        cv2.circle(imgOriginal, (i[0], i[1]), 2, (0, 0, 255), 3)
        diz[c] = i
        diz[c][0] = int(diz[c][0])
        diz[c][1] = int(diz[c][1])
        diz[c][2] = int(diz[c][2])
        roi[c] = [diz[c][0] - diz[c][2], diz[c][1] - diz[c][2], diz[c][2], diz[c][2]]
        c += 1

    cou = c
    res = [0, 0, 0, 0, 0, 0]
    cir = 0
    cropped = [0, 0, 0, 0]

    print roi[0]
    while (cir < cou):
        print cir
        cv2.rectangle(imgOriginal, (roi[cir][0], roi[cir][1]),
                      (roi[cir][0] + roi[cir][2] + roi[cir][2], roi[cir][1] + roi[cir][2] + roi[cir][2]), (255, 0, 0),
                      2)
        res[cir] = filt[int(roi[cir][1]):int(roi[cir][1] + roi[cir][2] + roi[cir][2]),
                   int(roi[cir][0]):int(roi[cir][0]) + int(roi[cir][2] + roi[cir][2])]
        print [int(roi[cir][0]), int(roi[cir][0]) + int(roi[cir][2] + roi[cir][2]), int(roi[cir][1]),
               int(roi[cir][1] + roi[cir][2] + roi[cir][2])]
        cir += 1

    last_i = 0
    renk_i = 0
    renk_j = 0
    last_j = 0
    buli = [0, 0, 0, 0]
    bulj = [0, 0, 0, 0, 0]
    sayas = 0
    j = 0
    c = 0
    i = 0
    counter = 0
    t = 0
    yenicount = 0
    egim = [0, 0, 0, 0, 0, 0, 0]
    while (yenicount < cir):
        print "counter: ", yenicount
        isl = res[yenicount]
        rows, cols = isl.shape
        while (i < rows - 3):
            while (j < cols - 3):
                if (res[yenicount][i, j] > 5):
                    renk_i = i + renk_i
                    renk_j = j + renk_j
                    counter += 1
                j += 1
            i += 1
            j = 0

        i = 0
        j = 0
        if counter==0:
            counter=1
        buli[yenicount] = renk_i / counter
        bulj[yenicount] = renk_j / counter
        renk_i = 0
        renk_j = 0

        print "i j", buli[yenicount], bulj[yenicount]
        print "row col", rows / 2, cols / 2
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.line(res[yenicount], (bulj[yenicount], buli[yenicount]), (rows / 2, cols / 2), (255, 255, 255))
        counter = 0

        egimust = -float((buli[yenicount] - (rows / 2)))
        egimalt = float((bulj[yenicount] - (cols / 2)))
        print "egimust:", egimust
        print "egimalt:", egimalt
        if egimalt==0:
            egimalt=0.00001

        egim[yenicount] = (np.arctan(egimust / egimalt)) * (180 / np.pi)
        print "egim=", egim[yenicount]
        if egim[yenicount] < 0:
            egim[yenicount] = egim[yenicount] + 360
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(imgOriginal, str(int(egim[yenicount])), (diz[yenicount][0], diz[yenicount][1]), font, 2,
                    (255, 255, 255), 2, cv2.LINE_AA)
        yenicount += 1

    cv2.imshow('detected circles', imgOriginal)
    cv2.waitKey(30)

>>>>>>> b70be5849246137222a3511a73c9e1e8b87fd238
cv2.destroyAllWindows()