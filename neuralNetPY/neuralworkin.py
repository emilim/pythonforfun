from bientropy import bien, tbien
from bitstring import Bits
import random

def listToString(s): 
    str1 = ""  
    for ele in s: 
        str1 += ele   
    return str1 
arr = []
for n in range(32):
    r = random.uniform(0, 1)
    if r >= 0.2:
        arr.append('1')
    if r < 0.2:
        arr.append('0')
bitString = listToString(arr)
print(bitString)


bit = tbien(Bits('0b'+bitString))
print("tbien: ", bit)
print(bit * len(bitString))

bit1 = bien(Bits('0b'+bitString))
print("bien: ", bit1)
print(bit1 * len(bitString))
