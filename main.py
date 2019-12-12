import loaddata
import Method
import Detect

if __name__ == '__main__':
	input_dir = input('--input_dir:')
	output_dir = input('--output_dir:')
	datas = loaddata.Dataset(input_dir)
	datas.creat_outdir(output_dir)


	SIZE = 5
	for i in range(datas.getlen()):
		print(datas.getname(i))
		img = datas.getitem(i)
		r = Detect.search(img)
		img1 = img.copy()
		img2 = img.copy()
		for row in range(5,img.shape[0]-5):
			for col in range(5,img.shape[1]-5):
				if r[row][col] == 255:
					img1[row][col] = Method.canny1(img, r, row, col)
					img1[row][col] = Method.equalize(img,img1[row][col],row,col)
				else:
					img1[row][col] = img[row][col]

		for row in range(5,img.shape[0]-5):
			for col in range(5,img.shape[1]-5):
				if r[row][col] == 255:
					#img2[row][col] = Method.canny(img1, r, row, col)
					img2[row][col] = Method.c_mean(img1, row, col, SIZE)
					img2[row][col] = Method.equalize(img1,img2[row][col],row,col)
				else:
		 			img2[row][col] = img1[row][col]
		# for row in range(3,img.shape[0]-3):
		#   	for col in range(3,img.shape[1]-3):
		#   		img2[row][col] = Method.mean(img1, row, col, SIZE)

		datas.writeitem(Detect.double2uint8(img2),i)
		#print('PSNR:',PSNR(img2,img))
		#print('SSIM:',SSIM(img2,img))

