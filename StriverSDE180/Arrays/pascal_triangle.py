class Solution:
    def generate(self, n: int) -> List[List[int]]:
        
        def helper(n):
            if n==1:
                ans.append([1])
            else:
                helper(n-1)    
                l = [1]        
                for i in range(1, n-1):    
                    l.append(ans[-1][i] + ans[-1][i-1])
                l.append(1)
                ans.append(l)
        ans = []
        helper(n)
        return ans
# https://leetcode.com/submissions/detail/751439489/
