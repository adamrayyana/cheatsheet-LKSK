from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes

# One huge prime (1000 bits)
p = getPrime(100)
# One tiny prime (50 bits) - This is the "Weak Link"
q = getPrime(100)
print(p)
n = p * q
e = 65537

phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)

flag = b"LKSKOTAMENANGLAH{weak}"
# Convert the string to a single large integer
m = bytes_to_long(flag)

# Encrypt the flag
c = pow(m, e, n)
print(f"N = {n}")
print(f"e = {e}")
print(f"c = {c}")