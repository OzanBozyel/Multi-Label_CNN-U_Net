"""
@author:  Ozan Bozyel 
"""
from processor import procedure

# Hastanının DICOM dosyalarının olduğu klasörün yolunu giriniz.
path = ''
predict = procedure(path).general_processor()