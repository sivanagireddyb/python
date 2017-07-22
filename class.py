#!/usr/bin/python
# this is not good method bcz mistakes can take place while passing para meteres/individiually all time
class Employee():
	pass
emp_1=Employee()
emp_2=Employee()

print emp_1
print emp_2


emp_1.first='user'
emp_1.last='bu'
emp_1.pay='user.pu@company.mail'
emp_1.mail=10000


emp_2.first='user'
emp_2.last='bu'
emp_2.mail='gmail.com'
emp_2.pay=2000

print emp_1.mail
print emp_2.mail
