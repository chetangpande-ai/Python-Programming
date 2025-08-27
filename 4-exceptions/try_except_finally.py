# Example 5: Handling multiple files with exception handling
def loaddata(files):
    try:
        for a in files:
            print(a)
            #print(a.read())
    except Exception as e:
        print("file not found", e)
    else:#gets executed if there is no exception
        print("else section got executed - file read successfully")
    finally:
        print("Execution completed.")

files = ["data1.txt", "data2.txt", "data3.txt"]
loaddata(files)

print("*****************************************************************")
def divide():
    try:
        a=input("Enter a number: ")
        a=int(a)
        a=100/a
    except ValueError as e:
        print("Value Error--", e)
    else:
        print("result of operation is", a)
    finally:
        print("code executed successfully")

divide()