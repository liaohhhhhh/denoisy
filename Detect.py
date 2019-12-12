import numpy as np
import cv2 as cv
from scipy import stats
import loaddata
import Method
def double2uint8(I, ratio=1.0):
    return np.clip(np.round(I*ratio), 0, 255).astype(np.uint8)

def search(img):
	img_YCC = cv.cvtColor(img,cv.COLOR_BGR2YCrCb)
	Y,Cr,Cb = cv.split(img_YCC)
	# cv.imshow('Y',Y)
	# cv.imshow('U',Cr)
	# cv.imshow('V',Cb)
	# cv.waitKey()
	# cv.destroyAllWindows()
	r = np.zeros((img.shape[0],img.shape[1]))
	Cr_most = stats.mode(Cr)[0][0][0]
	Cb_most = stats.mode(Cb)[0][0][0]
	Cr_diff = abs(Cr.astype(int) - Cr_most)
	Cb_diff = abs(Cb.astype(int) - Cb_most)
	Y_mean  = np.mean(Y)
	Y_diff  = Y - Y_mean

	diff = Cr_diff + Cb_diff
	diff_mean = np.mean(diff)
	r[(diff >= 5)] = 255
	r[(Y < 60)] = 0
	r[diff >= 15] = 255

	for i in range(r.shape[0]):
		for j in range(r.shape[1]):
			if match(r, i, j):
				r[i,j] = 255

	return r

def match(r, i, j):
	row = r.shape[0]
	col = r.shape[1]

	score = 0
	if i==0 or i==row-1 or j==0 or j==col-1:
		return False

	if r[i+1][j]==255:
		score += 1
	if r[i-1][j]==255:
		score += 1
	if r[i][j+1]==255:
		score += 1
	if r[i][j-1]==255:
		score += 1

	if score >= 3:
		return True
	else:
		return False

		


if __name__ == '__main__':
	datas = loaddata.Dataset()
	for i in range(100):
		print(i)
		img = datas.getitem(i)
		r = search(img)
		datas.writeitem('./train_detect/',double2uint8(r),i)
		# cv.imshow('r',r)
		# cv.waitKey(0)
		# cv.destroyAllWindows()

