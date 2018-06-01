class Student:
	def __init__(self,rollno,name):
		self.rollno=rollno
		self.name=name
	def print(self):
		print("Rollno : {} , name : {} ".format(self.rollno,self.name))	

emp1 = Student(121,"sourav")
emp2 = Student(122,"shaurya")
emp1.print()
emp2.print()
