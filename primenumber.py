s1=int(input('start from:') )
s2=int(input("end with:"))

for num in range(s1,s2+1):
    
 if num>1:
     for i in range(2,num):
      if(num%i==0):
       break
     else:
      print(num)