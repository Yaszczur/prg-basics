###
# Saves to a file a list of employees working at a specified position.
#

# file names
employees_file = '08-FileHandling/it_company.csv'
position_file = '08-FileHandling/software_engineer.txt'

# Position
job_title = 'Software Engineer'

# write selected employees to a file
with open(employees_file, 'r') as in_file:
   with open(position_file, 'w') as out_file:
      for line in in_file:
         if job_title in line:
            out_file.write(line)
