import cv2 as cv
import sys

cap = cv.VideoCapture(0, cv.CAP_DSHOW)

if not cap.isOpened():
    sys.exit('카메라 연결 실패')

# 현재 디스플레이 모드를 담아둘 변수
display_mode = 'color'

while True:
    ret,frame = cap.read()
    if not ret:
        print('프레임 획득에 실패하여 루프를 나갑니다.')
        break

    # 변수 상태에 따라 imshow() 해야하는 영상 설정
    if display_mode == 'gray':
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow('Video display',gray)
    else: 
        cv.imshow('Video display',frame)

    # 키 입력에 따라 변수 변경
    key = cv.waitKey(1)
    if key == ord('g'):
        display_mode = 'gray'
    elif key == ord('c'):
        display_mode = 'color'
    elif key == ord('q'):
        break

cap.release()
cv.destroyAllWindows()