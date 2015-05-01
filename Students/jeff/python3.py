import random 
import numpy as np 

NumberTrials = 10001

sequenceX = []

sequenceY = []

sequenceS = []

sequenceM = []
Mvalue=[]
s=01
for TrialIndex in range(0, NumberTrials):

	sequenceX.append(random.randint(1, 6))

	sequenceY.append(random.randint(1, 6))

	sequenceS.append(sequenceX[TrialIndex] + sequenceY[TrialIndex])

	sequenceM.append(max(sequenceX[TrialIndex], sequenceY[TrialIndex]))

PMFofSM = np.zeros((13, 7))

for TrialIndex in range(0, NumberTrials):

	PMFofSM[sequenceS[TrialIndex], sequenceM[TrialIndex]] += 1

	PMFofSM /= float(NumberTrials)

"""print PMFofSM"""

for item in sequenceM:
	s+=1
	if item==3:
		Mvalue.append(sequenceS[s])
		if s==NumberTrials-1:
			s=0
	elif s==NumberTrials-1:
		s=0
SgivenM=np.zeros(12)
for value in Mvalue:
	for s in range(2,12):
		if value is s:
			SgivenM[s]+=1
for number in SgivenM:
	print(number/float(len(Mvalue)))