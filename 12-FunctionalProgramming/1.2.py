n1 = float(input("Wprowadź pierwszą liczbę (n1): "))
n2 = float(input("Wprowadź drugą liczbę (n2): "))

mean = lambda x, y: (x + y) / 2

result = mean(n1, n2)
print(f"The arithmetic mean of {n1} and {n2} is {result}")