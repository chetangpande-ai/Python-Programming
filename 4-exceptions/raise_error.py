def take_age():
    try:
        age=input("Enter your age:")
        age=int(age)
        if age <0 or age >100:
            raise ValueError("Age must be between 0 and 100, please enter a valid age")
        else:
            print("Valid age:", age)
    except Exception as e:
        print("Exception is:", e)

take_age()