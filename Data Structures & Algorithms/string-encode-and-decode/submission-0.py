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
                word = ""
                str_size = ""
                while (int_size > 0 and i < s_size):
                    i += 1
                    word += s[i]
                    int_size -= 1
                original.append(word)
            else:
                str_size += s[i]
            
            i += 1
        
        return original
