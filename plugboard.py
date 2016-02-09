class PlugBoard:
	def __init__(self, numSymbols):
		self.numSymbols = numSymbols
		self.mapping = dict()
	def setCables(self, *cables):
		self.mapping = dict()
		for a, b in cables:
			self.mapping[a] = b
			self.mapping[b] = a
	def feed(self, symbolId):
		if symbolId in self.mapping:
			return self.mapping[symbolId]
		return symbolId
