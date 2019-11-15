from bitstring import BitArray
from Crypto.Cipher import AES


class PrivateAddrSolver(object):
    def __init__(self, addr, key):
        self.addr = BitArray(hex=addr.replace(':', ''))
        self.key = self.swap_buf(key)
        # self.key = key
        self.cipher = AES.new(key, AES.MODE_ECB)
        if self.addr[46:] != 0b10:
            return None

    def swap_buf(self, buf):
        result = bytearray(buf)
        result.reverse()
        return bytes(result)

    def parse(self):
        # ah(k, r) -> e(k, r') mod 2^24
        _addr = self.addr
        _prand = self.swap_buf(_addr[:24].tobytes())
        _hash = self.swap_buf(_addr[24:].tobytes())

        # r' = padding || r
        plaintext = _prand + b'\x00' * 13
        plaintext = self.swap_buf(plaintext)
        ciphertext = self.cipher.encrypt(plaintext)
        swapped = self.swap_buf(ciphertext)
        if swapped[:3] == _hash:
            return True
