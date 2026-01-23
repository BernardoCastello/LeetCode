class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        for i in s:
            if i in t:
                t = t.replace(i,'',1)
                
            else:
                return False
            
        if len(t) == 0:
            return True
        
        return False
    
S = Solution()
print(S.isAnagram("anagam","agaram"))