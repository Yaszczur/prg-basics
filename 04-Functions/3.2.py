###
# Generates and prints a random number between 1 and 6,
# similar to rolling a dice
#
import random

# Używamy funkcji random.randint(a, b), która zwraca
# losową liczbę całkowitą N, taką że a <= N <= b.
# Zakres 1 i 6 są włączone.
dice_roll = random.randint(1, 6)

print(f'The dice roll result (random number between 1 and 6) is: {dice_roll}')