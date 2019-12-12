import cv2 as cv
import numpy as np

def SSIM(img_result, img_origin, SIZE=20):
	k = int(SIZE/2)
	k1 = 0.01
	k2 = 0.03
	c1 = (k1 * 255) ** 2
	c2 = (k2 * 255) ** 2
	c3 = c2 / 2
	a = b = g = 1
	
	num = 0
	SSIM = 0
		
	for i in range(k,img_origin.shape[0]-k):
		for j in range(k,img_origin.shape[1]-k):
			num += 1
			x = img_result[i-k:i+k+1,j-k:j+k+1]
			y = img_origin[i-k:i+k+1,j-k:j+k+1]
			u_x = np.mean(x)
			u_y = np.mean(y)
			o_x = np.mean((x - u_x) ** 2) ** 0.5
			o_y = np.mean((y - u_y) ** 2) ** 0.5
			o_xy = np.mean((x - u_x) * (y - u_y))
			L = (2 * u_x * u_y + c1) / (u_x ** 2 + u_y ** 2 + c1)
			C = (2 * o_x * o_y + c2) / (o_x ** 2 + o_y ** 2 + c2)
			S = (o_xy + c3) / (o_x * o_y + c3)
			SSIM  += (L ** a) * (C ** b) * (S ** g)

	return SSIM / num



