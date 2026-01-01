class Student:
    def __init__(self,name,age,id):
        self.name=name
        self.age=age
        self.id=id

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}, ID: {self.id}"
    
    def register_student(self,course):
        return f"Student {self.name} has been registered for the course: {course}"
    

if __name__ == "__main__":
    student = Student("Alice", 20, "S12345")
    print(student.register_student("Mathematics"))
    print(student.get_info())