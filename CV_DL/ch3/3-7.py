# 영역 연산은 주로 컨볼루션(convolution)을 통해 이루어짐
# 컨볼루션은 입력 영상의 각 화소에 필터를 적용해 곱의 합을 구함
# 컨볼루션의 기본 개념은 도서 설명 참고
import cv2 as cv
import numpy as np

img = cv.imread('source/ch3/soccer.jpg')
img = cv.resize(img, dsize=(0,0), fx=0.4, fy=0.4)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.putText(gray, 'soccer', (10,20), cv.FONT_HERSHEY_SIMPLEX, \
           0.7, (255,255,255), 2)
cv.imshow('Original', gray)

# 스무딩 적용, GaussianBlur(영상, 필터의 크기, 표준편차)
# 표준편차를 0.0으로 설정하면 필터 크기를 보고 자동으로 추정함
# hstack()으로 가우시안블러를 적용한 영상 3개를 이어붙임
smooth = np.hstack((cv.GaussianBlur(gray, (5,5), 0.0), \
                    cv.GaussianBlur(gray, (9,9), 0.0), \
                    cv.GaussianBlur(gray, (15,15), 0.0)))
cv.imshow('Smooth', smooth)

# 엠보싱 필터를 정의
femboss = np.array([[-1.0, 0.0, 0.0],
                    [ 0.0, 0.0, 0.0],
                    [ 0.0, 0.0, 1.0]])

# 엠보싱 필터는 오른쪽 아래 화소에서 왼쪽 위 화소를 빼서 음수가 발생
# gray 배열은 np.int8형임, 부호가 없는 1바이트 정수형
# filter2D()는 주어진 영상 배열과 같은 형태의 배열을 출력함
# 따라서 음수가 발생하면 이상한 값으로 바뀌어 저장됨
gray16 = np.int16(gray)

# filter2D()를 int16형태의 gray16에서 동작하여 음수까지 저장
# 여기에 128을 더하고(-255~255 -> -127~383) np.clip() 적용까지
# 해주면 비로소 0~255 범위 -> 그리고 결과 영상을 uint8 
emboss = np.uint8(np.clip(cv.filter2D(gray16, -1, femboss)+128, 0, 255))

# 이번에는 np.clip을 하지 않았을때 부작용
emboss_bad = np.uint8(cv.filter2D(gray16, -1, femboss)+128)

# 이번에는 np.clip도 안하고 np.int16 변환도 안했을 때 부작용
emboss_worse = cv.filter2D(gray, -1, femboss)

cv.imshow('Emboss', emboss)
cv.imshow('Emboss_bad', emboss_bad)
cv.imshow('Emboss_worse', emboss_worse)

cv.waitKey()
cv.destroyAllWindows()