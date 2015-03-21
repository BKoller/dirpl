from Helpers import *
import os

class ValueExpression:

	BIN_OPS = {'<':'<', '>': '>', '==':'==', '!=':'!=', '|':'or',
			'&':'and', '-':'-', '+':'+', '*':'*', '\\':'/'}

	def __init__(self, path):
		self.path = path
		self.op = ValueExpression.BIN_OPS[path.split('/')[-1]]
		self.rands = []

	def walk(self):
		for child in os.listdir(root):


	def __str__(self):
		return "(%s %s %s)" % (self.rands[0], self.op, self.rands[1])

