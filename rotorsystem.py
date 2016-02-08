class Rotor:
	def __init__(self, forwardMapping, notches=set(), canBeAdvanced=True, canDoubleStep=False):
		self.notches = notches
		self.numSymbols = len(forwardMapping)
		self.forwardMapping = forwardMapping
		self.backwardMapping = [None] * len(forwardMapping)
		for i in range(len(self.forwardMapping)):
			self.backwardMapping[self.forwardMapping[i]] = i
		self.rotation = 0
		self.ringRotation = 0
		self.canDoubleStep = canDoubleStep
		self.canBeAdvanced = canBeAdvanced
	def _add(self, a, b):
		return (a + b) % self.numSymbols
	def setRotation(self, rotation):
		self.rotation = rotation
	def rotate(self, dRotation):
		self.rotation = self._add(self.rotation, dRotation)
	def setRingRotation(self, ringRotation):
		self.ringRotation = ringRotation
	def feedForward(self, symbolId):
		wireRot = self.rotation - self.ringRotation
		return self._add(-wireRot, self.forwardMapping[self._add(wireRot, symbolId)])
	def feedBackward(self, symbolId):
		wireRot = self.rotation - self.ringRotation
		return self._add(-wireRot, self.backwardMapping[self._add(wireRot, symbolId)])
	def willStep(self):
		return self.rotation in self.notches
	def twoAfterStep(self):
		return self._add(self.rotation, -2) in self.notches
	def advance(self):
		advanceNext = False
		if self.willStep():
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
		advanceNext = True
		for rotorNum in range(len(self.rotors)):
			lastRotor = None if rotorNum - 1 < 0 else self.rotors[rotorNum - 1]
			rotor = self.rotors[rotorNum]
			doubleStep = False
			if lastRotor and rotor.canDoubleStep:
				doubleStep = lastRotor.twoAfterStep() and rotor.willStep()
			if (advanceNext or doubleStep) and rotor.canBeAdvanced:
				advanceNext = rotor.advance()
		curSymbolId = symbolId
		for rotor in self.rotors:
			curSymbolId = rotor.feedForward(curSymbolId)
		curSymbolId = self.reflector.feed(curSymbolId)
		for rotor in reversed(self.rotors):
			curSymbolId = rotor.feedBackward(curSymbolId)
		return curSymbolId
