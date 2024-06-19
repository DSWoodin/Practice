# 컴퓨터 비전은 인식 정확률도 중요하지만 시간 효율도 대단히 중요
# 물체 추적에 있어서는 초당 수십 장의 고해상도 영상을 처리해야
# 직접 작성한 코드와 OpenCV 제공 함수의 처리 시간 비교
import cv2 as cv
import numpy as np
import time

# for문 2개를 이용, 이미지의 모든 화소에 접근해 컬러를 명암으로 변환
def my_cvtGray(bgr_img):
    # np.zeros로 모든 요소를 0으로 초기화
    g = np.zeros([bgr_img.shape[0], bgr_img.shape[1]])
    for r in range(bgr_img.shape[0]):
        for c in range(bgr_img.shape[1]):
            # B, G, R 채널 각각의 화소에 가중치를 곱한 것을 적용
            g[r,c] = 0.114*bgr_img[r,c,0] + \
                     0.587*bgr_img[r,c,1] + \
                     0.229*bgr_img[r,c,2]
    return np.uint8(g)

# Gray2 함수는 Gray함수와 동일한 결과지만 파이썬 배열 연산을 활용
def my_cvtGray2(bgr_img):
    g = np.zeros([bgr_img.shape[0], bgr_img.shape[1]])
    g = 0.114*bgr_img[:,:,0] + \
        0.587*bgr_img[:,:,1] + \
        0.299*bgr_img[:,:,2]
    return np.uint8(g)

img = cv.imread('source/ch3/girl_laughing.jpg')

# 모두 동일한 기능 수행하는 함수들, 처리 시간 비교 (def 2개, cv 1개)
start = time.time()
my_cvtGray(img)
print('My time1:', time.time()-start)

start = time.time()
my_cvtGray2(img)
print('My time2:', time.time()-start)

start = time.time()
cv.cvtColor(img, cv.COLOR_BGR2GRAY)
print('OpenCV time:', time.time()-start)

# 배열 연산을 사용하는 Gray2가 Gray보다 압도적으로 빠름
# -> 파이썬에서 가능한 배열 연산을 사용해야 함, for문은 오래 걸림
# 그보다도 OpenCV 함수가 더 빠름, OpenCV 함수는 C와 C++ 언어로 
# 작성되었고, 최적화에 노력을 기울여 빠른 속도를 자랑함