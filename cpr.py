#First attempt at the cpr-module.


def verMod11(cprNumbVect):
    """Perform modulus 11 check for validity of CPR-number"""
    
    if len(cprNumbVect) != 10:
        raise ValueError("CPR-number to be validated must be 10 ciphers.")
    
    sumation = 0
    cntrlVect = [4,3,2,7,6,5,4,3,2,1]
    for index in range(len(cntrlVect)):
        sumation += cprNumbVect[index]*cntrlVect[index]
    rem = sumation % 11
    
    if rem == 0:
        return True
    else:
        return False

def genMod11Cipher(cprNumbVect):
    """Generate the 10th control cipher given the 9 previous"""
    sumation = 0
    cntrlVect = [4,3,2,7,6,5,4,3,2,1]
    for index in range(9): #Notice that the loop is only over 9 indices.
        sumation += cprNumbVect[index]*cntrlVect[index]
    rem = sumation % 11
    result = 11-rem #Calc. how much should be added to rem to make the remainder zero
    if result != 10:
        return result
    else:
        return None
        
    

def gen7CipherList(birthYear):
    """Takes an integer birthyear and returns a sorted list of possible 7th CPR digit"""
    #Note: While one can speculate how CPR numbers will be extended to years
    #beyond 2057, it is currently not defined. I therefor opted for this simple
    #implementation.
    if birthYear >= 1858 and birthYear < 1900:
        return [5,6,7,8]
    elif birthYear >= 1900 and birthYear < 1937:
        return [0,1,2,3]
    elif birthYear >= 1937 and birthYear < 2000:
        return [0,1,2,3,4,9]
    elif birthYear >= 2000 and birthYear < 2037:
        return [4,5,6,7,8,9]
    elif birthYear >= 2037 and birthYear < 2057:
        return [5,6,7,8]
    else:
        print("Warning. The birthyear", str(birthYear), "is outisde the covered range from 1858 to 2057. Returning empty list.")
        return []

### WIP ###    
# def generateCpr(birthDate,sex,N=40):
#     """Generate sorted CPR-numbers given birthDate and sex."""
    
#     cprList = list()
#     cnt = 0
    
#     birthYear = birthDate[5]*1000+birthDate[6]*100+birthDate[7]*10+birthDate[8]
#     first6 = birthDate[0:4]+birthDate[6:8]
#     poss7Cipher = gen7CipherList(birthYear)
#     for cipher7 in poss7Cipher:
#         for cipher8 in range(10):
#             for cipher9 in range(10):
#                 first9 = first6+str(cipher7)+str(cipher8)+str(cipher9)
#                 cipher10 = genMod11Cipher(first9)
#                 if cipher10 != None:
#                     cprList.append(first9+str(cipher10))
#                     cnt +=1
#                 if cnt == N:
#                     break
                