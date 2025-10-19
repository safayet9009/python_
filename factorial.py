s=int(input("enter factorial number:"))
fact=1
if s<0:
 print("factorial doesn't exist")
elif s==0:
 print("factorial of 0 is 1")
else:
    for i in range(1,s+1):
     fact=fact*i
'print'     
print(fact)
