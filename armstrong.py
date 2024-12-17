d=int(input("Enter your number"))
sum=0
tem=d
while d>0:
    digit=d%10
    sum=sum+digit**3
    d=d//10
if tem==sum:
    print("it's armstrong")
else:
    print("it's not armstrong")