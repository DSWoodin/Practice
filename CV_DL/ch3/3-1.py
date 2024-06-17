import cv2 as cv
import sys

img = cv.imread('source/ch3/soccer.jpg')

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

# 원본 이미지 디스플레이
cv.imshow('originial_', img)
# 원본 이미지 배열 구조 확인
# 원본 이미지 (948,1434,3) -> 행 948개(y), 열 1434개(x), 컬러채널(3)
print(img.shape)


# 영상 이미지의 채널 
# 채널 0: Blue 채널, 채널 1: Green 채널, 채널 2: Red 채널
# 채널 3: RGB 채널, 채널 4: RGBA 채널(여기서 A는 Alpha:투명도)
# 채널 5이상: 가시광선, 적외선 등 특수 스펙트럼 채널

# 슬라이싱 영역 설정
# // 연산자는 나눗셈의 몫을 반환
y1 = img.shape[0]//2 # == 948//2
x1 = img.shape[1]//2 # == 1434//2
# 슬라이싱한 영상 디스플레이: 왼쪽 상단
# img[0:y1, 0:x1, :] == img[0:474, 0:717, 0:3]
cv.imshow('Upper left half', img[0:y1, 0:x1, :])

# 슬라이싱 영역 설정
y2 = img.shape[0]//4   # = = 948//4
y3 = 3*img.shape[0]//4 # == 3*948//4
x2 = img.shape[1]//4   # == 1434//4
x3 = 3*img.shape[1]//4 # == 3*1434//4
# 슬라이싱한 영상 디스플레이: 중앙
# img[y2:y3, x2:x3, :] == img[237:711, 358:1075, 0:3]
cv.imshow('Center half', img[y2:y3, x2:x3, :])

cv.imshow('R channel', img[:, :, 2])
cv.imshow('G channel', img[:, :, 1])
cv.imshow('B channel', img[:, :, 0])

cv.waitKey()
cv.destroyAllWindows()