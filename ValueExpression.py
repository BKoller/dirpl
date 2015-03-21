from Helpers import *
from IntLit import *
from FuncCall import *
from Var import *
import os

class ValueExpression:	

	def __init__(self, path):
		self.path = path
		self.op = BIN_OPS[path.split('/')[-1]]
		self.rands = []
		self.walk()

	def walk(self):
		children = os.listdir(self.path)
		children.sort()
		for child in children:
			fullpath = self.path + '/' + child
			child = os.listdir(fullpath)[0]
			fullpath = fullpath + '/' + child
			if isIntLit(child):
				self.rands.append(IntLit(fullpath))
			elif isValueExpression(child):
				self.rands.append(ValueExpression(fullpath))
			elif isFuncCall(child):
				self.rands.append(FuncCall(fullpath))
			elif isVar(child):
				self.rands.append(Var(fullpath))

	def __str__(self):
		return "(%s %s %s)" % (self.rands[0], self.op, self.rands[1])

