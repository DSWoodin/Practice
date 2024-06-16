import cv2 as cv
import sys

img = cv.imread('source/ch2/girl_laughing.jpg')

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

# 'laugh'를 직사각형에서 조금 떨어뜨리고
# 화살표를 이용해 'laugh'가 직사각형을 가르키도록 확장
cv.rectangle(img, (830,30), (1000,200), (0,0,255), 2)
cv.putText(img, 'laugh', (660,90), cv.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)
# arrowedLine(영상, 시작좌표, 끝좌표, 색깔, 두께, 선 종류, shift값, 화살표 머리 크기)
cv.arrowedLine(img, (750,84), (820,84), (0,255,0), 3, cv.LINE_8, 0, 0.2) 
cv.imshow('Draw',img)

cv.waitKey()
cv.destroyAllWindows()