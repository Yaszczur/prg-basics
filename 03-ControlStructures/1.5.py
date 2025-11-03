total_tasks = 20
tasks_ok = int(input("Enter number of correctly completed tasks: "))
test_passed = False

if tasks_ok >= 0.5 * total_tasks:
    test_passed = True

if test_passed:
    print('Congratulations! You passed the test.')
else:
    print('Unfortunately, you failed the test.')