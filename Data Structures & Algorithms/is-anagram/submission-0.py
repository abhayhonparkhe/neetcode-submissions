class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        atoz_frequency=[0] * 26

        if len(s) != len(t):
            return False
        for chr in s:
            index= ord(chr) - ord('a')
            atoz_frequency[index]+=1
        for chr in t:
            index= ord(chr) - ord('a')
            atoz_frequency[index]-=1        
        
        for alphabet in atoz_frequency :
            if alphabet != 0 :
                return False
    
        return True