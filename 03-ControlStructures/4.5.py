###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''
shift = 1 

for char in plain_text:
    # Check if the character is a letter
    if char.isalpha():
        # Read the character's code (use ord())
        char_code = ord(char)
        
        # Determine the base for the case (A=65 or a=97)
        if char.islower():
            base = ord('a') # 97 for lowercase
        else:
            base = ord('A') # 65 for uppercase
            
        # Apply the Caesar cipher formula with wrap-around (% 26)
        # 1. Convert to 0-25 index: (char_code - base)
        # 2. Add the shift: + shift
        # 3. Apply wrap-around: % 26
        # 4. Convert back to ASCII: + base
        new_char_code = (char_code - base + shift) % 26 + base

        # Replace new character code with its corresponding character (use chr())
        encrypted_character = chr(new_char_code)
        
        # Add encrypted character to encrypted text
        encrypted_text += encrypted_character
    
    # If the character is not a letter (like a space or punctuation), keep it as is
    else:
        encrypted_text += char

print(f"Plain text: {plain_text}")
print(f"Encrypted text: {encrypted_text}")