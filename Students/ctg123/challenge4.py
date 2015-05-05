# Chaance Graves
# ECEN 303
# Dr. Chamberland
# Python Challenge 4

import random

NumberTrials = 1000 
sequenceX = []
sequenceY = []
sequenceZ = []


for TrialIndex in range(0, NumberTrials):
	sequenceX.append(random.randint(1,6))
	if sequenceX[TrialIndex] == 1 or sequenceX[TrialIndex] == 3 or sequenceX[TrialIndex] == 5:
		sequenceY.append(random.randint(1,6))
	else:
		sequenceY.append(0)
	sequenceZ.append(sequenceX[TrialIndex] + sequence[TrialIndex])
	
	# Look at the empirical distribution of Z
	
	percent = []
	for OutcomeIndex in range(2, 12):
		percent.append(sequenceZ.count(OutcomeIndex) / float(NumberTrials))
	print ("The program has calulated the probability value to be:")
	print '\n' # new line
	print (percent) # program result
	
	# The total probability of Z is Pr(Z=4) -> 2/9. Below is to show how the program perfroms according to the number of trials specified above. 
	print(" The hand calculated value is 2/9 = 0.2222...")
	
