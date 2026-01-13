class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self): 
        print(f"Name: {self.name}, Age: {self.age}")

if __name__ == "__main__":
    student1 = Student("John Doe", 20)
    student1.display_info()