class BidirectionalMapping:
	def __init__(self, forwardMapping):
		self.forwardMapping = forwardMapping
		self.backwardMapping = [None] * len(self.forwardMapping)
		for i in range(len(self.forwardMapping)):
			self.backwardMapping[self.forwardMapping[i]] = i
	def __len__(self):
		return len(self.forwardMapping)
	def feedForward(self, symbolId):
		return self.forwardMapping[symbolId]
	def feedBackward(self, symbolId):
		return self.backwardMapping[symbolId]

def _rotationCorrect(feedFcn):
	def wrapped(self, symbolId):
		rotatedId = (symbolId + self.rotation) % len(self.mapping)
		outputId = feedFcn(self, rotatedId)
		unrotatedOutputId = (outputId - self.rotation) % len(self.mapping)
		return unrotatedOutputId
	return wrapped

class RotatorMapping:
	def __init__(self, mapping):
		self.mapping = mapping
		self.rotation = 0
	def __len__(self):
		return len(self.mapping)
	def getRotation(self):
		return self.rotation
	def setRotation(self, rotation):
		self.rotation = rotation % len(self.mapping)
	def rotate(self, amount=1):
		self.rotation = (self.rotation + amount) % len(self.mapping)
	@_rotationCorrect
	def feedForward(self, symbolId):
		return self.mapping.feedForward(symbolId)
	@_rotationCorrect
	def feedBackward(self, symbolId):
		return self.mapping.feedBackward(symbolId)

class Rotor:
	def __init__(self, forwardMapping, notches=set(), advancingEnabled=True, doubleStepEnabled=False):
		self.notches = notches
		self.ringRotator = RotatorMapping(BidirectionalMapping(forwardMapping))
		self.rotorRotator = RotatorMapping(self.ringRotator)
		self.doubleStepEnabled = doubleStepEnabled
		self.advancingEnabled = advancingEnabled
	def getRotation(self):
		return self.rotorRotator.getRotation()
	def setRotation(self, rotation):
		self.rotorRotator.setRotation(rotation)
	def rotate(self, amount=1):
		self.rotorRotator.rotate(amount)
	def getRingRotation(self):
		return self.ringRotator.getRotation()
	def setRingRotation(self, rotation):
		self.ringRotator.setRotation(-rotation)
	def feedForward(self, symbolId):
		return self.rotorRotator.feedForward(symbolId)
	def feedBackward(self, symbolId):
		return self.rotorRotator.feedBackward(symbolId)
	def willStep(self):
		return self.rotorRotator.getRotation() in self.notches
	def willDoubleStep(self):
		return self.doubleStepEnabled and self.willStep()
	def twoAfterStep(self):
		self.rotorRotator.rotate(-2)
		willStep = self.willStep()
		self.rotorRotator.rotate(2)
		return willStep
	def advance(self):
		if self.advancingEnabled:
			advanceNext = self.willStep()
			self.rotate()
			return advanceNext
		return False

class Reflector:
	def __init__(self, mapping):
		self.mapping = mapping
	def feed(self, symbolId):
		return self.mapping[symbolId]

class RotorSystem:
	def __init__(self, reflector, *rotors):
		self.reflector = reflector
		self.rotors = tuple(reversed(rotors))
	def advanceRotors(self):
		isDoubleStep = False
		for rotor in self.rotors:
			if not isDoubleStep or (isDoubleStep and rotor.willDoubleStep()):
				advanceNext = rotor.advance()
				isDoubleStep = rotor.twoAfterStep()
			else:
				advanceNext = False
				isDoubleStep = False
			if not advanceNext and not isDoubleStep:
				break
	def feed(self, symbolId):
		self.advanceRotors()
		curSymbolId = symbolId
		for rotor in self.rotors:
			curSymbolId = rotor.feedForward(curSymbolId)
		curSymbolId = self.reflector.feed(curSymbolId)
		for rotor in reversed(self.rotors):
			curSymbolId = rotor.feedBackward(curSymbolId)
		return curSymbolId
