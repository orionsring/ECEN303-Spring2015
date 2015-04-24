import random

SampleSpaceSize = 2 # bits can only take 2 values: 0 or 1.
NumberTrials = 10000 # change to 10,100,1000,10000,etc...

TrialSequence = [] # first column
for TrialIndex in range(0, NumberTrials):
    TrialSequence.append(random.randrange(SampleSpaceSize))

    # Then, look at the empirical distribution of the ratios of zeros and ones.

    percent = [] # second column 
    for OutcomeIndex in range(0, SampleSpaceSize):
        percent.append(TrialSequence.count(OutcomeIndex)/ float(NumberTrials))
    print(percent)

    # Explore how the empirical distribution changes as N increases 10.0, 100.0, 1000.0, 10000.0
