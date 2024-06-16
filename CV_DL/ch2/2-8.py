import cv2 as cv
import sys

img = cv.imread('source/ch2/girl_laughing.jpg')

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

# 마우스 드래그로 도형 크기를 조절하기
# 드래그는 마우스를 클릭한 채 커서를 이동해 버튼을 놓는 행위
# 버튼을 클릭했을 때와 놓았을 때 좌표를 읽어 직사각형을 그리면 됨
def draw(event, x, y, flags, param):
    # ix와 iy라는 전역 변수(global variable) 선언
    # 전역 변수가 아니면 ix와 iy는 함수가 시작할 때 생겼다가
    # 끝날 때 소멸하는 지역 변수로 작용해, 드래그하는 동안 발생하는
    # 여러 번의 함수 호출에서 생성과 소멸을 거듭해 좌표값 유지 못함
    global ix,iy

    if event == cv.EVENT_LBUTTONDOWN:
        # 마우스 좌클릭을 하면 x,y 좌표를 전역 변수 ix,iy에 저장
        ix,iy = x,y
    elif event == cv.EVENT_LBUTTONUP:
        # 마우스 우클릭을 하면 x,y 좌표와 ix,iy 좌표로 직사각형 생성
        cv.rectangle(img, (ix,iy), (x,y), (0,0,255), 2)
    
    cv.imshow('Drawing',img)

cv.namedWindow('Drawing')
cv.imshow('Drawing',img)

cv.setMouseCallback('Drawing',draw)

while(True):
    if cv.waitKey(1)==ord('q'):
        cv.destroyAllWindows()      
        break   