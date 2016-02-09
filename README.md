# Enigma

A customizable enigma machine implementation in Python.  Supports an unlimited number of symbols and an unlimited number of rotors.  Comes with preset rotors and reflectors actually used in WWII.

## Running

Clone the repository and run `python3 main.py` to run the default configuration.

The default decrypts the Enigma M4 message found on `http://www.cryptomuseum.com/crypto/enigma/msg/p1030681.htm`.

## Customizing

You can customize both the components and the settings of the enigma machine in `main.py`.

First, choose the components of the enigma machine to make up a `StringEnigmaMachine` object:
* `StringEnigmaMachine(symbols, reflector, *rotors)`

Next, you can adjust the current settings of the machine with several methods:
* `ringSetting(settings)`
* `startPosition(positions)`
* `setCables(cables)`

Alternatively, if you don't want to use strings you can create an `EnigmaMachine` object and specify a list of symbols of any type to use with the reflector and rotors:
* `EnigmaMachine(symbols, reflector, *rotors)`

## Encrypting / Decrypting

To encrypt or decrypt, simply create a new machine, choose some settings, then use the `feedSymbols` method to run a message through the machine:
* `feedSymbols(symbols)`

Since enigma machines are symmetrical, encryption and decryption is the same process.  Running an encrypted message through the machine again after changing the settings back will yield the unencrypted message.
