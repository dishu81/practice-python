var1=open("blank.txt","w")
english=int(input("enter your english marks"))
hindi=int(input("enter your hindi marks"))
maths=int(input("enter your maths marks"))
detail="{},{},{}.".format(english, hindi,maths)
print(detail)
var1.write(detail)
var1.close()

var1=open("blank.txt","r")
data=var1.read()
print(data)
record=data.split(" , ")
print(record)
var1.close()

# var1=open("blank.txt","a")
# add=english+hindi+maths
# detail="total={}/n.".format(english+hindi+maths)
# print(detail)
# var1.write(detail)
# var1.close()

# var1=open("blank.txt","a")
# avg=(english+hindi+maths)/3
# detail="avg={}.".format(english+hindi+maths)
# peint(detail)
# var1.write(detail)
# var1.close()
 