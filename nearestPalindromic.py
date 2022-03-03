class Solution:
    def nearestPalindromic(self, n: str) -> str:
        m = len(n)
        candidates = [10 ** (m - 1) - 1, 10 ** m + 1] # 999...999(10^(len-1) - 1), 100...001(10^len + 1)
        selfPrefix = int(n[:(m+1)//2]) # 取n的前一半：12345取123
        for x in range(selfPrefix - 1, selfPrefix + 2): # 在[selfPrefix-1, selfPrefix+1]中遍历可行解
            y = x if m % 2 == 0 else x // 10
            print('y', y)
            while y:
                x = x * 10 + y % 10
                y //= 10
            candidates.append(x)

        print(candidates)
        ans = -1
        selfNumber = int(n)
        for candidate in candidates:
            if candidate != selfNumber:
                if ans == -1 or \
                        abs(candidate - selfNumber) < abs(ans - selfNumber) or \
                        abs(candidate - selfNumber) == abs(ans - selfNumber) and candidate < ans:
                    ans = candidate
        return str(ans)
