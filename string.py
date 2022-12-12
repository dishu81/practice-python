x=input("enter value:")
y=""
for i in x:
	if ord(i)>=65 and ord (i)<=90:
		a=ord(i)+32
		b=chr(a)
		y=y+b
	else:
		y=y+i
print("value before conversion=",x)
print("value after conversion=",y)	