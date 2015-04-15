import random
import numpy as np

NumberTrials = 100000
sequenceX = []
sequenceY = []
sequenceS = []
sequenceM = []

for TrialIndex in range(0, NumberTrials):
	sequenceX.append(random.randint(1,6))					#X and Y are discrete RV between 1 and 6
	sequenceY.append(random.randint(1,6))
	sequenceS.append(sequenceX[TrialIndex] + sequenceY[TrialIndex])		#S = X + Y
	sequenceM.append(max(sequenceX[TrialIndex], sequenceY[TrialIndex]))	#M is the max of X and Y

PMFofSM = np.zeros((13,7))							#13x7 matrix of zeros (sum can be 0 to 12, max can be 6)

for TrialIndex in range(0, NumberTrials):
	PMFofSM[sequenceS[TrialIndex], sequenceM[TrialIndex]] += 1		#increment those values

PMFofSM /= float(NumberTrials)

np.set_printoptions(precision=4)
print("Joint PMF:")
print(PMFofSM)

#code for empirical distribution of S given M
#PMFofSM / PMFofM, where PMFofM = sum over all S of PMFofSM
PMFofM = [0]*7
for s in range(0,13):
	for m in range(0,7):
		PMFofM[m] += PMFofSM[s,m]
print("PMF of M:")
print(PMFofM)
PMFofSgM = np.zeros((13,7))
for s in range(0,13):
	for m in range(0,7):
		if(PMFofM[m] != 0):
			PMFofSgM[s,m] = PMFofSM[s,m] / PMFofM[m]
print("PMF of S given M:")
print(PMFofSgM)
#The PMF of S given M is zero when S <= M and S > 2M, Pr(S=2M|M) = 1/(1+2(M-1)) and Pr(M<S<2M|M) = 2/(1+2(M-1))
