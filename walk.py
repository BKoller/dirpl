from IntLit import IntLit
from Var import Var
from Definition import Definition
from ValueExpression import ValueExpression
from FuncCall import FuncCall
from Helpers import *
import os

def walk(root):
	for child in os.listdir(root):
		fullpath = root + '/' + child
		if isDefinition(child):
			print(Definition(fullpath))
	for child in os.listdir(root):
		fullpath = root + '/' + child
		if isIntLit(child):
			code = str(IntLit(fullpath))
			print('print("' + code + '")')
			print('print(' + code + ')')
		elif isValueExpression(child):
			code = str(ValueExpression(fullpath))
			print('print("' + code + '")')
			print('print(' + code + ')')
		elif isFuncCall(child):
			code = str(FuncCall(fullpath))
			print('print("' + code + '")')
			print('print(' + code + ')')

def main():
	root = "./test"
	walk(root)

if __name__ == "__main__":
	main()
