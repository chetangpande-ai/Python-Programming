import os as os_module
# This section demonstrates multiple try-except blocks,
# handling different types of exceptions such as ValueError,
# ZeroDivisionError, and a generic Exception.

try:
    a = input("enter number:")
    a = int(a)
    print(a)
    # print(10/0)  # Removed to avoid ZeroDivisionError
    print(os_module.listdir())
except ValueError as e:
    print("ValueError:", e)
except ZeroDivisionError as e:
    print("ZeroDivisionError:", e)
except Exception as e:
    print("Exception error:", e)    