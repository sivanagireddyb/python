#!/usr/bin/python
# Exception handling

try:
  fh = open("exception.txt","r")
  fh.write("this is test file for exception handling")
except IOError:
  print("ERROR:cant find file or read data")

else:
  print("written sucsessfully")
  fh.close()
