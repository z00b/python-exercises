'''
>>> cat = Cat('Spike')
>>> cat.speak()
'Spike says "Meow"'
>>> dog = Dog('Bowzer')
>>> cat.can_swim()
False
>>> dog.can_swim()
True
>>> dog.speak()
'Bowzer says "Woof"'
>>> fish = Fish('Goldie')
>>> fish.speak()
"Goldie can't speak"
>>> fish.can_swim()
True
>>> generic = Pet('Bob')
Traceback (most recent call last):
    ...
TypeError: Can't instantiate abstract class Pet with abstract methods can_swim
'''


if __name__ == '__main__':
    import doctest
    doctest.testmod()
