# Try Except example3.py
#Multiple Exception Handling
#ValueError and ZeroDivisionError
try:
    #print(10/0)
    print(int("helo"))
except (ValueError, ZeroDivisionError) as e:
    print("after exception")
    print("You cannot divide a number by zero", e)


#Example of finally block
print("*****************try catch with finally block******************")
try:
    print(10/0)
    print("hello")
except Exception as e:
    print("after exception")
    print("You cannot divide a number by zero", e)
finally:
    print("I will execute no matter what")

#Example of finally block
print("*****************generic try catch******************")

try:
    print(10/2)
    print("hello")  

except Exception as e:
    print("after exception")
    print("You cannot divide a number by zero", e)