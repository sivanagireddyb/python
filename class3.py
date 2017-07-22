#!/usr/bin/python

class sample:
	def __init__(self,name,sur,age):
		self.peru=name
		self.inti=sur
		self.vay=age
	def fullname(self):
		return '{} {}'.format(emp1.peru, emp1.inti)

emp1=sample('siva','b',34)

print emp1.peru
print (emp1.fullname())
