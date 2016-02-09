import machine
import rotorsystem

def charToId(character):
	return ord(character.lower()) - 97

def stringToIds(string):
	return [charToId(character) for character in string]

def makeRotor(string, notchesChars=set(), advancingEnabled=True, doubleStepEnabled=False):
	notches = set(charToId(character) for character in notchesChars)
	return rotorsystem.Rotor(stringToIds(string), notches, advancingEnabled=advancingEnabled, doubleStepEnabled=doubleStepEnabled)

reflectorB = rotorsystem.Reflector(stringToIds("YRUHQSLDPXNGOKMIEBFZCWVJAT"))
reflectorC = rotorsystem.Reflector(stringToIds("FVPJIAOYEDRZXWGCTKUQSBNMHL"))
reflectorCThin = rotorsystem.Reflector(stringToIds("RDOBJNTKVEHMLFCWZAXGYIPSUQ"))
rotor1 = makeRotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ")
rotor2 = makeRotor("AJDKSIRUXBLHWTMCQGZNPYFVOE")
rotor3 = makeRotor("BDFHJLCPRTXVZNYEIWGAKMUSQO")
rotor5 = makeRotor("VZBRGITYUPSDNHLXAWMJQOFECK", {"D"})
rotor6 = makeRotor("JPGVOUMFYQBENHZRDKASXLICTW", {"Z", "M"}, doubleStepEnabled=True)
rotor8 = makeRotor("FKQHTLXOCBJSPDZRAMEWNIUYGV", {"Z", "M"})
rotorBeta = makeRotor("LEYJVCNIXWPBQMDRTAKZGFUHOS", advancingEnabled=False)

class StringEnigmaMachine(machine.EnigmaMachine):
	def __init__(self, symbols, *args):
		machine.EnigmaMachine.__init__(self, tuple(char for char in symbols), *args)
	def ringSetting(self, ringSettings):
		machine.EnigmaMachine.ringSetting(self, *tuple(char for char in ringSettings))
	def startPosition(self, startPositions):
		machine.EnigmaMachine.startPosition(self, *tuple(char for char in startPositions))
	def setCables(self, cables):
		splitCables = cables.split()
		machine.EnigmaMachine.setCables(self, *tuple((cable[0], cable[1]) for cable in splitCables))
	def feedSymbols(self, inputSymbols):
		return "".join(machine.EnigmaMachine.feedSymbols(self, inputSymbols))