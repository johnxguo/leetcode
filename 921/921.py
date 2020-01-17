class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        uncom = 0
        toadd = 0
        for c in S:
            if c == '(':
                uncom += 1
            else:
                if uncom == 0:
                    toadd += 1
                else:
                    uncom -= 1
        return uncom + toadd

if __name__ == "__main__":
    print(Solution().minAddToMakeValid('))(())('))

