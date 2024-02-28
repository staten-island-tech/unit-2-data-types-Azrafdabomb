y = int(input("Number 1: "))
x = int(input("Number 2: "))

def gcf():
    y = int(input("Number 1: "))
    x = int(input("Number 2: "))

commonxfactors = []

gcfah = []
def xfactors():
    for i in range(1, x + 1):
        if(x % i == 0 and y % i == 0):
            commonxfactors.append(i)

xfactors()

for i in commonxfactors:
    if i == i in commonxfactors:
        gcfah.append(i)
 
gcf = max(gcfah)
print(gcf)