import cv2


fgbg= cv2.createBackgroundSubtractorMOG2(200,15,1)
fgbg2= cv2.createBackgroundSubtractorMOG2(200,15,1)
cap = cv2.VideoCapture(0)
k=0
fps=0
sayac=0
while 1:
    ret, img = cap.read()
    img = cv2.GaussianBlur(img, (5, 5), 3)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    frame=img
    while fps<200:
       ret, frame = cap.read()
       fgmask = fgbg2.apply(frame, learningRate=0.005)
       fps+=1
       print "Training"
       if fps>199:
           print "Training Ends"

    fgmask = fgbg2.apply(frame,learningRate=0.0001)

    cv2.imshow('fg', fgmask)
    cv2.imshow('img', img)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()