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
		self.toStrings = {
				'ifelse':self.ifelseStr,
				}
	
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
			elif isListLit(child):
				self.args.append(ListLit(fullpath))

	def ifelseStr(self):
		code = str(self.args[1]) + ' if '
		code += str(self.args[0]) + ' else '
		code += str(self.args[2])
		return code

	def definedStr(self):
		code = self.functor + '('
		code += ', '.join([str(e) for e in self.args]) + ')'
		return code

	def __str__(self):
		return self.toStrings.get(self.functor, self.definedStr)()

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
		elif isListLit(child):
			self.body = ListLit(fullpath)

	def __str__(self):
		formalstring = '(' + ','.join(self.formals)
		if len(self.formals) > 0:
			formalstring += ','
		formalstring += ')'
		code = 'def ' + self.name
		code += formalstring + ': \n'
		code += '\ttry:\n'
		code += '\t\tif not ' + formalstring + ' in ' + self.cache + ':\n\t\t\t'
		code += self.cache + '[' + formalstring + '] = ' + str(self.body) + '\n\t'
		code += 'except:\n\t\t'
		code += 'return ' + str(self.body) + '\n\t'
		code += 'return ' + self.cache + '[' + formalstring + ']\n'
		code += self.cache + ' = {}'
		return code

class ListLit:
	def __init__(self, path):
		self.path = path
		self.elems = []
		self.walk()
	
	def walk(self):
		children = [int(c) for c in os.listdir(self.path)]
		children.sort()
		children = [str(c) for c in children]
		for child in children:
			fullpath = self.path + '/' + child
			child = os.listdir(fullpath)[0]
			fullpath = fullpath + '/' + child
			if isIntLit(child):
				self.elems.append(IntLit(fullpath))
			elif isValueExpression(child):
				self.elems.append(ValueExpression(fullpath))
			elif isFuncCall(child):
				self.elems.append(FuncCall(fullpath))
			elif isVar(child):
				self.elems.append(Var(fullpath))

	def __str__(self):
		code = '[' + ', '.join([str(e) for e in self.elems]) + ']'
		return code

class Lambda:
	def __init__(self, path):
		self.path = path 
		parts = path.split('/')[-1].split('_')
		self.formals = parts[1:]
		self.walk()

	def walk(self):
		children = os.listdir(self.path)
		children.sort()
		self.isCall = True if len(children) == 2 else False
		fullpath = self.path + '/' + children[0]
		child = os.listdir(fullpath)[0]
		fullpath = fullpath + '/' + child
		if isIntLit(child):
			self.body = IntLit(fullpath)
		elif isValueExpression(child):
			self.body = ValueExpression(fullpath)
		elif isFuncCall(child):
			self.body = FuncCall(fullpath)
		elif isVar(child):
			self.body = Var(fullpath)
		elif isListLit(child):
			self.body = ListLit(fullpath)		
		if self.isCall:
			fullpath = self.path + '/' + children[1]
			child = os.listdir(fullpath)[0]
			fullpath = fullpath + '/' + child
			if isIntLit(child):
				self.arg = IntLit(fullpath)
			elif isValueExpression(child):
				self.arg = ValueExpression(fullpath)
			elif isFuncCall(child):
				self.arg = FuncCall(fullpath)
			elif isVar(child):
				self.arg = Var(fullpath)
			elif isListLit(child):
				self.arg = ListLit(fullpath)		
	def __str__(self):
		formalstring = ','.join(self.formals)
		code = '(lambda ' + formalstring + ' : ' + str(self.body) + ')'
		if self.isCall:
			code += '(' + str(arg) + ')'
		return code
