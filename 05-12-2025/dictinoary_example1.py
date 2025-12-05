#Dictionary Example
emp_names={'E001':'Alice','E002':'Bob','E003':'Charlie'}

print(type(emp_names))
for emp_id, emp_name in emp_names.items():
    print(f'Employee ID: {emp_id}, Employee Name: {emp_name}')

#dictionary with nested dictionaries
emp_details={
    'E001': {'name': 'Alice', 'age': 30, 'department': 'HR'},
    'E002': {'name': 'Bob', 'age': 25, 'department': 'IT'},
    'E003': {'name': 'Charlie', 'age': 28, 'department': 'Finance'}
}


for emp_id, details in emp_details.items():
    print(f'Employee ID: {emp_id}, Name: {details["name"]}, Age: {details["age"]}, Department: {details["department"]}')