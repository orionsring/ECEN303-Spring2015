# Name: Minda Wei
# GitHub ID: @minda-wei
# ECEN 303, Chamberland Spring 2015
# Python Challenge 4

import random

# Instantiate variables for the arrays of X Y Z
sequenceX = []
sequenceY = []
sequenceZ = []
NumberTrials = 10000
expectedPMF = [.1944, 0.0278, 0.2222, 0.0556, 0.2500, 0.0833, 0.0556, 0.0556, 0.0278, 0.0278]

# Calculating experimental PMF of Z=X+Y
for TrialIndex in range (0, NumberTrials):
    sequenceX.append(random.randint(1, 6))

    if sequenceX[TrialIndex] % 2 != 0:
        sequenceY.append(random.randint(1, 6))
    else:
        sequenceY.append(0)

    sequenceZ.append(sequenceX[TrialIndex] + sequenceY[TrialIndex])

# Calculating percent error between experimental and expected
percent = []
percenterror = []
for OutcomeIndex in range(2, 12):
    percent.append(sequenceZ.count(OutcomeIndex)/float(NumberTrials))

percenterror = (percent[2]-expectedPMF[2])/expectedPMF[2]*100

# Outputs
print("Experimental: " + str(percent))
print("Expected:     " + str(expectedPMF))
print("\nPercent Error of Z=4: " + str(percenterror) + "%")

"""
Hand-calculations (Combos | Pr)

1:  DNE                         Pr(1) = 0
2:  (2,X) (1,1)                 Pr(2) = 7/36
3:  (1,2)                       Pr(3) = 1/36
4:  (4,X) (1,3) (3,1)           Pr(4) = 8/36
5:  (1,4) (3,2)                 Pr(5) = 2/36
6:  (6,X) (1,5) (3,2) (5,1)     Pr(6) = 9/36
7:  (1,6) (3,4) (5,2)           Pr(7) = 3/36
8:  (3,5) (5,3)                 Pr(8) = 2/36
9:  (3,6) (5,4)                 Pr(9) = 2/36
10: (5,5)                       Pr(10) = 1/36
11: (5,6)                       Pr(11) = 1/36
12: DNE                         Pr(12) = 0
"""
