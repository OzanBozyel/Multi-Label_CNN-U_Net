"""
@author: Ozan
"""
import cv2
import numpy as np
import pandas as pd
import settings
from matplotlib import pyplot as plt

class Volume_Calculation:
    def __init__(self,
                 orjinal_images_array,
                 mask_array,
                 volume,
                 paths,
                 print_report = settings.REPORT ):
        self.orjinal_images = orjinal_images_array
        self.mask = mask_array
        self.volume = volume
        self.report = print_report
        self.path = paths
        
    def Calculation(self):
        df = pd.DataFrame(columns=['Original_Image','Tumor_Mask','Total_Tumor_Volume'])
        
        Original_Image = []
        Tumor_Mask = []
        Total_Tumor_Volume = []
        
        t_volume = 0
        b_volume = 0
        for i in range(self.mask.shape[0]):
            p_mask = self.mask[i]
            Original_Image.append(self.orjinal_images[i])
            
            tumor_number = round((len(p_mask[p_mask==4])*self.volume*16*0.001))
            brain_number = round((len(p_mask[p_mask==3])*self.volume*16*0.001))
            
            Total_Tumor_Volume.append(tumor_number)
               
            tumor_mask = (p_mask==4)*1
            Tumor_Mask.append(tumor_mask)
            
            t_volume = t_volume + tumor_number
            b_volume = b_volume + brain_number
        

        df['Original_Image'] = Original_Image
        df['Tumor_Mask'] = Tumor_Mask
        df['Total_Tumor_Volume'] = Total_Tumor_Volume
        
            
        Sort = df.sort_values(by = ['Total_Tumor_Volume'], ascending = [False])
        
        image = Sort.iloc[0][0]
        path_1 = self.path + 'Images/res.jpg'
        cv2.imwrite(path_1,image)
        res_img = cv2.imread(path_1,0)
        t_mask = Sort.iloc[0][1]
        brain_vol = b_volume + t_volume
        
        
        if self.report:
            bitmap_preds = np.squeeze((t_mask > 0.98).astype(np.uint8) *30)
            beta = (1-0.5)
            alpha = 0.5
            dst = cv2.addWeighted(res_img,alpha, bitmap_preds, beta, 0 )
            res_path =self.path + 'Images/result.png'
            plt.imsave(res_path,dst)
            return t_volume,brain_vol
        else:
            print('Total tumor volume: ',t_volume)
            print('Total brain volume: ',brain_vol)
            pass
