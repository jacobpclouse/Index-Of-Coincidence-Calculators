def read_file(filename):
    with open(filename, "r") as f:
        data = f.read().replace('\n', '')
    return data

def index_of_coincidence(data):
    n = len(data)
    freq = [0] * 26
    for c in data:
        if c.isalpha():
            freq[ord(c.lower()) - ord('a')] += 1
    ic = 0
    for f in freq:
        ic += f * (f - 1)
    ic = ic / (n * (n - 1))
    return ic

# MAIN:

filename = input("Enter the filename: ")
data = read_file(filename)
ic = index_of_coincidence(data)
print("The Index of Coincidence is:", ic)
