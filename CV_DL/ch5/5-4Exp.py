# 어린이보호구역 표지판 매칭

import cv2 as cv
import numpy as np

# 이미지 로드
img1 = cv.imread('source/ch5/kid.jpg')
gray1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
img2 = cv.imread('source/ch5/road.jpg')
gray2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

# SIFT 생성 및 특징점 검출
sift = cv.SIFT_create()
kp1, des1 = sift.detectAndCompute(gray1, None)
kp2, des2 = sift.detectAndCompute(gray2, None)

# FLANN 매칭
flann_matcher = cv.DescriptorMatcher_create(cv.DescriptorMatcher_FLANNBASED)
knn_match = flann_matcher.knnMatch(des1, des2, 2)  # 최근접 2개

# 매칭 비율 테스트
T = 0.7
good_match = []
for nearest1, nearest2 in knn_match:
    if (nearest1.distance / nearest2.distance) < T:
        good_match.append(nearest1)

# 매칭 점들 추출
points1 = np.float32([kp1[gm.queryIdx].pt for gm in good_match])
points2 = np.float32([kp2[gm.trainIdx].pt for gm in good_match])
H, _ = cv.findHomography(points1, points2, cv.RANSAC)

# 원본 이미지 크기
h1, w1 = img1.shape[0], img1.shape[1]

# 원본 이미지의 꼭짓점들
box1 = np.float32([[0,0], [0,h1-1], [w1-1,h1-1], [w1-1,0]]).reshape(4,1,2)

# 호모그래피 변환
box2 = cv.perspectiveTransform(box1, H)

# 호모그래피 변환은 이미지를 투영 공간으로 변환하는 과정에서
# 이미지의 기하학적 왜곡으로 인해 비틀리거나 변형된 형태일 수 있음
# box2를 이용해 polyline을 그리는 과정을 약간 수정
# boundingRect()를 이용해 원본 이미지의 꼭짓점 좌표로부터
# 변환된 꼭짓점들을 포함하는 최소 직사각형을 계산한 다음,
# 그 직사각형을 그려서 비틀린 box가 아닌 직사각형 box를 그리기

# 보정된 사각형
rectified_box = np.int32(box2)

# 사각형의 외접 직사각형 계산
x, y, w, h = cv.boundingRect(rectified_box)
rectified_box = np.array([[x,y], [x,y+h], [x+w,y+h], [x+w,y]], \
                         dtype=np.int32).reshape(-1,1,2)

# 변환된 이미지를 원본 이미지에 그리기
img2 = cv.polylines(img2, [rectified_box], True, (0,255,0), 4)
img_match = np.empty((max(h1, img2.shape[0]), w1+img2.shape[1], 3), dtype=np.uint8)
cv.drawMatches(img1, kp1, img2, kp2, good_match, img_match, \
               flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

cv.imshow('Matches and Homography', img_match)

# 실행 결과 어린이보호 표지판을 잘 매칭하였음
# 다만, '어린이보호' 글자에서 추출된 특징점이 표지판 위에 있는
# '어린이보호구역' 글자에 잘못 매칭된 현상도 확인할 수 있음

cv.waitKey(0)
cv.destroyAllWindows()
