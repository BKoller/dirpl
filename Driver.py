from IntLit import *
from Var import *
from ValueExpression import *
from Helpers import *
import os, sys

def walk(root):
	for child in os.listdir(root):
		fullpath = root + '/' + child
		if isDefinition(child):
			print(Definition(fullpath))
	for child in os.listdir(root):
		fullpath = root + '/' + child
		if isIntLit(child):
			code = str(IntLit(fullpath))
			print('print("> ' + code + '")')
			print('print(' + code + ')')
		elif isValueExpression(child):
			code = str(ValueExpression(fullpath))
			print('print("> ' + code + '")')
			print('print(' + code + ')')
		elif isFuncCall(child):
			code = str(FuncCall(fullpath))
			print('print("> ' + code + '")')
			print('print(' + code + ')')

def main():
	if len(sys.argv) != 2:
		print('usage: ' + argv[0] + ' <program directory>')
		return -1
	root = sys.argv[1]
	walk(root)
	return 0

if __name__ == "__main__":
	main()
