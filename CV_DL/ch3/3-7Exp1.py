import cv2 as cv
import numpy as np

img = cv.imread('source/ch3/soccer.jpg')
img = cv.resize(img, dsize=(0,0), fx=0.4, fy=0.4)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.putText(gray, 'soccer', (10,20), cv.FONT_HERSHEY_SIMPLEX, \
           0.7, (255,255,255), 2)
cv.imshow('Original', gray)

# 가우시안 스무딩
Gaussian_smooth = np.hstack((cv.GaussianBlur(gray, (5,5), 0.0), \
                             cv.GaussianBlur(gray, (9,9), 0.0), \
                             cv.GaussianBlur(gray, (15,15), 0.0)))
cv.imshow('Gaussian smooth', Gaussian_smooth)

# 메디안 스무딩
Median_smooth = np.hstack((cv.medianBlur(gray, 5), \
                           cv.medianBlur(gray, 9), \
                           cv.medianBlur(gray, 15)))
cv.imshow('Median smooth', Median_smooth)

cv.waitKey()
cv.destroyAllWindows()

# 가우시안 스무딩과 메디안 스무딩은 육안으로 비교해도 차이가 큼

# 가우시안 스무딩은 가우시안 분포를 기반으로 하는 가중치를 적용
# 고주파 노이즈를 제거하는 효과적이지만
# 이미지의 경계가 모호해지고 전체적으로 이미지가 흐려짐

# 메디안 스무딩은 픽셀 값의 중간값을 사용하는 방법
# 소금-후추 노이즈 같은 급격한 픽셀 값 변화 제거에 효과적이고
# 이미지의 경계를 잘 유지하며, 세부 구조가 잘 보존됨

# 소금(최대값)-후추(최소값) 노이즈 -> 급격한 픽셀값 변화