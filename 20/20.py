class Solution:
    def isValid(self, s: str) -> bool:
        co = s.strip('"')
        if not co:
            return True
        stack = []
        for c in co:
            if not self.judge_c(c, '{', '}', stack): return False
            if not self.judge_c(c, '[', ']', stack): return False
            if not self.judge_c(c, '(', ')', stack): return False
        return not bool(stack)

    def judge_c(self, c, d, e, stack):
        if c == d:
            stack.append(c)
        elif c == e:
            if not stack or stack[-1] != d:
                return False
            else:
                stack.pop()
        return True

if __name__ == "__main__":
    so = Solution()
    print(str(so.isValid(input())).lower())