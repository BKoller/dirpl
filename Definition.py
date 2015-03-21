from Helpers import *
from ValueExpression import ValueExpression
import os

class Definition:
	def __init__(self, path):
		self.path = path 
		parts = path.split('/')[-1].split('_')
		self.name = parts[0].lstrip(':')
		self.formals = parts[1:]
		self.walk()

	def walk(self):
		child = os.listdir(self.path)[0]
		if isIntLit(child):
			self.body = IntLit(fullpath)
		elif isValueExpression(child):
			self.body = ValueExpression(fullpath)
		elif isFuncCall(child):
			self.body = FuncCall(fullpath)
		elif isVar(child):
			self.body = Var(fullpath)

	def __str__(self):
		code = 'def ' + self.name
		code += '(' + ','.join(self.formals) + '): '
		code += 'return '
		code += str(self.body)

		return code
