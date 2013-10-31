"""A collection of bits that can be set, cleared, and toggled by number.

Based on code from https://wiki.python.org/moin/BitArrays and converted to
a class-based version for ease of use.
"""

__author__ = 'Brian Landers <brian@packetslave.com>'

import array


class BitField(object):

    __slots__ = ['__max_bit', '__bytes']

    def __init__(self, bits):
        if bits < 1:
            raise ValueError(bits)

        self.__max_bit = bits - 1

        recs = bits >> 5  # number of 32-bit ints required to store bits

        if bits & 31:  # not an even multiple
            recs += 1

        self.__bytes = array.array('I', (0,) * recs)  # unsigned 32-bit int

    def set(self, bit):
        """Set a given bit in the field to on."""
        if bit < 0 or bit > self.__max_bit:
            raise ValueError(bit)

        self.__bytes[bit >> 5] |= (1 << (bit & 31))

    def clear(self, bit):
        """Clear a given bit in the field."""
        if bit < 0 or bit > self.__max_bit:
            raise ValueError(bit)

        self.__bytes[bit >> 5] &= ~(1 << (bit & 31))

    def toggle(self, bit):
        """Toggle a given bit in the field from off to on, or vise versa."""
        if bit < 0 or bit > self.__max_bit:
            raise ValueError(bit)

        self.__bytes[bit >> 5] ^= (1 << (bit & 31))

    def test(self, bit):
        """Returns True if a given bit in the field is on."""
        if bit < 0 or bit > self.__max_bit:
            raise ValueError(bit)

        return 0 != self.__bytes[bit >> 5] & (1 << (bit & 31))
