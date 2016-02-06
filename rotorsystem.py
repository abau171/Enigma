class Rotor:
	def __init__(self, forwardMapping, notches=set()):
		self.notches = notches
		self.numSymbols = len(forwardMapping)
		self.forwardMapping = forwardMapping
		self.backwardMapping = [None] * len(forwardMapping)
		for i in range(len(self.forwardMapping)):
			self.backwardMapping[self.forwardMapping[i]] = i
		self.rotation = 0
	def _add(self, a, b):
		return (a + b) % self.numSymbols
	def rotate(self, dRotation):
		self.rotation = self._add(self.rotation, dRotation)
	def feedForward(self, symbolId):
		return self._add(-self.rotation, self.forwardMapping[self._add(self.rotation, symbolId)])
	def feedBackward(self, symbolId):
		return self._add(-self.rotation, self.backwardMapping[self._add(self.rotation, symbolId)])
	def advance(self):
		advanceNext = False
		if self.rotation in self.notches:
			advanceNext = True
		self.rotate(1)
		return advanceNext

class Reflector:
	def __init__(self, mapping):
		self.mapping = mapping
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
		for rotor in self.rotors:
			advanceNext = rotor.advance()
			if not advanceNext:
				break
		return curSymbolId
