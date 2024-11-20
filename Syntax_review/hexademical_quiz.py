#Python Essential Training: Chapter 3 Quiz
#Write your own function to convert a h exademical string (up to 3 chars long)
#to a decimal integer. Do not use the integer class, write your own function.

def hexToDec(hexNum):
    #Dictionary containing conversions:
    hexDict = {
        '0' : 0,
        '1' : 1,
        '2' : 2,
        '3' : 3,
        '4' : 4,
        '5' : 5,
        '6' : 6,
        '7' : 7,
        '8' : 8,
        '9' : 9,
        'A' : 10,
        'B' : 11,
        'C' : 12,
        'D' : 13,
        'E' : 14,
        'F' : 15,
    }
    #Calculate hex conversion using loop: 
    result = 0
    digit = 0
    for i in range((len(hexNum) - 1), -1, -1):
        #print('i: ' + str(i))
        currChar = hexNum[i]
        #print('currChar = ' + str(currChar))
        if currChar in hexDict:
            hexDigit = hexDict[currChar]
            #print('hexDigit = ' + str(hexDigit))
            #print('digit = ' + str(digit))
            currDigit = (hexDigit * 16 ** digit)
            #print('currDigit = ' + str(hexDigit) + ' * 16 ** ' + str(digit))
            #print('currDigit = ' + str(currDigit))
            result = result + currDigit
            digit = digit + 1
        else:
            print('Input must be a valid string of hex characters.')
            return None
    return result


print("'FA1010' converted from hex to dec = " + str(hexToDec('FA1010')))