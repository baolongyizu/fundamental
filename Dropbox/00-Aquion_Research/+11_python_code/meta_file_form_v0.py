import os
import csv
import pandas as pd

# direct the folder to the HC folder structure
os.chdir(r"C:\Test Data\_formatted data\R&D\HC")


cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in '%s': %s" % (cwd, files)) # output the file location and file names
print(files)

doe_general = {} # dictionary to store all the data structures

for does in files:
    path = r'C:\Test Data\_formatted data\R&D\HC' + '\\' + does # iteration through all folders in the sub folder
    os.chdir(path)
    does_cwd = os.getcwd()
    doe_files = os.listdir(does_cwd)  # Get all the files in that directory

    print("Files in '%s': %s" % (does_cwd, doe_files))
    print(doe_files)
    for csv_names in doe_files:
        if 'csv' in csv_names:
            doe_general[does] = pd.read_csv(csv_names)
            doe_general[does]['DoE'] = does # read all the summary file document into the panda data frame

os.chdir(r"C:\Test Data\_DoE Summary")

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in '%s'doe_general[does] for does in doe_general.keys(): %s" % (cwd, files))
print(files)

doe_comb = pd.concat([doe_general[does] for does in doe_general.keys()])
print(doe_comb)
doe_comb.to_csv('_doe_inter_summary.csv')
