from Helpers import *
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
			code = str(IntLit(fullpath))
		elif isValueExpression(child):
			code = str(ValueExpression(fullpath))
		elif isFuncCall(child):
			code = str(FuncCall(fullpath))



	def __str__(self):
		code = 'def ' + self.name + ':\n'

		return code
