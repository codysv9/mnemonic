#!/usr/bin/python3.7

import hashlib
import os

wordlist = open('wordlist.txt', 'r').read().split()

def Mnemonic(ENT):

    if not len(ENT) * 8 in [128, 256]:

        return 'Entropy does not have the required size of 16 or 32 bytes'

    if not type(ENT) == bytes:

        ENT = str(ENT).encode()

    Hash = hashlib.sha256(ENT).hexdigest()

    Base = bin(int(ENT.hex(), 16))
    Base = Base[2:].zfill(len(ENT) * 8)
    Base = Base + bin(int(Hash, 16))[2:].zfill(256)[:len(ENT) * 8 // 32]

    Mnemonic_Result = ''

    for index in range(len(Base) // 11):

        Mnemonic_Result += wordlist[
            int(Base[index * 11 : (index + 1) * 11], 2)
        ] + ' '

    return Mnemonic_Result

S = os.urandom(32)

m = Mnemonic(S)

print('Entropia: ' + S.hex())
print('Mnemonic: ' + m)


