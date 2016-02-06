import random
import rotorsystem
import plugboard
import machine

def randomRotor(numSymbols, numNotches):
	forwardMapping = [symbolId for symbolId in range(numSymbols)]
	random.shuffle(forwardMapping)
	possibleNotches = set(symbolId for symbolId in range(numSymbols))
	notches = set()
	for _ in range(numNotches):
		notch = random.choice(tuple(possibleNotches))
		possibleNotches.remove(notch)
		notches.add(notch)
	return rotorsystem.Rotor(forwardMapping, notches)

def randomReflector(numSymbols):
	symbolIds = set(symbolId for symbolId in range(numSymbols))
	mapping = [None] * 26
	while len(symbolIds) > 0:
		a = random.choice(tuple(symbolIds))
		symbolIds.remove(a)
		b = random.choice(tuple(symbolIds))
		symbolIds.remove(b)
		mapping[a] = b
		mapping[b] = a
	return rotorsystem.Reflector(mapping)

def randomRotorSystem(numSymbols, numRotors, numNotchesPerRotor):
	rotors = tuple(randomRotor(numSymbols, numNotchesPerRotor) for _ in range(numRotors))
	reflector = randomReflector(numSymbols)
	return rotorsystem.RotorSystem(reflector, *rotors)

def randomPlugBoard(numSymbols, numCables):
	plugBoard = plugboard.PlugBoard(26)
	unused = set(symbolId for symbolId in range(numSymbols))
	for _ in range(numCables):
		a = random.choice(tuple(unused))
		unused.remove(a)
		b = random.choice(tuple(unused))
		unused.remove(b)
		plugBoard.addCable(a, b)
	return plugBoard

def randomEnigmaMachine(symbols, numRotors, numNotchesPerRotor, numCables):
	numSymbols = len(symbols)
	rotorSystem = randomRotorSystem(numSymbols, numRotors, numNotchesPerRotor)
	plugBoard = randomPlugBoard(numSymbols, numCables)
	return machine.EnigmaMachine(symbols, rotorSystem, plugBoard)

if __name__=="__main__":
	random.seed(0)
	m = randomEnigmaMachine("abcdefghijklmnopqrstuvwxyz", 3, 1, 10)
	print(m.feedSymbols("vqwexhfdxbden"))