from random import *
import numpy as np
from pylab import *


def bernoulli():
	#generates a Bernoulli random variable with parameter p = 0:75
	r = random()
	if r <= 0.75:
		#success case
		return 1
	else:
		#failure case
		return 0

def sequence(n):
	#generates a swquence of n elements
	TrialSequence = []

	for i in range(0,n):
		num = 0
		#Each random variable in the sequence is the sum of 10 independent Bernoulli random variables
		for j in range(0,10):
			#print(i)
			num = num + bernoulli()
		TrialSequence.append(num)
	return TrialSequence

NumberTrials = [100, 1000, 10000]

percent = []

TrialSequence = sequence(NumberTrials[2])


for OutcomeIndex in range(0, 11):
	percent.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials[0]))
print (percent)



plot(percent, 'o')
y = np.cumsum(percent)
plot(y,'r--')

show()
