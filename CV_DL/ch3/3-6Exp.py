# 히스토그램 평활화 함수를 직접 작성하여 cv.equalizeHist()와 비교
# cv.equalizeHist()를 이용한 평활화 결과와 예시 3-4에서 소개된
# 평활화 과정에는 큰 차이가 있어서 다른 결과가 나옴

# histogram_equalization()으로 구현한 예시 3-4의 평활화 과정에서는
# 0부터 L-1까지의 값 즉 0~7까지의 값으로 스케일링하지만,
# cv.equalizeHist()는 기본적으로 0~255의 값으로 스케일링을 진행하고,
# 이 과정에서 발생하는 반올림 오류는 결과 차이를 만들 수 있음

# 함수 처리 시간은 cv.equalizeHist() 함수가 def 함수보다 훨씬 빠름

# GPT를 이용해 코드 작성
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import timeit

def histogram_equalization(image, L):
    # 히스토그램 계산
    hist = cv.calcHist([image], [0], None, [L], [0, L]).flatten()
    # 정규화 히스토그램 계산
    hist_normalized = hist / hist.sum()
    # 누적 정규화 히스토그램 계산
    cdf = hist_normalized.cumsum()
    cdf_normalized = np.round(cdf * (L - 1))
    # 원래 명암 값을 새로운 명암 값으로 매핑
    image_equalized = cdf_normalized[image.flatten()].reshape(image.shape)
    return image_equalized.astype(np.uint8), hist, cdf_normalized

# 입력 이미지 배열
image = np.array([[1, 2, 2, 2, 1, 1, 2, 0],
                  [2, 6, 7, 6, 6, 4, 3, 0],
                  [2, 6, 7, 6, 6, 4, 3, 2],
                  [2, 5, 6, 6, 6, 4, 3, 2],
                  [2, 5, 6, 6, 5, 5, 3, 2],
                  [2, 5, 5, 5, 3, 3, 3, 2],
                  [2, 2, 3, 3, 3, 1, 1, 1],
                  [2, 2, 1, 1, 1, 1, 1, 1]], dtype=np.uint8)

L = 8  # 명암 단계

# 사용자 정의 히스토그램 평활화 적용 시간 측정
custom_duration = timeit.timeit('histogram_equalization(image, L)', globals=globals(), number=1000) / 1000
print('Custom equalization time:', custom_duration)

# OpenCV 히스토그램 평활화 적용 시간 측정
cv_duration = timeit.timeit('cv.equalizeHist(image)', globals=globals(), number=1000) / 1000
print('OpenCV equalization time:', cv_duration)

# 사용자 정의 히스토그램 평활화 적용
image_equalized_custom, hist, cdf_normalized = histogram_equalization(image, L)

# OpenCV 히스토그램 평활화 적용
equalized_image_cv = cv.equalizeHist(image)

# OpenCV 결과를 8단계로 조정
equalized_image_cv_adjusted = np.clip(equalized_image_cv / 32, 0, L-1).astype(np.uint8)

# 결과 시각화
plt.figure(figsize=(16, 8))

# 원본 이미지
plt.subplot(2, 3, 1)
plt.imshow(image, cmap='gray', vmin=0, vmax=L-1)
plt.title('Original Image')
plt.axis('off')

# 사용자 정의 히스토그램 평활화 이미지
plt.subplot(2, 3, 2)
plt.imshow(image_equalized_custom, cmap='gray', vmin=0, vmax=L-1)
plt.title('Custom Equalized Image\nTime: {:.6f} seconds'.format(custom_duration))
plt.axis('off')

# OpenCV 히스토그램 평활화 이미지
plt.subplot(2, 3, 3)
plt.imshow(equalized_image_cv_adjusted, cmap='gray', vmin=0, vmax=L-1)
plt.title('OpenCV Equalized Image\nTime: {:.6f} seconds'.format(cv_duration))
plt.axis('off')

# 원본 히스토그램
plt.subplot(2, 3, 4)
hist_orig = cv.calcHist([image], [0], None, [L], [0, L]).flatten()
plt.plot(np.arange(L), hist_orig, color='blue', marker='o', linestyle='-', alpha=0.7)
plt.title('Original Histogram')
for i in range(L):
    plt.text(i, hist_orig[i], str(int(hist_orig[i])), ha='center', va='bottom')

# 사용자 정의 평활화 히스토그램
equalized_hist_custom = cv.calcHist([image_equalized_custom], [0], None, [L], [0, L]).flatten()
plt.subplot(2, 3, 5)
plt.plot(np.arange(L), equalized_hist_custom, color='green', marker='o', linestyle='-', alpha=0.7)
plt.title('Custom Equalized Histogram')
for i in range(L):
    plt.text(i, equalized_hist_custom[i], str(int(equalized_hist_custom[i])), ha='center', va='bottom')

# OpenCV 평활화 히스토그램
equalized_hist_cv = cv.calcHist([equalized_image_cv_adjusted], [0], None, [L], [0, L]).flatten()
plt.subplot(2, 3, 6)
plt.plot(np.arange(L), equalized_hist_cv, color='red', marker='o', linestyle='-', alpha=0.7)
plt.title('OpenCV Equalized Histogram')
for i in range(L):
    plt.text(i, equalized_hist_cv[i], str(int(equalized_hist_cv[i])), ha='center', va='bottom')

plt.tight_layout()
plt.show()