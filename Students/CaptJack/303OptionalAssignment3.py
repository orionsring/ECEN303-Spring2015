# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 13:55:20 2015

@author: CaptainKyle
"""
#My guess as to what the structure of the conditional PMF of S given M will 
#look like is something like all zeros except for a diagonal from top left
#to bottom right whose width thickens as it decends. Source: I just did the HW

import random 
import numpy as np
# if you don't have this, get it. it's fun and easy to use.
#https://pypi.python.org/pypi/colorama
from colorama import Fore, Back, Style

#basic set up stuff
NumberTrials = 10000
Die1 = []
Die2 = []
Sum = []
Max = []
Indextesting=[[0 for x in range(10)]for x in range(10)] #now i have my empty matrix
Indextesting[1][5]=1

#rolling the die and filling the matricies
for TrialIndex in range (0,NumberTrials):
    Die1.append(random.randint(1,6))
    Die2.append(random.randint(1,6))
    Sum.append(Die1[TrialIndex]+Die2[TrialIndex])
    Max.append(max(Die1[TrialIndex], Die2[TrialIndex]))

#setting up the PMFs
PMFofSM = np.zeros((13,7))    
PMFofM = np.zeros(13)
PMFofS = np.zeros(13)
PMFofSGM = np.zeros((13,7))

#getting the joint PMF and the PMF of the max number
for TrialIndex in range(0, NumberTrials):
    PMFofSM[Sum[TrialIndex], Max[TrialIndex]]+=1
    PMFofM[Max[TrialIndex]] += 1 #not needed but for fun

#turning into probability
PMFofSM /= float(NumberTrials)
PMFofM /= float(NumberTrials)

#getting the conditional PMF
for i in range (1,7):
    columnprobsum=0
    for j in range (1,13):
        columnprobsum += PMFofSM[j][i]
    for k in range (1,13):
        PMFofSGM [k][i]= PMFofSM[k][i]/columnprobsum

#print matrix function will not work with a different sized matrix. 
#was too lazy
#color=fun. yay!
def printMatrix(testMatrix):
    for i in range (0,13):
        for j in range(0,7):
            if j==6:
                if testMatrix[i][j]==0:
                    print(Style.BRIGHT+ Fore.RED + "%2f" % (testMatrix[i][j]))
                elif testMatrix[i][j] >0 and testMatrix[i][j] < .2:
                    print(Style.BRIGHT+Fore.MAGENTA + "%2f" % (testMatrix[i][j]))
                elif testMatrix[i][j] > .2 and testMatrix[i][j] < .4:
                    print(Style.BRIGHT+Fore.BLUE + "%2f" % (testMatrix[i][j]))
                elif testMatrix[i][j] > .4 and testMatrix[i][j] < .6:
                    print(Style.BRIGHT+Fore.CYAN + "%2f" % (testMatrix[i][j]))
                elif testMatrix[i][j] > .6 and testMatrix[i][j] < .8:
                    print(Style.BRIGHT+ Fore.GREEN + "%2f" % (testMatrix[i][j]))
                elif testMatrix[i][j] > .8 and testMatrix[i][j] <= 1:
                    print(Style.BRIGHT+Fore.BLACK + "%2f" % (testMatrix[i][j]))
            else:
                if testMatrix[i][j]==0:
                    print(Style.BRIGHT+Fore.RED + "%2f" % (testMatrix[i][j]), end =" ")
                elif testMatrix[i][j] > 0 and testMatrix[i][j] < .2:
                    print(Style.BRIGHT+Fore.MAGENTA + "%2f" % (testMatrix[i][j]), end =" ")
                elif testMatrix[i][j] > .2 and testMatrix[i][j] < .4:
                    print(Style.BRIGHT+Fore.BLUE + "%2f" % (testMatrix[i][j]), end =" ")
                elif testMatrix[i][j] > .4 and testMatrix[i][j] < .6:
                    print(Style.BRIGHT+Fore.CYAN + "%2f" % (testMatrix[i][j]), end =" ")
                elif testMatrix[i][j] > .6 and testMatrix[i][j] < .8:
                    print(Style.BRIGHT+Fore.GREEN + "%2f" % (testMatrix[i][j]), end =" ")
                elif testMatrix[i][j] > .8 and testMatrix[i][j] <= 1:
                    print(Style.BRIGHT+Fore.BLACK + "%2f" % (testMatrix[i][j]), end =" ")
            
printMatrix(PMFofSGM)
