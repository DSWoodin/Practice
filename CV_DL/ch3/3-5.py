# 영상 처리 연산 -> 화소가 새로운 값을 받는 과정
# 새로운 값을 어디에서 받는가? 점 연선, 영역 연산, 기하 연산
# 점 연산은 자기 자신으로부터 값을 받음 ex)오츄 알고리즘
# 영역 연산은 이웃 화소 값을 이용해 새로운 값 ex)모폴로지
# 기하 연산은 기하학적 변환에 따라 다른 곳으로부터 값을 받음

# 명암 조절 -> 상수를 곱해서 더하기만 하는 선형(linear) 연산
# 인간의 눈은 빛의 밝기 변화에 비선형적으로 반응함
# 명얌 10을 20으로 올렸을 때와, 120을 130으로 올렸을 때
# 같은 양만큼 늘었지만 인간이 느끼는 밝아짐의 정도는 다름
# 감마 보정(gamma correction)은 이런 비선형성을 수학적으로 표현
import cv2 as cv
import numpy as np

img = cv.imread('source/ch3/soccer.jpg')
img = cv.resize(img, dsize=(0,0), fx=0.25, fy=0.25)

# 감마 보정
# gamma(영상, 감마값) -> 감마값 default를 1.0으로 설정
# 감마값이 1이면 원본, 1보다 작으면 밝아짐, 1보다 크면 어두워짐
def gamma(f, gamma=1.0):
    f1 = f/255.0 # L=256이라 가정, 255.0으로 나눠 [0,1] 범위 정규화
    # type(f1[0,0,0]) -> numpy.float64, 즉 f1은 64비트 실수형
    # 감마 보정식에 따라 계산하고 np.int8 적용해 8비트 정수형으로
    return np.uint8(255*(f1**gamma))

# hstack()으로 감마값이 다른 영상들을 이어붙임
# hstack()이 여러 배열을 받을수 있도록 (튜플 형태로) 전달해야 함
gc = np.hstack((gamma(img,0.5), gamma(img,0.75), gamma(img,1.0), \
                gamma(img,2.0), gamma(img,3.0)))
cv.imshow('gamma',gc)

cv.waitKey()
cv.destroyAllWindows()