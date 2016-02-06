class Rotor:
	def __init__(self, *mapDef):
		self.numSymbols = len(mapDef)
		self._validateMapping(mapDef)
		self.forwardMapping = {a: b for (a, b) in mapDef}
		self.backwardMapping = {b: a for (a, b) in mapDef}
		self.rotation = 0
	def _validateMapping(self, mapDef):
		sources = set(symbolId for symbolId in range(self.numSymbols))
		targets = set(symbolId for symbolId in range(self.numSymbols))
		for (a, b) in mapDef:
			assert a in sources
			sources.remove(a)
			assert b in targets
			targets.remove(b)
		assert len(sources) == 0 and len(targets) == 0
	def _add(self, a, b):
		return (a + b) % self.numSymbols
	def rotate(self, dRotation):
		self.rotation = self._add(self.rotation, dRotation)
	def feedForward(self, symbolId):
		return self._add(-self.rotation, self.forwardMapping[self._add(self.rotation, symbolId)])
	def feedBackward(self, symbolId):
		return self._add(-self.rotation, self.backwardMapping[self._add(self.rotation, symbolId)])

class Reflector:
	def __init__(self, *mapDef):
		self.numSymbols = len(mapDef) * 2
		self._validateMapping(mapDef)
		self.mapping = dict()
		for (a, b) in mapDef:
			self.mapping[a] = b
			self.mapping[b] = a
	def _validateMapping(self, mapDef):
		symbolIds = set(symbolId for symbolId in range(self.numSymbols))
		for (a, b) in mapDef:
			assert a in symbolIds
			symbolIds.remove(a)
			assert b in symbolIds
			symbolIds.remove(b)
		assert len(symbolIds) == 0
	def feed(self, symbolId):
		return self.mapping[symbolId]

class RotorSystem:
	def __init__(self, reflector, *rotors):
		self.reflector = reflector
		self.rotors = rotors
	def feed(self, symbolId):
		curSymbolId = symbolId
		for rotor in self.rotors:
			curSymbolId = rotor.feedForward(curSymbolId)
		curSymbolId = self.reflector.feed(curSymbolId)
		for rotor in reversed(self.rotors):
			curSymbolId = rotor.feedBackward(curSymbolId)
		return curSymbolId
