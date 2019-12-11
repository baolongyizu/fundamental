import csv

from matplotlib import pyplot as plt
import os
import re
import pandas as pd
from os import listdir
from os.path import isfile, join

os.chdir(r"C:\Users\wwu\Desktop\Play_ground")

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in '%s': %s" % (cwd, files))

file_summary = pd.read_csv(r'C:\Users\wwu\Desktop\Play_ground\DoE_102_HCSummary.csv')

cal_record = pd.read_csv(r"C:\Users\wwu\Desktop\Play_ground\09_Calcination Record.csv")
half_cell = pd.read_csv(r'C:\Users\wwu\Desktop\Play_ground\16_Half Cell Test.csv')
cal_test = pd.read_csv(r"C:\Users\wwu\Desktop\Play_ground\10_Calicination Test.csv")
cal_merge = pd.merge(cal_test, cal_record, how='left', on=None, left_on='calcination id', right_on='calcination id',
                     left_index=False, right_index=False, sort=True,
                     suffixes=('_x', '_y'), copy=True, indicator=False,
                     validate=None)
doe102_hcsummary = pd.read_csv(r"C:\Users\wwu\Desktop\Play_ground\DoE_102_HCSummary.csv")

# print(cal_record.head())
# print(cal_test.head())
print(doe102_hcsummary.head())
cal_merge.to_csv('cal_merge.csv', encoding='utf-8', index=False)

# print(half_cell.head())
merge_file = pd.merge(half_cell, cal_merge, how='left', on = None, left_on = 'calcination id', right_on =
 'calcination id', left_index=False, right_index=False, sort=True, suffixes=('_x', '_y'), copy=True,
 indicator=False,validate=None)

print(merge_file.head())

merge_file.to_csv('merge_file_hc_ct.csv', encoding='utf-8', index=False)

meta_merge_file = pd.merge(doe102_hcsummary, merge_file, how='left', on = None, left_on = 'Serial Number', right_on =
 'serial number', left_index=False, right_index=False, sort=True, suffixes=('_x', '_y'), copy=True,
 indicator=False,validate=None)

meta_merge_file.to_csv('meta_merge_file.csv', encoding='utf-8', index = False)
# plt.plot(file['Cycle Number'],file['Discharge Specific Capacity_(mAh/g)'], marker = 'o')
# plt.plot(file['Cycle Number'],file['Discharge Specific Capacity_(mAh/g)'], marker = '+')
# plt.show()
