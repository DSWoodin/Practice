import skimage
import numpy as np
import cv2 as cv

img = skimage.data.coffee()
cv.imshow('Coffee image', cv.cvtColor(img, cv.COLOR_RGB2BGR))

# compactness와 n_segments값을 변화시키면서 효과 비교
slic1 = skimage.segmentation.slic(img, compactness=20, n_segments=300)
sp_img1 = skimage.segmentation.mark_boundaries(img, slic1)
sp_img1 = np.uint8(sp_img1*255.0)

slic2=skimage.segmentation.slic(img,compactness=40,n_segments=300)
sp_img2=skimage.segmentation.mark_boundaries(img,slic2)
sp_img2=np.uint8(sp_img2*255.0)

slic3=skimage.segmentation.slic(img,compactness=20,n_segments=600)
sp_img3=skimage.segmentation.mark_boundaries(img,slic3)
sp_img3=np.uint8(sp_img3*255.0)

slic4=skimage.segmentation.slic(img,compactness=40,n_segments=600)
sp_img4=skimage.segmentation.mark_boundaries(img,slic4)
sp_img4=np.uint8(sp_img4*255.0)

cv.imshow('Super pixels (compact 20, segment 300)',cv.cvtColor(sp_img1,cv.COLOR_RGB2BGR))
cv.imshow('Super pixels (compact 40, segment 300)',cv.cvtColor(sp_img2,cv.COLOR_RGB2BGR))
cv.imshow('Super pixels (compact 20, segment 600)',cv.cvtColor(sp_img3,cv.COLOR_RGB2BGR))
cv.imshow('Super pixels (compact 40, segment 600)',cv.cvtColor(sp_img4,cv.COLOR_RGB2BGR))

# 실행결과 compactness가 높을수록 슈퍼화소가 네모네모
# n_segment가 높을수록 슈퍼화소 개수가 많아짐, 하나의 크기는 작아짐

cv.waitKey()
cv.destroyAllWindows()