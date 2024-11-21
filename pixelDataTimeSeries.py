import sys
from osgeo import gdal
import numpy
import os
import csv
from csv import writer
#the following imports were derived from the example code
import pandas
import matplotlib as mpl
import matplotlib.pyplot as plt

#define main if necessary?

latitude = 114.6784901 #West
longitude = 32.5346909 #North

#ideally, you would open the CSV here and just write to it with every iteration of the for loop

storageArray = [] #storage for pixeldata
storageArrayIndex = 0

#iterate through the directory, opening the specified files and extracting the data to storageArray
for filename in os.listdir('C:\pyBAITSSS_Testing\nldas\yuma2019\p038r037\2019'):
    if filename[0:16] == "ET_veg_2019_09230":
        dataset = gdal.Open(filename)
        if dataset is None:
            print("Failed to open File")
        else:
            #define image dimensions
            imgWidth = dataset.RasterXSize()
            imgHeight = dataset.RasterYSize()
            bands = dataset.RasterCount() #(not really sure why I need this)

            #the following two blocks of code should be done outside the loop
            #Geotransform 
            transformCoefficients = dataset.GetGeoTransform() #gets coefficients
            xOrigin = transformCoefficients[0]                #extracts coefficients (not necessary)
            yOrigin = transformCoefficients[3]
            pixelWidth = transformCoefficients[1]
            pixelHeight = transformCoefficients[5]
            #rowRotation = transformCoefficients[2] #this and colRotation are usually 0, hence they were ommitted 
            #colRotation = transformCoefficients[4]
            #Use calcWorldtoPixel() instead?

            xPixel = (latitude  - xOrigin)/pixelWidth    
            yPixel = (longitude - yOrigin)/pixelHeight
            #xPixel = (latitude - rowRotation*(Y_line) - xOrigin)/pixelWidth (for if rowRotation wasn't 0) #what is yLine?

            #TO DO: Get data from xPixel and yPixel
            pixelData = 0 #placeholder

            #put pixelData in storageArray
            storageArray[storageArrayIndex] = pixelData
            storageArrayIndex += 1 #storageArray++


#make csv to write to and write to the csv
with open('ET_veg_2019_data', 'w', newline='') as csvfile: #modified the with statement?
    writerObj = csv.writer(csvfile, delimiter=" ", quotechar='|', quoting=csv.QUOTE_MINIMAL) #creates a wrtier object? it appears to be similar to an output buffer
    #can I reference the writer outside of the with statement? check this later

    #write pixelData to the CSV
    storageArrayIterator = 0
    while storageArrayIterator < storageArrayIndex:
        writerObj.writerow(storageArray[storageArrayIterator]) 
        storageArrayIterator += 1

    #TO DO: Ensure that the csv data is properly written 


#create the graph, reading the data from the csv (might actually just be better to read the data from the array in this implementation)

#the following code was modified from "Example code.py"
mpl.rcParams['figure.dpi'] = 1700
mpl.rcParams['axes.linewidth'] = 0.1
title_font =0.7
title_y = 0.53
markersize = 0.05
ma_tick_len = 0.7
mi_tick_len = 0.5
width_ticks = 0.1
fontsize_letter = 1.4
line_1_1 = 0.1
alpha = 1
grid_li_width = 0.05
labelpad = 0.5
pad = 0.5
line_t_series = 0.14
line_t_se_mean = 0.3
linewidth=0.15

plt.rcParams["font.family"] = "Times New Roman"

params = {'legend.fontsize':1.5,
      'axes.labelsize': 1.5,
      'axes.titlesize': 1.5,
      'xtick.labelsize' :1.5,
      'ytick.labelsize' :1.5,
      'mathtext.fontset': 'cm',
      'mathtext.rm': 'serif', 
      "xtick.bottom" : True,
      "ytick.left" : True,
      }

mpl.rcParams.update(params)
            
#TO DO: Finish graph creation