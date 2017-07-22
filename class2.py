#!/usr/bin/python
# so here we creating constructor and method for make it easy and reusable

class Employee:
	
	num_of_employee=0	

	raise_amount = 1.04 #class variable

	def __init__(self,first,last,pay):#constructor
		self.fname=first #instance variables
		self.lname=last
		self.email=self.fname + '.' + self.lname + '@gmail.com'
		self.sal=pay
		
		Employee.num_of_employee += 1		

	def fullname(self): #function or method
		return '{} {}'.format(self.fname, self.lname)
	
	def apply_raise(self):
		self.pay = int(self.sal * Employee.raise_amount ) 

emp1=Employee('siva','nagireddy',5000)
emp2=Employee('nsre','reddy',70000)


emp1.raise_amount=1.05 #do we can change instance vslues individually

print (emp1.email)
print emp2.sal
print (emp1.fullname())
print (emp2.fullname())

print(emp1.sal)
print (emp1.raise_amount)
emp1.apply_raise()
print (emp1.pay)

print(emp2.raise_amount)
emp2.apply_raise()
print emp2.pay

print Employee.num_of_employee

print(emp1.__dict__) #this is to print name pace of employee 1, here raise_amount is instance variable bcz we declared it#




 
print(emp2.__dict__)# it is class variable ,didnt declared for emp2 seperatly


print(Employee.__dict__)
