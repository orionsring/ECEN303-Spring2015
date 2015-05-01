import random
import numpy as np
import matplotlib.pyplot as plt
import pylab as pl
from decimal import *
NumberTrials = 1000
sequenceX = []
sequenceY = []
sequenceS = []
sequenceM = []
Mis4=[]
i=0
for TrialIndex in range(0, NumberTrials):
	sequenceX.append(random.randint(1,6))
	sequenceY.append(random.randint(1,6))
	sequenceS.append(sequenceX[TrialIndex] + sequenceY[TrialIndex])
	sequenceM.append(max(sequenceX[TrialIndex], sequenceY[TrialIndex]))

PMFofSM = np.zeros((13,7))

for TrialIndex in range(0, NumberTrials):
	PMFofSM[sequenceS[TrialIndex], sequenceM[TrialIndex]] += 1

	PMFofSM /= float(NumberTrials)
for item in sequenceM:
	i+=1
	if item==4:
		Mis4.append(sequenceS[i])
		if i==NumberTrials-1:
			i=0
	elif i==NumberTrials-1:
		i=0
PMFofSgM=[0]*12
for value in Mis4:
	for i in range(2,12):
		if value is i:
			PMFofSgM[i] += 1
for number in PMFofSgM:
	print(number/float(len(Mis4)))
#the distribution looks like a uniform distribution