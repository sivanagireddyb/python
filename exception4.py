#!/usr/bin/python

def divide(x,y):
	try:
	  result=x/y
	except ZeroDivisionError:
 	  print"division bu zero"
	else:
	  print "result is" , result
	finally:
	  print "finally excecuted"

divide(1,2)
divide(1,0)
