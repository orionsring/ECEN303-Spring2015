# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 10:22:17 2015

@author: CaptainKyle
"""

from random import randrange
#from pylab import *
import matplotlib.pyplot as plt

#playing with random variables
#pcount =0
#qcount=0
#p=0
#n=10000
#for x in range(0,n):
#    irand = randrange(0,n)
#    if irand <= (.75*n):
#        pcount=pcount+1
#    else:
#        qcount=qcount+1
#p=pcount/n     
#print(p)
#
n=100000
p=.75
matrix=[[0 for x in range(10)]for x in range(n)] #now i have my empty matrix
sumMatrix=[0 for x in range(n)] #another empty matrix to hold the sums
#testing matrix indexing
#matrix[0][0]=1
#matrix[1][0]=2
#matrix[0][1]=3

def bernoulli(p): #This function gives me my bernoulli variable with p success
    e=0
    rand=randrange(0,100)
    if (rand/100) <= p:
        e=1
    else:
        e=0
    return e
    
#testing bernoulli method. IT WORKS
#k=0
#for y in range(0,100):
#    t=bernoulli(.75)
#    if t==1:
#        k=k+1
#print(k)
    
for x in range (0,n):                #Here is the main code
    sum=0                            # have to reset the sum every time
    for y in range(0,10):            #sums of 10 bernoulli random variables
        matrix[x][y]=bernoulli(p)    #gives each index a variable
        sum=sum+matrix[x][y]         #sums up the 10
    sumMatrix[x]=sum                 #puts sum into new matrix


# the histogram of the data
# i apologize for the sloppiness of the graph. It was very diffcult for me to
# understand all the code for making it look pretty. 
# I also blame the randomness.
num_bins = 10                   #not sure if this is right,but i looks the best
n, bins, patches = plt.hist(sumMatrix, num_bins, normed=1, align='mid', facecolor='green', alpha=0.5)
#add normed=1 to display a percentage instead of total

plt.xlabel('Number of Ones')
plt.ylabel('Probability')
plt.title(r'Binomial random variable distribution')
plt.show()

#observations about ditribution:
#1. Every time I run it there seems to be a total probabiltity of less than 5%
# for getting 4 or less 1s. 
#2. The probability of getting other numbers seems to vary a lot with each 
#trial (because of the randomness) I saw the probability of getting 10 1s push
#25%
#3. It is interesting to note that for every run of the program, 
# the probability of getting 8 1s vs 7 1s is always higher. considering the 
# probability is 75%. I would think 7 and 8 would tradeoff evenly. I'm sure 
#If i did the math I would see why this happens.
#4. definitely not a normal distribution
#5. The mean hovers around 75%
#6. I am looking at the pmf correct?