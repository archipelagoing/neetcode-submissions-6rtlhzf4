class Solution:
    def reverseBits(self, n: int) -> int:
        # reverse bits in large blocks first
        #gradually reverse smaller & smaler blocks
        # 1 0

        res = 0
        for i in range(32):
#  bit = (n >> i) & 1 extracts the single bit at index i (counting from the right, starting at index 0) from the integer n, returning either 1 or 0
            bit = (n >> i) & 1
            res = res | (bit << (31-i))
        return res
        