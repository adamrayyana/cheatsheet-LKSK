#!/usr/bin/env python3

try:    
    from Crypto.Util.number import long_to_bytes
except ImportError:
    print("install pycryptodome dulu, `pip install pycryptodome --break-system-packages`")
    exit()
try:
    from requests import get
except ImportError:
    print("install requests dulu, `pip install requests --break-system-packages`")
    exit()
N = 1085719257235378588036063648378852961160444474536696071137781
e = 65537
c = 547139188693832776935007446530210085068966515908707976294982



# kalau lama bisa ke factordb manual aja terus taro N-nya (https://factordb.com/)
factors_json = get(f"https://factordb.com/api?query={N}").json()
factors = [int(x[0]) for x in factors_json['factors']]
print(factors)

p,q = factors
phi = (p-1)*(q-1)
# cari d
d = pow(e, -1, phi)
# decrypt
m = pow(c, d, N)
print(long_to_bytes(m).decode())