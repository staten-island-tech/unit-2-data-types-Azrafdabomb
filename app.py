y = int(input("Number 1: "))
x = int(input("Number 2: "))


def gcf():
    y = int(input("Number 1: "))
    x = int(input("Number 2: "))

commonfactors = []
def xfactors():
    for i in range(1, x + 1):
        if(x % i == 0):
            commonfactors.append(i)


def yfactors():
    for i in range(1, y + 1):
        if(y % i == 0):
            commonfactors.append(i)
yfactors()
xfactors()