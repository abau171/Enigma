import random
import dialsystem

def randomDial(numSymbols):
	targets = set(symbolId for symbolId in range(numSymbols))
	mapping = []
	for source in range(numSymbols):
		target = random.choice(tuple(targets))
		targets.remove(target)
		mapping.append((source, target))
	return dialsystem.Dial(*tuple(mapping))

def randomReflector(numSymbols):
	symbolIds = set(symbolId for symbolId in range(numSymbols))
	mapping = []
	while len(symbolIds) > 0:
		a = random.choice(tuple(symbolIds))
		symbolIds.remove(a)
		b = random.choice(tuple(symbolIds))
		symbolIds.remove(b)
		mapping.append((a, b))
	return dialsystem.Reflector(*tuple(mapping))

def randomDialSystem(numSymbols, numDials):
	dials = tuple(randomDial(numSymbols) for _ in range(numDials))
	reflector = randomReflector(26)
	return dialsystem.DialSystem(reflector, *dials)
