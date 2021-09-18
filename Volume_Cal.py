# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 16:12:48 2021

@author: Ozan
"""
import cv2
import numpy as np
import pandas as pd
import settings

class Volume_Calculation:
    def __init__(self,
                 orjinal_images_array,
                 mask_array,
                 volume,
                 print_report = settings.REPORT ):
        self.orjinal_images = orjinal_images_array
        self.mask = mask_array
        self.volume = volume
        self.report = print_report
        
        
    def Calculation(self):
        df = pd.DataFrame(columns=['Original_Image','Tumor_Mask','Total_Tumor_Volume','Total_Brain_Volume'])
        
        Original_Image = []
        Tumor_Mask = []
        Total_Tumor_Volume = []
        Total_Brain_Volume = []
        t_volume = 0
        b_volume = 0
        for i in range(self.mask.shape[0]):
            p_mask = self.mask[i]
            Original_Image.append(self.orjinal_images[i])
            tumor_number = round((len(p_mask[p_mask==120])*self.volume*16*0.001))
            brain_number = round((len(p_mask[p_mask==30])*self.volume*16*0.001))
            
            Total_Tumor_Volume.append(tumor_number)
            
            brain_volume = brain_number + tumor_number
            Total_Brain_Volume.append(brain_volume)
            
            tumor_mask = (p_mask==120)*1
            Tumor_Mask.append(tumor_mask)
            
            t_volume = t_volume + tumor_number
            b_volume = b_volume + brain_volume 
            
        df['Original_Image'] = Original_Image
        df['Tumor_Mask'] = Tumor_Mask
        df['Total_Tumor_Volume'] = Total_Tumor_Volume
        df['Total_Brain_Volume'] = Total_Brain_Volume
            
        Sort = df.sort_values(by = ['Total_Tumor_Volume'], ascending = [False])
        
        image = Sort.iloc[0][0]
        t_mask = Sort.iloc[0][1]
        brain_vol = b_volume + t_volume
        if self.report:
            return image,t_mask,t_volume,brain_vol
        else:
            print('Total tumor volume: ',t_volume)
            print('Total brain volume: ',brain_vol)
            pass
        
            
            
            
        









































