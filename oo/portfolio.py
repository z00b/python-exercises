'''
>>> p = Portfolio()
>>> stocks = (('APPL', 1000, 251.80, 252.73),
...           ('CSCO', 5000, 23.09, 23.74),
...           ('GOOG', 500, 489.23, 491.34),
...           ('MSFT', 2000, 24.63, 25.44))
...
>>> for stock in stocks:
...     p.add(Investment(*stock))
>>> print p['APPL']
1000 shares of APPL worth 252730.00
>>> p['GOOG'].quantity
500
>>> p['GOOG'].close
491.33999999999997
>>> p['GOOG'].open
489.23000000000002
>>> for stock in p:
...     print stock
1000 shares of APPL worth 252730.00
5000 shares of CSCO worth 118700.00
500 shares of GOOG worth 245670.00
2000 shares of MSFT worth 50880.00
>>> for stock in p.sorted('open'):
...     print stock.name
CSCO
MSFT
APPL
GOOG
>>> p['MSFT'].gain
0.81000000000000227
>>> p['CSCO'].total_gain
3249.9999999999927
>>> 'GOOG' in p
True
>>> 'YHOO' in p
False
'''

if __name__ == '__main__':
    import doctest
    doctest.testmod()
