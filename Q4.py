# -*- coding: utf-8 -*-
import os
import glob

data_path = "C:\\Users\\ACER\\Desktop\\Test_system\\data"
data_files = glob.glob(data_path +'\\*.log')

SN   = []
date = []

for data_file in data_files:
    filename = os.path.basename(data_file)
    (file, ext) = os.path.splitext(filename)
    split = file.split("_")

    SN = split[0]
    
    same_files = glob.glob(data_path +'\\'+ SN +'*.log')
    same_file = sorted(same_files)
    for i in same_file[0:-1]:
        os.remove(i)
        
   
