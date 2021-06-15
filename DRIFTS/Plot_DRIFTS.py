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

##Get files set up
path = os.getcwd()
def getcsv(path):
    csvfile =[]
    csvfilename = []
    for file in [doc for doc in os.listdir(path) if doc.endswith('.CSV')]:
        csvfile.append(file)
        csvfilename.append(file.replace(".CSV",""))
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
            plt.plot(x, -y-pos, label=csvfilename[pos])
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
plt.xlim(4000,1000)
#plt.ylim(4000,1500)
plt.yticks([])
plt.xlabel('Wavenumber (cm^-1)')
plt.ylabel('Transmittance (a.u.)')
plt.title('DRIFTS')
plt.show()

