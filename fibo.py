
s=int(input("Enter the total number of fibonacci sequence"))
num1,num2=0,1
for i in range(s):
    print(num1,end=" ") 
    res=num1+num2
    num1=num2
    num2=res
