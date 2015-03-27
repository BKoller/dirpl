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
	expressions = os.listdir(root)
	expressions.sort()
	for child in expressions:
		if child.isalpha():
			fullpath = root + '/' + child
			child = os.listdir(fullpath)[0]
			fullpath = fullpath + '/' + child
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

def makeStdLib():
	print('count = len')
	print('def join(l1, l2): return l1 + l2')
	print('def part(l, i, j): return l[i:j]')
	print('def first(l): return l[0]')
	print('def last(l): return l[-1]')

def main():
	if len(sys.argv) != 2:
		print('usage: ' + argv[0] + ' <program directory>')
		return -1
	root = sys.argv[1]
	makeStdLib()
	walk(root)
	return 0

if __name__ == "__main__":
	main()
