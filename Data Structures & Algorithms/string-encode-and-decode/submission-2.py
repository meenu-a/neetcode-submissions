class Solution:

    def encode(self, strs: List[str]) -> str:
        concat = ""
        for string in strs:
            concat += str(len(string)) + "#"
            concat += string
        
        return concat

    def decode(self, s: str) -> List[str]:
        original = []
        str_size = ""
        s_size = len(s)
        i = 0
        while (i < s_size):

            if(s[i] == "#"):
                int_size = int(str_size)
                str_size = ""
                word = s[i+1 : i+int_size+1]
                original.append(word)
                i += int_size
            else:
                str_size += s[i]
            
            i += 1
        
        return original
