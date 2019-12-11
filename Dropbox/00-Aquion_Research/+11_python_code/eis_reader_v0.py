import string
import csv
#import matplotlib.pyplot as plt
import os
import re

from os import listdir
from os.path import isfile, join

path = r"C:\Users\wwu\Desktop\Play_ground\eis_reader"

os.chdir(path)

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in '%s': %s" % (cwd, files))



onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]

if 'eis.csv' in files:
    files.remove('eis.csv')

WORDLIST_FILENAME= files

print(WORDLIST_FILENAME)

def load():  # load data sets
    wordList = {}
    inFile = {}
    for item in WORDLIST_FILENAME:
        print(item)
        inFile[item] = open(item, 'r')
        wordList[item] = inFile[item].readlines()
        print("  ", len(wordList[item]), "words loaded.")
    return wordList


def reducelines():  # reduce the lines from header
    newList = {}
    for item in WORDLIST_FILENAME:
        f = load()[item]
        redNum = f[1].split(' ')
        listnum = ''
        for i in redNum:
            if i.isdigit():
                listnum = i
                newList[item] = f[int(listnum) - 1:]
    return newList

n= reducelines()
print(type(n))

with open("./%s" % ('eis.csv'),'w', newline='') as csvfile:
    eiswriter = csv.writer(csvfile, delimiter ="," , quoting=csv.QUOTE_MINIMAL)
    i=0
    for keys in n:
        list_write = n[keys][0].split('\t')
        list_write.append('serial id')
        list_write.append('iteration')
        eiswriter.writerow(list_write)
        i=i+1
        if i>0:
            break
            
    for keys in n:
        for i in range(1,len(n[keys])):
            list_data = n[keys][i].split('\t')
            list_data.append(keys[0:10])
            list_data.append(keys[14])
            eiswriter.writerow(list_data)
            

