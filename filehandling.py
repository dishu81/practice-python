# var1=open("intro.txt","a")
# var1.write ("disha malviya")
# var1.close()
# var1=open("intro.txt","r")
# data=var1.read()
# print(data)
# var1.close()
f=open("telephone.txt","a")
name=input("enter your name:")
age=input("enter your age:")
city=input("enter your city:")
detail="Hi I am {}. I am{} year old.\n I live in{}.".format(name,age,city)
print(detail)
f.write(detail)
f.close()
f=open("telephone.txt","r")
data= f.read()                            
print(data)
f.close
