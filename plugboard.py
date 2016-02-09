class PlugBoard:
	def __init__(self, numSymbols):
		self.numSymbols = numSymbols
		self.mapping = dict()
	def addCables(self, *cables):
		for cable in cables:
			self.addCable(cable)
	def addCable(self, cable):
		a, b = cable
		assert a < self.numSymbols and b < self.numSymbols
		assert a not in self.mapping or b not in self.mapping
		self.mapping[a] = b
		self.mapping[b] = a
	def removeCableAt(self, a):
		if a in self.mapping:
			b = self.mapping[a]
			del self.mapping[a]
			del self.mapping[b]
	def removeAllCables(self):
		self.mapping = dict()
	def feed(self, symbolId):
		if symbolId in self.mapping:
			return self.mapping[symbolId]
		return symbolId
