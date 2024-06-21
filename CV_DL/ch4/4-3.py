# 검출한 에지 맵에서 에지 화소는 1, 아닌 화소는 0으로 표시함
# 사람 눈에는 에지가 연결된 선분으로 보이는데, 에지 맵에는 연결 관계가
# 암시적으로 나타나 있을 뿐 명시적으로 표현 되어 있지 않음
# 이들을 연결해서 경계선으로 변환, 경계선을 직선으로 변환하면
# 이후 단계인 물체 표현, 물체 인식에 무척 유리함

# 8-연결 에지 화소(픽셀을 기준으로 상하좌우, 대각선을 포함한 8방향)를
# 서로 연결하여 경계선(Contour)을 구성할 수 있음
# 에지 맵에서 경계선 찾기
import cv2 as cv
import numpy as np

img = cv.imread('source/ch4/soccer.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
canny = cv.Canny(gray, 100, 200)

# findContours() 함수는 경계선을 찾아주는 함수임
# 첫 번째 인수는 경계선을 찾을 에지 영상

# 두 번째 인수는 경계선 검출 모드를 지정함
# 이는 경계선이 계층적으로 조직되는 방식을 결정함
# RETR_EXTERNAL: 최외각 경계선만 검출
# RETR_LIST: 모든 경계선을 검출, 계층 관계를 구성하지 않음
# RETR_CCOMP: 모든 경계선을 검출, 두 레벨의 계층을 구성
#             외각 경계는 첫 번째 레벨, 내곽 경계는 두 번째 레벨 배치
# RETR_TREE: 모든 경계선을 검출, 전체 계층 구조를 구성

# 세 번째 인수는 경계선을 근사(단순화)하는 방법을 지정
# CHAIN_APPROX_NONE: 모든 경계선 포인트를 저장
# CHAIN_APPROX_SIMPLE: 직선의 양 끝 포인트만 저장
# cv2.CHAIN_APPROX_TC89_L1 또는 cv2.CHAIN_APPROX_TC89_KCOS: Teh-Chin
# 알고리즘으로 굴곡이 심한 점을 찾아 그것들만 저장

# findContours()로 검출된 경계선 포인트들의 좌표를 contour로 반환
# contour == [[x1,y1], [x2,y2], ...]
# hierarchy는 경계선 간의 관계를 반환 받음
# hierarchy == [[Next, Previous, First_Child, Parent], ....]
contour, hierarchy = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

# 128p. 맨 밑줄, "이 프로그램은 cv.RETR_LIST로 설정해 맨 바깥쪽 
# 경계선만 찾도록 지시한다."는 오타인 것으로 보임
# 맨 바깥쪽 경계선만 찾도록 지시하는 파라미터는 RETR_EXTERNEL 방식

# 길이가 50 이상인 경계선만 골라 lcontour 객체에 저장
# findContours()는 시작점부터 끝점까지 추적한 다음 역추적하여
# 시작점으로 돌아오도록 경계선을 표현하기 때문에 > 100으로
# 설정해야 실제로는 길이가 50 이상인 경계선만 남김
lcontour = []
for i in range(len(contour)):
    if contour[i].shape[0] > 100:
        lcontour.append(contour[i])

# drawContours(영상, 경계선, -1, 색, 두께) 함수로 경계선 그리기
# 세번째 인수를 -1로 설정하면 모든 경계선을 그리고,
# 양수로 설정하면 해당 번호에 해당하는 경계선 하나만 그림
cv.drawContours(img, lcontour, -1, (0,255,0), 3)

cv.imshow('Original with contours', img)
cv.imshow('Canny', canny)

cv.waitKey()
cv.destroyAllWindows()