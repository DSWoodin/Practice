import cv2 as cv
import numpy as np

img=np.array([[0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,1,0,0,0,0,0,0],
              [0,0,0,1,1,0,0,0,0,0],
              [0,0,0,1,1,1,0,0,0,0],
              [0,0,0,1,1,1,1,0,0,0],
              [0,0,0,1,1,1,1,1,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0], # 실수 연산 가능하도록 float32
              [0,0,0,0,0,0,0,0,0,0]],dtype=np.float32) 

# 1x3과 3x1의 미분을 위한 필터 ux, uy 생성(122p. 1차 미분 에지 연산자 참고)
# ux는 [[]] -> 2차원 배열, 형태는 (1,3): 한 행과 세 열, 수평 방향의 필터
ux = np.array([[-1,0,1]])

# transpose() 함수는 numpy 배열의 축을 전환하는 역할
# uy는 수직 방향 필터를 나타내려는 의도로 보이지만, Python에서 transpose()는
# 1차원 배열에 효과가 없기 때문에 uy는 여전히 1차원 배열(3,)을 유지함
# 따라서 1차원 배열인 uy에 transpose()를 적용한 것은 아무런 효과가 없음
# 수직 방향의 필터가 되려면 'reshape(-1, 1)' 또는 '[:, np.newaxis]'를 사용해야
uy = np.array([-1,0,1]).transpose()

# getGaussianKernel()로 스무딩을 위한 1차원 가우시안 필터를 생성(101p. 참고)
# getGaussianKernel(3,1)에서 첫 번째 인수 3은 커널 사이즈를 의미 -> 3x3 크기
# 두 번째 인수는 가우시안 커널의 표준 편차를 의미
k = cv.getGaussianKernel(3,1)

# k는 생성했던 1차원 가우시안 커널, k.transpose()는 이 커널의 전치(transpose)
# k가 1차원 벡터로 만들어 졌기 때문에 k와 k.transpose()는 본질적으로 같음
# np.outer()는 두 벡터의 외적을 계산 -> k와 k.transpose()의 요소들의 곱을 통해
# 최종적으로 2차원 가우시안 필터를 생성
g = np.outer(k, k.transpose())

# filter2D()로 이미에 2차원 필터(커널)을 적용
# filter2D(이미지, ddepth, 적용할 필터)
# ddepth는 출력 이미지의 원하는 깊이, CV_32F는 32비트 부동소수점 수
# 아래는 2차 모멘트 행열을 구성하는 요소들을 계산 -> 특징 가능성 맵 C를 계산
dy = cv.filter2D(img, cv.CV_32F, uy)
dx = cv.filter2D(img, cv.CV_32F, ux) 
dyy = dy*dy
dxx = dx*dx
dyx = dy*dx
gdyy = cv.filter2D(dyy, cv.CV_32F, g) # G ⊛ dy^2
gdxx = cv.filter2D(dxx, cv.CV_32F, g) # G ⊛ dx^2
gdyx = cv.filter2D(dyx, cv.CV_32F, g) # G ⊛ dx*dy
C = (gdyy*gdxx - gdyx*gdyx) - 0.04*(gdyy+gdxx)*(gdyy+gdxx) # 특징 가능성 맵 C

# C.shape == (10, 10) 이므로, C.shape[0]-1 == 9, C.shape[1]-1 == 9
# 10x10 크기의 2차원 배열에 비최대 억제를 적용
# 가장자리([0,x], [x,0], [9,x], [x,9])는 적용할수 없으므로
# [1,1] ~ [8,8] 범위의 요소들에게만 접근하여 적용 

# 'C[j,i] > C[j-1:j+2, i-1:i+2]' 구문은 중심 원소(C[j,i])가 주변 
# 3x3 크기의 각 원소보다 큰지를 평가하여 3x3 불리언 배열을 생성
# 불리언 배열의 sum()을 적용하여 '8'과 같은지 판단
# -> 8은 최대 True의 개수 ('중심 원소 > 중심 원소'가 성립 불가능해서)

# sum()을 한번더 적용한 것은 코드적인 오류로 보임
# 배열연산을 사용하지 않고 for문을 사용한 것도 코드적인 아쉬움

# 결론적으로 중심 원소가 0.1보다 크면서 주변 8개 이웃 원소보다 
# 큰 극점(특징점)들을 원본 배열 img에 9로 표시
for j in range(1, C.shape[0]-1):
    for i in range(1, C.shape[1]-1): # 비최대 억제 적용
        if C[j,i] > 0.1 and sum(sum(C[j,i] > C[j-1:j+2, i-1:i+2])) == 8:
            img[j,i] = 9           

np.set_printoptions(precision=2)
print(dy) 
print(dx) 
print(dyy) 
print(dxx) 
print(dyx) 
print(gdyy) 
print(gdxx) 
print(gdyx) 
print(C) 
print(img)

# 모든 요소가 0인 160x160 크기의 배열 popping 생성
# 데이터 타입을 uint8로 설정하여 0~255의 정수값을 가질 수 있도록
# 160x160 크기의 popping 배열을 10x10 크기의 C 배열과 대응시키기 위해
# j//16, i//16를 사용, 0.06을 더하고 700을 곱하는 이유는
# 값을 조정하여 uint8 범위 내에 맞도록 스케일링
# 결론적으로 특징 가능성 맵 C를 16배 확대하여 시각화
popping = np.zeros([160,160], np.uint8)
for j in range(0, 160):
    for i in range(0, 160):
        popping[j,i] = np.uint8((C[j//16, i//16]+0.06)*700)

cv.imshow('Image Display2',popping)    
cv.waitKey()
cv.destroyAllWindows()

# 실행 결과 검출된 세 특징점이 모두 물체의 모통이(corner)에 위치
# 실제 영상에 해리스 특징점을 적용 -> 코너뿐 아니라 블롭(blob)도 검출
# 블롭은 주변보다 밝거나 어두운 불규칙한 영역을 말함
# 해리스 특징점은 이동과 회전에 불변이지만, 스케일에는 불변하지 않음