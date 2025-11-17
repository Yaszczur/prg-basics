###
# Program for testing built-in functions
#
# 1. Największa liczba
max_number = max(7, 5, 6, 3, 8, 2)
print(f'Max number of 7,5,6,3,8,2 is {max_number}')

# 2. Najmniejsza liczba
min_number = min(4, 7, 2, 3, 9, 8)
print(f'Min number of 4,7,2,3,9,8 is {min_number}')

# 3. Długość frazy
str_length = len("computer science")
print(f'The number of characters in "computer science" is {str_length}')

# 4. Litera odczytana z klawiatury
# Używamy funkcji input() do pobrania tekstu od użytkownika
# Poniższa linia zostanie wykonana po uruchomieniu programu
# Oczekuje, że użytkownik wpisze coś i naciśnie Enter
print('-' * 20) # Separator dla czytelności
print('Wprowadź dowolną literę:')
user_input_letter = input()
print(f'Letter read from the keyboard is: {user_input_letter}')
print('-' * 20)

# 5. Liczba reprezentująca ciąg "20303"
# Używamy funkcji int() do konwersji ciągu znaków na liczbę całkowitą
number_from_string = int("20303")
print(f'Number representing the string "20303" is: {number_from_string}')

# 6. Ciąg binarny reprezentujący liczbę dziesiętną 304
# Używamy funkcji bin() do konwersji na postać binarną (z prefixem '0b')
binary_string = bin(304)
print(f'Binary string representing decimal number 304 is: {binary_string}')

# 7. Ciąg szesnastkowy reprezentujący liczbę dziesiętną 304
# Używamy funkcji hex() do konwersji na postać szesnastkową (z prefixem '0x')
hexadecimal_string = hex(304)
print(f'Hexadecimal string representing decimal number 304 is: {hexadecimal_string}')

# 8. Liczba całkowita reprezentująca kod Unicode znaku €
# Używamy funkcji ord() do uzyskania wartości całkowitej (kod punktowy Unicode) znaku
unicode_code_euro = ord('€')
print(f'Integer representing the Unicode code of the € sign is: {unicode_code_euro}')

# 9. Wartość bezwzględna liczby -17
# Używamy funkcji abs() do uzyskania wartości bezwzględnej
absolute_value = abs(-17)
print(f'Absolute value of -17 is: {absolute_value}')