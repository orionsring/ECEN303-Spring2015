import random

SampleSpaceSize = 2
NumberTrials = 10000

TrialSequence = []
for TrialIndex in range(0, NumberTrials):
	TrialSequence.append(random.randrange(SampleSpaceSize))

percent = []
for OutcomeIndex in range(0, SampleSpaceSize):
	percent.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))
print(percent)