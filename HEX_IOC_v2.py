# USE THIS ONE -- Edited on Windows 10 - may need to be edited if you want to use on Linux/MacOS

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Importing Libraries / Modules 
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
import binascii


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Functions
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# --- Function that computes IOC from ciphertext read from binary file ---
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


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# MAIN 
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
filename = input("Give me the filename: ")
output_name = input("REQUIRED: What do you want the output to be called?: ")

# Open the file in binary mode and read its contents
with open(filename, 'rb') as f:
    ciphertext_bytes = f.read()

# Compute the index of coincidence
ic = compute_index_of_coincidence(ciphertext_bytes)

# Print the result
print("The index of coincidence is:", ic)

# # # save string to file
text_file = open(f"IC_{output_name}.txt", "w")
n = text_file.write(f"The index of coincidence for {filename} is: {ic}" )
text_file.close()