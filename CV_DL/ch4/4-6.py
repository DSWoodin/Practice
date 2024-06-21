import skimage
import numpy as np
import cv2 as cv
import time

coffee = skimage.data.coffee()

start = time.time() # 분할하는데 걸린 시간 측정을 위해

# start_label 파라미터는 생성된 슈퍼 화소의 레이블 번호를 몇부터
# 시작하는지를 설정함, default는 1임
slic = skimage.segmentation.slic(coffee, compactness=20, \
                                 n_segments=600, start_label=1)

# rag_mean_color()는 슈퍼 화소를 노드로 사용하고 'similarity'를
# 에지 가중치로 사용한 그래프를 구성하여 g 객체에 저장
g = skimage.graph.rag_mean_color(coffee, slic, mode='similarity')

# cut_normalized() 함수로 slic객체와 g객체를 이용해 정규화 절단
# ncut은 화소에 영역 번호를 부여한 맵이 됨
ncut = skimage.graph.cut_normalized(slic, g)

print(coffee.shape, ' Coffee 영상을 분할하는데', time.time()-start, '초 소요')

# 영역의 개수 출력
print(np.unique(ncut))
print(np.unique(ncut).size) # 27개의 영역

# mark_boundaries()로 coffee 영상에 영역 분할 정보를 담은 ncut 맵을
# 이용하여 영역 경계를 표시하고 marking객체에 저장
marking = skimage.segmentation.mark_boundaries(coffee, ncut)

# 0~1 사이의 실수를 가진 marking을 0~255 사이의 uint8형으로 변환
ncut_coffee = np.uint8(marking*255.0)

cv.imshow('Normalized cut', cv.cvtColor(ncut_coffee, cv.COLOR_RGB2BGR))

# 실행 결과 책상과 커피 잔, 잔 받침이 서로 구분되었는데 각각은
# 여러 개의 영역으로 과잉 분할(over segmentation)되었음
# 특히 색상 변화가 심한 스푼이 심하게 과잉 분할되었음

cv.waitKey()
cv.destroyAllWindows()

# 지금까지의 영역 분할은 영상의 색상 정보에만 의존하므로, 이웃한
# 두 물체가 비슷한 색상을 가지는 경우 하나의 영역으로 분할됨
# 또한 색상 변화가 심한 물체는 과잉 분할됨
# 영역 분할에 대한 고전적 접근 방법 연구는 에지와 영역 정보를 결합해
# 성능을 높인 Arbelaez2011 논문 이후에 뚜렷한 개선이 없음

# 다행히 딥러닝 시대로 전환하면서 분할에 혁신이 일어남