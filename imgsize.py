# http://stackoverflow.com/a/20380514/1789574

import struct
import imghdr

def get_image_size(fname):
    '''Determine the image type of fhandle and return its size.
    from draco'''
    fhandle = open(fname, 'rb')
    head = fhandle.read(24)
    if len(head) != 24:
        return
    sig = imghdr.what(fname)
    if sig == 'png':
        check = struct.unpack('>i', head[4:8])[0]
        if check != 0x0d0a1a0a:
            return
        w, h = struct.unpack('>ii', head[16:24])
    elif sig == 'gif':
        w, h = struct.unpack('<HH', head[6:10])
    elif sig == 'jpeg':
        try:
            fhandle.seek(0) # Read 0xff next
            size = 2
            ftype = 0
            while not 0xc0 <= ftype <= 0xcf:
                fhandle.seek(size, 1)
                byte = fhandle.read(1)
                while ord(byte) == 0xff:
                    byte = fhandle.read(1)
                ftype = ord(byte)
                size = struct.unpack('>H', fhandle.read(2))[0] - 2
            # We are at a SOFn block
            fhandle.seek(1, 1)  # Skip `precision' byte.
            h, w = struct.unpack('>HH', fhandle.read(4))
        except Exception: #IGNORE:W0703
            return
    elif sig=='bmp': 
        fhandle.seek(18)
        w=int.from_bytes(fhandle.read(4),byteorder='little')
        h=int.from_bytes(fhandle.read(4),byteorder='little')
    elif fname.endswith('.ico'):
        fhandle.seek(6)
        w=int.from_bytes(fhandle.read(1),byteorder='little')
        if w==0:
            w=256
        h=int.from_bytes(fhandle.read(1),byteorder='little')     
        if h==0:
            h=256   
    else:
        return
    return w, h
