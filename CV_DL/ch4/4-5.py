# 영역 분할(region segmentation)은 물체가 점유한 영역을 구분하는 작업
# 에지는 물체의 경계를 지정하므로, 에지가 완벽하면 영억 분할은 불필요
# 의미 있는 단위로 분할하는 방식을 의미 분할(semantic segmentation)
# 여기에선 의미를 고려하지 않고 명암이나 컬러의 변화만 보고
# 영역을 분할하는 고전적인 기법 사용

# 오츄 이진화를 여러 임계값을 사용하도록 확장하여 영역 분할 가능

# 군집화 알고리즘을 활용해 영역 분할 가능

# 워터셰드(watershed)는 비가 오면 오목한 곳에 웅덩이가 생기는 현상을
# 모방하는 연산인데, 워터셰드를 확장하여 영역 분할 가능

# 때로 영상을 아주 작은 영역으로 분할하여 사용하는 경우가 있음
# 화소보다 크고 물체보다 작은 영역을 슈퍼 화소(super-pixel)라고 함
# 대표 슈퍼 화소 알고리즘은 SLIC(Simple Linear Iterative Clustering)
# SLIC는 k-평균 군집화(K-means Clustering) 알고리즘과 비슷하게
# 작동하지만 처리 과정이 단순하고 성능이 좋아 인기가 높음

# SLIC 과정
# 1. 입력 영상을 K개의 슈퍼 화소로 분할하기 위해 전체 영역을
# 등간격으로 K개로 나누어 각 영역의 중심을 초기 군집 중심으로 지정함
# 2. 초기 군집 중심이 우연히 물체 경계에 놓이는 것을 방지하기 위해
# 초기 중심의 3x3 이웃에서 그레이디언트가 가장 낮은 화소로 이동
# SLIC는 화소를 색상과 위치를 나타내는 5차원 벡터로 표현함
# ex) C1 -> (R,G,B,x,y) -> (100,120,50,1,2)
# 3. 영상의 모든 화소 각각에 대해 주위 4개 군집(2x2 크기)의 중심과
# 자신까지 거리를 계산해서 가장 유사한 군집 중심에 할당
# 4. 할당이 끝나면 각 군집 중심은 할당된 화소들을 평균해 중심 갱신
# 5. 3~4번 과정을 반복하여 군집 중심들이 더 이상 이동하지 않거나,
# 이동량이 임계치보다 작으면 수렴했다고 판단하고 알고리즘 종료

# skimage 라이브러리의 slic()를 사용해 SLIC 알고리즘 구현
import skimage
import numpy as np
import cv2 as cv

# skimage 라이브러리에서 제공하는 커피 사진을 입력 이미지로 사용
img = skimage.data.coffee()
# skimage도 영상을 표시하는 함수가 있지만 여기서는 OpenCV를 사용
# 두 라이브러리 모두 numpy 배열로 이미지를 표현하기 때문에 호환가능
# skimage는 RGB 순서로 저장하고 OpenCV는 BGR 순서로 저장하기 때문에
# COLOR_RGB2BGR를 사용하여 skimage 이미지를 BGR 순서로 변환
cv.imshow('Coffee image', cv.cvtColor(img, cv.COLOR_RGB2BGR))

# slic(영상, 슈퍼 화소의 모양, 슈퍼 화소의 개수)으로 슈퍼 화소 분할
# compactness의 값이 클수록 네모에 가까운 모양이 만들어지는 대신
# 슈퍼 화소의 색상 균일성이 낮아짐
slic1 = skimage.segmentation.slic(img, compactness=20, n_segments=600)
# mark_boundaries()로 slic1의 분할 정보를 img에 표시한 결과를 저장
sp_img1 = skimage.segmentation.mark_boundaries(img, slic1)
# 0~1의 실수로 표현된 sp_img1를 0~255으로 바꾸고 uin8t형으로 변환
sp_img1 = np.uint8(sp_img1*255.0)

# compactness 값만 바꾸고 동일한 진행
slic2=skimage.segmentation.slic(img,compactness=40,n_segments=600)
sp_img2=skimage.segmentation.mark_boundaries(img,slic2)
sp_img2=np.uint8(sp_img2*255.0)

cv.imshow('Super pixels (compact 20)',cv.cvtColor(sp_img1,cv.COLOR_RGB2BGR))
cv.imshow('Super pixels (compact 40)',cv.cvtColor(sp_img2,cv.COLOR_RGB2BGR))

# 실행 결과, 책상의 경계 및 커피 잔의 둥그런 경계가 잘 분할됨
# compactness 인수를 크게 하니 네모 모양이 잘 유지되지만
# 슈퍼 화소의 색상 균일성이 낮아지는 현상을 확인 가능
# 이는 하나의 슈퍼 화소가 더 다양한 색상을 포함하게 된다는 뜻임

# SLIC 알고리즘이 화소를 색상과 위치 정보를 담은 5차원 벡터(R,G,B,x,y)
# 로 표현하고, 픽셀을 클러스터링 하는 과정에서 색상거리와 위치거리를
# 고려하는데, compactness 인수는 2가지 거리의 상대적 중요성을 조절함

# compactness 인수가 작아지면 색상거리가 더 중요한 역할을 하므로
# 슈퍼 화소 내의 픽셀들이 색상이 매우 유사하고, 슈퍼 화소의 형태는
# 색상에 맞추어 더 자유로운 모양을 가지게 됨

# 반대로 compactness 인수가 커지면 위치거리가 더 중요해지므로
# 슈퍼 화소는 형태적으로 더 정렬하고 컴팩트한 모양(정사각형)을
# 유지하려고 함, 결과적으로 슈퍼 화소 내의 픽셀들이 다양한 색상을
# 포함할 수 있어 이를 색상 균일성이 낮아진다고 표헌함

cv.waitKey()
cv.destroyAllWindows()