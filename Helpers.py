BIN_OPS = {'\\\\':'//', '%':'%', '<=':'<=', '>=': '>=','<':'<', '>': '>', '==':'==', '!=':'!=', '|':'or',
			'&':'and', '-':'-', '+':'+', '*':'*', '\\':'/'}

def isIntLit(name):
	return name.isdigit()

def isDefinition(name):
	return name[0] == ':'

def isFuncCall(name):
	return name.endswith('()')

def isValueExpression(name):
	return name in BIN_OPS 

def isVar(name):
	return name.isalpha()
