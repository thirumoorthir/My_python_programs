#!/usr/bin/python:
# -*- coding: utf-8 -*-
#this program is to download image from an url with different name on every day
import facebook
import time,os
img_date= time.strftime("%d%m")#This line outputs date format as DDMM,we want this on our code to wget image files from the URL
year=time.strftime("%Y")#this line outputs year Value
url= "http://srirangaminfo.com/cal/"+year+"/"+img_date+".jpg"# here we are using sring concatination so that we can add two strings

newfile = "C:\\Users\\\\Documents\\Python_study\\"+"image.jpg"#creating new file location as a variable
os.remove(newfile)

import wget
wget.download(url)#using Wget we are downloading pic from that page mentioned in url variable 
oldfile = "C:\\Users\\\\Documents\\Python_study"+"\\"+img_date+".jpg"#creating old file location as an variable

try:
  os.rename(oldfile,newfile)
except:
  print (" Seams like file already downloaded")
