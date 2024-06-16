import cv2 as cv
import sys

# imread()는 지정된 영상 파일을 폴더에서 읽어옴
img = cv.imread('source/ch2/soccer.jpg')

if img is None:
    # sys 모듈의 exit() 함수를 이용해 프로그램 종료
    sys.exit('파일을 찾을 수 없습니다.')
    
# imshow()로 영상을 윈도우에 디스플레이
# imshow(윈도우 이름, 디스플레이할 영상)
cv.imshow('Image Display',img)

# waitKey()는 키보드의 키가 눌릴 때까지 기다리다가,
# 눌리면 해당 키의 유니코드를 반환함
# 인수를 생략하거나 0으로 설정하면 무한정 기다림
# 시간 지정은 밀리초 단위의 정수 -> waitKey(10000) -> 10초 기다림
# 지정한 시간동안 키 입력이 일어나지 않으면 -1을 반환
cv.waitKey()

# 모든 윈도우 닫기
cv.destroyAllWindows()
# waitKey()와 destroyAllWindows()가 없으면
# imshow()로 윈도우가 나타나고 즉시 프로그램이 종료되어 윈도우 못 봄

print(type(img))
# img 객체는 numpy.ndarray 클래스임

print(img.shape)
# 배열 모양은 948x1434x3 크기의 3차원 배열임
# -> 948개의 행과 1434개의 열을 가진 채널 3개로 구성
# 3개 채널은 앞쪽부터 B,G,R임
# 보통 RGB 순서인데 OpenCV에서는 기본이 BGR임

print(img[0,0,0], img[0,0,1], img[0,0,2])
# (0,0)픽셀의 화소가 B162, G104, R98임을 알 수 잇음
# 그림판으로 (0,0)을 스포이트로 찍어도 같은 결과 (가장 좌상단 픽셀)