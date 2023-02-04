# class student:
# 	def __init__(self, name, course, subject):
# 		self.name=name
# 		self.course=course
# 		self.subject=subject
# 	def show(self):
# 		print("name:",self.name)
# 		print("course:",self.course)
# 		print("subject:",self.subject)
# s1=student("disha","bca","python")
# s1.show()

class student:
	def __init__(self):
		self.name=input("enter name:")
		self.course=input("enter course:")
		self.subject=input("enter subject:")
	def show(self):
		print("name:",self.name)
		print("course:",self.course)
		print("subject:",self.subject)
s1=student()
s1.show()