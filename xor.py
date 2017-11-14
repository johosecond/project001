def strxor(mct, k):     # xor two strings of different lengths
    if len(mct) > len(k):
        i = 0
        o = ''
        while i < len(mct):
           o = "".join([o , chr(ord(mct[i]) ^ ord(k[i % len(k)]))])
           i += 1
        return o
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(mct, k[:len(mct)])])

def encrypt(msg, key):
    c = strxor(msg, key)
    return c

def decrypt(ct, key):
    m = strxor(ct, key)
    return m

def str2hex(a):
    return a.encode('hex')

def hex2str(a):
    return a.decode('hex')

if __name__ == '__main__':

    m    = hex2str('89E33F8C4F135AFE654915596BB1B305C768')

    k    = 'EJ'  # <-- Chipher Key 
    # k ... 0100 01010 10 01010

    # m & k XOR Encrypt
    # ct   = encrypt(m, k)

    print "-- message --\n" + str2hex(m)
    print "-- secret key --\n" + str2hex(k)
    # print "-- cipher text --\n" + str2hex(ct)

    # XOR Decrypt
    m2   = decrypt(m, k)
    
    print "-- decrypted text --\n" + str2hex(m2)
    
