
str=input("Enter String: ")
count1=0;
count2=0;
for i in str:
    if i.isdigit():
        count1+=1;
    elif i.isalpha():
        count2+=1;
print("Number of digits in string : ",count1)
print("Number of alphabets in string : ",count2)
        
    