import os
import os.path
from scipy.misc import imread, imsave, imresize
import numpy as np
import cv2

path_dir='/tmp/imagenet/malignant'
change='changed_'
file_list=os.listdir(path_dir)
	

for i in range(len(file_list)) :

	img = imread(file_list[i])

	img_tinted = img * [1, 0.95, 0.9]

	img_tinted = imresize(img_tinted, (300, 300))

	imsave('resized_image.png', img_tinted)

	img_color = cv2.imread( 'resized_image.png', cv2.IMREAD_COLOR )
	
	height, width, channel = img_color.shape
	img_gray = np.zeros( (height,width), np.uint8 )
	#print(height, width, channel)


	for y in range(0, height):
	    for x in range(0, width):
	        b = img_color.item(y,x,0)
	        g = img_color.item(y,x,1)
	        r = img_color.item(y,x,2)
	
	        gray = (int(b)+int(g)+int(r))/3.0
	
	        if gray>255:
	            gray=255
	
	        img_gray.itemset( y, x, gray)
	
	
	print (file_list[i], "changing complete")
	cv2.imwrite(change+file_list[i], img_gray )
	
	cv2.waitKey(0)
	cv2.destroyAllWindows()	
