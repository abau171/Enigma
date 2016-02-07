import rotorsystem, plugboard, machine
import presets

rs = rotorsystem.RotorSystem(presets.reflectorB, presets.rotor3, presets.rotor2, presets.rotor1)
print([rs.feed(0) for _ in range(5)])