num=int(input("Please enter a number:"))

def factor():
    for i in range(1, num + 1):
        if num%i == 0:
            print(i)
        else:
            i+1
factor()