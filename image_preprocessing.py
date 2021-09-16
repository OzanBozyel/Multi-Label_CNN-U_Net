# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 19:43:05 2021

@author: Ozan
"""

import pydicom
import numpy as np
import os
from glob import glob
import random
import sys
import cv2
from keras.utils import normalize


Sequances = ['AX FLAIR_longTR', 'FLAIR_reg', 'FLAIR', 'AX FLAIR', 'RAIN_STRYKER/FLAIR' ]

class Path_Loader_Label_Encoder:
    def __init__(self,path):
        self.path = path

    def main(self):
        
        dicom_file_path = glob(os.path.join(self.path,"*.dcm"))
        
        n = len(dicom_file_path)
        try:
            if n == 1:
                a = 0
            elif n != 1:
                a = random.randint(0, n)
   
            dc = pydicom.read_file(dicom_file_path[a])
        except (UnboundLocalError,IndexError):
            return print('There is not dicom file found in file path.')
        try:
            new_folder_name = 'Images'
            new_folder_path_dir = self.path
            new_folder_path = os.path.join(new_folder_path_dir, new_folder_name) 
            os.mkdir(new_folder_path) 
        except FileExistsError:
            pass
        
        try:
            Seq = dc.SeriesDescription
            Body = dc.BodyPartExamined
            if (list.count(Sequances, Seq) == 1):
                if (Body == 'BRAIN'):
                    pass
            else:
                print('Sequence or body part is wrong.')
                sys.exit()
        except AttributeError:
            return print('There is a lack of information in the file..')
        
        
        background = np.zeros((512,512,3),dtype= np.uint8)
        for i in range(n):
            dicom = pydicom.read_file(dicom_file_path[i])
            im = dicom.pixel_array
            image_resize = cv2.resize(im, None, fx=1, fy=1)
            rb, cb = background.shape[:2]
            rs, cs = image_resize.shape[:2]
            top = int((rb-rs)/2)
            bottom = int(rb - rs - top)
            left = int((cb-cs)/2)
            right = int(cb - cs - left)
            res = cv2.copyMakeBorder(image_resize, top, bottom,
                         left, right, cv2.BORDER_CONSTANT)
            
            resize_img = cv2.resize(res,(128,128), interpolation=cv2.INTER_AREA)
            np_zeros = np.zeros((512,512),dtype=np.uint8)
            norm_im = cv2.normalize(resize_img, np_zeros, 0, 255, cv2.NORM_MINMAX)
            Normalization_Path =  self.path + 'Images/file_' + str(i) + '.jpg'
            cv2.imwrite(Normalization_Path,norm_im)
            
            img = cv2.imread(Normalization_Path, 1)
            lab_img= cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
            x, y, z = cv2.split(lab_img)
            clahe = cv2.createCLAHE(clipLimit=0.002, tileGridSize=(8,8))
            clahe_img = clahe.apply(x)
            updated_lab_img2 = cv2.merge((clahe_img,y,z))
            CLAHE_img = cv2.cvtColor(updated_lab_img2, cv2.COLOR_LAB2BGR)
            CLAHE_Path = self.path + 'Images/file_' + str(i) + '.jpg'
            cv2.imwrite(CLAHE_Path, CLAHE_img)
            
        
        images = []
        for i in range(n):
            prediction_image_path = self.path + 'Images/file_' + str(i) + '.jpg'
            prediction_image = cv2.imread(prediction_image_path, 0)
            prediction_image_normalize = np.expand_dims(normalize(prediction_image, axis=1),2)
            prediction_image_end = np.expand_dims(prediction_image_normalize, 0)
            images.append(prediction_image_end)
            
        prediction_images = np.array(images)

        return prediction_images
   




