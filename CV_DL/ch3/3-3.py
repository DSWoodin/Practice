import cv2 as cv
import sys

img = cv.imread('source/ch3/soccer.jpg')

# 오츄 알고리즘으로 최적의 임계값 T를 계산해 이진화
# threshold()의 첫 번째 인수가 img[:,:,2]이므로 R 채널을 이진화
# 두 번째, 세 번째 인수는 명암값의 범위를 지정
# 네 번째 인수는 오츄 알고리즘으로 이진화를 진행하라는 의미
# threshold()는 알고리즘이 찾은 최적 임곗값과 이진화된 영상을 반환
t, bin_img = cv.threshold(img[:,:,2], 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
print('오츄 알고리즘이 찾은 최적 임곗값=', t)

cv.imshow('R channel', img[:,:,2]) # R 채널 영상
cv.imshow('R channel binarization', bin_img) # R 채널 이진화 영상

cv.waitKey()
cv.destroyAllWindows()

# 컴퓨터 비전은 문제를 최적화(optimization) 문제로 공식화해 해결
# 오츄 알고리즘의 공식에서 매개변수 t는 해 공간(solution space) 구성
# 해 공간이란 발생할 수 있는 모든 해의 집합
# L = 256이면, 해 공간은 {0,1,2,...,255}이다
# 해 공간이 작아서 오츄 알고리즘은 모든 후보 해에 대해서
# 일일이 계산하고 최소가 되는 t를 최적해로 결정 -> 임계값
# 이와 같이 모든 해를 다 검사하는 방법: 낱낱 탐색 알고리즘

# 낱낱 탐색 알고리즘(exhaustive search algorithm)은 해 공간의 크기가
# 수만~수억 or 무한대인 컴퓨터 비전 문제를 해결하기 시간이 너무 걸림
# 물체의 외각선을 찾는 스네이크 알고리즘은 명암 변화와 곡선의
# 매끄러운 정도가 최대가 되는 최적해를 탐욕 알고리즘으로 찾음
# 신경망 학습에는 역전파 알고리즘을 사용해 최소 오류의 최적해 찾음

# 화소의 연결성에는 4-연결성과 8-연결성이 있음
# 이진 영상에서 1의 값을 가진 연결된 화소의 집합을 연결 요소라고 함
# OpenCV에서 연결 요소는 connectedComponents() 함수로 찾음