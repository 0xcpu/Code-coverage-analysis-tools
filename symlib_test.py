import sys
import symlib

test_lib    = "ntoskrnl.exe"
test_name   = "KiDispatchInterrupt"
test_offset = 0x10

if len(sys.argv) >= 3:
    test_lib  = sys.argv[1]
    test_name = sys.argv[2]

print("[+] Testing addrbyname()...")

# step 1: query symbol offset by name
addr_1 = symlib.addrbyname(test_lib, test_name)
if addr_1 == None:
    print("ERROR: {0:s}!{1:s}() is not found".format(test_lib, test_name))
    sys.exit(-1)

print("INFO: {0:s}!{1:s}() is at offset 0x{2:08x}".format(test_lib, test_name, addr_1))
print("[+] Testing namebyaddr()...")

# step 2: query symbol name by offset
name_1 = symlib.namebyaddr(test_lib, addr_1)
if name_1 == None:
    print("ERROR: Symbol for offset 0x{0:08x} is not found".format(addr_1))
    sys.exit(-1)

if name_1 != test_name:
    print("[-] Test failed")
    sys.exit(-1)

print("[+] Testing bestbyaddr()...")

# step 3: query best symbol by offset
best_symbol = symlib.bestbyaddr(test_lib, addr_1 + test_offset)
if best_symbol == None:
    print("ERROR: Best symbol for offset 0x{0:08x} is not found".format(addr_1 + test_offset))
    sys.exit(-1)

if best_symbol[0] != name_1 or best_symbol[1] != test_offset:
    print("[-] Test failed")
    sys.exit(-1)

print("[+] Test passed")
