class Solution:
    def reverseBits(self, n: int) -> int:
        # we need to get the bits one by one. how?
        # lets take the logic & 1
        # 0 & 1 = 0; 1 & 1 = 1
        # how can we shift the bits to the left?
        # 1 0

        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res = res | (bit << (31-i))
        return res
        


        