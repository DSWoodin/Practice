# OpenCV에서 함수로 제공되는 에지 연산자는 매우 다양함
# cv.Scharr() 연산자와 cv.Sobel() 연산자 적용 결과 비교
import cv2 as cv
import numpy as np

img = cv.imread('source/ch4/soccer.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Sobel() 적용
grad_sobel_x = cv.Sobel(gray, cv.CV_32F, 1, 0, ksize=3)
grad_sobel_y = cv.Sobel(gray, cv.CV_32F, 0, 1, ksize=3)
sobel_x = cv.convertScaleAbs(grad_sobel_x)
sobel_y = cv.convertScaleAbs(grad_sobel_y)
sobel_edge_strength = cv.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)

# Scharr() 적용
# Scharr은 3x3 크기의 고정된 커널 사이즈를 사용하므로 ksize인수 없음
grad_scharr_x = cv.Scharr(gray, cv.CV_32F, 1, 0)
grad_scharr_y = cv.Scharr(gray, cv.CV_32F, 0, 1)
scharr_x = cv.convertScaleAbs(grad_scharr_x)
scharr_y = cv.convertScaleAbs(grad_scharr_y)
scharr_edge_strength = cv.addWeighted(scharr_x, 0.5, scharr_y, 0.5, 0)

cv.imshow('Original',gray)
cv.imshow('Sobel X', sobel_x)
cv.imshow('Sobel Y', sobel_y)
cv.imshow('Sobel Edge Strength', sobel_edge_strength)
cv.imshow('Scharr X', scharr_x)
cv.imshow('Scharr Y', scharr_y)
cv.imshow('Scharr Edge Strength', scharr_edge_strength)

# 출력 결과 Scharr()가 Sobel()보다 더 선명하고 정밀한 에지 검출
# 노이즈에 민감한 Scharr(), 잔디 부분의 에지가 많이 검출됨

cv.waitKey()
cv.destroyAllWindows()