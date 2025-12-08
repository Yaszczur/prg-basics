###
# Prints employees employed in a specified position.
#

# Employee List
file_name = '08-FileHandling/it_company.txt'

# Position
job_title = 'Software Engineer'

with open(file_name, 'r') as file:
   for line in file_name:
      if job_title in file_name:
         print(f'Number of the employees: ', {file_name})