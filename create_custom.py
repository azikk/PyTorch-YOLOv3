import os
import shutil
import random

TXT_PATH = './data/custom/train.txt'
VAL_TXT = './data/custom/valid.txt'
IMAGE_PATH = './data/custom/images/'
LABEL_PATH = './data/custom/labels/'

def add_img_to_custom_txt():
	labels = os.listdir('/home/BP9/image/2w3_label_voc/')
	imagenames = os.listdir(IMAGE_PATH)

	f = open(TXT_PATH,'w')
	for label_name in labels:
		if label_name.split('.')[0] + '.jpg' in imagenames:
			f.write(IMAGE_PATH+label_name.split('.')[0]+'.jpg\n')


def nfromm(m, n, unique=True): # 0 to m , pick n
    """
    :param m:
    :param n:
    :param unique:
    :return:
    """
    if unique:
        box = [i for i in range(m)]
        out = []
        for i in range(n):
            index = random.randint(0, m - i - 1)
            out.append(box[index])
            box[index], box[m - i - 1] = box[m - i - 1], box[index]
        return out
    else:
        out = []
        for _ in range(n):
            out.append(random.randint(0, m - 1))
        return out

def choice_some_to_val():
	filenames = os.listdir(IMAGE_PATH)
	val_list = nfromm(len(filenames)-1, 80)
	val_img_path = '/home/BP9/winner/PyTorch-YOLOv3/data/custom/image_val/'

	train_txt = open(TXT_PATH, 'w')
	val_txt = open(VAL_TXT, 'w')

	for filename in filenames:
		if filenames.index(filename) in val_list:
			shutil.copyfile(IMAGE_PATH + filename, val_img_path + filename)
			val_txt.write('data/custom/images/'+filename+'\n')
			print(filename)
		else:
			train_txt.write('data/custom/images/'+filename+'\n')
	#print(1)


def move_image():
	filenames = os.listdir(LABEL_PATH)
	path1 = '/home/BP9/image/212Imglabel/'
	for filename in filenames:
		img = filename.split('.')[0] + '.jpg'
		shutil.copyfile(path1 + img, IMAGE_PATH + img)

def change_voc_label_to_coco():
	filenames = os.listdir('/home/BP9/image/2w3_label_voc/')
	save_path = '/home/BP9/image/2w3_label_coco/'

	for filename in filenames:
		fo = open('/home/BP9/image/2w3_label_voc/' + filename, 'r')
		f = open(save_path + filename, 'w')

		done = 0
		while not done:
			line = fo.readline()
			if (line != ''):
				alist = line.split(' ')
				f.write('0 {} {} {} {}\n'.format(alist[1], alist[2], alist[3], alist[4]))
			else:
				done = 1
		fo.close()
		f.close()


def temp():
	filenames = os.listdir('/home/BP9/image/2/2_img/')
	save_path = '/home/BP9/winner/PyTorch-YOLOv3/data/samples/'
	random_list = nfromm(len(filenames)-1, 100)
	for i in random_list:
		shutil.copyfile('/home/BP9/image/2/2_img/'+filenames[i], save_path +filenames[i])

#add_img_to_custom_txt()
#choice_some_to_val()

#move_image()
#temp()
change_voc_label_to_coco()