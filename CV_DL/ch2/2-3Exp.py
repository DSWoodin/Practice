import cv2 as cv
import sys

img = cv.imread('source/ch2/soccer.jpg')

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# 0.1, 0.2, ... 1.0으로 축소한 영상 10개를 서로 다른 윈도우로 출력
for i in range(1,11):
    fx = i * 0.1
    fy = i * 0.1
    gray_small = cv.resize(gray, dsize=(0,0), fx=fx, fy=fy)
    cv.imshow(f'Gray image {fx}', gray_small)

cv.waitKey()
cv.destroyAllWindows()