# Chaance Graves
# ECEN 303
# Dr. Chamberland
# Python Challenge 3

import random 
import numpy as np


# Sum of S = X + Y
# M = max(X,Y)

NumberTrials = 100000 # you can choose how many you want to run
# All arrays are initialized and correspond to it's respective random variable.
sequenceX = []
sequenceY = []
sequenceS = []
sequenceM = []

for TrialIndex in range(0, NumberTrials): 
	sequneceX.append(random.randint(1,6)) #
	sequneceX.append(random.randint(1,6))
	sequneceX.append(sequenceX[TrialIndex] + sequenceY[TrialIndex]) #This is S = X + Y
	sequneceX.append(max(sequenceX[TrialIndex], sequenceY[TrialIndex])) # M = max(X,Y)
	
	PMFofSM = np.zeros((13,7))										# produces a matrix for 0
	
	for TrialIndex in range(0,NumberTrials):
		PMFofSM[sequenceS[TrialIndex], sequenceM[TrialIndex]] += 1
		
	PMFofSM /= float(NumberTrials)
	
	PMFofM = np.zeros(12)

	for TrialIndex in range(0,NumberTrials):
		PMFofM[sequenceM[TrialIndex]] += 1
		
	PMFofM /= float(NumberTrials)
	
	PMFofM = np.zeros((13,7))

	for TrialIndex in range(0,NumberTrials): # conditional pmf states the for S given M = pmf of SM/(pmf of m)
		PMFofSgivenM[sequenceS[TrialIndex], sequenceM[TrialIndex]] = [[PMFofSM[sequenceS[TrialIndex], sequenceM[TrialIndex]]] / PMFofM[sequenceM[TrialIndex]]
		
	PMFofSgivenM /= float(NumberTrials)

# show results
print PMFofSM
print PMFofM
print PMFofSgivenM
