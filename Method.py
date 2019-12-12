import numpy as np
import cv2 as cv
import math as m

m1 = np.array([[-1, 0, 1],
			   [-1, 0, 1],
			   [-1, 0, 1]])
m2 = np.array([[-1,-1,-1],
			   [ 0, 0, 0],
			   [ 1, 1, 1]])
m3 = np.array([[-1, 0, 0, 0, 1],
			   [-1, 0, 0, 0, 1],
			   [-1, 0, 0, 0, 1],
			   [-1, 0, 0, 0, 1],
			   [-1, 0, 0, 0, 1],])
m4 = np.array([[-1,-1,-1,-1,-1],
			   [ 0, 0, 0, 0, 0],
			   [ 0, 0, 0, 0, 0],
			   [ 0, 0, 0, 0, 0],
			   [ 1, 1, 1, 1, 1]])

def canny(f, r, i, j):
	result = np.zeros((3))
	# print(i,',',j,',',f.shape)
	
	g = cv.cvtColor(f,cv.COLOR_BGR2GRAY)
	theta = 0
	Gx = (np.dot(np.array([[1, 1, 1]]), (m1 * g[i-1:i+2, j-1:j+2]))).dot(np.array([[1], [1], [1]]))
	Gy = (np.dot(np.array([[1, 1, 1]]), (m2 * g[i-1:i+2, j-1:j+2]))).dot(np.array([[1], [1], [1]]))
	if Gx[0] == 0:
		result = insert90(g, r, i, j)
	else:
		temp = (np.arctan(Gy[0] / Gx[0])) * 180 / np.pi
		if Gx[0]*Gy[0] > 0:
				if Gx[0] > 0:
					theta = np.abs(temp)
				else:
					theta = np.abs(temp) - 180

		if Gx[0]*Gy[0] < 0:
			if Gx[0] > 0:
				theta = (-1) * np.abs(temp)
			else:
				theta = 180 - np.abs(temp)
		if(		((theta >= -22.5) and (theta < 22.5)) or
				((theta <= -157.5) and (theta > -180)) or
				((theta >= 157.5) and (theta < 180))):
			result = insert0(f, r, i, j)
		elif(	((theta >= 22.5) and (theta < 67.5)) or
				((theta <= -112.5) and (theta > -157.5))):
			result = insert45(f, r, i, j)
		elif(	((theta >= 67.5) and (theta < 122.5)) or
				((theta <= -67.5) and (theta > -122.5))):
			result = insert90(f, r, i, j)
		elif(	((theta >= 122.5) and (theta < 157.5)) or
				((theta <= -22.5) and (theta > -67.5))):
			result = insert135(f, r, i, j)
	return result

def canny1(f, r, i, j):
	result = np.zeros((5))
	# print(i,',',j,',',f.shape)
	
	g = cv.cvtColor(f,cv.COLOR_BGR2GRAY)
	theta = 0
	# Gx = (np.dot(np.array([[1, 1, 1, 1, 1]]), (m3 * g[i-2:i+3, j-2:j+3]))).dot(np.array([[1], [1], [1], [1], [1]]))
	# Gy = (np.dot(np.array([[1, 1, 1, 1, 1]]), (m4 * g[i-2:i+3, j-2:j+3]))).dot(np.array([[1], [1], [1], [1], [1]]))
	Gx = (np.dot(np.array([[1, 1, 1]]), (m1 * g[i-1:i+2, j-1:j+2]))).dot(np.array([[1], [1], [1]]))
	Gy = (np.dot(np.array([[1, 1, 1]]), (m2 * g[i-1:i+2, j-1:j+2]))).dot(np.array([[1], [1], [1]]))
	if Gx[0] == 0:
		result = insert90(g, r, i, j)
	else:
		temp = Gy[0] / Gx[0]
		if abs(temp) > 4:
			result = insert90(g, r, i, j)
		else:
			temp = round(float(temp))
			result = insert(g, r, i ,j, temp)
	return result

def insert(g, r, i, j, temp):

	x_step = 1
	y_step = temp
	XL = XH = i
	YL = YH = j

	while XL > 1 and YL > abs(y_step) and YL < (r.shape[1] - abs(y_step)):
		if r[XL][YL] == 255:
			XL -= x_step
			YL -= y_step
		else:
			break
	while XH < (r.shape[0] - 1) and YH > abs(y_step) and YH < (r.shape[1] - abs(y_step)):
		if r[XH][YH] == 255:
			XH += x_step
			YH += y_step
		else:
			break


	d1 = ((XL - i) ** 2 + (YL - j) ** 2) ** 1/2
	d2 = ((XH - i) ** 2 + (YH - j) ** 2) ** 1/2
	d1 = d1 ** 5
	d2 = d2 ** 5	
	return ((g[XL][YL].astype(float) * d1+ g[XH][YH].astype(float) * d2) // (d1 + d2)).astype(int)

def insert0(g, r, i, j):
	XL = XH = i

	while r[XL][j] == 255 and XL > 0:
		XL -= 1
	while r[XH][j] == 255 and XH < (r.shape[0]-1):
		XH += 1

	d1 = (i - XL) ** 5
	d2 = (XH - i) ** 5
	return ((g[XL][j].astype(float) * d1+ g[XH][j].astype(float) * d2) // (d1 + d2)).astype(int)

def insert45(g, r, i, j):
	XL = XH = i
	YL = YH = j

	while r[XL][YH] == 255 and XL > 0 and YH < (r.shape[1]-1):
		XL -= 1
		YH += 1
	while r[XH][YL] == 255 and XH < (r.shape[0]-1) and YL > 0:
		XH += 1
		YL -= 1

	d1 = (2 * (i - XL)) ** 5
	d2 = (2 * (XH - i)) ** 5
	return ((g[XL][YH].astype(float) * d1 + g[XH][YL].astype(float) * d2) // (d1 + d2)).astype(int)

def insert90(g, r, i, j):
	YL = YH = j

	while r[i][YL] == 255 and YL > 0:
		YL -= 1
	while r[i][YH] == 255 and (YH < r.shape[1] - 1):
		YH += 1

	d1 = (j - YL) ** 5
	d2 = (YH - j) ** 5
	return ((g[i][YL].astype(float) * d1 + g[i][YH].astype(float) * d2) // (d1 + d2)).astype(int)

def insert135(g, r, i, j):
	XL = XH = i
	YL = YH = j

	while r[XL][YL] == 255 and XL > 0 and YL > 0: 
		XL -= 1
		YL -= 1
	while r[XH][YH] == 255 and XH < (r.shape[0]-1) and YH < (r.shape[1]-1):
		XH += 1
		YH += 1

	d1 = (2 * (i - XL)) ** 5
	d2 = (2 * (XH - i)) ** 5
	return ((g[XL][YL].astype(float) * d1 + g[XH][YH].astype(float) * d2) // (d1 + d2)).astype(int)


def median(f, i, j, size=3):
	k = int(size/2)
	s = [[],[],[]]

	XL = max(0,i-k)
	XH = min(f.shape[0],i+k+1)
	YL = max(0,j-k)
	YH = min(f.shape[1],j+k+1)

	for i in range(XL,XH):
		for j in range(YL,YH):
			s[0].append(f[i][j][0])
			s[1].append(f[i][j][1])
			s[2].append(f[i][j][2])
	s[0].sort()
	s[1].sort()
	s[2].sort()
	r = np.zeros((3))
	r[0] = s[0][int((size**2-1)/2)]
	r[1] = s[1][int((size**2-1)/2)]
	r[2] = s[2][int((size**2-1)/2)]
	return r

def c_median(f, i, j, size=5):
	k = int(size/2)
	s = [[],[],[]]
	XL = max(0,i-k)
	XH = min(f.shape[0],i+k+1)
	YL = max(0,j-k)
	YH = min(f.shape[1],j+k+1)

	row = XL
	col = YL
	while row < XH:
		s[0].append(f[row][col][0])
		s[1].append(f[row][col][1])
		s[2].append(f[row][col][2])
		row += 1

	while col < YL:
		s[0].append(f[row][col][0])
		s[1].append(f[row][col][1])
		s[2].append(f[row][col][2])
		col += 1

	while row >= XL:
		s[0].append(f[row][col][0])
		s[1].append(f[row][col][1])
		s[2].append(f[row][col][2])
		row -= 1

	while col > YL:
		s[0].append(f[row][col][0])
		s[1].append(f[row][col][1])
		s[2].append(f[row][col][2])
		col -= 1

	s[0].sort()
	s[1].sort()
	s[2].sort()
	r = np.zeros((3))
	r[0] = s[0][len(s[0])//2]
	r[1] = s[1][len(s[1])//2]
	r[2] = s[2][len(s[2])//2]
	return r

def mean(f, i, j, size=3):
	k = int(size/2)
	r = np.zeros((3))
	r[0] = np.mean(f[i-k:i+k+1,j-k:j+k+1][0])
	r[1] = np.mean(f[i-k:i+k+1,j-k:j+k+1][1])
	r[2] = np.mean(f[i-k:i+k+1,j-k:j+k+1][2])
	return r.astype(int)

def c_mean(g, i, j, size = 5):
	f = g.astype(float)
	k = int(size/2)
	s = [[],[],[]]
	XL = max(0,i-k)
	XH = min(f.shape[0],i+k+1)
	YL = max(0,j-k)
	YH = min(f.shape[1],j+k+1)

	row = XL
	col = YL
	while row < XH:
		s[0].append(f[row][col][0])
		s[1].append(f[row][col][1])
		s[2].append(f[row][col][2])
		row += 1

	while col < YL:
		s[0].append(f[row][col][0])
		s[1].append(f[row][col][1])
		s[2].append(f[row][col][2])
		col += 1

	while row >= XL:
		s[0].append(f[row][col][0])
		s[1].append(f[row][col][1])
		s[2].append(f[row][col][2])
		row -= 1

	while col > YL:
		s[0].append(f[row][col][0])
		s[1].append(f[row][col][1])
		s[2].append(f[row][col][2])
		col -= 1

	r = np.zeros((3))
	r[0] = np.mean(s[0])
	r[1] = np.mean(s[1])
	r[2] = np.mean(s[2])

	return r.astype(int)


def equalize(f, r, i, j, size = 10):
	k = int(size/2)
	R,G,B = cv.split(f)
	R = np.mean(R)
	G = np.mean(G)
	B = np.mean(B)
	r_sum = sum(r)
	f0 = R / (R + G + B)
	f1 = G / (R + G + B)
	f2 = B / (R + G + B)
	r[0] = r_sum * f0
	r[1] = r_sum * f1
	r[2] = r_sum * f2

	return r
