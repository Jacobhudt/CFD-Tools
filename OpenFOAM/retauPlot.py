"""
Tool for plotting and calculating the average Re_tau based on the 
pressuregradient from the momentumsource in a pipe.

"""

import os
import numpy as np
import linecache
import re
import matplotlib.pyplot as plt

time_temp = os.listdir(os.path.abspath(os.getcwd()))

D = 0.1 #diameter

L = 1 #length

time = []

for fold in time_temp:
    if fold.isnumeric():
        if not int(fold)==0:
            time.append(int(fold))
        
time.sort()
retau=[]

for s in time:
    data = re.findall("[+-]?\d+\.\d+",linecache.getline(f'{s}/uniform/momentumSourceProperties',19))
    retau.append(np.sqrt(float(data[0])*D/((4*L)))*D/2/(1.5e-05))
    
avg = round(sum(retau)/len(time),2)

plt.plot(time,retau)

plt.ylabel(f"Re_tau, avg = {avg}")
plt.xlabel("time[s]")

print(f'Average Re_tau over {time[-1]-time[0]} seconds = {avg}')

plt.show()