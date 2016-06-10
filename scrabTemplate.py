import cv2
import numpy as np
import track
import tic
import wiringpi2 as wiringpi


wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(25, 0) # pin 22 right n left


xo=[]
for j in range(0,9):
    xo.append('B')
cam=cv2.VideoCapture(0)

q=raw_input("Keep block at start of 1st position and press q-->")
for i in xrange(30):
    ret,frame=cam.read()
ret,frame=cam.read()
img_rgb=frame
#img_rgb = cv2.imread('board.PNG')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('oo.PNG',0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.75
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
    print pt
    xs=pt[0]
    ys=pt[1]
cv2.imshow("frame",img_rgb)
#cam.release()
del(cam)
#cv2.destroyAllWindows()

cam=cv2.VideoCapture(0)
q=raw_input("Keep block at end of 1st position and press q-->")
for i in xrange(30):
    ret,frame=cam.read()
ret,frame=cam.read()
img_rgb=frame
#img_rgb = cv2.imread('board.PNG')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('oo.PNG',0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.75
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
    print pt
    xe=pt[0]
    ye=pt[1]
cv2.imshow("frame",img_rgb)
#cam.release()
del(cam)
cv2.destroyAllWindows()

while(1):

    arduinoFlag=wiringpi.digitalRead(25)
    
    q=input("Enter q after getting ready to play-->")
    arduinoFlag=1
    #cam=cv2.VideoCapture(0)
    while(arduinoFlag):
        for j in range(0,9):
            xo[j]='B'
        cam=cv2.VideoCapture(0)
        for i in xrange(30):
            ret,frame=cam.read()
        ret,frame=cam.read()
        img_rgb=frame
    #img_rgb = cv2.imread('board.PNG')
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        template = cv2.imread('oo.PNG',0)
        w, h = template.shape[::-1]

        res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
        threshold = 0.75
        loc = np.where( res >= threshold)
        for pt in zip(*loc[::-1]):
            cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
            b=track.track(pt[0],pt[1],xs,ys,xe,ye)
            xo[b-1]='O'

        template = cv2.imread('xx.PNG',0)
        w, h = template.shape[::-1]

        res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
        threshold = 0.6
        loc = np.where( res >= threshold)
        for pt in zip(*loc[::-1]):
            cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
            b=track.track(pt[0],pt[1],xs,ys,xe,ye)
            xo[b-1]='X'

        print xo
        temp="".join(xo)
        final=tic.tictactoe(temp,'X')
        z=([i for i in xrange(len(temp)) if temp[i] != final[i]])
        if len(z)>0:
            print(z[0]+1)
        cv2.imshow("frame",img_rgb)
        q=input("press q for next move-->")
        cv2.imwrite('res.png',img_rgb)
        if cv2.waitKey(1) & 0xff==ord('q'):
            break
        del(cam)

        arduinoFlag=0
        cv2.destroyAllWindows()


