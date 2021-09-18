# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 19:17:25 2021

@author: Ozan
"""

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import time
import settings

class PDF:
    def __init__(self,
                 patient_info,
                 volums,
                 path,
                 logo=settings.LOGO):
        self.patient_info = patient_info
        self.path = path
        self.logo = logo
        self.volums = volums
    
    def Report(self):
        name = self.patient_info[0]
        tc = self.patient_info[1]
        age = self.patient_info[2]
        sex = self.patient_info[3]
        weight = self.patient_info[4]
        
        b_vol = self.volums[0] + 'cm3'
        t_vol = self.volums[1] + 'cm3'
        
        pdf_path = self.path + 'Radyoloji_Raporu.pdf'
        pdf = canvas.Canvas(pdf_path, pagesize=A4)
        
        pdf.setLineWidth(.3)
        pdf.line(25,665,572,665)
        pdf.line(25,20,572,20)
        pdf.line(25,665,25,20)
        pdf.line(572,665,572,20)
        pdf.setFont('Times-Roman', 8)
        pdf.drawImage(self.logo,45,730,width=90,height=90)
        pdf.line(25,690,572,690) 
        pdf.line(25,820,572,820)
        pdf.line(25,820,25,690)
        pdf.line(572,690,572,820)
        pdf.line(160,820,160,690)
        pdf.line(25,730, 160,730)

        pdf.drawString(85,720,'T.C.')
        pdf.drawString(53,710,'INONU UNIVERSITESI')
        pdf.drawString(35,700,'BIYOMEDIKAL MUHENDISLIGI')

        pdf.setFont('Times-Roman', 12)
        pdf.drawString(300,755,'RADYOLOJI RAPORU')
        
        pdf.setFont('Times-Roman', 15)

        pdf.drawString(47,635,'Hasta Bilgisi')
        pdf.line(25,630,160,630)
        pdf.line(160,665,160,20)
        
        pdf.setFont('Times-Roman', 10)
        pdf.drawString(30,610,'Adi Soyadi:')
        pdf.drawString(80,610,name)
        
        pdf.drawString(30,595,'T.C. :')
        pdf.drawString(55,595,tc)
        
        pdf.drawString(30,580,'Yas:')
        pdf.drawString(50,580,age)

        pdf.drawString(30,565,'Cinsiyet:')
        pdf.drawString(70,565,sex)

        pdf.drawString(30,550,'Kilo:')
        pdf.drawString(55,550,weight)
        
        formatted_time = time.ctime()
        Times = '%s' % formatted_time

        pdf.drawString(30,535,'Tarih:')
        pdf.drawString(55,535,Times)
        
        pdf.drawString(30,520,'Toplam Beyin Hacmi:')
        pdf.drawString(120,520,b_vol)

        pdf.drawString(30,505,'Toplam Tümör Hacmi:')
        pdf.drawString(125,505,t_vol)
        pdf.line(25,485,160,485)
        pdf.drawString(450,150,'Radyoloji Uzmani')
        pdf.setFont('Times-Roman', 8)
        pdf.drawString(470,140,'(..../..../......)')
        pdf.drawString(480,130,'imza')
        
        im_path = self.path + 'Images/result.png'
        pdf.drawImage(im_path,165,260,width=400,height=400)

        pdf.line(160,250,572,250)

        return pdf.save()
        
        
        























