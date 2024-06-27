import cv2 as cv

img = cv.imread('source/ch5/mot_color70.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# OpenCV는 SIFT 특징점을 검출하고 영상에 표시해주는 함수를 제공함

# SIFT_create() 함수로 SIFT 특징점을 추출을 위한 sift 객체 생성

# 매개변수 nfeatures는 검출할 특징점 개수를 지정하는데, 기본값 0으로
# 설정하면 모든 특징점을 반환하고, 개수를 지정하면 신뢰도 순으로 반환

# 매개변수 nOctaveLayers는 옥타브 개수를 지정

# 매개변수 contrastThreshold는 테일러 확장으로 미세 조정 시에 사용
# 값이 클수록 적은 수의 특징점이 검출됨

# 매개변수 edgeThreshold는 에지에서 검출된 특징점을 걸러내는 데 사용
# 값이 클수록 덜 걸러내어 많은 수의 특징점이 검출됨

# 매개변수 sigma는 옥타브 0의 입력 영상에 적용할 가우시안 표준편차
sift = cv.SIFT_create()


# sift 객체의 detectAndCompute()는 특징점과 기술자를 찾아내는 함수

# 특징점 검출과 기술자 검출을 나누어 처리하려면 아래와 같음
# kp = sift.detect(gray, None)
# des = sift.compute(gray, kp)

# detectAndCompute()의 2번째 파라미터인 mask=None으로 설정하여
# 마스크 이미지가 아닌 전체 이미지에서 특징점을 검출하게 설정
kp, des = sift.detectAndCompute(gray, None)

# drawKeypoints()를 통해 검출한 특징점을 gray 영상에 표시

# drawKeypoints(입력 이미지, 특징점, 출력이미지, 특징점 그리기 옵션)

# 출력이미지 outImage 매개변수는 특징점이 그려진 이미지를 출력할
# 이미지를 지정하는데, None으로 하면 입력 이미지의 복사본 위에 그림

# 특징점 그리기 옵션은 flags 매개변수로 지정함
# 가장 일반적인 옵션은 DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
# 이 플래그는 특징점의 크기와 각도까지 함께 그려주어
# 특징점의 방향성과 중요성을 나타내줌
gray = cv.drawKeypoints(gray, kp, None, flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv.imshow('sift', gray)

# 실행 결과 원의 중심은 특징점의 위치, 반지름은 스케일, 원 안에
# 표시된 선분은 지배적인 방향을 의미함
# 반지름이 큰것은 해당 특징점이 큰 스케일에서 검출되었음을 의미
# len(kp)를 통해 4415개의 특징점이 검출되었음을 알 수 있음

cv.waitKey()
cv.destroyAllWindows()

# SIFT의 성공 이후 다양한 변종 알고리즘이 발표되었음
# 특징점 검출에는 SURF, FAST, AGAST가 대표적이고
# 기술자 추출에는 PCA-SIFT, GLOH, 모양 컨텍스트, 이진 기술자 등등