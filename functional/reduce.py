'''
>>> series1 = (0, 1, 2, 3, 4, 5)
>>> series2 = (2, 4, 8, 16, 32)
>>> power_reducer = add_powers(2)
>>> power_reducer(series1)
55
>>> power_reducer(series2)
1364
>>>
>>> power_reducer = add_powers(3)
>>> power_reducer(series1)
225
>>> power_reducer(series2)
37448
'''

if __name__ == '__main__':
    import doctest
    doctest.testmod()
