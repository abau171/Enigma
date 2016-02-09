import rotorsystem, plugboard, machine
import presets

m = presets.StringEnigmaMachine("ABCDEFGHIJKLMNOPQRSTUVWXYZ", presets.reflectorCThin, presets.rotorBeta, presets.rotor5, presets.rotor6, presets.rotor8)
m.ringSetting("EPEL")
m.startPosition("NAEM")
m.setCables("AE BF CM DQ HU JN LX PR SZ VW")

eMessageKey = "QEOB"
eMessage = "LANOTCTOUARBBFPMHPHGCZXTDYGAHGUFXGEWKBLKGJWLQXXTGPJJAVTOCKZFSLPPQIHZFXOEBWIIEKFZLCLOAQJULJOYHSSMBBGWHZANVOIIPYRBRTDJQDJJOQKCXWDNBBTYVXLYTAPGVEATXSONPNYNQFUDBBHHVWEPYEYDOHNLXKZDNWRHDUWUJUMWWVIIWZXIVIUQDRHYMNCYEFUAPNHOTKHKGDNPSAKNUAGHJZSMJBMHVTREQEDGXHLZWIFUSKDQVELNMIMITHBHDBWVHDFYHJOQIHORTDJDBWXEMEAYXGYQXOHFDMYUXXNOJAZRSGHPLWMLRECWWUTLRTTVLBHYOORGLGOWUXNXHMHYFAACQEKTHSJW"

print("Encrypted Message Key:", eMessageKey)
messageKey = m.feedSymbols(eMessageKey)
print("Decrypted Message Key:", messageKey)

print("Encrypted Message:", eMessage)
m.startPosition(messageKey)
message = m.feedSymbols(eMessage)
print("Decrypted Message:", message)