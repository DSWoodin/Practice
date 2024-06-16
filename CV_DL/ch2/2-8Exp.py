import cv2 as cv
import sys
import math

img = cv.imread('source/ch2/girl_laughing.jpg')

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

def draw(event, x, y, flags, param):
    global ix,iy

    # 좌클릭은 직사각형을 그리고, 우클릭은 원을 그리도록 확장
    if event == cv.EVENT_LBUTTONDOWN or event == cv.EVENT_RBUTTONDOWN:
        ix,iy = x,y
    elif event == cv.EVENT_LBUTTONUP:
        cv.rectangle(img, (ix,iy), (x,y), (0,0,255), 2)
    elif event == cv.EVENT_RBUTTONUP:
        # 두 점사이의 거리를 구하는 공식 사용, 드래그한 지점 -> 반지름
        distance = int(math.sqrt((x-ix)**2 + (y-iy)**2))
        cv.circle(img, (ix,iy), distance, (255,0,0), 2)

    cv.imshow('Drawing',img)

cv.namedWindow('Drawing')
cv.imshow('Drawing',img)

cv.setMouseCallback('Drawing',draw)

while(True):
    if cv.waitKey(1)==ord('q'):
        cv.destroyAllWindows()      
        break   