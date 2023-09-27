num=int(input("Please enter a number:"))
num2=int(input("Please enter another number:"))

def factor1():
    for i in range(1, num + 1):
        if num%i == 0:
            print(i)
        else:
            i+1
def factor2():
    for i in range(1, num2 + 1):
        if num%i == 0:
            print(i)
        else:
            i+1
factor1()
factor2()