sum = 0

for i in range(1,11):
    if not i%2==0:
        continue
    sum += sum + i

print(f'Sum is {sum}')