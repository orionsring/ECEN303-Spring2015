#Name: Everett Harrell
#ECEN 303
#Python Challenge 3

import random
import numpy as np

NumberTrials = 10000	#Number of Trials in simulation
sequenceX = []			#Die X RV
sequenceY = []			#Die Y RV
sequenceS = []			#Random Variable S = sum of X and Y
sequenceM = []			#RV M = max of X and Y

for TrialIndex in range(0, NumberTrials):
    sequenceX.append(random.randint(1, 6))	#roll of first die for X
    sequenceY.append(random.randint(1, 6))	#roll of second die for Y
    sequenceS.append(sequenceX[TrialIndex] + sequenceY[TrialIndex])	#sum of X and Y
    sequenceM.append(max(sequenceX[TrialIndex], sequenceY[TrialIndex]))	#max of X and Y

PMFofSM = np.zeros((13,7)) #intialize the PMF of S&M to zero everywhere

for TrialIndex in range(0, NumberTrials):
    PMFofSM[sequenceS[TrialIndex], sequenceM[TrialIndex]] += 1 #increment the array by 1 
    														   #at the proper S and M
    														   
PMFofSM /= float(NumberTrials)	#normalize the distribution

PMFofM = np.zeros((7,1))	#intialize the PMF of M to zero everywhere

for TrialIndex in range(0, NumberTrials):
	PMFofM[sequenceM[TrialIndex]] += 1	#increment the array by 1 
    								    #at the proper M

PMFofM /= float(NumberTrials)	#normalize the distribution

PMFofSgM = np.zeros((13,7))	#intialize the PMF of S given M to zero everywhere

#PMF of SgM = PMF of SM / PMF of M
#Have to divide component by component...
#This section divides each value of the PMFofSM by the corresponding PMFofM

for TrialIndex in range(0, NumberTrials):
	PMFofSgM[sequenceS[TrialIndex], sequenceM[TrialIndex]] = \
		PMFofSM[sequenceS[TrialIndex], sequenceM[TrialIndex]] \
		/PMFofM[sequenceM[TrialIndex]]

print PMFofSM
print PMFofM
print PMFofSgM

#As N increases, the values start to represent the actual values calculated by hand
#You can expect a distibution that begins to spread out more as M increases because
#as the max increases, the different numbers of sums increases as well.