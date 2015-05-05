# Chaance Graves
# ECEN 303
# Dr. Chamberland
# Python Challenge 3

import random 
import numpy as np


# Sum of S = X + Y
# M = max(X,Y)

NumberTrials = 100000
sequenceX = []
sequenceY = []
sequenceS = []
sequenceM = []

for TrialIndex in range(0, NumberTrials): 
	sequneceX.append(random.randint(1,6))
	sequneceX.append(random.randint(1,6))
	sequneceX.append(sequenceX[TrialIndex] + sequenceY[TrialIndex])
	sequneceX.append(max(sequenceX[TrialIndex], sequenceY[TrialIndex]))
	
	PMFofSM = np.zeros((13,7))
	
	for TrialIndex in range(0,NumberTrials):
		PMFofSM[sequenceS[TrialIndex], sequenceM[TrialIndex]] += 1
		
	PMFofSM /= float(NumberTrials)
	
for items in sequenceM:
			i+=1
			if items= 4: 
	PMFofM /
