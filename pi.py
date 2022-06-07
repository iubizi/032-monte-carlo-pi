inside = 0
points = 0

from random import random as rand
import numpy as np

# get pi/4.0
while True:
    
    dist = np.linalg.norm( np.array([1, 1]) -
                           np.array([rand(), rand()]) )
    
    if dist <= 1:
        inside += 4 # get pi
    points += 1

    if points % 1e6 == 0: 
        print(inside/points)

# Monte Carlo algorithm:
# Use a large number of random points to obtain statistical results.
