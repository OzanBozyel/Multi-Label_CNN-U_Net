# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 18:00:29 2021

@author: Ozan
"""

import cv2
import numpy as np
from PIL import Image
import settings
import os
from skimage import io
import sys

class Outcome:
    def __init__(self,
                 images,
                 path,
                 formats=settings.OUTPUT_FORMAT):
        self.images = images
        self.formats = formats
        self.output_path = path
        
    def Prediction_Outcome(self):
        if (self.formats == '.jpg'):
            for i in range(self.images.shape[0]):
                img = self.images[i] *30
                img_path = self.output_path + 'kk/Results_' + str(i) + self.formats
                cv2.imwrite(img_path,img)
        elif (self.formats == '.jpeg'):
            for i in range(self.images.shape[0]):
                img = self.images[i] *30
                img_path = self.output_path + 'kk/Results_' + str(i) + self.formats
                cv2.imwrite(img_path,img)    
        elif (self.formats == '.png'):
            for i in range(self.images.shape[0]):
                img = self.images[i] *30
                img_path = self.output_path + 'kk/Results_' + str(i) + self.formats
                cv2.imwrite(img_path,img)
        elif (self.formats == '.tif'):
            print('ozan')
            img_path = self.output_path + 'ozan' + self.formats
            io.imsave(img_path, self.images)
        return  print('The guessing process is over. Please check the results from the file path.')
        






























