from IntLit import IntLit
from Var import Var
from Definition import Definition
from ValueExpression import ValueExpression
from Helpers import *
import os

def walk(root, expressions):
	for child in os.listdir(root):
		fullpath = root + '/' + child
		if isIntLit(child):
			expressions.append(IntLit(fullpath))
		elif isDefinition(child):
			expressions.append(Definition(fullpath))
		elif isValueExpression(child):
			expressions.append(ValueExpression(fullpath))

def main():
	root = "./test"
	expressions = []
	walk(root, expressions)
	for expr in expressions:
		print(expr)

if __name__ == "__main__":
	main()
