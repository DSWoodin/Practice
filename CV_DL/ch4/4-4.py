import cv2 as cv

img = cv.imread('source/ch4/apples.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# HoughCircles()는 원을 검출해 중심과 반지름을 저장한 리스트를 반환
# 첫번째 인수: 원을 검출할 입력 이미지, 반드시 그레이스케일 이미지

# 두번째 인수: 사용할 허프 변환 알고리즘, 현재 지원되는 옵션은 하나뿐
# cv.HOUGH_GRADIENT는 에지 방향 정보를 추가로 사용하는 알고리즘임

# 세번째 인수: 누적 배열의 크기, 1로 설정하면 입력 영상의 크기와 같음

# 네번째 인수: 검출된 원의 중심들 사이의 최소 거리, 작을수록 많은 원이
# 검출될 수 있지만 너무 크면 원이 누락될 수 있음

# 다섯번째 인수: 케니 에지 검출기의 상위 임계값(Thigh)
# 하위 임계값 Tlow는 Thigh의 절반으로 자동으로 설정됨

# 여섯번째 인수: 비최대 억제를 적용할 때 쓰는 임계값, 이 값이
# 낮으면 더 많은 원이 검출되지만 잘못된 원(False Postive)도 많아짐

# 일곱, 여덟번째 인수: 검출할 원의 최소 반지름, 최대 반지름
apples = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, 200, param1=150, \
                         param2=20, minRadius=50, maxRadius=120)

for i in apples[0]:
    # circle(영상, (원의 중심 좌표), 반지름, 색, 두께)
    cv.circle(img, (int(i[0]), int(i[1])), int(i[2]), (255,0,0), 2)

cv.imshow('Apple detection',img)

# 실행 결과, 사과를 제대로 찾은 경우도 있지만 없는 곳을 검출한
# 거짓긍정(False Positive)과 있는데 놓친 거짓부정(False Negative)도
# 있으며, 위치가 틀어진 경우도 있음
# 파라미터를 이리저리 변경하며 조정해봐야 함

cv.waitKey()
cv.destroyAllWindows()