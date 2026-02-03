from Crypto.Util.number import getPrime, bytes_to_long

def generate_params(message_bytes, e=3):
    m = bytes_to_long(message_bytes)
    
    # Kita butuh setidaknya k = e ciphertext
    results = []
    
    for i in range(e):
        p = getPrime(512)
        q = getPrime(512)
        n = p * q
        
        # Pastikan m < n
        if m >= n:
            raise ValueError("Pesan terlalu besar untuk modulus n")
            
        c = pow(m, e, n)
        results.append((n, c))
        
    return results

# Data input
flag = b"LKSKOTAMENANGLAH{broadcast}"
e_val = 3

print(f"Encrypting flag: {flag.decode()}\n")

try:
    data = generate_params(flag, e_val)
    
    # Output untuk tantangan CTF
    print(f"e = {e_val}")
    for i, (n, c) in enumerate(data):
        print(f"--- Receiver {i+1} ---")
        print(f"n{i+1} = {n}")
        print(f"c{i+1} = {c}\n")

except Exception as e:
    print(f"Error: {e}")