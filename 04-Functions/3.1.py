###
# To use the functions available in an external module,
# you must include that module in your program.
import math

# Pierwiastek kwadratowy z 7
square_root = math.sqrt(7)
print(f'A square root of 7 is {square_root}')

# Logarytm naturalny (ln) z 5
# Używamy funkcji math.log()
natural_log = math.log(5)
print(f'Natural logarithm of 5 is {natural_log}')

# Sinus z 90 stopni
# Funkcje trygonometryczne w Pythonie (math.sin) przyjmują argumenty w radianach.
# Najpierw konwertujemy 90 stopni na radiany za pomocą math.radians().
angle_degrees = 90
angle_radians = math.radians(angle_degrees)
sine_value = math.sin(angle_radians)
# Wynik dla sin(90) powinien być bliski 1.0
print(f'Sine of 90 degrees is {sine_value}')