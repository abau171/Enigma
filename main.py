import rotorsystem, plugboard, machine
import presets

rotors = (presets.rotorBeta, presets.rotor5, presets.rotor6, presets.rotor8)
rs = rotorsystem.RotorSystem(presets.reflectorCThin, *rotors)
rotors[0].setRotation(13)
rotors[0].setRingRotation(4)
rotors[1].setRotation(0)
rotors[1].setRingRotation(15)
rotors[2].setRotation(4)
rotors[2].setRingRotation(4)
rotors[3].setRotation(12)
rotors[3].setRingRotation(11)

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

rotors[0].setRotation(2)
rotors[1].setRotation(3)
rotors[2].setRotation(18)
rotors[3].setRotation(25)

print(m.feedSymbols("LANOTCTOUARBBFPMHPHGCZXTDYGAHGUFXGEWKBLKGJWLQXXTGPJJAVTOCKZFSLPPQIHZFXOEBWIIEKFZLCLOAQJULJOYHSSMBBGWHZANVOIIPYRBRTDJQDJJOQKCXWDNBBTYVXLYTAPGVEATXSONPNYNQFUDBBHHVWEPYEYDOHNLXKZDNWRHDUWUJUMWWVIIWZXIVIUQDRHYMNCYEFUAPNHOTKHKGDNPSAKNUAGHJZSMJBMHVTREQEDGXHLZWIFUSKDQVELNMIMITHBHDBWVHDFYHJOQIHORTDJDBWXEMEAYXGYQXOHFDMYUXXNOJAZRSGHPLWMLRECWWUTLRTTVLBHYOORGLGOWUXNXHMHYFAACQEKTHSJW".lower()))
# print(m.feedSymbols("krkrallexxfolgendesistsofortbekanntzugebenxxichhabefolgelnbebefehlerhaltenxxjansterledesbisherigxnreichsmarschallsjgoeringjsetztderfuehrersieyhvrrgrzssadmiralyalsseinennachfolgereinxschriftlschevollmachtunterwegsxabsofortsollensiesaemtlichemassnahmenverfuegenydiesichausdergegenwaertigenlageergebenxgezxreichsleiteikktulpekkjbormannjxxobxdxmmmdurnhfkstxkomxadmxuuubooiexkp".lower()))
