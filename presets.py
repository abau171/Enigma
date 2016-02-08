import rotorsystem

def charToId(character):
	return ord(character.lower()) - 97

def stringToIds(string):
	return [charToId(character) for character in string]

def makeRotor(string, notchesChars=set(), canBeAdvanced=True, canDoubleStep=False):
	notches = set(charToId(character) for character in notchesChars)
	return rotorsystem.Rotor(stringToIds(string), notches, canBeAdvanced=canBeAdvanced, canDoubleStep=canDoubleStep)

reflectorB = rotorsystem.Reflector(stringToIds("YRUHQSLDPXNGOKMIEBFZCWVJAT"))
reflectorC = rotorsystem.Reflector(stringToIds("FVPJIAOYEDRZXWGCTKUQSBNMHL"))
reflectorCThin = rotorsystem.Reflector(stringToIds("RDOBJNTKVEHMLFCWZAXGYIPSUQ"))
rotor1 = makeRotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ")
rotor2 = makeRotor("AJDKSIRUXBLHWTMCQGZNPYFVOE")
rotor3 = makeRotor("BDFHJLCPRTXVZNYEIWGAKMUSQO")
rotor5 = makeRotor("VZBRGITYUPSDNHLXAWMJQOFECK", {"D"})
rotor6 = makeRotor("JPGVOUMFYQBENHZRDKASXLICTW", {"Z", "M"}, canDoubleStep=True)
rotor8 = makeRotor("FKQHTLXOCBJSPDZRAMEWNIUYGV", {"Z", "M"})
rotorBeta = makeRotor("LEYJVCNIXWPBQMDRTAKZGFUHOS", canBeAdvanced=False)
