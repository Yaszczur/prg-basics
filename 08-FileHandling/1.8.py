def number_of_words(text):
    words = text.split(' ')
    return len(words)

def read_from_file(name):
    with open(name, 'r') as file:
        content = file.read()
        return content.splitlines()
    
lines = read_from_file('08-FileHandling/pets.txt')
for line in lines:
    print(f'Words: {number_of_words(line)}. {line}')