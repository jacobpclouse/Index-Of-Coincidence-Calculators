# Use this one
import binascii

def compute_index_of_coincidence(ciphertext):
    n = len(ciphertext)
    freqs = [0] * 256
    for byte in ciphertext:
        freqs[byte] += 1
    ic = 0
    for freq in freqs:
        ic += freq * (freq - 1)
    ic = ic / (n * (n - 1))
    return ic


filename = input("Give me the filename: ")

# Open the file in binary mode and read its contents
with open(filename, 'rb') as f:
    ciphertext_bytes = f.read()

# Compute the index of coincidence
ic = compute_index_of_coincidence(ciphertext_bytes)

# Print the result
print("The index of coincidence is:", ic)
