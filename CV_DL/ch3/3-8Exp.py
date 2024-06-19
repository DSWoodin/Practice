import cv2 as cv
import sys

# 이미지 읽기
img = cv.imread('source/ch3/rose.png')
if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

# 전역 변수 선언
ix, iy = -1, -1 # 초기값 설정: -1이라는 좌표는 없으므로 -1로 설정
drawing = False # 초기값 설정

# 마우스 콜백 함수
def draw(event, x, y, flags, param):
    global ix, iy, drawing, img

    # 좌클릭 -> 클릭 좌표 저장, drawing을 True로 변경
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    
    # 드래그 과정에서 직사각형의 크기를 보여주는 실시간 피드백 제공
    # '드래그'는 마우스가 계속해서 움직이는 과정임
    # 마우스가 움직이는 매 프레임마다 직사각형을 그려야하는데
    # 원본 이미지에 그리면 직사각형들이 계속해서 겹쳐질 것임
    # 따라서 마우스가 움직일 때마다 이미지 복사본을 생성하고
    # 생성된 복사본에 직사각형을 그림
    # '드래그'의 매 프레임마다 이미지를 초기화하면서 직사각형을 그림
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing:
            temp_img = img.copy()
            cv.rectangle(temp_img, (ix, iy), (x, y), (0, 0, 255), 2)
            cv.imshow('Drawing', temp_img)
    
    # 우클릭 -> 클릭 좌표와 이전에 저장한 좌클릭 좌표로 직사각형 그림
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        cv.rectangle(img, (ix, iy), (x, y), (0, 0, 255), 2)
        cv.imshow('Drawing', img)
        display_resized_patches(ix, iy, x, y)

def display_resized_patches(x1, y1, x2, y2):
    global img
    # 영역 추출
    patch = img[y1:y2, x1:x2]
    
    # 보간 방법으로 패치 확대
    patch1 = cv.resize(patch, dsize=(0, 0), fx=5, fy=5, interpolation=cv.INTER_NEAREST)
    patch2 = cv.resize(patch, dsize=(0, 0), fx=5, fy=5, interpolation=cv.INTER_LINEAR)
    patch3 = cv.resize(patch, dsize=(0, 0), fx=5, fy=5, interpolation=cv.INTER_CUBIC)

    # 확대된 패치 보여주기
    cv.imshow('Resize nearest', patch1)
    cv.imshow('Resize bilinear', patch2)
    cv.imshow('Resize bicubic', patch3)

# 창 설정 및 마우스 콜백 설정
cv.namedWindow('Drawing')
cv.imshow('Drawing', img)
cv.setMouseCallback('Drawing', draw)

# 프로그램 종료 대기
while True:
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break