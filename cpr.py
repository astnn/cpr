#First attempt at the cpr-module.

import numpy as np



def verMod11(cprNumbVect):
    """Check if given CPR-number using modulus 11 method."""
    
    cntrlVect = np.array([4,3,2,7,6,5,4,3,2,1])
    verVect = cprNumbVect*cntrlVect
    rem = verVect.sum() % 11
    
    if rem == 0:
        return True
    else:
        return False

testCpr = np.array([2,1,1,0,6,2,5,6,2,9])
print('Given CPR number is:', str(verMod11(testCpr)))