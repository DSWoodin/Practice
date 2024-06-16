import cv2 as cv
import sys

# 마우스로 클릭한 곳에 직사각형 그리기
# 마우스를 다루려면 콜백 함수(callback function) 사용해야
# 클릭이나 커서 이동 같은 이벤트는 언제 발생할지 모르기 때문

img = cv.imread('source/ch2/girl_laughing.jpg')

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

# event는 이벤트의 종류, x와 y는 이벤트가 일어난 순간 커서 위치
def draw(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN: # 마우스 좌클릭하면
        # 높이 너비 200의 빨간 직사각형 생성
        cv.rectangle(img, (x,y), (x+200,y+200), (0,0,255), 2)
    elif event == cv.EVENT_RBUTTONDOWN: # 마우스 우클릭하면
        # 높이 너비 100의 파란 직사각형 생성
        cv.rectangle(img, (x,y), (x+100,y+100), (255,0,0), 2)
    
    # 바뀐 img(직사각형이 그려진)를 윈도우에 반영
    cv.imshow('Drawing',img)

# 'Drawing'이라는 이름의 원도우 생성
cv.namedWindow('Drawing')

# 'Drawing'에 img를 디스플레이
cv.imshow('Drawing',img)

# 'Drawing'에서 마우스 이벤트가 발생하면 draw라는 콜백 함수를 호출
# 마우스 이벤트: 버튼 클릭, 버튼에서 손 놓기, 커서 이동, 휠 돌리기 등
cv.setMouseCallback('Drawing',draw)

while(True): # 마우스 이벤트가 언제 반복할지 모르므로 무한 반복
    if cv.waitKey(1) == ord('q'): # q 입력하면 윈도우 닫고 루프 탈출
        cv.destroyAllWindows()
        break