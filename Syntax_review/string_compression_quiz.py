#Python Essential Training Chapter 4 Quiz:
#Write a function encodeString() that will encode a string such as 'AAAAABBBBAAA'
#and return a list of tuples: [('A', 5), ('B', 4), ('A', 3)].
#Write a corresponding function decodeString that returns the original string given the list. 

def encodeString(inputString):
    result = []
    count = 1
    prevChar = inputString[0]
    print('First char = ' + prevChar)
    for i in range(1, len(inputString)):
        char = inputString[i]
        print('Current char = ' + str(char))
        if char == prevChar:
            print('Curr char == prev char.')
            count = count + 1
            print('Incrementing count = ' + str(count))
        else:
            print('New char detected.')
            result.append((prevChar, count))
            print('Appending new tuple to list = ' + str(prevChar) + ', ' + str(count))
            count = 1
            prevChar = char
            print('Restting count to 1 and setting prevChar = ' + str(prevChar))
    return result

myString = "AAAA"
encoded = encodeString(myString)
print(encoded)

##Note to self: Leaving off for 11/20/24. Realized that I did not provide a case for reaching the end 
# of the string. Fix this. 
