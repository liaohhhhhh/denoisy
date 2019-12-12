import os
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt 


class Dataset:
	def __init__(self, inpath):
		
		filelist = os.listdir(inpath)
		filelist.sort()
		self.list_img_name = []
		self.inpath = inpath
		

		
		for filename in filelist:
			self.list_img_name.append(filename)

	def creat_outdir(self, outpath):
		self.outpath = outpath
		os.makedirs(outpath)

	def getitem(self, index):
		#print(self.list_img_name[index])
		img = cv.imread(self.inpath + '/' + self.list_img_name[index])
		return img

	def getname(self, index):
		return self.list_img_name[index]

	def writeitem(self, img_result, index):
		outpath = self.outpath + '/' + self.list_img_name[index]
		cv.imwrite(outpath,img_result)
		return

	def getlen(self):
		return len(self.list_img_name)

# if __name__ == '__main__':
# 	datas = Dataset()
# 	for i in range(3):
# 		img = datas.getitem(i)
# 		datas.writeitem(img,i)
