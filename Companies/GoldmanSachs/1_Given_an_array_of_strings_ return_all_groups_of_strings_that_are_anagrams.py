#---------Solved on Leetcode----------------------------------
# python3
# Runtime: 7048 ms, faster than 5.00% of Python3 online submissions for Group Anagrams.
# Memory Usage: 20.1 MB, less than 9.74% of Python3 online submissions for Group Anagrams.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups=[]
        for i in strs:
            group=sorted(list(i))
            if group not in groups:
                groups.append(group)
                
        str_to_group = [sorted(list(i)) for i in strs]
        group_map = list(zip(str_to_group,strs))
       
        result=[]
        for i in groups:
            g=[]
            for j in group_map:
                if j[0]==i:
                    g.append(j[1])
            result.append(g)
        return result
