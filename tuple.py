tuple1=(25,10,25.5,"star wars")
for i in tuple1:
	print("index=",tuple1.index(i))
	print("value=", i)
	print("type=",type(i))
	print("id=", id(i))
tuple1.append("disha")
print(tuple1.pop)	

