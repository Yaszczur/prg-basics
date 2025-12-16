categories = ["Food", "Transport", "Rent", "Entertainment"]
expenses = [500, 150, 1000, 200]

max_expense = expenses[0]
most_expensive_category = categories[0]

for i in range(1, len(expenses)):
    current_expense = expenses[i]
    current_category = categories[i]

    if current_expense > max_expense:
        max_expense = current_expense
        most_expensive_category = current_category

print(f'The most expensive category is {most_expensive_category} and amount of it is {max_expense}')