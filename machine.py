import rotorsystem, plugboard

class EnigmaMachine:
	def __init__(self, symbols, reflector, *rotors):
		self.symbols = symbols
		self.rotorSystem = rotorsystem.RotorSystem(reflector, *rotors)
		self.plugBoard = plugboard.PlugBoard(len(self.symbols))
		self.symbolIds = dict()
		for i in range(len(self.symbols)):
			symbol = self.symbols[i]
			self.symbolIds[symbol] = i
	def getSymbol(self, symbolId):
		return self.symbols[symbolId]
	def getSymbolId(self, symbol):
		return self.symbolIds[symbol]
	def ringSetting(self, *ringSettings):
		convertedRingSettings = tuple(self.getSymbolId(symbol) for symbol in ringSettings)
		self.rotorSystem.ringSetting(*convertedRingSettings)
	def startPosition(self, *startPositions):
		convertedStartPositions = tuple(self.getSymbolId(symbol) for symbol in startPositions)
		self.rotorSystem.startPosition(*convertedStartPositions)
	def setCables(self, *cables):
		convertedCables = tuple((self.getSymbolId(a), self.getSymbolId(b)) for a, b in cables)
		self.plugBoard.setCables(*convertedCables)
	def feedSymbol(self, inputSymbol):
		curSymbolId = self.getSymbolId(inputSymbol)
		curSymbolId = self.plugBoard.feed(curSymbolId)
		curSymbolId = self.rotorSystem.feed(curSymbolId)
		curSymbolId = self.plugBoard.feed(curSymbolId)
		return self.getSymbol(curSymbolId)
	def feedSymbols(self, inputSymbols):
		result = [self.feedSymbol(inputSymbol) for inputSymbol in inputSymbols]
		return result
