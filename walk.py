import os

class Definition:
	def __init__(self, dirname):
		self.dirname = dirname
		parts = dirname.split('_')
		self.name = parts[0].lstrip(':')
		self.formals = parts[1:]

	def walk(self):
		...

	def __str__(self):
		code = 'def ' + self.name + ':\n'

		return code

class ValueExpression:
	def __init__(self):
		...

	def walk(self):
		...

	def __str__(self):
		...

def isFuncDef(name):
	return name[0] == ':'

def walk(root, expressions):
	for child in os.listdir(root):
		fullpath = root + '/' + child
		if isFuncDef(child):
			expressions.append(Definition(child))

def main():
	root = "./test"
	expressions = []
	walk(root, expressions)
	for expr in expressions:
		print(expr)

if __name__ == "__main__":
	main()
