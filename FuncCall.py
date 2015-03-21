from Helpers import *
from IntLit import IntLit
from Var import Var
from ValueExpression import *
import os

class FuncCall:
	def __init__(self, path):
		self.path = path
		self.functor = path.split('/')[-1][:-2]
		self.args = []
		self.walk()

	def walk(self):
		children = os.listdir(self.path)
		children.sort()
		for child in children:
			fullpath = self.path + '/' + child
			child = os.listdir(fullpath)[0]
			fullpath = fullpath + '/' + child
			if isIntLit(child):
				self.args.append(IntLit(fullpath))
			elif isValueExpression(child):
				self.args.append(ValueExpression(fullpath))
			elif isFuncCall(child):
				self.args.append(FuncCall(fullpath))
			elif isVar(child):
				self.args.append(Var(fullpath))

	def __str__(self):
		code = self.functor + "("
		code += ', '.join([str(e) for e in self.args])
		code += ")"
		return code
