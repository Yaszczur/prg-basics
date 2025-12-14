###
# String manipulation
#

movie = "The Lord of the Rings: The Return of the King"

# print number of characters
print('Number of characters: ', len(movie))

# print title in capital letters
print('Title in capital letters: ', movie.upper())

# print title in small letters
print('Title in small letters: ', movie.lower())

# print how many times the vowel "e" appears in the title
e_count = movie.lower().count('e')
print('The vowel letter "e" appears: ', e_count, 'times')

# print where in the text is the word "Lord"
lord_index = movie.find('Lord')
print('The word "Lord" starts at index: ', lord_index)

# print where in the text is the word "dragon"
dragon_index = movie.find('dragon')
print('The word "dragon" starts at index: ', dragon_index)