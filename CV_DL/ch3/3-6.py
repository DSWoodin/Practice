# 히스토그램 평활화(histogram equalization)는 히스토그램이
# 평평하게 되도록 영상을 조작해 영상의 명암 대비를 향상시킴

# 히스토그램 평활화의 자세한 과정은 교재에 수록된 식을 참고
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('source/ch3/mistyroad.jpg')

# gray는 2D 배열임, 시각화 하기 위해서는 컬러맵을 지정해야 함
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) # 명암 영상으로 변환
plt.imshow(gray, cmap='gray'), plt.xticks([]), plt.yticks([]), plt.show()

h = cv.calcHist([gray], [0], None, [256], [0,256]) # 히스토그램 계산
plt.plot(h, color='r', linewidth=1), plt.show()

equal = cv.equalizeHist(gray) # equalizeHist()로 히스토그램 평활화
plt.imshow(equal, cmap='gray'), plt.xticks([]), plt.yticks([]), plt.show()

h = cv.calcHist([equal], [0], None, [256], [0,256]) # 히스토그램 재계산
plt.plot(h, color='r', linewidth=1), plt.show()