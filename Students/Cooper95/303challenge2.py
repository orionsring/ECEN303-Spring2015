import random
import matplotlib
import matplotlib.pyplot as plt

SampleSpaceSize = 11
NumberBernoullis = 10
NumberTrials = 10000

TrialSequence = []
for TrialIndex in range(0, NumberTrials):
    #make sum
    sum = 0
    for BernoulliIndex in range(0, NumberBernoullis):
        #create Bernoulli RV with p = .75
        if random.randrange(100) < 75:
            sum += 1
    TrialSequence.append(sum)

percent = []
for OutcomeIndex in range(0, SampleSpaceSize):
	percent.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))
print(percent)

plt.plot(percent)
plt.show()
