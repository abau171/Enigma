import machine, rotorsystem, plugboard, presets

m = presets.StringEnigmaMachine(presets.alphabet, presets.ReflectorCThin(), presets.RotorBeta(), presets.Rotor5(), presets.Rotor6(), presets.Rotor8())
m.ringSetting("EPEL")
m.startPosition("NAEM")
m.setCables("AE BF CM DQ HU JN LX PR SZ VW")

eMessageKey = "QEOB"
eMessage = "LANOTCTOUARBBFPMHPHGCZXTDYGAHGUFXGEWKBLKGJWLQXXTGPJJAVTOCKZFSLPPQIHZFXOEBWIIEKFZLCLOAQJULJOYHSSMBBGWHZANVOIIPYRBRTDJQDJJOQKCXWDNBBTYVXLYTAPGVEATXSONPNYNQFUDBBHHVWEPYEYDOHNLXKZDNWRHDUWUJUMWWVIIWZXIVIUQDRHYMNCYEFUAPNHOTKHKGDNPSAKNUAGHJZSMJBMHVTREQEDGXHLZWIFUSKDQVELNMIMITHBHDBWVHDFYHJOQIHORTDJDBWXEMEAYXGYQXOHFDMYUXXNOJAZRSGHPLWMLRECWWUTLRTTVLBHYOORGLGOWUXNXHMHYFAACQEKTHSJW"

print("Encrypted Message Key: ", eMessageKey)
messageKey = m.feedSymbols(eMessageKey)
print("Decrypted Message Key: ", messageKey)
print()

print("Encrypted Message")
print(eMessage)
print()
m.startPosition(messageKey)
message = m.feedSymbols(eMessage)
print("Decrypted Message")
print(message)
print()
