'''
>>> # Create a parking lot with 2 parking spaces
>>> lot = ParkingLot(2)
>>> # Create a car and park it in the lot
>>> car = Car('Audi','R8', '2010')
>>> lot.park(car)
>>> car = Car('VW', 'Vanagon', '1981')
>>> lot.park(car)
>>> car = Car('Buick','Regal', '1988')
>>> lot.park(car)
'Lot Full'
>>> lot.spaces = 3
>>> lot.park(car)
>>> car.make
'Buick'
>>> car.model
'Regal'
>>> car.year
'1988'
>>> for c in lot:
...     print c
2010 Audi R8
1981 VW Vanagon
1988 Buick Regal
>>> for c in lot.cars_by_age():
...     print c
1981 VW Vanagon
1988 Buick Regal
2010 Audi R8
>>> for c in lot:
...     print c
2010 Audi R8
1981 VW Vanagon
1988 Buick Regal
'''


if __name__ == '__main__':
    import doctest
    doctest.testmod()
