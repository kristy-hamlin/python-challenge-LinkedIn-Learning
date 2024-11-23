animalDict = {
    'a': ['antelope', 'anteater', 'armadillo'],
    'b': ['bear', 'bison', 'bunny'],
    'c': ['cat', 'crocodile', 'cheetah'],
    'd': ['dog', 'dingo', 'dolphin'],
}

def dictionary_types_demo():
    print(animalDict.keys())
    print(type(animalDict.keys()))
    print(animalDict.values())
    print(type(animalDict.values()))
    print(animalDict.items())
    print(type(animalDict.items()))

def without_continue_demo():
    for letter, animals in animalDict.items():
        print(letter)
        print(animals)
        print()

def continue_demo():
    #continue allows you to skip the rest of an iteration
    for letter, animals in animalDict.items():
        if letter == 'b':
            continue
        print(letter)
        print(animals)
        print()

def no_break_demo():
    #Outer loop prints the letter for each dict item
    #Inner loop prints each animal in the list.
    for letter, animals in animalDict.items():
        print(letter)
        for animal in animals:
            print(animal)
        print()

def break_demo():
    #Break breaks out of the current loop.
    #Therefore, this break statement should end the
    #animals list when an animal in a given list has more
    #than 5 letters.
    for letter, animals in animalDict.items():
        print(letter)
        for animal in animals:
            if len(animal) > 4:
                break
            print(animal)
        print()

def break_else_demo():
    #I'm not sure I'm understanding break/else correctly.
    #When you add a break in a for loop, the else
    #will only be triggered if the break was not triggered.
    for letter, animals in animalDict.items():
        print(letter)
        for animal in animals:
            if len(animal) > 7:
                break
            print(animal)
        else:
            print('all animals under 8 letters.')

def finding_primes_demo():
    #Find all primes between 2 and 100.
    for num in range(2, 100):
        for factor in range(2, int(num**0.5) + 1):
            if num % factor == 0:
                break
        else:
            print(f'{num} is prime!')

finding_primes_demo()


