#!/usr/bin/python
def function(level):
	if level<1:
		raise Exception(level)
		#this code below is not excecuted
		#if we raise exception
	else:
		print ("its tru so exception not raised")
	return level
try:
   i=function(-10)
#   i=function(6)
   print("level", i)

except Exception as e:
  print("error in level arg" , e.args[0])
