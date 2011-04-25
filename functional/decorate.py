'''
>>> data = '{"username": "oscar", "password": "trashcan", "account": 1234, "amount": 12.03}'
>>> deposit(data)
'OK'
>>> data = '{"username": "oscar", "password": "trash", "account": 1234, "amount": 14.98}'
>>> deposit(data)
'Invalid Password'
>>> data = '{"username": "oscar", "password": "trashcan", "account": 1234, "amount": 4.12}'
>>> withdraw(data)
'OK'
>>> data = '{"username": "oscar", "password": "trashcan", "account": 1235, "amount": 2.54}'
>>> withdraw(data)
'Invalid Account'
>>> data = '{"username": "oscar", "password": "trashcan", "account": 1234}'
>>> balance(data)
'7.91'
>>> data = '{"username": "oscar", "password": "trashcan"}'
>>> balance(data)
'No Account Number Provided'

Hint: that's json data
'''

def deposit(account, amount=0.00):
    pass

def withdraw(account, amount=0.00):
    pass

def balance(account):
    pass

if __name__ == '__main__':
    import doctest
    doctest.testmod()
