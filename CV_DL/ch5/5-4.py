import cv2 as cv
import numpy as np

img1 = cv.imread('source/ch5/mot_color70.jpg')[190:350, 440:560]
gray1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
img2 = cv.imread('source/ch5/mot_color83.jpg')
gray2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

sift = cv.SIFT_create()
kp1,des1=sift.detectAndCompute(gray1,None)
kp2,des2=sift.detectAndCompute(gray2,None)

flann_matcher=cv.DescriptorMatcher_create(cv.DescriptorMatcher_FLANNBASED)
knn_match=flann_matcher.knnMatch(des1,des2,2)	# 최근접 2개

T=0.7
good_match=[]
for nearest1,nearest2 in knn_match:
    if (nearest1.distance/nearest2.distance)<T:
        good_match.append(nearest1)

# dir(good_match[0])를 print하여 객체의 속성과 메서드를 확인
# -> print(dir(good_match[0]))
# good_match[0]은 OpenCV의 'DMatch' 클래스의 인스턴스이며,
# 'DMatch' 객체는 다양한 속성들을 포함하지만 그 중에서도 주요 속성은
# 1. 'distance': 기술자(특징점)사이의 거리
# 2. 'queryIdx': 첫 번째 영상에서의 기술자(특징점) 인덱스
# 3. 'trainIdx': 두 번째 영상에서의 기술자(특징점) 인덱스
# 즉, a_{i}와 b_{j}가 매칭 쌍이라면 queryIdx는 i, trainIdx는 j임

# 키포인트 배열인 kp1과 kp2에서 특징점 인덱스를 이용해서 객체를
# 참조하고, KeyPoint의 속성 중 하나인 'pt'를 사용해서 키포인트의
# (x,y) 좌표를 튜플로 반환

# 참고: 키포인트의 속성은 pt(좌표), size(크기), angle(방향), .....

# 첫 번째 영상의 특징점 좌표들을 추출하여 points1에 저장
# 두 번째 영상의 특징점 좌표들을 추출하여 points2에 저장
points1 = np.float32([kp1[gm.queryIdx].pt for gm in good_match])
points2 = np.float32([kp2[gm.trainIdx].pt for gm in good_match])

# 밑줄(_)을 변수로 설정하는 이유는 해당 변수에 반환된 값이 있지만,
# 그 값을 사용하지 않겠다는 것을 명시적으로 나타내기 위함
# Python에서 관용적으로 사용되는 패턴
# findHomography() 함수 이용해 호모그래피 행렬을 추정하여 H에 저장
H, _ = cv.findHomography(points1, points2, cv.RANSAC)

# 첫 번재 영상과 두 번째 영상의 가로 세로 길이를 변수에 저장
h1, w1 = img1.shape[0], img1.shape[1]
h2, w2 = img2.shape[0], img2.shape[1]

print(h1, w1)
print(h2, w2)

# 첫 번째 영상의 네 구석의 좌표를 box1에 저장
# 예를 들어 가로세로 200x100 크기의 영상이면,
# 가로의 인덱싱은 0에서 199까지이고 세로는 0에서 99까지라서 -1 해줌

# reshape(4,1,2)는 perspectiveTransform() 함수에 알맞은 형태로 변형
# 4: 4개의 좌표(점)
# 1: 각 점은 1개의 배열로 묶임
# 2: 각 점은 (x,y)의 2개의 값을 가짐
# reshape() 후의 box1 배열의 형태: [
#                                   [[0, 0]],
#                                   [[0, h1-1]],
#                                   [[w1-1, h1-1]],
#                                   [[w1-1, 0]]
#                                  ]
box1 = np.float32([[0,0], [0,h1-1], [w1-1,h1-1], [w1-1,0]]).reshape(4,1,2)

# 첫 영상의 좌표에 호모그래피 행렬 H를 적용하여 두 번째 영상에 투영
box2 = cv.perspectiveTransform(box1, H)

# polyline()으로 두번째 영상에 box2를 그리기
# polyline(이미지, pts, isClosed, color, thickness)

# pts에는 그릴 다각형의 꼭짓점 좌표를 나타내는 점들의 배열
# 이 배열은 numpy 배열이고 int32형식으로 변환되어야 함

# isClosed=True -> 첫 번째 점과 마지막 점을 연결히여 닫힌 다각형
img2 = cv.polylines(img2, [np.int32(box2)], True, (0,255,0), 8)

# 두 이미지를 가로로 나란히 놓고, 특징점 정보와 매칭 정보를 그리기
img_match=np.empty((max(h1,h2), w1+w2, 3), dtype=np.uint8)
cv.drawMatches(img1, kp1, img2, kp2, good_match, img_match, \
               flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

cv.imshow('Matches and Homography',img_match)

k=cv.waitKey()
cv.destroyAllWindows()

# 호모그래피 행렬을 이용하여 특징점으로 버스 위치에 box를 잘 그렸음