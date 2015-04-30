
import random

NumberTrials = 10000
SequenceX = []
SequenceY = []
SequenceZ = []
percent = []

for TrialIndex in range(0, NumberTrials):
    SequenceX.append(random.randint(1,6))
    if SequenceX[TrialIndex] == 1 or SequenceX[TrialIndex] == 3 or SequenceX[TrialIndex] == 5:
        SequenceY.append(random.randint(1,6))
    else:
        SequenceY.append(random.randint(0,0))
    SequenceZ.append(SequenceX[TrialIndex] + SequenceY[TrialIndex])

for OutcomeIndex in range(2,12):
    percent.append(SequenceZ.count(OutcomeIndex)/float(NumberTrials))
print(percent) 