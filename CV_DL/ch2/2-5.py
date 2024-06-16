import cv2 as cv
import numpy as np
import sys

# 2-5는 2-4에서 몇가지 라인만 추가
# 비디오에서 수집한 영상을 이어 붙이기
cap = cv.VideoCapture(0, cv.CAP_DSHOW)

if not cap.isOpened():
    sys.exit('카메라 연결 실패')

frames=[] # 프레임들을 저장할 비어있는 리스트
while True:
    ret,frame = cap.read()

    if not ret:
        print('프레임 획득에 실패하여 루프를 나갑니다.')
        break
    
    cv.imshow('Video display',frame)

    key = cv.waitKey(1)
    if key == ord('c'): # c키가 들어오면 프레임을 리스트에 추가
        frames.append(frame)
    elif key == ord('q'): # q키가 들어오면 루프 탈출
        break

cap.release() 
cv.destroyAllWindows()

if len(frames) > 0: # 수집된 프레임이 있다면
    imgs = frames[0] # 첫 번째 프레임은 imgs에 저장
    for i in range(1, min(3, len(frames))): # 최대 3개까지만
        # hstack() 이용하여 프레임들을 이어 붙임
        imgs = np.hstack((imgs, frames[i]))
    
    cv. imshow('collected images', imgs)

    cv.waitKey()
    cv.destroyAllWindows()

print(len(frames)) 
print(frames[0].shape) # 프레임이 480x640x3의 3차원 배열임
print(imgs.shape) # 열이 1920로 늘어남 -> 가로로 3개를 이어붙여서