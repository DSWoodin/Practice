import cv2 as cv
import sys

img = cv.imread('source/ch2/girl_laughing.jpg')

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

# OpenCV는 직선:line, 직사각형:rectangle, 다각형:polylines,
#          원:circle, 타원:ellipes, 문자열:putText 등등 제공
# rectangle의 첫 번째 인수는 직사각형을 그릴 영상
# 두 번째 인수는 직사각형의 왼쪽 위 구석점의 좌표 (x,y)
# 세 번째 인수는 직사각형의 오른쪽 아래 구석점의 좌표 (x,y)
# 네 번째 인수는 직사각형의 색(B,G,R), 각각 0~255
# 다섯 번째 인수는 직사각형의 두께
cv.rectangle(img, (830,30), (1000,200), (0,0,255), 2)

# putText(영상, 써넣을 문자열, 문자열의 왼쪽 아래 구석점의 위치,
#         폰트 종류, 글자 크기, 글자 색, 글자 두께)
cv.putText(img, 'laugh', (830,24), cv.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)

cv.imshow('Draw',img)

cv.waitKey()
cv.destroyAllWindows()