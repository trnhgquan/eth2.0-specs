from pymerkles.complex import Container, Vector, List
from pymerkles.basic import boolean, uint, uint8, uint16, uint32, uint64, uint128, uint256
from pymerkles.bitfields import BitVector as Bitvector, BitList as Bitlist
from pymerkles.byte_vector import ByteVector
from pymerkles.core import BasicView, View, TypeDef


class bit(boolean):
    pass


byte = uint8

# Define special Byte vector view types, these are bytes-like:
# raw representation instead of backed by a binary tree. Inheriting Python "bytes"
Bytes1 = ByteVector[1]
Bytes4 = ByteVector[4]
Bytes8 = ByteVector[8]
Bytes32 = ByteVector[32]
Bytes48 = ByteVector[48]
Bytes96 = ByteVector[96]
