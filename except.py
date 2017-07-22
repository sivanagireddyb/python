#!/usr/bin/python
def temp_convert(var):
	try:
		return int(var)

	except ValueError:
		print ("the argument does not contain numbers" , var)
#	else:
#		prnit (" int")	
#call function

temp_convert("xyz")
