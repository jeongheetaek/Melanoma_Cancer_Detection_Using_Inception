import os
import os.path
import shutil
import json

dir_path='/tmp/imagenet/melanoma'

if not os.path.isdir('/tmp/imagenet/melanoma/benign'):
	os.mkdir('/tmp/imagenet/melanoma/benign')
if not os.path.isdir('/tmp/imagenet/melanoma/malignant'):
	os.mkdir('/tmp/imagenet/melanoma/malignant')

if not os.path.isdir('/tmp/imagenet/melanoma/benign/jpg'):
	os.mkdir('/tmp/imagenet/melanoma/benign/jpg')
if not os.path.isdir('/tmp/imagenet/melanoma/benign/json'):
	os.mkdir('/tmp/imagenet/melanoma/benign/json')
if not os.path.isdir('/tmp/imagenet/melanoma/malignant/jpg'):
	os.mkdir('/tmp/imagenet/melanoma/malignant/jpg')
if not os.path.isdir('/tmp/imagenet/melanoma/malignant/json'):
	os.mkdir('/tmp/imagenet/melanoma/malignant/json')


file_list=os.listdir(dir_path)
file_list.sort()

for i in range(len(file_list)) :
	filepath = dir_path+'/'+file_list[i]
	filepath2 = dir_path+'/'+file_list[i-1]

	ext=os.path.splitext(file_list[i])[-1]
	if ext == '.json' :
		with open(filepath) as data_file: 
    			data = json.load(data_file)
		if data["meta"]["clinical"]["benign_malignant"] == "benign" : 
			shutil.move(filepath, dir_path+'/benign/json')
			shutil.move(filepath2, dir_path+'/benign/jpg')
		if data["meta"]["clinical"]["benign_malignant"] == "malignant" : 
			shutil.move(filepath, dir_path+'/malignant/json')
			shutil.move(filepath2, dir_path+'/malignant/jpg')
		print ("file moving...")

print ("complete file moving!")


	
