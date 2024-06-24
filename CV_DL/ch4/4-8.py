# 특징의 불변성과 등변성 개념
# 면적은 회전에 불변, 축소에는 불변이 아님
# 면적은 회전에 등변이 아님, 축소에는 등변
# 물체의 중심 축을 나타내는 주축은 회전에 불변이 아님, 축소에 불변

# 모멘트(Moment)는 분포나 형태의 특성을 수치적으로 나타내는 방법
# 이미지 처리에서는 도형의 형태, 위치, 크기, 방향등의 특징을 분석
# 영역의 면적, 중점을 구해 중심 모멘트 정의 -> (자세한 수식은 도서참고)
# 중심 모멘트 등으로 특징 추출 -> 열행 분산, 둘레, 둥근 정도, 주축방향

# 텍스처는 이미지 내에서 픽셀의 배치 패턴을 나타냄
# 텍스처 특징은 이러한 패턴을 수치적으로 표현해 이미지 분석에 사용
# 텍스쳐 특징을 추출하는 강력한 방법 2가지, LBP와 LTP

# LBP(Local Binary Patterns)는 주변 화소와의 비교로 이진패턴 생성
# 1. 기준 픽셀을 중심으로 8개 이웃 픽셀과 명암값 비교
# 2. 기준 픽셀 보다 크거나 같으면 1, 작으면 0으로 이진화
# 3. 이진 패턴을 8비트 이진수로 변환 -> 0~255의 값을 가지는 패턴
# 4. 이미지 내의 모든 픽셀에 LBP 계산하여 히스토그램 생성
# 5. 최종 특징 벡터 산출 (256차원 특징 벡터)

# LTP(Local Ternary Patterns)는 삼진화(Ternary) 방식과 임계값
# 설정을 통해 작은 명암 변화에 민감한 LBP의 단점을 보완
# 1. 기준 픽셀을 중심으로 8개 이웃 픽셀과 명암값 비교
# 2. 임계값 t를 사용해 기준 '픽셀값-t'보다 작은 화소는 -1,
# '픽셀값+t'보다 큰 화소는 +1, 나머지는 0으로 삼진화
# 3. 삼진 패턴을 2개의 이진 패턴으로 분리(양성 LTP, 음성 LTP)
# 4. 양성 및 음성 LTP에 대해 각각 히스토그램 생성
# 5. 히스토그램을 결합하여 최종 특징 벡터 산출 (512차원 특징 벡터)

# LBP, LTP 등으로 수치적으로 추출된 텍스처 특징을 이용해
# 객체 인식, 분류, 질병 진단, 포면 결함 검출 등 다양한 분야에 사용
# LBP와 LTP는 로컬 주변 값에 기초해 특징 추출하므로, 노이즈에 강함

import skimage
import numpy as np
import cv2 as cv

# horse()는 말이 차지한 영역은 False, 배경은 True로 표시한 영상임
orig = skimage.data.horse()
# '0 또는 1'(True or False)에서 말 영역은 255, 배경은 0으로 변환
img = 255 - np.uint8(orig)*255
cv.imshow('Horse', img)

# findContours()로 경계선 추출, len(contours) 해보면 경계선이 1개임
contours, hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, \
                                      cv.CHAIN_APPROX_NONE)
img2 = cv.cvtColor(img, cv.COLOR_GRAY2BGR) # 컬러 디스플레이용 영상
# drawContours()로 핑크색 경계선 그리기
cv.drawContours(img2, contours, -1, (255, 0, 255), 2)
cv.imshow('Horse with contour', img2)

# contours의 0번 요소를 꺼내 저장, 이후 코드가 경계선 하나를 처리해서
contour = contours[0] 

# print(m) 해보면 m은 딕셔너리, key가 'm00', 'm01', 'm10', ...
m = cv.moments(contour) # 모멘트 추출
area = cv.contourArea(contour) # 경계선으로 둘러싸인 면적 계산
cx, cy = m['m10']/m['m00'], m['m01']/m['m00'] # 중점 계산식 (도서 참고)

# arcLength로 둘레 길이 계산, True는 contour가 폐곡선임을 알림
perimeter = cv.arcLength(contour, True)
roundness = (4.0*np.pi*area) / (perimeter*perimeter) # 둥근 정도 계산
print('면적=',area, '\n중점=(',cx,',',cy,')', \
      '\n둘레=',perimeter, '\n둥근 정도=',roundness)

img3 = cv.cvtColor(img, cv.COLOR_GRAY2BGR) # 컬러 디스플레이용 영상

# approxPolyDP()는 경계선을 직선으로 근사함
# 직선 근사는 복잡한 경계선을 간단한 직선 세그먼트로 표현하여
# 데이터의 전체적인 형태를 유지하면서 데이터 복잡성을 줄임
# 직선 근사 알고리즘의 과정에 대해서는 도서 참고
# 두번째 인수인 8은 임계값, 세번째 인수 True는 폐곡선임을 알림
contour_approx = cv.approxPolyDP(contour, 8, True)
# 근사한 결과를 img3에 녹색으로 표시
cv.drawContours(img3, [contour_approx], -1, (0, 255, 0), 2)

# 볼록 헐(Convex Hull)은 주어진 점 집합을 포함하는 
# 가장 작은 볼록 다각형(Convex Polygon)을 의미
# 이는 점 집합의 경계점들로 이루어진 다각형을 형성
# -> 데이터의 범위나 외각을 파악하는데 도움이 됨
hull = cv.convexHull(contour) # 볼록 헐 계산
# 계산된 볼록 헐을 drawContours()에 입력 할 수 있는 형태로 변환
hull = hull.reshape(1, hull.shape[0], hull.shape[2])
cv.drawContours(img3, hull, -1, (0,0,255), 2)

cv.imshow('Horse with line segments and convex hull',img3)

cv.waitKey()
cv.destroyAllWindows()