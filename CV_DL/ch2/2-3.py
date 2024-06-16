import cv2 as cv
import sys

img = cv.imread('source/ch2/soccer.jpg')

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

# cvtColor()는 변환된 영상을 반환함
# cvtColor(변환할 컬러 영상을 가진 객체, 변환 타입)
# COLOR_BGR2GRAY는 BGR로 표현된 컬러 영상을 명암으로 변환
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# resize()는 함수로 영상의 크기를 변환
# resize(입력 영상, dsize=변환할 크기, fx=, fy=)
# dsize=(0,0)으로 지정하면 비율을 지정하는 fx와 fy의 값에 따름
# dsize=(0,0)이고 fx=0.5, fy=0.5이므로 가로세로 모두 반으로 축소
gray_small = cv.resize(gray, dsize=(0,0), fx=0.5, fy=0.5)

# imwrite()는 지정한 영상을 지정한 파일에 저장
cv.imwrite('source/ch2/soccer_gray.jpg', gray)
cv.imwrite('source/ch2/soccer_gray_small.jpg', gray_small)

# 서로 다른 3개의 윈도우에서 영상 출력
cv.imshow('Color image',img)
cv.imshow('Gray image',gray)
cv.imshow('Gray image small',gray_small)

cv.waitKey()
cv.destroyAllWindows()

# BGR 영상을 명암 영상으로 변환하는 공식
# https://docs.opencv.org/3.4/de/d25/imgproc_color_conversions.html