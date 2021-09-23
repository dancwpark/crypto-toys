from cryptography.fernet import Fernet
from utils import party
from utils import buffer

# Example of using GC to compute bitwise-AND 
## where each bit comes from a party member
## This is a toy example where the party members
##  can infer the other's decision/bit from
##  the result, but does not learn more (or earlier)

# Some Set-Up
Alice = party.Actor("Alice")
Bob = party.Actor("Bob")
room = buffer.Buffer(0)
room.add_party(Alice)
room.add_party(Bob)

# Alice Generates 4 keys
## One for each bit choice for Alice and Bob
a0 = Fernet.generate_key()
a1 = Fernet.generate_key()
b0 = Fernet.generate_key()
b1 = Fernet.generate_key()

## Data represents results of
##  a & b
##          0   1 
##       +--------
##     0 |  0   0
##     1 |  0   1
data = [b'0', b'0', b'1', b'0']
c00 = Fernet(b0).encrypt(Fernet(a0).encrypt(data[0]))
c10 = Fernet(b0).encrypt(Fernet(a1).encrypt(data[1]))
c11 = Fernet(b1).encrypt(Fernet(a1).encrypt(data[0]))
c01 = Fernet(b1).encrypt(Fernet(a0).encrypt(data[0]))

# Prepares to send keys to Bob via oblivious transfer
keya = a1
keyb0 = b0
keyb1 = b1

# Bob
## Oblivious Transfer of keyb0 and keyb1
## Assume Bob selected 0
##  Bob has keya and keyb0 

# oblivious transfer is not done in this toy example
Alice.send([c00, c10, c11, c01], room)
Alice.send([keya, keyb0], room)

msgs = Bob.recieve(room)
keys = Bob.recieve(room)
keyb = keys[1]
keya = keys[0]
c00 = msgs[0]
c10 = msgs[1]
c11 = msgs[2]
c01 = msgs[3]

# From the message, Bob knows if Alice and Bob both chose the bit value
#  1. Bob can share the result with Alice if they wish.
try:
    print(Fernet(keya).decrypt(Fernet(keyb).decrypt(c00)))
    print('c00')
except:
    print("Cannot Open")
try:
    print(Fernet(keya).decrypt(Fernet(keyb).decrypt(c10)))
    print('c10')
except:
    print("Cannot Open")
try:
    print(Fernet(keya).decrypt(Fernet(keyb).decrypt(c11)))
    print('c11')
except:
    print("Cannot Open")
try:
    print(Fernet(keya).decrypt(Fernet(keyb).decrypt(c01)))
    print('c01')
except:
    print("Cannot Open")

