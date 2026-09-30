class Solution:

    def encode(self, strs: List[str]) -> str:
        final_encoded_str = ""
        for word in strs:
            encoded_word = str(len(word)) +"#"+ word 
            final_encoded_str += encoded_word
        return final_encoded_str

    def decode(self, s: str) -> List[str]:
        res=[]
        i=0
        while i < len(s):
            # Move j forward to find the delimiter '#'
            j=i
            while s[j] != "#":
                j+=1
            
            length = int(s[i:j])
            decoded_word = s[j+1:j+1+length]
            res.append(decoded_word)    
                
            i=j+1+length

        return res
