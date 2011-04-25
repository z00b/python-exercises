'''
>>> check_acl('127.0.0.1')
False
>>> allow('192.168.1.1')
>>> check_acl('192.168.1.1')
True
>>> allow('10.0.1.0/28')
>>> check_acl('10.0.1.1')
True
>>> check_acl('10.0.1.145')
False
>>> allow('172.16.128.0', '255.255.128.0')
>>> check_acl('172.16.0.1')
False
>>> check_acl('172.16.200.1')
True
'''
def allow(ip, mask):
    pass
    
def check_acl(ipaddress):
    return False

if __name__ == '__main__':
    import doctest
    doctest.testmod()
