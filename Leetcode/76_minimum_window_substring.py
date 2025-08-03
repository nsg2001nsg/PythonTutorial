
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        res = ""
        dic = {}
        formed = 0
        ml = float('inf')
        for c in t:
            if c in dic:
                dic[c][0] += 1
                continue
            dic[c] = [1, 0]

        for right in range(len(s)):
            if s[right] in dic:
                dic[s[right]][1] += 1
                if dic[s[right]][1] == dic[s[right]][0]:
                    formed += 1

            while formed == len(dic):
                wl = right - left + 1
                if wl < ml:
                    ml = wl
                    res = s[left:right+1]

                if s[left] in dic:
                    dic[s[left]][1] -= 1
                    if dic[s[left]][1] < dic[s[left]][0]:
                        formed -= 1

                left += 1

        return res


sol = Solution()
print(sol.minWindow("ADOBECODEBANC", "ABC"))


