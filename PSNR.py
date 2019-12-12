import cv2 as cv
import numpy as np
import loaddata
import math

def PSNR(img_result, img_origin):
	weight = img_result.shape[0] * img_result.shape[1]
	diff = (img_result - img_origin) ** 2

	MSE = sum(diff[diff != 0]) / weight
	PSNR = 10 * math.log10(255 ** 2 / MSE)
	return PSNR

if __name__ == '__main__':
	data_result = loaddata.Dataset()
	data_origin = loaddata.Dataset()