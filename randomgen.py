import random
import rotorsystem
import plugboard
import machine

def randomRotor(numSymbols):
	targets = set(symbolId for symbolId in range(numSymbols))
	mapping = []
	for source in range(numSymbols):
		target = random.choice(tuple(targets))
		targets.remove(target)
		mapping.append((source, target))
	return rotorsystem.Rotor(*tuple(mapping))

def randomReflector(numSymbols):
	symbolIds = set(symbolId for symbolId in range(numSymbols))
	mapping = []
	while len(symbolIds) > 0:
		a = random.choice(tuple(symbolIds))
		symbolIds.remove(a)
		b = random.choice(tuple(symbolIds))
		symbolIds.remove(b)
		mapping.append((a, b))
	return rotorsystem.Reflector(*tuple(mapping))

def randomRotorSystem(numSymbols, numRotors):
	rotors = tuple(randomRotor(numSymbols) for _ in range(numRotors))
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

def randomEnigmaMachine(symbols, numRotors, numCables):
	numSymbols = len(symbols)
	rotorSystem = randomRotorSystem(numSymbols, numRotors)
	plugBoard = randomPlugBoard(numSymbols, numCables)
	return machine.EnigmaMachine(symbols, rotorSystem, plugBoard)

if __name__=="__main__":
	random.seed(0)
	m = randomEnigmaMachine("abcdefghijklmnopqrstuvwxyz", 3, 10)
	print(m.feedSymbols("jclhpolqwpeql"))