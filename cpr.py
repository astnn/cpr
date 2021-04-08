# A. S. Nielsen 2021


def verMod11(cprNumbVect):
    """Perform modulus 11 check for validity of CPR-number"""
    
    if len(cprNumbVect) != 10:
        raise ValueError("CPR-number to be validated must be 10 ciphers.")
    
    sumation = 0
    cntrlVect = [4,3,2,7,6,5,4,3,2,1]
    for index in range(len(cntrlVect)):
        sumation += int(cprNumbVect[index])*cntrlVect[index]
    rem = sumation % 11
    
    if rem == 0:
        return True
    else:
        return False

def genMod11Cipher(cprNumbVect):
    """Generate the 10th control cipher given the 9 previous. Returns string holding all 10 ciphers. Return None if control cipher cannot be generated."""
    sumation = 0
    cntrlVect = [4,3,2,7,6,5,4,3,2,1]
    for index in range(9): #Notice that the loop is only over 9 indices.
        sumation += int(cprNumbVect[index]) * cntrlVect[index]
    rem = sumation % 11
    if rem == 0:
        cipher10 = 0
    else:
        cipher10 = 11-rem #Calc. how much should be added to rem to make the remainder zero
    if cipher10 != 10:
        return cprNumbVect+str(cipher10)
    else:
        return None
        
    

def gen7CipherList(birthYear):
    """Takes an integer birthyear and returns a sorted list of possible 7th CPR digit"""
    #Note: While one can speculate how CPR numbers will be extended to years
    #beyond 2057, it is currently not defined. I therefor opted for this simple
    #implementation.
    if birthYear >= 1858 and birthYear < 1900:
        return ['5','6','7','8']
    elif birthYear >= 1900 and birthYear < 1937:
        return ['0','1','2','3']
    elif birthYear >= 1937 and birthYear < 2000:
        return ['0','1','2','3','4','9']
    elif birthYear >= 2000 and birthYear < 2037:
        return ['4','5','6','7','8','9']
    elif birthYear >= 2037 and birthYear < 2057:
        return ['5','6','7','8']
    else:
        print("Warning. The birthyear", str(birthYear), "is outisde the covered range from 1858 to 2057. Returning empty list.")
        return []

def sexCheck(sex, cprString):
    """Check that the known sex matches that of the CPR-number"""
    #Input:
        #sex, int, 0 for female, 1 for male.
        #cprString, str[10], holds a CPR-number
    #Output:
        #True/False, logical, True if sex matches, False if it does not.
    
    return int(cprString[-1]) % 2 == sex
    
### WIP ###    
def generateCpr(birthDateAndSex,N=40):
    """Generate sorted CPR-number list given birthDate and sex."""
    #Input:
        #birthDateAndSex, str, formatted as DDMMYYYY[sex], where sex is M for male and F for female.
        #N, int, Maximum amount of CPR-numbers to be generated.
    #Output:
        #cprList, sorted (asc) list of valid CPR numbers formated as strings.
    #Note: This function assumes previus input control.
    
    cprList = list()
    cnt = 0
    
    if birthDateAndSex[-1].upper() == 'M':
        sex = 1
    else:
        sex = 0
    
    birthDate = birthDateAndSex[0:8]
    
    birthYear = int(birthDate[4])*1000+int(birthDate[5])*100+int(birthDate[6])*10+int(birthDate[7])
    first6 = birthDate[0:4]+birthDate[6:8]
    poss7Cipher = gen7CipherList(birthYear)
    for cipher7 in poss7Cipher:
        if cnt == N:
            break
        for cipher8 in "0123456789":
            if cnt == N:
                break
            for cipher9 in "0123456789":
                first9 = first6+cipher7+cipher8+cipher9
                possCPR = genMod11Cipher(first9)
                if possCPR != None and sexCheck(sex,possCPR):
                    cprList.append(possCPR)
                    cnt +=1
                if cnt == N:
                    break
                
                
    return cprList


# cprList = generateCpr("01061990F",1000)
