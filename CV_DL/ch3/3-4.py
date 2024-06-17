# 영상 변환 과정에서 물체가 여러 영역으로 분리되거나 다른 물체가
# 한 영역으로 붙는 경우 등의 부작용을 누그러뜨리기 위해 모폴로지
# 모폴로지(morphology)는 구조 요소(structuring element)를 이용함
# 모폴로지의 기본 연산은 팽창(dilation)과 침식(erosion)

# 팽창은 구조 요소의 중심을 1인 화소 p에 씌운 다음,
# 구조 요소에 해당하는 모든 화소를 1로 바꿈, 1인 화소에 모두 적용
# 침식은 구조 요소의 중심을 1인 화소 p에 씌운 다음,
# 구조 요소에 해당하는 모든 화소가 1인 경우에 p를 1로 유지,
# 그렇지 않으면 0으로 바꿈

# 팽창은 작은 홈을 메우거나 끊어진 영역을 하나로 연결하는 효과
# 침식은 영역의 경계에 솟은 돌출 부분을 깍는 효과
# 팽창과 침식의 효과는 구조 요소의 모양에 따라 달라짐
# 팽창은 영역을 키우고 침식은 영역을 작게 만듬
# 침식을 수행한 영상에 팽창을 적용하면 대략 원래 크기를 유지
# 침식한 결과에 팽창을 적용하는 연산을 열림(opening),
# 팽창한 결과에 침식을 적용하는 연산을 닫힘(closing)이라고 함

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# jpg는 손실 압축 방식의 이미지 파일 형식으로, 복잡한 이미지를 
# 효율적으로 저장하기 위해 파일 크기를 크게 줄이는데 중점을 둠
# -> 투명도를 처리하는 Alpha 채널을 지원하지 않음
# IMREAD_UNCHANGED 인수를 주어 모든 채널을 읽어오도록 지정함
# RGBA 포맷을 지원하지 못하는 jpg 파일과는 달리,
# 4채널을 포함할수도 있는 png파일을 불러올 때는
# IMREAD_UNCHANGED 인수를 주는 것을 습관화해야 데이터 손실 방지
img = cv.imread('source/ch3/JohnHancocksSignature.png', cv.IMREAD_UNCHANGED)

# img.shape -> img는 크기가 525x1920이고 채널이 4개인 이미지임
# 서명을 담고 있는 4번째 채널에 오츄 알고리즘 적용
t, bin_img = cv.threshold(img[:,:,3], 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)

# cmap 파라미터로 컬러맵을 지정, 컬러맵은 각 픽셀에 매핑될 색상 지정
# cmap='gray'로 설정해 명암 영상으로 출력
# xticks와 yticks에 빈 리스트를 전달하여 눈금 숨기기
plt.imshow(bin_img, cmap='gray'), plt.xticks([]), plt.yticks([])
plt.title('Signature'), plt.show()

# 모폴로지 효과를 확인하기 위해 영상의 일부만 슬라이싱
# 525x1920 크기의 img를 왼쪽 하단부의 263x263 부분을 슬라이싱
b = bin_img[262:525, 0:263]
plt.imshow(b, cmap='gray'), plt.xticks([]), plt.yticks([])
plt.title('piece of Signature'), plt.show()

# 구조 요소를 담은 배열
se = np.uint8([[0,0,1,0,0],
               [0,1,1,1,0],
               [1,1,1,1,1],
               [0,1,1,1,0],
               [0,0,1,0,0]])

# 팽창 연산 적용, dilate(영상, 구조 요소, 적용횟수=1)
b_dilation = cv.dilate(b, se, iterations=1)
plt.imshow(b_dilation, cmap='gray'), plt.xticks([]), plt.yticks([])
plt.title('Dilation'), plt.show()

# 침식 연산 적용, erode(영상, 구조 요소, 적용횟수=1)
b_erosion = cv.erode(b, se, iterations=1)
plt.imshow(b_erosion, cmap='gray'), plt.xticks([]), plt.yticks([])
plt.title('Erosion'), plt.show()

# 닫힘 연산 적용 -> 팽창 결과에 침식 연산
b_closing = cv.erode(b_dilation, se, iterations=1)
plt.imshow(b_closing, cmap='gray'), plt.xticks([]), plt.yticks([])
plt.title('Closing'), plt.show()