#!/usr/bin/python
def function(list):
	print("print value before fun change:", list)
	list[2]=100
	print("values inside funcyion after change:", list)
	return
list=[10,20,30]
function(list)
print("values outside function aftere change:", list)
