#!/usr/bin/python
#scope
total=0 #global var
def sum(a,b):
	total=a+b #local var
	print"inside fun local",total
	return total
sum(10,20)
print"outside fun global",total
