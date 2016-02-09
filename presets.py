import machine
import rotorsystem

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class StringRotor(rotorsystem.Rotor):
	def __init__(self, symbols, forwardMapping, notches=set(), advancingEnabled=True, doubleStepEnabled=False):
		charIds = {symbols[charId]: charId for charId in range(len(symbols))}
		convertedForwardMapping = [charIds[char] for char in forwardMapping]
		convertedNotches = set(charIds[char] for char in notches)
		rotorsystem.Rotor.__init__(self, convertedForwardMapping, convertedNotches, advancingEnabled=advancingEnabled, doubleStepEnabled=doubleStepEnabled)

def genAlphabetRotor(forwardMapping, notches=set(), advancingEnabled=True, doubleStepEnabled=False):
	class AlphabetRotor(StringRotor):
		def __init__(self):
			StringRotor.__init__(self, alphabet, forwardMapping, notches, advancingEnabled=advancingEnabled, doubleStepEnabled=doubleStepEnabled)
	return AlphabetRotor

class StringReflector(rotorsystem.Reflector):
	def __init__(self, symbols, mapping):
		charIds = {symbols[charId]: charId for charId in range(len(symbols))}
		convertedMapping = [charIds[char] for char in mapping]
		rotorsystem.Reflector.__init__(self, convertedMapping)

def genAlphabetReflector(mapping):
	class AlphabetReflector(StringReflector):
		def __init__(self):
			StringReflector.__init__(self, alphabet, mapping)
	return AlphabetReflector

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
		return "".join(machine.EnigmaMachine.feedSymbols(self, [char for char in inputSymbols]))

Rotor1 = genAlphabetRotor("RDOBJNTKVEHMLFCWZAXGYIPSUQ")
Rotor2 = genAlphabetRotor("AJDKSIRUXBLHWTMCQGZNPYFVOE")
Rotor3 = genAlphabetRotor("BDFHJLCPRTXVZNYEIWGAKMUSQO")
Rotor4 = genAlphabetRotor("ESOVPZJAYQUIRHXLNFTGKDCMWB")
Rotor5 = genAlphabetRotor("VZBRGITYUPSDNHLXAWMJQOFECK", {"D"}, doubleStepEnabled=True)
Rotor6 = genAlphabetRotor("JPGVOUMFYQBENHZRDKASXLICTW", {"Z", "M"}, doubleStepEnabled=True)
Rotor7 = genAlphabetRotor("NZJHGRCXMYSWBOUFAIVLPEKQDT")
Rotor8 = genAlphabetRotor("FKQHTLXOCBJSPDZRAMEWNIUYGV", {"Z", "M"}, doubleStepEnabled=True)
RotorBeta = genAlphabetRotor("LEYJVCNIXWPBQMDRTAKZGFUHOS", advancingEnabled=False)
RotorGamma = genAlphabetRotor("FSOKANUERHMBTIYCWLQPZXVGJD", advancingEnabled=False)

ReflectorA = genAlphabetReflector("EJMZALYXVBWFCRQUONTSPIKHGD")
ReflectorB = genAlphabetReflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
ReflectorC = genAlphabetReflector("FVPJIAOYEDRZXWGCTKUQSBNMHL")
ReflectorBThin = genAlphabetReflector("ENKQAUYWJICOPBLMDXZVFTHRGS")
ReflectorCThin = genAlphabetReflector("RDOBJNTKVEHMLFCWZAXGYIPSUQ")
