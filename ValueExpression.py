from Helpers import *
from IntLit import *
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
		if self.functor == 'ifelse':
			code = str(self.args[1]) + ' if '
			code += str(self.args[0]) + ' else '
			code += str(self.args[2])
		else:
			code = self.functor + '('
			code += ', '.join([str(e) for e in self.args]) + ')'
		return code

class Definition:
	def __init__(self, path):
		self.path = path 
		parts = path.split('/')[-1].split('_')
		self.name = parts[0].lstrip(':')
		self.formals = parts[1:]
		self.cache = self.name + '.d'
		self.walk()

	def walk(self):
		child = os.listdir(self.path)[0]
		fullpath = self.path + '/' + child
		if isIntLit(child):
			self.body = IntLit(fullpath)
		elif isValueExpression(child):
			self.body = ValueExpression(fullpath)
		elif isFuncCall(child):
			self.body = FuncCall(fullpath)
		elif isVar(child):
			self.body = Var(fullpath)

	def __str__(self):
		formalstring = '(' + ','.join(self.formals)
		if len(self.formals) > 0:
			formalstring += ','
		formalstring += ')'
		code = 'def ' + self.name
		code += formalstring + ': \n'
		code += '\tif not ' + formalstring + ' in ' + self.cache + ':\n\t\t'
		code += self.cache + '[' + formalstring + '] = ' + str(self.body) + '\n\t'
		code += 'return ' + self.cache + '[' + formalstring + ']\n'
		code += self.cache + ' = {}'
		return code
