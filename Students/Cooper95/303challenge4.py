import random

NumberTrials = 1000000
sequenceX = []
sequenceY = []
sequenceZ = []

for TrialIndex in range(0, NumberTrials):
	sequenceX.append(random.randint(1,6))
	if sequenceX[TrialIndex]%2 == 1:					#if X is Odd, roll again
		sequenceY.append(random.randint(1,6))
	else:
		sequenceY.append(0)						#else add 0
	sequenceZ.append(sequenceX[TrialIndex]+sequenceY[TrialIndex])

percent = []

for OutcomeIndex in range(2,12):
	percent.append(sequenceZ.count(OutcomeIndex) / float(NumberTrials))	#percentage of outcomes
print(percent)

#By hand using total probability, Pr(Z=4)=2/9. the empirical result gets closer with more trials
