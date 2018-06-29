import os
import os.path
from scipy.misc import imread, imsave, imresize
import numpy as np
import cv2
import json
import shutil

dir_path='/tmp/imagenet/melanoma'
benign_jpg_dir='/tmp/imagenet/melanoma/benign/jpg'
benign_json_dir='/tmp/imagenet/melanoma/benign/json'
malignant_jpg_dir='/tmp/imagenet/melanoma/malignant/jpg'
malignant_json_dir='/tmp/imagenet/melanoma/malignant/json'
change='changed_'

benign_jpgfile_list=os.listdir(benign_jpg_dir)
benign_jpgfile_list.sort()
benign_jsonfile_list=os.listdir(benign_json_dir)
benign_jsonfile_list.sort()
malignant_jpgfile_list=os.listdir(malignant_jpg_dir)
malignant_jpgfile_list.sort()
malignant_jsonfile_list=os.listdir(malignant_json_dir)
malignant_jsonfile_list.sort()


if not os.path.isdir('/tmp/imagenet/melanoma/benign/changed'):
	os.mkdir('/tmp/imagenet/melanoma/benign/changed')
if not os.path.isdir('/tmp/imagenet/melanoma/malignant/changed'):
	os.mkdir('/tmp/imagenet/melanoma/malignant/changed')


for i in range(len(benign_jpgfile_list)) :

	with open(benign_json_dir+'/'+benign_jsonfile_list[i]) as data_file: 
    		data = json.load(data_file)
	
	pixelX = data["meta"]["acquisition"]["pixelsX"]
	pixelY = data["meta"]["acquisition"]["pixelsY"]

	img = imread(benign_jpg_dir+'/'+benign_jpgfile_list[i])
	img_tinted = img * [1, 0.95, 0.9]

	img_tinted = imresize(img_tinted, (300, int(300*(pixelX/pixelY))))

	imsave('resized_image.png', img_tinted)

	img_color = cv2.imread( 'resized_image.png', cv2.IMREAD_COLOR )
	
	height, width, channel = img_color.shape
	img_gray = np.zeros( (height,width), np.uint8 )	
	
	for y in range(0, height):
	    for x in range(0, width):
	        b = img_color.item(y,x,0)
	        g = img_color.item(y,x,1)
	        r = img_color.item(y,x,2)
	
	        gray = (int(b)+int(g)+int(r))/3.0
	
	        if gray>255:
	            gray=255
	
	        img_gray.itemset( y, x, gray)	
	
	print (benign_jpgfile_list[i], "changing complete")

	cv2.imwrite(change+benign_jpgfile_list[i], img_gray)
	shutil.move(dir_path+'/'+change+benign_jpgfile_list[i], dir_path+'/benign/changed')
	
	
	cv2.waitKey(0)
	cv2.destroyAllWindows()	


for i in range(len(malignant_jpgfile_list)) :

	with open(malignant_json_dir+'/'+malignant_jsonfile_list[i]) as data_file: 
    		data = json.load(data_file)
	
	pixelX = data["meta"]["acquisition"]["pixelsX"]
	pixelY = data["meta"]["acquisition"]["pixelsY"]

	img = imread(malignant_jpg_dir+'/'+malignant_jpgfile_list[i])
	img_tinted = img * [1, 0.95, 0.9]

	img_tinted = imresize(img_tinted, (300, int(300*(pixelX/pixelY))))

	imsave('resized_image.png', img_tinted)

	img_color = cv2.imread( 'resized_image.png', cv2.IMREAD_COLOR )
	
	height, width, channel = img_color.shape
	img_gray = np.zeros( (height,width), np.uint8 )	
	
	for y in range(0, height):
	    for x in range(0, width):
	        b = img_color.item(y,x,0)
	        g = img_color.item(y,x,1)
	        r = img_color.item(y,x,2)
	
	        gray = (int(b)+int(g)+int(r))/3.0
	
	        if gray>255:
	            gray=255
	
	        img_gray.itemset( y, x, gray)	
	
	print (malignant_jpgfile_list[i], "changing complete")

	cv2.imwrite(change+malignant_jpgfile_list[i], img_gray)
	shutil.move(dir_path+'/'+change+malignant_jpgfile_list[i], dir_path+'/malignant/changed')
	
	
	cv2.waitKey(0)
	cv2.destroyAllWindows()	
