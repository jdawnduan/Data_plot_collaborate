#-------------------------------------------------------------------------------
# Name:        UVvisplot
# Purpose:     plot UV-vis data
#
# Author:      KillingPhysics_DawnDuan
#
# Created:     27/06/2020
# Updated:     06/29/2020
# Copyright:   (c) KillingPhysics_DawnDuan 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import csv
import os
#plt.style.use('seaborn-pastel')
def removeheader(filenames):
    for a in range(len(filenames)):
        with open(filenames[a], 'r') as fin:
            text = fin.readlines()[43:]
            with open("r"+filenames[a], 'w+') as f:
                for line in range(len(text)):
                    f.write(text[line])
    return()

##Get files set up
path = os.getcwd()
def getcsv(path):
    csvfile =[]
    csvfilename = []
    for file in [doc for doc in os.listdir(path) if doc.endswith('.txt')]:
        csvfile.append(file)
        csvfilename.append(file.replace(".txt",""))
    return(csvfile, csvfilename)

csvfile = getcsv(path)[0]
csvfilename = getcsv(path)[1]
rownum = 0
pos=0
while True:
    try:
        for i in csvfile:
            x, y = np.loadtxt(i, delimiter=',', skiprows = rownum, unpack=True)
            #plt.plot(x, y)
            plt.plot(x, y, label=csvfilename[pos])
            print(pos)
            pos += 1
            print("plot")
        break
    except:
        rownum +=1
        print(rownum)
        continue

current_handles, current_labels = plt.gca().get_legend_handles_labels()
#reversed_handles = list(reversed(current_handles))
#reversed_labels = list(reversed(current_labels))
#plt.legend(reversed_handles, reversed_labels)
plt.legend(current_handles, current_labels)
plt.xlim(350,470)
#plt.ylim(0,0.3)
plt.yticks([])
plt.xlabel('Wavelength (nm)')
plt.ylabel('Abs (a.u.)')
plt.title('UV-Vis')
plt.show()

