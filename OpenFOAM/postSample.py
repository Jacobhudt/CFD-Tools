import os
import numpy as np
import shutil
import argparse

new = os.listdir(os.path.abspath(os.getcwd()) + "/sampleDict")
new.sort()

start = float(new[0])
end = float(new[-1])
dt = float(new[1]) - float(new[0])

os.rename("sampleDict/" + new[0] + '/interface/faceCentres', 'points')

for i in np.arange(start, end, dt):

	float(i)
	j = round(i, 7)
	if (j - int(j) == 0):
		j = int(j)
	
	sourceU = "sampleDict/" + f'{j}/interface/vectorField/U'
	destinationU =  "sampleDict/" + f'{j}/U'
	sourceNUT = "sampleDict/" + f'{j}/interface/scalarField/nut'
	destinationNUT = "sampleDict/" + f'{j}/nut'

	os.rename(sourceU, destinationU)
	os.rename(sourceNUT, destinationNUT)
	shutil.rmtree("sampleDict/" + f'{j}/interface')
	
os.rename("sampleDict", "inlet")
