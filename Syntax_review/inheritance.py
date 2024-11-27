# Python Essential Training: Chapter 7
# Inheritance

# Example 1: Extending a Class ------------------------------------------------
class Dog:
    _legs = 4
    _isFurry = True
    def __init__(self, name, size, eyeColor):
        self.name = name
        self.size = size
        self.eyeColor = eyeColor
    
    def speak(self):
        print(f'{self.name} says: Bark!')
    
    def getLegs(self):
        return self._legs

# To extend a class in Python, you provide the parent class in parenthesis after
# the child class name. 
# This child class inherits all the properties and functions of the parent class:
class Sheltie(Dog):
    # To override a method, provide a method of the same signature
    # and the child's method will override the parent's method.
    def speak(self):
        print(f'{self.name} says: bark bark bark bark bark bark')
    
    # We can also provide additional methods that are not in the parent class:
    def cuteStare(self):
        print(f'{self.name} is staring at you intensely with profound {self.eyeColor} eyes.')

def dogDemo():
    jordy = Dog('Jordy', 'medium', 'brown')
    jordy.speak()
    print(jordy.getLegs())

def sheltieDemo():
    lacey = Sheltie('Lacey', 'tiny', 'blackest black')
    lacey.speak()
    lacey.cuteStare()

# Example 2: Extending a Python Built-in Class ------------------------------------------------
# Let's extend the Python list() class as an example. 
class UniqueList(list):
    # The super() function is used to get the parent instance of a function.
    # For example, if we just used self.append() below, the function would be 
    # calling itself and lead to infinite recursion. We want to call the list()
    # class's .append(). 
    def append(self, item):
        if item in self:
            return
        super().append(item)


def uniqueListDemo():
    ul = UniqueList()
    ul.append(1)
    ul.append(1)
    ul.append(2)
    ul.append(3)
    ul.append(4)
    ul.append(3)
    print(ul)



# Example 3: Overriding a Parent Constructor ------------------------------------------------
# You can also use super() to call the parent constructor. You should call it first
# within the child constructor. 
# This is important if you want your child class to have instance variables in addition
# to what the parent class has. 
class UniqueList(list):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def append(self, item):
        if item in self:
            return
        super().append(item)


def uniqueListDemo():
    ul = UniqueList("my name is Darcy")
    ul.append(1)
    ul.append(1)
    ul.append(2)
    ul.append(3)
    ul.append(4)
    ul.append(3)
    print(ul.name)
    print(ul)

# Now I want to see how overriding the parent constructor works when the
# parent constructor requires inputs:
class Sheltie(Dog):
    def __init__(self, name, size, eyeColor, breederName, coatPattern):
        super().__init__(name, size, eyeColor)
        self.breederName = breederName
        self.coatPattern = coatPattern

    def speak(self):
        print(f'{self.name} says: bark bark bark bark bark bark')
    
    def cuteStare(self):
        print(f'{self.name} is staring at you intensely with profound {self.eyeColor} eyes.')

    def getStats(self):
        print(f'{self.name} Stats: ------')
        print(f'Size: {self.size}')
        print(f'Eye Color: {self.eyeColor}')
        print(f'Breeder Name: {self.breederName}')
        print(f'Coat Pattern: {self.coatPattern}')

def constructorDemo():
    jordy = Sheltie('Jordy', 'Medium', 'Brown', 'Himark', 'Sable')
    jordy.getStats()

constructorDemo()
