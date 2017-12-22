import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')    # yuz tarama dosyasi

cap = cv2.VideoCapture(0)        #Videoyu almak icin
k=0
fps=0
sayac=0
while 1:    #Surekli dongu

    ret, img = cap.read()    #goruntudeki kareyi al
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   #goruntuyu BGR formatindan gri formata cevir
    frame=img
    faces = face_cascade.detectMultiScale(gray, 1.2, 5)    #resimdeki yuzleri ara

    # faces= [ [x,y,w,h], [x,y,w,h].....] seklinde bir dizi
    # x,y yuz bulunan yeri, w ve h yuzun boyutlarini gosterir

    c = 0       ##for dongusunun donme sayisi

    print faces
    for (x, y, w, h) in faces:      # faces dizisinin icindeki eleman sayisi kadar dongu yap
# b g r        blue green red

        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
        # bulunan yuzu dortgen icine al   --> rectangle() fonksiyonu

        c = c + 1

    print c,"yuz var"

    cv2.imshow('Goruntu', img)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()