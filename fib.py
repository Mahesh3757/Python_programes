a=int(input("Enter a number : "))
print("Entered number is = ",a )
temp=a
sum=0
while temp>0:
   dig =temp%10
   sum+=dig**3
   temp//=10
if a==sum:
    print(a,"Armstrong")
else:
    print(a,"not Armstrong")

