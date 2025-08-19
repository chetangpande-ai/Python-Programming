def multiply(a, b,c):
    print( a * b*c)

multiply(3, 4,5)


def add(**kwagrs):
    print(type(kwagrs))
    for i in kwagrs:
        print(kwagrs.get(i))

add(a=1, b=2, c=3)

print("**************")

a=[23,32,13,42,12,34,56,78,90]
print (sum(a))

