t1=0
t2=1
n=int(input("enter n value"))
print(t1)
print(t2)
for i in range(2,n):
    fib=t1+t2
    t1=t2
    t2=fib
    print(fib)
