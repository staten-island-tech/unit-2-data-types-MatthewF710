num=int(input("Please enter a number:"))
num2=int(input("Please enter another number:"))
factors=[]
factors2=[]

print("CALCULATIONS:")
def factor():
    for i in range(1, num + 1):
        if num%i == 0:
            print(i)
            factors.append(i)
        else:
            i+1
factor()
print(factors)

def factor2():
    for i in range(1, num2 + 1):
        if num2%i == 0:
            print(i)
            factors2.append(i)
        else:
            i+1
factor2()
print(factors2)

cf=[]

for gf in factors:
    for gf2 in factors2:
        if gf==gf2:
            cf.append(gf)
print("FINAL GCF:")
print(max(cf))

exit()
for i in range(1, num+1):
    if (num%i==0) and (num2%i==0):
        gcf=i
print(gcf)
exit()