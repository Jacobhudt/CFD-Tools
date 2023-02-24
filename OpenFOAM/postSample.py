import os
import numpy as np
import shutil
import argparse

""" Script for postprocessing sampled outlet data, and moving it to the correct directory for
	the timeVaryingMappedFixedValue boundary condition in OpenFOAM.
"""
project = os.path.abspath(os.getcwd())
new = os.listdir(project + "/postProcessing/sampleDict")
new.sort()

start = float(new[0])
end = float(new[-1])
dt = float(new[1]) - float(new[0])

os.rename(project + "/postProcessing/sampleDict/" + new[0] + '/interface/faceCentres', 'points')

directory = project + "/postProcessing/sampleDict/" 

for i in np.arange(start, end, dt):

	float(i)
	j = round(i, 7)
	if (j - int(j) == 0):
		j = int(j)
	
	sourceU = directory + f'{j}/interface/vectorField/U'
	destinationU =  directory + f'{j}/U'
	sourceNUT = directory + f'{j}/interface/scalarField/nut'
	destinationNUT = directory + f'{j}/nut'

	os.rename(sourceU, destinationU)
	os.rename(sourceNUT, destinationNUT)
	shutil.rmtree(directory + f'{j}/interface')
	
shutil.move(directory, project + "/constant/boundaryData/Inlet")
