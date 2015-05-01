import random

NumberTrials = 1000
sequenceX=[]
sequenceY=[]
sequenceZ=[]

for TrialIndex in range(0, NumberTrials):
	sequenceX.append(random.randint(1,6))
	if sequenceX[TrialIndex] == 1 or sequenceX[TrialIndex] == 3 or sequenceX[TrialIndex} == 5:
		sequenceY.append(random.randint(1,6))
	else:
		sequenceY.append(0)
	sequenceZ.append(sequenceX[TrialIndex} + sequenceY[TrialIndex])
precent = []
for OutcomeIndex in range(2, 12):
	percent.append(sequenceZ.count(OutcomeIndex) / float(NumberTrials))
print(precent)
#By hand using total probability, Pr(Z=4) is 2/9. the empirical result is more accurate the more trials preformed