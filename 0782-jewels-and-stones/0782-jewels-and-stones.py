class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # O(n*m)

        # count = 0
        # for stone in stones:
        #     if stone in jewels:
        #         count += 1
            
        # return count

        # O(n + m)
        s = set(jewels) # ('a', 'A')
        count = 0
        for stone in stones:
            if stone in s:
                count += 1
            
        return count