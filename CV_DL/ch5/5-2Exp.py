import cv2 as cv

img = cv.imread('source/ch5/mot_color70.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# 키포인트를 2, 4, 8, 16, ..., 512개를 생성하고 각 결과를 비교
for i in range(1, 10):
    keypoints = 2**i
    sift = cv.SIFT_create(nfeatures=keypoints)
    kp, des = sift.detectAndCompute(gray, None)
    gray = cv.drawKeypoints(gray, kp, None, flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv.imshow(f'sift_{keypoints}', gray)

# 실행결과 SIFT는 신호등, 표지판, 창문, 건물 모서리처럼
# 1. 주변과 명암대비가 확실하거나
# 2. 코너 처럼 여러 방향으로의 경계가 있거나
# 3. 표지판 처럼 상대적으로 복잡한 패턴이 존재하는
# 곳들을 키포인트로 검출해냄
# 이러한 기준에 따른 특징점 검출은 스케일 불변성을 유지함 

cv.waitKey()
cv.destroyAllWindows()