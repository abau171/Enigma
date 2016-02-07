import rotorsystem, plugboard, machine
import presets

rotors = (presets.rotor8, presets.rotor6, presets.rotor5, presets.rotorBeta)
rs = rotorsystem.RotorSystem(presets.reflectorCThin, *rotors)
rotors[3].rotate(13)
rotors[3].setRingRotation(4)
rotors[2].rotate(0)
rotors[2].setRingRotation(15)
rotors[1].rotate(4)
rotors[1].setRingRotation(4)
rotors[0].rotate(12)
rotors[0].setRingRotation(11)

def addCable(pb, letters):
	letters = letters.lower()
	pb.addCable(ord(letters[0])-97, ord(letters[1])-97)

pb = plugboard.PlugBoard(26)
addCable(pb, "AE")
addCable(pb, "BF")
addCable(pb, "CM")
addCable(pb, "DQ")
addCable(pb, "HU")
addCable(pb, "JN")
addCable(pb, "LX")
addCable(pb, "PR")
addCable(pb, "SZ")
addCable(pb, "VW")

m = machine.EnigmaMachine("abcdefghijklmnopqrstuvwxyz", rs, pb)
print(m.feedSymbols("qeob"))
