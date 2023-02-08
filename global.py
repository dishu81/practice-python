def myfunction():
		global i
 		x=int(input("enter value:"))           
 		y=int(input("enter value:"))
 		z=x+y
   		print(z)
		i="I am inside"
		#print(id(i))
 

i="I am fine"
#print(id(i))
print(i)     
myfunction()
print(i)
# being z a local bariable it cant accesed outside my myfunction