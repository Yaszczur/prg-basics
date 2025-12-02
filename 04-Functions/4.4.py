def sum_digits(number):
    suma = 0
    number = abs(number)
    x = str(number)
    for n in x:
        suma += int(n)
       #suma = suma + int(n) - to samo co wyzej
    return suma

print(sum_digits(-123))
