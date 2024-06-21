import cv2 as cv
import numpy as np

img = cv.imread('source/ch4/soccer.jpg')
# 원본 영상 img는 분할 알고리즘을 위해 원래 내용을 유지해야함
img_show = np.copy(img) # 붓 칠을 디스플레이할 목적의 영상 복사본

# 사용자의 붓칠에 따라 물체인지 배경인지 정보를 기록할 배열 mask
# np.zeros()로 데이터 타입이 np.uint8이며 크기가 원본 이미지와 같으며
# 모든 요소가 0으로 초기화된 배열을 생성
mask = np.zeros((img.shape[0], img.shape[1]), np.uint8)

# GrabCut 알고리즘에서는 각 픽셀을 다음 네 가지 클래스 중 하나로 분류
# cv.GC_BGD (0): 확실한 배경 (Definitely Background)
# cv.GC_FGD (1): 확실한 전경 (Definitely Foreground)
# cv.GC_PR_BGD (2): 잠재적인 배경 (Probably Background)
# cv.GC_PR_FGD (3): 잠재적인 전경 (Probably Foreground)
# mask의 모든 화소를 '배경일 것 같음'(잠재적 배경)으로 초기 설정
mask[:,:] = cv.GC_PR_BGD

BrushSiz = 9 # 붓의 크기 
LColor, RColor = (255,0,0), (0,0,255) # 파란색(물체)과 빨간색(배경)

# 좌클릭은 파란색, 우클릭은 빨간색으로 붓을 그림
def painting(event,x,y,flags,param):
    # 좌클릭, 우클릭, 좌클릭하며 이동, 우클릭하며 이동이 발생하면
    # 복사본 이미지인 img_show에 붓으로 그리고
    # mask 배열에는 붓을 그린 부분 GC_FGD 또는 GC_BGD로 기록하여
    # 확실히 물체인지 or 확실히 배경인지를 기록함
    if event==cv.EVENT_LBUTTONDOWN: # 좌클릭하면 파란색       
        cv.circle(img_show,(x,y),BrushSiz,LColor,-1)	
        cv.circle(mask,(x,y),BrushSiz,cv.GC_FGD,-1)
    elif event==cv.EVENT_RBUTTONDOWN: # 우클릭하면 빨간색 
        cv.circle(img_show,(x,y),BrushSiz,RColor,-1)	
        cv.circle(mask,(x,y),BrushSiz,cv.GC_BGD,-1)
    # event는 특정 마우스 이벤트, flags는 현재 마우스 상태
    elif event==cv.EVENT_MOUSEMOVE and \
        flags==cv.EVENT_FLAG_LBUTTON: # 좌클릭하고 이동하면 파란색
        cv.circle(img_show,(x,y),BrushSiz,LColor,-1)
        cv.circle(mask,(x,y),BrushSiz,cv.GC_FGD,-1)
    elif event==cv.EVENT_MOUSEMOVE and \
        flags==cv.EVENT_FLAG_RBUTTON: # 우클릭하고 이동하면 빨간색
        cv.circle(img_show,(x,y),BrushSiz,RColor,-1)	
        cv.circle(mask,(x,y),BrushSiz,cv.GC_BGD,-1)

    cv.imshow('Painting',img_show)

cv.namedWindow('Painting')
cv.setMouseCallback('Painting', painting)

while(True): # 붓 칠을 끝내려면 'q'키를 누르기
    if cv.waitKey(1) == ord('q'):
        break

# 붓 칠을 끝내면 GrabCut 적용
# grabCut() 함수가 내부에서 사용할 배경 히스토그램과 물체 히스토그램을 
# 생성하고 0으로 초기화, 히스토그램은 실수이며 65개의 칸을 가짐
background = np.zeros((1,65), np.float64)
foreground = np.zeros((1,65), np.float64)

# grabCut의 첫번째 인수는 원본 영상, 두번째 인수는 mask 배열임
# mask 배열은 원본 이미지와 데이터 타입이 같아야 하며, 각 픽셀의
# 상태를 나타내는 값으로 구성((ex) cv.GC_BGD, cv.GC_FGD, ...)

# 세번째 인수는 초기 관심 영역을 지정하는데, None설정하여 전체 영역

# 네번째와 다섯번째 인수는 배경과 물체 히스토그램

# 여섯번째 인수는 GrabCut 알고리즘이 수렴할 때까지 반복될 최대 횟수

# 일곱번째 인수(mode)는 GrabCut 알고리즘이 초기화되는 방법을 지정
# GrabCut 알고리즘이 어떻게 시작될지를 결정함
# GC_INIT_WITH_MASK은 마스크를 사용해서 초기화하라고 설정함
# 이 모드는 사용자가 정의한 mask를 기반으로 GrabCut을 시작하라는 뜻
cv.grabCut(img, mask, None, background, foreground, 5, cv.GC_INIT_WITH_MASK)

# np.where(조건, 조건이 True일 때 선택되는 값, 조건이 False일 때 선택되는 값)
# np.where()을 이용해 '확실히 배경' 또는 '배경일것 같음' 화소는 0으로,
# '확실히 전경(물체)' 또는 '전경일것 같음' 화소는 1로 값을 변경
mask2 = np.where((mask==cv.GC_BGD)|(mask==cv.GC_PR_BGD), 0, 1).astype('uint8')

# 2차원 배열(x,y)인 mask2에 새로운 축을 추가하여 3차원 배열로 확장
# 결과적으로 mask2는 (height, width, 1(1은 채널))의 형태가 됨
# 원본 이미지인 img는 RGB 이미지이므로 (height, width, 3)의 배열임
# -> np.newaxis를 통해 차원을 확장한 mask2와 img를 요소별 곱셈함
# 마스크 배열이 1인 위치에서는 1이 곱해져 원래 이미지 값이 유지되고,
# 마스크 배열이 0인 위치에서는 0이 곱해져 값이 0이 됨
# -> mask2에서 '확실히 배경' 또는 '배경일것 같음' 화소를 0으로 설정
# 했으므로, img*mask2는 배경을 제거하는 효과가 나타남
grab = img*mask2[:, :, np.newaxis]

cv.imshow('Grab cut image',grab)  

cv.waitKey()
cv.destroyAllWindows()