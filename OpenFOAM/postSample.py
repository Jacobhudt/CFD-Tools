import os
import numpy as np
import shutil
import argparse

""" Script for postprocessing sampled outlet data, and moving it to the correct directory for
    the timeVaryingMappedFixedValue boundary condition in OpenFOAM. Make sure to run it in the
    top level of the case directory.
"""

new = os.listdir(os.path.abspath(os.getcwd()) + "/postProcessing/sampleDict")
new.sort()

start = float(new[0])
end = float(new[-1])
dt = float(new[1]) - float(new[0])

os.rename("/postProcessing/sampleDict/" + new[0] + '/interface/faceCentres', 'points')

for i in np.arange(start, end, dt):

	float(i)
	j = round(i, 7)
	if (j - int(j) == 0):
		j = int(j)
	
	sourceU = "/postProcessing/sampleDict/" + f'{j}/interface/vectorField/U'
	destinationU =  "/postProcessing/sampleDict/" + f'{j}/U'
	sourceNUT = "/postProcessing/sampleDict/" + f'{j}/interface/scalarField/nut'
	destinationNUT = "/postProcessing/sampleDict/" + f'{j}/nut'

	os.rename(sourceU, destinationU)
	os.rename(sourceNUT, destinationNUT)
	shutil.rmtree("/postProcessing/sampleDict/" + f'{j}/interface')
	
shutil.move("/postProcessing/sampleDict", "/constant/boundaryData/inlet")

