# 동차 좌표와 동차 행렬을 이용한 기하 변환 -> 도서 설명 참고
# 3가지 기하 변환: 이동, 회전, 크기

# 이동, x방향으로 tx, y방향으로 ty만큼 이동
# np.array([[1, 0, tx],
#           [0, 1, ty],
#           [0, 0, 1 ]])

# 회전, 원점을 중심으로 반시계 방향으로 θ만큼 회전
# np.array([[cos_theta, -sin_theta, 0],
#           [sin_theta, cos_theta,  0],
#           [0,         0,          1]])

# 크기(스케일링), x방향으로 sx, y방향으로 sy만큼 크기 조정
# 1보다 크면 확대, 1보다 작으면 축소
# np.array([[sx, 0, 0],
#           [0, sy, 0],
#           [0, 0,  1]])

# 이동, 회전, 크기와 같은 변환 행렬은 아무리 여러개를 곱해도
# 직선은 직선을 유지, 평행선은 평행을 유지한다.
# 그 이유는 동차 행렬의 제3행이 [0,0,1]로 동일하기 때문
# -> 이런 성질의 변환을 어파인 변환(affine transformation)이라 함

# 영상의 기하 변환 -> 화소에 동차 변환을 적용해 영상을 회전 등 변환
# 화소 위치 연산 과정에서 실수값이 됨 -> 정수로 반올림 해버리면?
# -> 몇몇 화소들이 값을 받지 못해 구멍이 뚫리는 에일리어싱(aliasing)
# 에일리어싱을 방지하기 위해 안티 에일리어싱 하려면 후방 변환 사용
# 후방 변환은 변환 행렬의 역행렬을 사용함

# 실수 좌표를 정수 변환 시 반올림 -> 최근접 이웃(nearest neighbor)
# 최근접 이웃 방법은 에일리어싱이 심함 -> 보간을 이용하면 개선됨
# 보간 방법: 어떤 화소가 실수 좌표로 변환되어 여러 개의 화소에 
# 걸치게 되면 각 화소와 걸친 비율에 따라 가중 평균하여 화소값을 계산
# 보간 계산 방법에 따라서 양선형 보간, 양3차 보간 -> 도서 참고
import cv2 as cv

img = cv.imread('source/ch3/rose.png')
patch = img[250:350, 170:270, :] # 100x100 슬라이싱

img = cv.rectangle(img, (170,250), (270,350), (255,0,0), 3)
# fx와 fy를 5로 지정하여 5배 확대
# 최근접 이웃:INTER_NEAREST, 양선형 보간:INTER_LINEAR
# 양3차보간:INTER_CUBIC, (default는 양선형 보간임)
patch1 = cv.resize(patch, dsize=(0,0), fx=5, fy=5, interpolation=cv.INTER_NEAREST)
patch2 = cv.resize(patch, dsize=(0,0), fx=5, fy=5, interpolation=cv.INTER_LINEAR)
patch3 = cv.resize(patch, dsize=(0,0), fx=5, fy=5, interpolation=cv.INTER_CUBIC)

cv.imshow('Original',img)
cv.imshow('Resize nearest',patch1) 
cv.imshow('Resize bilinear',patch2) 
cv.imshow('Resize bicubic',patch3) 

cv.waitKey()
cv.destroyAllWindows()