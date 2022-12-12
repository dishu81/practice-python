# userstr=input("enter your string")
# reverse=" "

# for i in range(len(userstr)-1,-1,-1):
# 	reverse=reverse+userstr[i]
# print("user given string is {}".format(userstr))
# print("reverse string is {}".format(reverse))
fac1=int(input("enter your number"))
i=1

for j in range(1,fac1+1):
	i=i*j
print("factorial of {}={}".format(fac1,i))