# Python Essential Training: Chapter 10 Challenge
# Compressing ASCII Art

# Recall the encodeString() and decodeString() functions you wrote previously.
# In this challenge, your goal is to write two new functions, encodeFile() and decodeFile().

# encodeFile() should open a file containing an ASCII art string, perform some processing,
# and then write that data to a new file. The new file size should be smaller than the original
# file size. 

# decodeFile() should perform the reverse of the original modification to expand the data
# to its original form. It then returns the original string.



def encodeString(original_string):
    # I want to re-write this function for practice... I do not want to use JSON strings.
    # let's see if I can avoid that.
    encoded_string = ''
    prev_char = original_string[0]
    counter = 1
    for i in range(1, len(original_string)):
        char = original_string[i]
        if char == prev_char:
            # If same character is repeated, increment counter:
            counter = counter + 1
        else:
            # If new char is detected, write the previous info
            # to the string and start the counter over.
            encoded = str(counter) + ',' + str(prev_char) + ','
            encoded_string += encoded
            prev_char = char
            counter = 1
    # After the last loop iteration, the last char and counter
    # should still need to be encoded.
    # If the last char is a newline, ignore it:
    if prev_char == '\n':
        pass
    else:
        encoded = str(counter) + ',' + str(prev_char) + ','
        encoded_string += encoded
    return encoded_string

def decodeString(encoded_string):
    # The encoded strings consist of a number followed by a char.
    # Decoding should be the easy part:
    decoded_string = ''
    # I don't think a regular for loop will work since I need to 
    # process the chars in groups depending on the length
    # of the digits in the number:
    i = 0
    while i < len(encoded_string):
        if i == (len(encoded_string) - 1):
            # Ignore last newline:
            break
        # Numbers come first. Get digits up to the comma, could be
        # one or more digits:
        num = ''
        while(encoded_string[i].isdigit()):
            # print('Digit detected: ' + encoded_string[i])
            num += encoded_string[i]
            i += 1

        # discard comma 1
        if encoded_string[i] != ',':
            # print('Comma expected, not found!')
            return 'comma 1 not found failure'
        else:
            # print('Discarding comma 1')
            i += 1
        # convert string to int
        num = int(num)
        char = encoded_string[i]
        # print('Char detected: ' + char)
        i += 1
        # discard comma 2
        if encoded_string[i] != ',':
            # print('Comma expected, not found!')
            return 'comma 2 not found failure'
        else:
            # print('Discarding comma 2')
            i += 1
        decoded = ''
        for c in range(0, num):
            decoded += char
        # print('Appending to string: ' + decoded)
        decoded_string += decoded
    return decoded_string

# ----------------- Testing --------------------

# Okay, now that I have recreated encode and decode string, let me write
# the methods to encode and decode the files: 
def encodeFile(filename, new_filename):
    # Open the file, which will be txt file:
    with open(filename, 'r') as r:
        lines = r.readlines()
    encoded_lines = []
    for line in lines:
        # print('Encoding line: ' + line)
        # print('Encoded line: ' + encodeString(line))
        encoded_lines.append(encodeString(line))
    
    with open(new_filename, 'w') as w:
        for line in encoded_lines:
            # print('Writing line: ' + line)
            w.write(line + '\n')


def decodeFile(filename):
    # I am going to have this method print the ascii art to the screen,
    # because the prompt given doesn't say to return a new file or anything,
    # it just says to return the decoded string and that's not very exciting.
    with open(filename, 'r') as r:
        lines = r.readlines()
    decoded_lines = []
    i = 1
    for line in lines:
        # print('Decoding line: ' + str(i) + '-----------')
        decoded_lines.append(decodeString(line))
        i += 1
    for line in decoded_lines:
        print(line)

encodeFile('wolf.txt', 'result.txt')
decodeFile('result.txt')


