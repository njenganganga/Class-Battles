def sum(x, y):
    a=x+y
    return a
print(sum(10,20))


def courses(*args):
    for subject in args:
        print(subject)
        courses("big data","CCNA","OOP2")


