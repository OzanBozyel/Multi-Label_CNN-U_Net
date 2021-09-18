# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 18:27:20 2021

@author: Ozan
"""
import settings
from model import MODEL
from keras.models import load_model
import numpy as np

class Prediction:
    def __init__(self,images,
                 h5_file_path = settings.H5_FILE_PATH_UNET):
        self.images = images
        self.h5_file_path = h5_file_path

    def Predict(self):
        prediction_all_images = []
        pre_model = MODEL().U_NET()
        pre_model = load_model(self.h5_file_path)
        for i in range(self.images.shape[0]):
            img_prediction = pre_model.predict(self.images[i])
            predicted_img = np.argmax(img_prediction,axis=3)[0,:,:]
            prediction_all_images.append(predicted_img)
        prediction_all_images = np.array(prediction_all_images)
            
        return prediction_all_images 
        

        
        



















