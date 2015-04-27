import random
import matplotlib.pyplot as plot

NumberTrials = 10000
sequenceX = []
sequenceY = []
sequenceZ = []

for TrialIndex in range(0, NumberTrials):
	sequenceX.append(random.randint(1,6))
	if sequenceX[TrialIndex]==1 or sequenceX[TrialIndex]==3 or sequenceX[TrialIndex]==5:
		sequenceY.append(random.randint(1,6))
	else:
		sequenceY.append(0)
	sequenceZ.append(sequenceX[TrialIndex]+sequenceY[TrialIndex])

percent = []
for OutcomeIndex in range(2,12):
	percent.append(sequenceZ.count(OutcomeIndex) / float(NumberTrials))
print(percent);plot.plot(percent);plot.show() #display and plot
# by hand, Pr(4) = 8/36 = 2/9 = 0.2222. As N increases, it converges to this value.
