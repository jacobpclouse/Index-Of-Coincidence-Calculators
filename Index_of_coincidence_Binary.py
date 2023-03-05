import binascii

def get_ic(filename):
    with open(filename, 'rb') as f:
        data = f.read()

    # Convert binary data to hex string
    hex_str = binascii.hexlify(data).decode('utf-8')

    # Calculate the length of the file in bytes
    file_len = len(data)

    # Initialize the count dictionary
    count_dict = {char: 0 for char in range(256)}

    # Count the occurrences of each byte value
    for byte in data:
        count_dict[byte] += 1

    # Calculate the index of coincidence
    ic = 0
    for char in count_dict:
        ic += (count_dict[char] * (count_dict[char] - 1)) / (file_len * (file_len - 1))

    return ic

# -----------
# MAIN BELOW:
# -----------

# filename = 'encrypted_file.bin'
filename = input("What is the name of the Binary File?: ")
ic = get_ic(filename)
print(f'Index of coincidence: {ic}')
