BIN_OPS = {'\\\\':'//', '%':'%', '<=':'<=', '>=': '>=','<':'<', '>': '>', '==':'==', '!=':'!=', '|':'or',
			'&':'and', '-':'-', '+':'+', '*':'*', '\\':'/'}

RESERVED = ('ifelse', 'count', 'join', 'part', 'first', 'last')

def isIntLit(name):
	return name.isdigit() or (name[0] == '-' and name[1:].isdigit())

def isDefinition(name):
	if len(name) == 1:
		return False
	if name[1:] in RESERVED or name[1:] in BIN_OPS:
		return False
	return name[0] == ':' and name[1] != '_'

def isFuncCall(name):
	return name.endswith('()')

def isValueExpression(name):
	return name in BIN_OPS

def isVar(name):
	return name.isalpha()

def isListLit(name):
	return name == '@'

def isLambda(name):
	return name == ':' or (name[0] == ':' and name[1] == '_')
