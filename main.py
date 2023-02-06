# import sample1
# calculating permutation
import sample1 as s
n,r=int(input("enter your value:")),int(input("enter your value:"))
if n>=r:
	result=s.factorial(n)/s.factorial (n-r)
	print(result)
else:
	print("n should be greater than r")

# calculating combination
n,r=int(input("enter your value:")),int(input("enter your value:"))
if n>=r:
	result=s.factorial(n)/(s.factorial(r)*s.factorial(n-r))
	print(result)
else:
	print("n should be greater than r")