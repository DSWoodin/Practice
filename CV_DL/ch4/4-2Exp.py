import cv2 as cv

img = cv.imread('source/ch4/soccer.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Canny() 함수의 파라미터를 바꿔가며 상호 비교
canny1 = cv.Canny(gray, 50, 150)
canny2 = cv.Canny(gray, 100, 200)
canny3 = cv.Canny(gray, 100, 200, None, 3, True)
canny4 = cv.Canny(gray, 100, 200, None, 5, True)
# L2gradient를 True로 설정하니 더욱 정확한 에지 추출
# 커널 사이즈가 5로 커지니 너무 많은 노이즈 발생

cv.imshow('Original',gray)
cv.imshow('Canny1',canny1)
cv.imshow('Canny2',canny2)
cv.imshow('Canny3',canny3)
cv.imshow('Canny4',canny4)

cv.waitKey()
cv.destroyAllWindows()