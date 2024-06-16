import cv2 as cv
import sys

# videoCapture() 함수는 웹캠과 연결을 시도하고 결과를 반환
# 첫 번째 인수로 웹캠 번호를 지정, 웹캠이 하나면 0으로 지정
# 두 번째 인수 CAP_DSHOW는 비디오가 화면에 바로 나타나게 함
cap = cv.VideoCapture(0, cv.CAP_DSHOW)

# 웹캠과 연결에 실패하면 cap 객체의 isOpened 함수가 False값을 가짐
if not cap.isOpened():
    sys.exit('카메라 연결 실패')

while True:
    # read() 함수는 호출한 순간의 영상 한 장(프레임)을 획득하고,
    # ret 객체에 성공여부, frame 객체에 프레임을 저장
    ret,frame = cap.read()

    # 프레임 획득 실패하면 루프 탈출
    if not ret:
        print('프레임 획득에 실패하여 루프를 나갑니다.')
        break
    
    # 획득한 프레임을 디스플레이
    cv.imshow('Video display',frame)

    # 1밀리초동안 키입력을 기다리고 q를 입력하면 루프 탈출
    # waitKey시간을 길게 주면 지연이 발생해 비디오가 매끄럽지 않음
    key = cv.waitKey(1)
    if key == ord('q'):
        break

cap.release() # 카메라와 연결 해제
cv.destroyAllWindows()