import cv2 as cv
import numpy as np

img = cv.imread('source/ch4/soccer.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# 소벨 연산자 적용하여 에지 강도 맵을 구하기 -> Sobel()
# 두번째 인수는 결과 영상을 32비트 실수 맵에 저장하라
# CV_32F를 사용하는 이유는 에지 강도 맵이 음수를 포함하며 실수이기 때문임
# (에지 방향 맵, f'x맵, f'y맵도 마찬가지)
# 세번째 인수(x 방향 미분 차수)와 네번째 인수(y 방향 미분 차수)로 방향 지정
# 다섯번째 인수로 커널 사이즈 지정 -> ksize=3은 3x3 커널을 사용하라
# 커널 사이즈는 1,3,5,7과 같은 홀수 값을 사용
grad_x = cv.Sobel(gray, cv.CV_32F, 1, 0, ksize=3)
grad_y = cv.Sobel(gray, cv.CV_32F, 0, 1, ksize=3)

# convertScaleAbs()는 이미지 스케일링과 절대값 변환을 수행할 수 있음
# 여기에서는 첫번째 인수인 입력 이미지 배열만 넣어서 절대값 변환만 수행
# convertScaleAbs()는 부호 없는 8비트 형인 CV_8U(numpy의 uint8과 같음)맵을 만듬
# 크기가 0보다 작은 값은 0, 255를 넘는 값은 255로 바꾸어 기록함
sobel_x = cv.convertScaleAbs(grad_x)
sobel_y = cv.convertScaleAbs(grad_y)

# sobel_x와 sobel_y에 각각 0.5의 가중치를 곱하여 에지 강도를 계산
# addWeighted(img1, a, img2, b, c) -> img1xa + img2xb + c
edge_strength = cv.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)

# 사실 addWeighted()는 에지 강도를 근사적으로 계산하는 간단한 방법임
# 정확한 에지 강도는 제곱합의 제곱근을 계산하는 함수를 사용해야
# magnitude()는 두 배열의 각 요소에 대해 다음을 계산함
# magnitude(x,y) = np.sqrt(x**2 + y**2)
edge_strength_exact = cv.magnitude(grad_x, grad_y)

# grad_x와 grad_y는 부동 소수점 데이터 타입인 CV_32F형임
# CV_32F형은 imshow()에서 제대로 표시되지 않으므로 CV_8U형으로 변환
edge_strength_exact = cv.convertScaleAbs(edge_strength_exact)

# addWeighted()는 그저 곱셈과 덧셈만 하기 때문에 음수인 요소들을
# convertScaleAbs()과정으로 양수로 만든 sobel_xy를 인수로 사용해야함
# (최종 화소 값이 음수면 안되기 때문에)

# 반면 magnitude()는 계산 과정이 제곱을 하기 때문에 음수 처리 가능
# 따라서 sobel_xy가 아니라 음수를 포함하는 grad_xy를 인수로 사용함

cv.imshow('Original',gray)
cv.imshow('sobelx',sobel_x)
cv.imshow('sobely',sobel_y)
cv.imshow('edge strength',edge_strength)
cv.imshow('edge strength exact',edge_strength_exact)

# x 방향 연산자를 적용한 sobel_x는 수직 방향 에지가 선명하게 나타남
# 반대로 sobel_y는 수평 방향의 에지가 선명함
# 명암 변화가 큰 곳에 더욱 선명한 에지가 나타난 현상도 확인가능
# addWeighted()로 계산한 에지 강도도 에지가 잘나타났지만,
# magnitude()로 계산한 에지 강도가 확실히 더욱 선명한 에지를 검출함

cv.waitKey()
cv.destroyAllWindows()