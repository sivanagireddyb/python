#!/usr/bin/python
import sys
def Hello(name):
	if name=='siva':
		name=name		
		print name

	else:
		print("Doesnotexist",name)

def main():
	Hello(sys.argv[1])
if __name__ == '__main__':
	main()
