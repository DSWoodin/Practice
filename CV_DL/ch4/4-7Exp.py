import cv2 as cv
import numpy as np

img = cv.imread('source/ch4/soccer.jpg')
img_show = np.copy(img)

mask = np.zeros((img.shape[0], img.shape[1]), np.uint8)
mask[:,:] = cv.GC_PR_BGD

BrushSiz = 9
LColor, RColor = (255,0,0), (0,0,255)
def painting(event,x,y,flags,param):
    if event==cv.EVENT_LBUTTONDOWN:      
        cv.circle(img_show,(x,y),BrushSiz,LColor,-1)	
        cv.circle(mask,(x,y),BrushSiz,cv.GC_FGD,-1)
    elif event==cv.EVENT_RBUTTONDOWN:
        cv.circle(img_show,(x,y),BrushSiz,RColor,-1)	
        cv.circle(mask,(x,y),BrushSiz,cv.GC_BGD,-1)
    elif event==cv.EVENT_MOUSEMOVE and \
        flags==cv.EVENT_FLAG_LBUTTON:
        cv.circle(img_show,(x,y),BrushSiz,LColor,-1)
        cv.circle(mask,(x,y),BrushSiz,cv.GC_FGD,-1)
    elif event==cv.EVENT_MOUSEMOVE and \
        flags==cv.EVENT_FLAG_RBUTTON:
        cv.circle(img_show,(x,y),BrushSiz,RColor,-1)	
        cv.circle(mask,(x,y),BrushSiz,cv.GC_BGD,-1)

    cv.imshow('Painting',img_show)

def grabcut():
    background = np.zeros((1, 65), np.float64)
    foreground = np.zeros((1, 65), np.float64)
    cv.grabCut(img, mask, None, background, foreground, 5, cv.GC_INIT_WITH_MASK)
    mask2 = np.where((mask == cv.GC_BGD) | (mask == cv.GC_PR_BGD), 0, 1).astype('uint8')
    grab = img * mask2[:, :, np.newaxis]
    cv.imshow('Grab cut image', grab)

# 창과 콜백 설정
cv.namedWindow('Painting')
cv.setMouseCallback('Painting', painting)

# 붓칠을 하고 결과를 확인하려면 'g'키를 누르기
# 결과가 마음에 안들면 덧칠하고 다시 'g'키 누르기
# 마음에 들때까지 위 과정을 반복 -> 끝내려면 'q'키를 눌러 종료
while True: 
    key = cv.waitKey(1)
    if key == ord('g'): # 영역 분할 결과를 확인하려면 'g'키를 누르기
        grabcut()
    elif key == ord('q'):  # 붓 칠을 끝내려면 'q'키를 누르기
        break

cv.destroyAllWindows()