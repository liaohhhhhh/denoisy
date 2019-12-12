import loaddata
from PSNR import PSNR
from SSIM import SSIM

if __name__ == '__main__':
	tfilename = input('--target_dir:')
	ofilename = input('--output_dir:')

	target_data = loaddata.Dataset(tfilename)
	output_data = loaddata.Dataset(ofilename)

	result = open('result.xls','w')
	result.write('Name\tPSNR\tSSIM\n')

	for i in range(1):#target_data.getlen()):
		output_img = output_data.getitem(i)
		target_img = target_data.getitem(i)
		name = target_data.getname(i)
		print("NAME:",name)
		psnr = PSNR(output_img,target_img)
		print("PSNR:",psnr)
		ssim = SSIM(output_img,target_img)
		print("SSIM:",ssim)
		result.write(name + '\t' + str(psnr) + '\t' + str(ssim) + '\n')

	result.close()