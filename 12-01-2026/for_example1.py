'''for with underscore (_) to ignore the index value'''
#example1
for _, value in enumerate(['apple', 'banana', 'cherry']):
    print(value)


#example 2
for _, char in enumerate('hello'):
    print(char)

#example 3
for _, item in enumerate([10, 20, 30, 40]):
    print(item)

#example 4
names=['Alice', 'Bob', 'Charlie']
for _, name in enumerate(names):
    print(name)
