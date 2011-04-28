'''
Have a look at the contents of the files 'obama.txt' and 'obama-exclude.txt'.
Then look at the final api call below: top(x) which takes a number and prints
the count and word that has 
>>> f = open('obama.txt')
>>> for line in f:
...    add_line(line)
...
>>> f.close()
>>> f = open('obama-exclude.txt')
>>> for line in f:
...    exclude_words(line)
...
>>> f.close()
>>> top(10)
68: our
60: we
23: us
17: they
13: you
12: nation
11: new
10: their
8: must
8: every
'''
def add_line(line):
    pass


def exclude_words(line):
    pass


def top(limit):
    pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()
