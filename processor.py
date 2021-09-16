# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 19:47:20 2021

@author: Ozan
"""
from image_preprocessing import Path_Loader_Label_Encoder
import numpy as np

class procedure:
    def __init__(self,path,formats=None):
        self.path = path
        self.formats = formats
        
    def general_processor(self):
        first_processing = Path_Loader_Label_Encoder(self.path).main()
        

        return first_processing
        
        
    
    














































