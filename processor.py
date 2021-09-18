# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 19:47:20 2021

@author: Ozan
"""
from image_preprocessing import Path_Loader_Label_Encoder
import numpy as np
from prediction import Prediction
from Volume_Cal import Volume_Calculation
import settings
from pdf_creating import PDF
from Outcome import Outcome



class procedure:
    def __init__(self,path,formats=None):
        self.path = path
        self.formats = formats
        
    def general_processor(self):
        orj_img,pre_img,patient,vol = Path_Loader_Label_Encoder(self.path).main()
        
        pred = Prediction(images=pre_img).Predict()
        
        calculation = Volume_Calculation(orjinal_images_array=orj_img, mask_array=pred, volume=vol).Calculation()
        
        if settings.REPORT:
            cal_vol = [calculation[2],calculation[3]]
            pdf_cre = PDF(patient_info=patient,volums=cal_vol,path=self.path).Report()
        else:
            pass
        
        ending = Outcome(pred, self.path)
        
        pass
        
        
    
    














































