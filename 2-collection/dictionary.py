#dictionary examples
employee_details = {
    1:{"name": "John", "age": 30, "department": "HR"},
    2:{"name": "Jane", "age": 25, "department": "Finance"},
    3:{"name": "Mike", "age": 35, "department": "IT"},
    4:{"name": "Sara", "age": 28, "department": "Marketing"}
}

for key in employee_details:
    print(employee_details.get(key).get("age"))
    if employee_details.get(key).get("age")==25:
        print("Employee found:", employee_details.get(key).get("name"))
        break

#tuple examples
employee_tuple = (1, "John", 30, "HR")
print("Employee ID:", employee_tuple[0])

#list examples
employee_list = ["John", 30, "HR"]
print("Employee Name:", employee_list[0])

