a=int(input("enter number"))
sum=0
temp=a
while a>0:
    rem=a%10
    sum=sum*rem*rem
    a=a//10
    if temp==sum:
        print("armstrong")
else:
    print("not an armstrong")