def isIntLit(name):
	return name.isdigit()

def isDefinition(name):
	return name[0] == ':'

def isValueExpression(name):
	return name in ValueExpression.BIN_OPS or name.isalpha()
