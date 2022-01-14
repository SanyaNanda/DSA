#---------Solved on Leetcode----------------------------------
# python3
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

#---------Solved on GFG---------------------------------------
# python3
class Solution:
    def Anagrams(self, words, n):
        '''
        words: list of word
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''
        groups=[]
        for i in words:
            group=sorted(list(i))
            if group not in groups:
                groups.append(group)
                
        str_to_group = [sorted(list(i)) for i in words]
        group_map = list(zip(str_to_group,words))
       
        result=[]
        for i in groups:
            g=[]
            for j in group_map:
                if j[0]==i:
                    g.append(j[1])
            result.append(g)
        return result
#  Driver Code Starts
if __name__ =='__main__':
    t= int(input())
    for tcs in range(t):
        n= int(input())
        words=input().split()
        
        ob = Solution()
        ans = ob.Anagrams(words,n)
        
        for grp in sorted(ans):
            for word in grp:
                print(word,end=' ')
            print()
