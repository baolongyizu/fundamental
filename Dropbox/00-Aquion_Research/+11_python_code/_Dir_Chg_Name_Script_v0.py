import glob, os
from os import listdir
from os.path import isfile, join
import string
import csv
import os
import re
DOEs = ['100']

temp = ['700C','750C','800C','820C','780C','760C']
duration =['Tim11','Tim8']
sprayDrylocation = ['Chamber','CYCLONE','CHAMBER', 'Cyclone','SD']
iteration = ['1']
scanratesum = ['P5MV','P33MV']
device = ['HC']
#
#
#
#
filepath = r"C:\Users\wwu\Desktop\Python_Data\+11_Add_String\Data"
onlyfiles = [f for f in listdir(filepath) if isfile(join(filepath, f))]

print(onlyfiles)

def rename(dir, pattern, titlePattern):
    for pathAndFilename in glob.iglob(os.path.join(dir, pattern)):
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))
        print(title)
        print(ext)
        title_key = title.split('_')
        print(title_key)
        
        print(sort(title_key))
        
        os.rename(pathAndFilename, 
                  os.path.join(dir, titlePattern % sort(title_key) + ext))
                  
def sort(title_key):
    
    mass = ''
    doe = ''
    sn = ''
    dev = ''
    dep = ''
    dura = ''
    temperature =''
    rpflag = 0
    itr = ''
    for item in title_key:
        if 'mg' in item:
            mass = item.upper()
        elif 'MG' in item:
            mass = item
        sn = title_key[1]
        for keys in DOEs:
            if keys in item:
                doe = keys

        
        
        for keys in device:
            if keys in item:
                dev = item

                
        for keys in duration:
            if keys in item:
                if keys == 'Tim8':
                    dura = '8HR'
                elif keys == 'Tim11':
                    dura = '11HR'

        for keys in scanratesum:
            if keys in item:
                scanrate = keys



        for keys in iteration:
            if keys in item:
                itr = keys

    print(sn)
    full_name = doe+'_'+sn + '_RND_'+dev +'_' + itr +'_CV_BH01_STP_FILM_PTFE_TUBE_P1_1_800C_' + dura +'_'+mass+'_80P_'+ scanrate +'_TOPAZ_'
    return full_name


rename(r'C:\Users\wwu\Desktop\Python_Data\+11_Add_String\Data', r'*.mpt', r'%s')
rename(r'C:\Users\wwu\Desktop\Python_Data\+11_Add_String\Data', r'*.txt', r'%s')