from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #res = []
        #self.dfs(res, "", n, n)
        return self.dfs_stack(n)
        
    def dfs(self, res, tmp, l, r):
        if l == r:
            if l == 0:
                res.append(tmp)
                return
            else:
                self.dfs(res, tmp + '(', l - 1, r)
        else:
            if l > 0:
                self.dfs(res, tmp + '(', l - 1, r)
            self.dfs(res, tmp + ')', l, r - 1)

    def dfs_stack(self, n):
        res = []
        stack = [')']
        l = n - 1
        r = n
        tmp = "("
        while stack:
            

if __name__ == "__main__":
    so = Solution()
    so.generateParenthesis(3)