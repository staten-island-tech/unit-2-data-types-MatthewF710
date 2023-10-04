

num=int(input("Please enter a number:"))
num2=int(input("Please enter another number:"))
factors=[]
factors2=[]
def factor():
    for i in range(1, num + 1):
        if num%i == 0:
            print(i)
        else:
            i+1

def factor2():
    for i in range(1, num2 + 1):
        if num2%i == 0:
            print(i)
        else:
            i+1
factors.append(factor)
factors2.append(factor2)
print(factors)
print(factors2)

for i in range():
    