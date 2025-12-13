def input_string(message):
    value = input(message)
    return value

def input_integer(message):
    value = input(message)
    return int(value)

def input_real(message):
    value = input(message)
    return float(value)

def input_boolean(message):
    value = input(message)
    return value.lower() in ('true', '1', 'yes', 'tak', 'y')

print(input_boolean("czy niebo jest niebieskie?"))

###
# Allows to enter and print employee data. Due to personal
# data protection, you can determine whether information about
# the employee's salary will be printed
#

# Reads employee's data from keyboard
first_name = input_string('Enter name: ')
last_name = input_string('Enter surname: ')
age = input_integer('Enter age: ')
salary = input_real('Enter salary: ')
is_salary_hidden = input_boolean('Hide salary? (y/n)')


# Prints employee's record
print('DATA RECORD')
print('===========')
print('Name:', first_name)
print('Last name', last_name)
print('Age', age)
if not is_salary_hidden:
    print('Salary:', salary)