def printName(name):
    print(f"Name: {name}")


if __name__ == "__main__":
    names = ['Alice', 'Bob', 'Charlie']
    for _, name in enumerate(names):
        printName(name)