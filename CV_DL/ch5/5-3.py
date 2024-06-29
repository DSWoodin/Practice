import cv2 as cv
import numpy as np
import time

img1 = cv.imread('source/ch5/mot_color70.jpg')[190:350, 440:560]
gray1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
img2 = cv.imread('source/ch5/mot_color83.jpg')
gray2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

sift = cv.SIFT_create()
kp1, des1 = sift.detectAndCompute(gray1, None)
kp2, des2 = sift.detectAndCompute(gray2, None)
print('특징점 개수:',len(kp1),len(kp2))

start = time.time()
# DescriptorMatcher_create() 함수로 특징점 매칭에 사용할 객체 생성
# 파라미터를 설정해 FLANN 기반으로 특징 기술자를 매칭을 수행하도록
flann_matcher = cv.DescriptorMatcher_create(cv.DescriptorMatcher_FLANNBASED)
# flann_matcher 객체의 knnMatch 함수를 호출하여 매칭 수행
# (des1, des2, 2) -> des1을 des2와 매칭하여 최근접 2개만 찾아라
knn_match = flann_matcher.knnMatch(des1, des2, 2)

# 최근접 이웃 거리 비율 전략을 사용해 좋은 쌍들만 추출
T = 0.7
good_match = []
for nearest1, nearest2 in knn_match:
    if (nearest1.distance / nearest2.distance) < T:
        good_match.append(nearest1)
print('매칭에 걸린 시간:',time.time()-start)

# np.empty()로 비어 있는 배열 생성 -> 빈 도화지의 역할
# np.empty(shape, dtype)에서 dtype은 0~255의 값을 가지는 uint8
# shape은 이미지 형태로 만들어야 하므로 (y,x,3) 여기서 3은 컬러채널
# y는 두 이미지 중에 더 큰 높이(max)로 선택
# x는 두 이미지를 가로로 이어 붙여야 하므로 두 이미지의 너비의 합
img_match = np.empty((max(img1.shape[0], img2.shape[0]), \
                      img1.shape[1]+img2.shape[1], 3), dtype=np.uint8)

# drawMatches()로 두 이미지 간의 특징점 매칭 결과를 시각화
# drawMathces(이미지1, 이미지1의 특징점, 이미지2, 이미지2의 특징점, \
#             두 이미지 간 매칭된 특징점, 매칭 결과를 그릴 빈 배열, \
#             flags= 그리기 방식을 결정하는 플래그)
# 매칭되지 않은 특징점은 그리지 않도록 플래그 설정
cv.drawMatches(img1, kp1, img2, kp2, good_match, img_match, \
               flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

cv.imshow('Good Matches', img_match)

# 출력 결과 모델 영상에서 231개, 장면 영상에서 4096개의 특징점 검출
# 거짓 긍정도 보이지만 대부분 옳은 매칭을 해냈고, 매칭 시간은 0.04초
# kd 트리 알고리즘을 구현한 FLANN의 빠른 속도를 확인함

k=cv.waitKey()
cv.destroyAllWindows()