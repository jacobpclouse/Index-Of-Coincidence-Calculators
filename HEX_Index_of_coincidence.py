import sys

# Define the alphabet (hexadecimal)
ALPHABET = "0123456789abcdef"

# Function to calculate the IOC for a given text
def ioc(text):
    freq = {}
    for c in ALPHABET:
        freq[c] = 0
    for c in text:
        freq[c] += 1
    n = len(text)
    ioc = 0
    for c in ALPHABET:
        ioc += (freq[c] * (freq[c] - 1)) / (n * (n - 1))
    return ioc

# Main function
def main():
    # Check command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python ioc.py filename")
        return

    # Read the input file
    with open(sys.argv[1], "r") as f:
        data = f.read().strip()

    # Convert the data from hexadecimal to ASCII
    text = ""
    for i in range(0, len(data), 2):
        text += chr(int(data[i:i+2], 16))

    # Calculate the IOC
    result = ioc(text)

    # Print the result
    print("Index of Coincidence: {}".format(result))

# Call the main function
if __name__ == "__main__":
    main()
