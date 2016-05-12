import sys
import cv2
import numpy

img = cv2.imread("tic.png")
template = cv2.imread("x.png")
th, tw = template.shape[:2]

result = cv2.matchTemplate(img, template, cv2.TM_CCORR_NORMED)
threshold = 0.99
loc = numpy.where(result >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + tw, pt[1] + th), 0, 2)

cv2.imwrite("tictactoe.png", img)
