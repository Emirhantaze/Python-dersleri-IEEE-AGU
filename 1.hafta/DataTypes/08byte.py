#       Bytes

#read from binary file, save efficient vb.

b = b"sfag45"
b2 = b"\x15\x26\x3a\x18" # {21,38,58,24}

bytes(5) # {0,0,0,0,0}
bytes((3, 6, 9, 11)) # {3,6,9,11}

bytes.fromhex("1526 3A18") # {21,38,58,24}
b.hex()
b.hex("-", 2) # 1526-3A18

#byte array mutable version
ba = bytearray()
ba = bytearray(10)
ba = bytearray((3,4,5,9,11))
ba = bytearray(b'Hi!')


