# 옥타브를 구성하는 가우시안 영상 개수를 지정하여
# n개의 가우시안 이미지와 n-1개의 DOG 이미지를 디스플레이

import numpy as np
import cv2 as cv

# 가우시안 영상의 개수를 지정
# input()을 이용해서 영상 개수를 지정하려고 시도했으나
# 출력 이미지들이 vscode 화면 뒤에 생성되는 이상한 현상 발생
# 코드 내에서 num_guassians 변수의 값을 변경하는 방법은 문제없음
num_gaussians = 6

img = cv.imread('source/ch5/mot_color70.jpg')[90:450, 340:660]
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# 초기 시그마 값과 비율 설정
initial_sigma = 1.6
k = 2**(1/3)

# 시그마 값 리스트 생성
sigma_values = [initial_sigma]
for i in range(1, num_gaussians):
    next_sigma = k * sigma_values[-1]
    sigma_values.append(next_sigma)

print("Sigma values:", sigma_values)

# 가우시안 블러를 적용한 이미지들을 저장 및 출력
smoothed_images = []
for i, sigma in enumerate(sigma_values, start=1):
    smoothed_image = cv.GaussianBlur(gray, (9, 9), sigma)
    smoothed_images.append(smoothed_image)
    cv.namedWindow(f'GaussianSmoothing{i}', cv.WINDOW_NORMAL)
    cv.imshow(f'GaussianSmoothing{i}', smoothed_image)

# DoG 이미지를 생성하고 표시
# subtract를 이용하여 가우시안 이미지들의 화소 차이를 계산
# 0~255까지 값으로 정규화도 추가적으로 진행
for i in range(len(smoothed_images) - 1):
    dog_image = cv.subtract(smoothed_images[i+1], smoothed_images[i])
    dog_image = cv.normalize(dog_image, None, 0, 255, cv.NORM_MINMAX)
    cv.namedWindow(f'DoG{i + 1}', cv.WINDOW_NORMAL)
    cv.imshow(f'DoG{i + 1}', dog_image)

cv.waitKey(0)
cv.destroyAllWindows()