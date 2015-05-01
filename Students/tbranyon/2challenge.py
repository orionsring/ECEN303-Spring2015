import random
import matplotlib.pyplot as plt
import numpy as np

def bernoulli():
    X = 0
    p = random.random()
    if p <= 0.75:
        X = 1
    return X


def bernoulli_composite():
    retval = 0
    for i in range(10):
        retval += bernoulli()
    return retval

results = []
N=1000000 #change as desired
for i in range(N):
    res = bernoulli_composite()
    results.append(res)
plt.hist(results, bins=np.arange(0.5, 10.5, 1))
plt.show()
#this should output a binomial distribution, since the sum of indepedent Bernoulli variables yields a binomial
#as N in increased, the empirical distribution approaches the nominal probability distribution

percent = []
for OutcomeIndex in range(0, 11):
    percent.append(results.count(OutcomeIndex) / float(N))
print("Proportion of results that fell in each value, 0-10:")
print percent
