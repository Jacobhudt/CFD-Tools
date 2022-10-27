#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script for plotting pressure gradient from the output of OpenFOAM.
!!x-axis is not accurate!!
!!the gradient gets printet out on avg 3 times per timestep,
   depending on the setup. !!
   
Only meant as a simple visual interperter.

"""
import numpy as np
import matplotlib.pyplot as plt
import re
import argparse

parser = argparse.ArgumentParser(description='Read output file from OpenFOAM (logfile)')
parser.add_argument("file_name", type=str,  help='logfile name')
args = parser.parse_args()

log = open(args.file_name, 'r')
log_text = log.read()
log.close()


match = re.findall(r"pressure gradient = (0.\d+)", log_text)
match = match[::3000]

grad_p = [float(x) for x in match]
time = range(0,len(grad_p))


plt.plot(time,grad_p)


plt.title(f'mean of grad(p) during a stable period = {round(np.mean(grad_p[-100:]),6)}')
plt.xlabel('timestep')
plt.ylabel('pressure gradient')
plt.show()
print(np.mean(grad_p[-100:]))