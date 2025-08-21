#example1
empdeatils = ("John", "Doe", 30, "Engineer")
print(type(empdeatils))

#for loop
for detail in empdeatils:
    print(detail)
    if detail=="John":
        print("emp name matched with john")
        break
