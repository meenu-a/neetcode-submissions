class Solution:

    def encode(self, strs: List[str]) -> str:
        concat = []
        for string in strs:
            concat.append(str(len(string)))
            concat.append("#")
            concat.append(string)
        
        return "".join(concat)

    def decode(self, s: str) -> List[str]:
        original = []
        s_size = len(s)
        i = 0
        j = 0

        while (i < s_size):

            if(s[i] == "#"):
                int_size = int(s[j : i])
                word = s[i+1 : i+int_size+1]
                original.append(word)
                i += int_size
                j = i+1
                 
            i += 1
        
        return original
