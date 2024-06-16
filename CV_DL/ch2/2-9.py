import cv2 as cv 
import sys

img=cv.imread('source/ch2/soccer.jpg')

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

BrushSiz = 5 # 붓의 크기: 5
LColor,RColor = (255,0,0),(0,0,255) # 붓 색깔: 파란색,빨간색

# 마우스가 이동한 궤적을 따라 페인팅하는 기능 구현
def painting(event, x, y, flags, param):
    # circle(영상, 원의 중심, 반지름, 색깔, 두께)
    # 두께를 -1로 설정하면 원의 내부가 채워짐
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img, (x,y), BrushSiz, LColor, -1)

    elif event == cv.EVENT_RBUTTONDOWN:
        cv.circle(img, (x,y), BrushSiz, RColor, -1)

    # flags 매개변수는 마우스의 현재 버튼 상태 확인에 사용됨
    # 아래 코드는 마우스 버튼이 눌리면서 이동하고 있는(and) 상황
    # EVENT_FLAG_LBUTTON 처럼 FLAG가 포함된 이벤트는 현재 상태를 전달
    # 만약 flags == 0으로 설정하면 아무 버튼도 눌리지 않은 상태
    elif event == cv.EVENT_MOUSEMOVE and flags == cv.EVENT_FLAG_LBUTTON:
        cv.circle(img, (x,y), BrushSiz, LColor, -1)

    elif event == cv.EVENT_MOUSEMOVE and flags == cv.EVENT_FLAG_RBUTTON:
        cv.circle(img, (x,y), BrushSiz, RColor, -1)

    cv.imshow('Painting',img)

cv.namedWindow('Painting')
cv.imshow('Painting',img)

cv.setMouseCallback('Painting',painting)

while(True):
    if cv.waitKey(1)==ord('q'):
        cv.destroyAllWindows()      
        break