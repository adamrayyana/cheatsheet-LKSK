from Crypto.Util.number import getPrime, bytes_to_long, GCD

def generate_common_modulus(message_bytes):
    m = bytes_to_long(message_bytes)
    
    # Buat satu modulus n untuk digunakan bersama
    p = getPrime(512)
    q = getPrime(512)
    n = p * q
    
    # Pilih e1 dan e2 yang gcd(e1, e2) == 1
    e1 = 65537
    e2 = 10007 # Bilangan prima lain agar pasti coprime
    
    if GCD(e1, e2) != 1:
        raise ValueError("e1 dan e2 harus coprime!")

    # Enkripsi pesan yang sama
    c1 = pow(m, e1, n)
    c2 = pow(m, e2, n)
    
    return n, e1, e2, c1, c2

# Data input
flag = b"LKSKOTAMENANGLAH{common_modulus_is_bad}"
n, e1, e2, c1, c2 = generate_common_modulus(flag)

print(f"--- Public Specs ---")
print(f"n = {n}")
print(f"e1 = {e1}")
print(f"e2 = {e2}")
print(f"\n--- Ciphertexts ---")
print(f"c1 = {c1}")
print(f"c2 = {c2}")