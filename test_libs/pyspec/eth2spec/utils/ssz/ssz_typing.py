from pymerkles.complex import Container, Vector, List
from pymerkles.basic import boolean, uint, uint8, uint16, uint32, uint64, uint128, uint256
from pymerkles.bitfields import BitVector as Bitvector, BitList as Bitlist
from pymerkles.bytes32 import Bytes32
from pymerkles.core import View

class bit(boolean):
    pass


byte = uint8

Bytes1 = Vector[byte, 1]
Bytes4 = Vector[byte, 4]
Bytes8 = Vector[byte, 8]

Bytes48 = Vector[byte, 48]
Bytes96 = Vector[byte, 96]
