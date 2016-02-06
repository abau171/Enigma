class EnigmaMachine:
	def __init__(self, symbolList, rotorSystem, plugBoard):
		self.symbolList = symbolList
		self.rotorSystem = rotorSystem
		self.plugBoard = plugBoard
		self.symbolIdMap = dict()
		for i in range(len(symbolList)):
			symbol = symbolList[i]
			self.symbolIdMap[symbol] = i
	def feedSymbol(self, symbol):
		curSymbolId = self.symbolIdMap[symbol]
		curSymbolId = self.plugBoard.feed(curSymbolId)
		curSymbolId = self.rotorSystem.feed(curSymbolId)
		curSymbolId = self.plugBoard.feed(curSymbolId)
		return self.symbolList[curSymbolId]
	def feedSymbols(self, symbols):
		result = ""
		for symbol in symbols:
			result += self.feedSymbol(symbol)
		return result
