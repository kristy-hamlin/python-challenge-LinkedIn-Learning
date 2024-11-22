#Python Essential Training Chapter 4 Quiz:
#Write a function encodeString() that will encode a string such as 'AAAAABBBBAAA'
#and return a list of tuples: [('A', 5), ('B', 4), ('A', 3)].
#Write a corresponding function decodeString that returns the original string given the list. 

def encodeString(inputString):
    result = []
    count = 1
    prevChar = inputString[0]
    #print('First char = ' + prevChar)
    for i in range(1, len(inputString)):
        char = inputString[i]
        if char == prevChar:
            count = count + 1
        else:
            new = (prevChar, count)
            result.append(new)
            #print('Adding tuple: ' + str(new))
            count = 1
            prevChar = char
    #Append the last tuple
    new = (prevChar, count)
    result.append(new)
    return result

#---------------------------Testing, passed:
# myString = "AAAABBBCCC"
# encoded = encodeString(myString)
# print(encoded)

# myString = "XXXYZHHH123"
# encoded = encodeString(myString)
# print(encoded)

# myString = "__ T Z"
# encoded = encodeString(myString)
# print(encoded)

def decodeString(inputList):
    result = ''
    for tuple in inputList:
        char, num = tuple
        newString = str(char * num)
        result = result + newString
    return result

myList = [('a', 5), ('b', 3), ('c', 3)]
string = decodeString(myList)
print(string)

myList = [('K', 1), ('R', 2), ('I', 3), ('S', 4), ('T', 5), ('Y', 6)]
string = decodeString(myList)
print(string)

#Both functions seem to work properly!