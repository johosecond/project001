def reverse(data):
    rdata = ''
    i = len(data) - 1
    j = 0
    while i >= 0:
       rdata += data[i]
       i -= 1
       j += 1
    return rdata
    

if __name__ == '__main__':

    import struct
    Q = open('q-hex.txt', 'rb').read()
    #Q = open('test-hex.txt', 'rb').read()

    ### Loop Start
    odata = ''
    i = 0
    while i + 1 < len(Q):
       sHex1 = "".join([Q[i],Q[i+1]])
       sHex2 = "".join([Q[i+2],Q[i+3]])
       odata += struct.pack('BB',int(sHex1,16),int(sHex2,16))
       i += 4
       ### Loop End
    print "Output Size = %d" % len(odata)
    #print "%02x" % ord(odata[0])
    #print "%02x" % ord(odata[1])
    #print "%02x" % ord(odata[2])
    #print "%02x" % ord(odata[3])
    out = open('q.bin', 'wb')
    #out.write(reverse(odata))
    out.write(odata)
    out.close()

    