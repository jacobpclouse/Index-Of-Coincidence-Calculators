import codecs
import string

def get_file_contents(filename):
    with codecs.open(filename, encoding='utf-8') as f:
        return f.read()

def calculate_ic(text):
    letter_count = dict.fromkeys(string.ascii_lowercase, 0)
    for letter in text:
        if letter.lower() in letter_count:
            letter_count[letter.lower()] += 1
    ic = sum([count * (count - 1) for count in letter_count.values()]) / (len(text) * (len(text) - 1))
    return ic

if __name__ == '__main__':
    # filename = 'file.txt'
    filename = input('Input Filename: ')
    file_contents = get_file_contents(filename)
    ic = calculate_ic(file_contents)
    print(f"The index of coincidence for {filename} is {ic:.5f}")
