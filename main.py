# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 20:13:03 2021

@author: Ozan
"""
from processor import procedure
import model
from prediction import Prediction




a = procedure(path ='C:/Users/Ozan/Desktop/ID_001/')
 
b = a.general_processor()




# a = model.U_NET()
# a = a.model(IMG_HEIGHT=128, IMG_WIDTH=128, IMG_CHANNELS=1,n_classes=5)  


kk = Prediction(b).Predict()












