# n=int(input("enter your number "))
# for i in range(0,n+1):
# 	for j in range(1,i+1):
# 		print(j,end="")
# 	print("\r")
	

# s2

n=int(input("enter your number:"))
for i in range (1,n+1):
	num=1
	for j in range(1,(n+1)-i):
		print(" ", end="")
	for k in range(1,i+1):
		print(num,end="")
		num=num+1
	print("\r")
 
 
