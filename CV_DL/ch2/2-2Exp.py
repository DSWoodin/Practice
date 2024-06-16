import cv2 as cv
import sys

# 서로 다른 영상 2개를 각각 img1, img2에 저장하고
# 서로 다른 윈도우에 디스플레이하는 프로그램으로 확장

img1 = cv.imread('source/ch2/soccer.jpg')
img2 = cv.imread('source/ch2/soccer_gray.jpg')

if img1 is None or img2 is None:
    sys.exit('파일을 찾을 수 없습니다.')
    
cv.imshow('Color Image Display',img1)
cv.imshow('Gray Image Display',img2)
cv.waitKey()
cv.destroyAllWindows()