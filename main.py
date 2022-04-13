# import os
import pandas as pd
import numpy as np
import h5py
from scipy.fftpack import fft, fftshift

import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams.update({'font.size': 20, 'text.usetex': True})

file = h5py.File("data.hdf", "r")
x =  file['XXX'][:]
# Y-variables
Y = file['YYY'][:] 
DFF = []   # dummies empty array
filesave=open('text.txt','w') # open a file 
filesave.write(" this is text generated header\n")
filesave.close()
for i in range(1000):
    """
    do your calculation here and create data array
    
    """
    New_array= np.array([])
    filesave=open('text.txt','a')
    filesave.write(str(New_array))
    filesave.write('\n')
    filesave.close()
    DFF.append(New_array)
