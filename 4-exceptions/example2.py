#Predefined Exceptions
#ZeroDivisionError


try:
    print(10/0)
    print("hello")
except Exception as e:
    print("after exception")
    print("You cannot divide a number by zero",e.message)

