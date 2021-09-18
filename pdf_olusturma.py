# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 13:12:36 2021

@author: Ozan
"""
from reportlab.pdfbase.pdfmetrics import stringWidth

from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas
import time
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image

canvas = canvas.Canvas("form.pdf", pagesize=A4)

canvas.setLineWidth(.3)

canvas.line(25,665,572,665)
canvas.line(25,20,572,20)
canvas.line(25,665,25,20)
canvas.line(572,665,572,20)



canvas.setFont('Times-Roman', 8)

canvas.drawImage('C:/Users/Ozan/Desktop/univlogo.jpg',45,730,width=90,height=90)

canvas.line(25,690,572,690) #dikdörtgen al çizgi
canvas.line(25,820,572,820) #dikdörtgen üst çizgi

canvas.line(25,820,25,690)#sol çizgi
canvas.line(572,690,572,820)#sağ çizgi

canvas.line(160,820,160,690)#resmi ortalayan çizgi




canvas.line(25,730, 160,730)

canvas.drawString(85,720,'T.C.')
canvas.drawString(53,710,'INONU UNIVERSITESI')
canvas.drawString(35,700,'BIYOMEDIKAL MUHENDISLIGI')



canvas.setFont('Times-Roman', 12)
canvas.drawString(300,755,'RADYOLOJI RAPORU')






canvas.setFont('Times-Roman', 15)

canvas.drawString(47,635,'Hasta Bilgisi')
canvas.line(25,630,160,630)
canvas.line(160,665,160,20)



canvas.setFont('Times-Roman', 9)
canvas.drawString(30,610,'Adi Soyadi:')
kk = 'Ozan Bozyel12345'
canvas.drawString(75,610,'Ozan Bozyel')


canvas.drawString(30,595,'T.C. :')
canvas.drawString(55,595,'11111111111')



canvas.setFont('Times-Roman', 10)
canvas.drawString(30,580,'Yas:')
canvas.drawString(50,580,'20')




canvas.drawString(30,565,'Cinsiyet:')
canvas.drawString(70,565,'Erkek')



canvas.drawString(30,550,'Kilo:')
canvas.drawString(55,550,'75')

import time
formatted_time = time.ctime()
ptext = '%s' % formatted_time

canvas.drawString(30,535,'Tarih:')
canvas.drawString(55,535,ptext)



canvas.drawString(30,520,'Toplam Beyin Hacmi:')
canvas.drawString(120,520,'2300m3')

canvas.drawString(30,505,'Toplam Tümör Hacmi:')
canvas.drawString(125,505,'2300m3')

canvas.line(25,485,160,485)





canvas.drawImage('C:/Users/Ozan/Desktop/file_13.jpg',165,260,width=400,height=400)

canvas.line(160,250,572,250)





canvas.drawString(450,150,'Radyoloji Uzmani')
canvas.setFont('Times-Roman', 8)
canvas.drawString(470,140,'(..../..../......)')

canvas.drawString(480,130,'imza')


canvas.save()