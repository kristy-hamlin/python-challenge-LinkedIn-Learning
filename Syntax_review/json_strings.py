# Python Essential Training Chapter 9:
# Working With JSON strings

import json
from json import JSONDecodeError, JSONEncoder

# Working with JSON is very common wit programming jobs. You should at least
# be familiar with how to encode and decode JSON strings in Python. 

# A JSON string is formatted very similarly to a Python dictionary, but it needs
# to be formatted correctly or the json.loads() function will throw an error.
# Because of this, it is common to surround json.loads() with a try/except.
# However, if successful, json.loads() returns a Python Dictionary:
def jsonLoadsDemo():
    jsonString = '{"a": "apple", "b": "baboon", "c": "cosmic", "d": "doggo"}'
    try:
        dic = json.loads(jsonString)
    except JSONDecodeError:
        print('Failure loading json string.')
    print(dic)

def jsonLoadsDemo2():
    # This one will purposely fail. Notice that we needed to impor thte JSONDecodeError:
    jsonString = '{"nose": "rhinarium", "eyes": "brown", "name": "Jordy",}' # Trailing comma not acceptable for JSON strings.
    dic = {}
    try:
        dic = json.loads(jsonString)
    except JSONDecodeError:
        print('JSON.loads() could not parse the string.')
    
# Taking a Python dictionary and turning into a JSON String can be easier,
# because if you have a valid Python dictionary, there's not a lot that
# can go wrong. This is called "dumping" for some reason. The json.dumps() 
# method accepts a Python dictionary and returns a JSON String:
def jsonDumpsDemo():
    dic = {'a': 'anybody', 'b': 'best', 'c': 'chinchilla'}
    jsonString = json.dumps(dic)
    print(jsonString)

# However, turning a Python dictionary into a JSON string is more work
# if your Python dictionary has objects and classes in it that the JSON
# encoder is not familiar with. Let's create a class to demonstrate:

class Word():
    def __init__(self, word):
        self.word = word
        self.firstLetter = word[0]
        self.lastLetter = word[-1]
        self.definition = ''

def jsonDumpsDemo2():
    dic = {'a': Word('anybody'), 'b': Word('best'), 'c': Word('chinchilla')}
    jsonString = json.dumps(dic)
    # This will fail if we do not provide a decoder for our class.

# To be able to encode classes of our own creation, we need to provide an
# Encoder class for the JSON Encoder. To do this, we create an encoder class
# that extends JSONEncoder. This is why we have also imported the JSONEncoder
# module, otherwise we would have to refer to it as json.JSONEncoder, so it's
# just more convenient to import it specifically and use the shorter name. 
class WordEncoder(JSONEncoder):
    # The method we need to override in JSONEncoder is the default method.
    # o represents the object being encoded. So in this method we need to
    # tell the JSONEncoder what we want the value to be in the JSON String
    # when it comes across such an object.
    # First, we check if the object is indeed a Word, if so, we will use the 
    # instance variable word as the value. However, we need to also remember
    # to pass any other objects to the default encoder using an if/else:
    def default(self, o):
        if type(o) == Word:
            return o.word
        else:
            return super().default(o)
        
# Finally, we need to pass our new encoder to the json.dumps() method so that it knows
# what decoder it is using. We pass it using the keyword variable cls in the json.dumps()
# method:
def jsonDumpsDemo3():
    dic = {'a': Word('anybody'), 'b': Word('best'), 'c': Word('chinchilla')}
    jsonString = json.dumps(dic, cls=WordEncoder)
    print(jsonString)
    # And voila! This works.

jsonDumpsDemo3()

# End of JSON parsing lesson. 