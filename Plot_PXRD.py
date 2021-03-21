#-------------------------------------------------------------------------------
# Name:        PXRDplot
# Purpose:     plot pxrd data (normalized) from xyd or csv file if you put them
#              and this code within the same folder
#
# Author:      KillingPhysics_DawnDuan
#
# Created:     28/06/2020
# Updated:     06/29/2020
# Copyright:   (c) KillingPhysics_DawnDuan 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import csv
import re
import os
import sys
import string
import time
start_time = time.time()
path = os.getcwd()
def convertxydtocsv(xydfilenames):
    for a in range(len(xydfilenames)):
        with open(xydfilenames[a], 'r') as f:
          plaintext = f.read()
        x = []
        y = []
        csvf = []
        plaintext = plaintext.split()
        i = 0
        n = 0
        with open(xydfilenames[a].replace(".xyd",".csv"),'w+') as csvf:
           while True:
                if i in range(len(plaintext)-1):
                    x.append(plaintext[i])
                    y.append(plaintext[i+1])
                    csvf.write(x[n]+","+y[n]+"\n")
                    n = n+1
                    i = i+2
                else:
                    break

def getcsv(path):
    xydfile = []
    csvfile =[]
    xydfilename = []
    csvfilename = []
    for file in [doc for doc in os.listdir(path) if doc.endswith('.xyd')]:
        xydfile.append(file)
        xydfilename.append(file.replace(".xyd",""))
    for file in [doc for doc in os.listdir(path) if doc.endswith('.csv')]:
        csvfile.append(file)
        csvfilename.append(file.replace(".csv",""))
    needconvert = set(xydfilename)-set(csvfilename)
    newfiles = [x + ".xyd" for x in needconvert]
    convertxydtocsv(newfiles)
    csvfile =[]
    csvfilename = []
    for file in [doc for doc in os.listdir(path) if doc.endswith('.csv')]:
        csvfile.append(file)
        csvfilename.append(file.replace(".csv",""))
    return(csvfile, csvfilename)
csvfile = getcsv(path)[0]
csvfilename = getcsv(path)[1]
#print(csvfile)
offsetmag = float(input("How much (%) do you want to offset?"))/100
offset = 0
print("loaded for plot")
pos=0
for i in csvfile:
    x, y = np.loadtxt(i, delimiter=',', unpack=True)
    newy = (y-min(y))/(max(y)-min(y))
    plt.plot(x, newy+offset, label=csvfilename[pos])
    pos += 1
    offset += float(offsetmag)

current_handles, current_labels = plt.gca().get_legend_handles_labels()
reversed_handles = list(reversed(current_handles))
reversed_labels = list(reversed(current_labels))
plt.legend(reversed_handles, reversed_labels)
plt.xlim(1,20)
plt.xticks(np.arange(1, 20, 2.0))
plt.yticks([])
plt.xlabel('Cu Kα 2θ (degree)')
plt.ylabel('Intensity (a.u.)')
plt.title('PXRD')
plt.show()
