from IntLit import IntLit
from Var import Var
from Definition import Definition
from ValueExpression import ValueExpression
import os

def isIntLit(name):
	return name.isdigit()

def isDefinition(name):
	return name[0] == ':'

def walk(root, expressions):
	for child in os.listdir(root):
		fullpath = root + '/' + child
		if isIntLit(child):
			expressions.append(IntLit(fullpath))
		elif isDefinition(child):
			expressions.append(Definition(fullpath))

def main():
	root = "./test"
	expressions = []
	walk(root, expressions)
	for expr in expressions:
		print(expr)

if __name__ == "__main__":
	main()
