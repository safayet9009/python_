s=int(input("enter the number:"))
rev=0
while s>0:
 rem=s%10
 rev=rev*10+rem
 s=s//10
print(rev) 
 