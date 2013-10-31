"""Tests for the BitField class."""

import unittest
import bitfield

__author__ = 'Brian Landers <brian@packetslave.com>'


class BitFieldTest(unittest.TestCase):
    """Tests for the BitField class."""

    def setUp(self):
        self.bits = bitfield.BitField(36)

    def test_constructor(self):
        for i in xrange(0, 36):
            self.assertFalse(self.bits.test(i))

    def test_constructor_args(self):
        with self.assertRaises(ValueError):
            _ = bitfield.BitField(0)
        with self.assertRaises(ValueError):
            _ = bitfield.BitField(-1)

    def test_set(self):
        for i in xrange(0, 36):
            self.assertFalse(self.bits.test(i))

        self.bits.set(17)

        for i in xrange(0, 17):
            self.assertFalse(self.bits.test(i))

        self.assertTrue(self.bits.test(17))

        for i in xrange(18, 36):
            self.assertFalse(self.bits.test(i))

    def test_set_args(self):
        with self.assertRaises(ValueError):
            self.bits.set(-1)
        with self.assertRaises(ValueError):
            self.bits.set(36)

    def test_clear(self):
        self.bits.set(17)
        self.assertTrue(self.bits.test(17))

        self.bits.clear(17)
        self.assertFalse(self.bits.test(17))

    def test_clear_args(self):
        with self.assertRaises(ValueError):
            self.bits.clear(-1)
        with self.assertRaises(ValueError):
            self.bits.clear(36)

    def test_toggle(self):
        self.assertFalse(self.bits.test(17))

        self.bits.toggle(17)
        self.assertTrue(self.bits.test(17))

        self.bits.toggle(17)
        self.assertFalse(self.bits.test(17))

    def test_toggle_args(self):
        with self.assertRaises(ValueError):
            self.bits.toggle(-1)
        with self.assertRaises(ValueError):
            self.bits.toggle(36)


if __name__ == '__main__':
    unittest.main()
