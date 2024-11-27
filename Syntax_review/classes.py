# Python Essential Training: Chapter 7


# Example Class 1: ---------------------------------------------------------------
# We will use the Dog class to illustrate the basics of class structure in Python,
# including writing a constructor, static versus instance variables, and getter functions.
class Dog:
    # Static variables are defined outside of the constructor.
    # Traditionally they are named with an underscore to signal
    # to the class user that they really should not be directly referenced:
    _legs = 4
    _isFurry = True
    _noseType = 'rhinarium'
    def __init__(self, name, eyeColor):
        # Instance variables are defined inside the constructor:
        self.name = name
        self.eyeColor = eyeColor
    
    # A getter function can be provided to access a certain class
    # property:
    def getLegs(self):
        return self._legs
    
    def speak(self):
        print(self.name + ' says: Bark!')

def dogClassDemo():
    # I want to be able to only execute this code when I want to:
    myDog = Dog('Jordy', 'brown')
    myDog.speak()
    print(myDog.name)

    # You can access a static variable either by using a particular instance,
    # or by using the Class itself:
    print(myDog.getLegs())
    print(Dog._legs)

    # Finally, note that there is variable scope when it comes to classes too.
    # For example, you could change the _legs value on Jordy without changing the 
    # class variable like so:
    print('Changing Jordy legs:')
    myDog._legs = 5
    print(myDog.getLegs())
    print(Dog._legs)


# Example Class 2: ---------------------------------------------------------------
# We will use the WordSet class to illustrate the difference between Static and Instance
# methods in Python, and overriding parent methods. 
class WordSet:
    def __init__(self):
        self.words = set()
    
    def addText(self, text):
        text = self.cleanText(text)
        for word in text.split():
            self.words.add(word)

    # Static methods:
    # Notice that cleanText() does not need self passed in, because all it does
    # is clean text and return it. It can be a static or class method.
    # Therefore, we can remove the 'self' parameter. But now we need
    # to ensure that when it is called, it is called using the Class.method(), 
    # and not self.method(), because self would be passed in and then we would have
    # a mismatch in the number of parameters. 
    # However, if we use the @staticmethod decorator, you can call the function using 
    # self.method() elsewhere in the class. Which method you choose depends on preference. 
    @staticmethod
    def cleanText(text):
        puncs = ['!', '.', ',', '\'']
        for p in puncs:
            text = text.replace(p, '')
        return text.lower()

def wordSetDemo():
    wordSet = WordSet()
    wordSet.addText("Of one thing I was absolutely certain. First, Edward was a vampire...")
    wordSet.addText("Happy Thanksgiving, mi familia")
    print(wordSet.words)

wordSetDemo() 