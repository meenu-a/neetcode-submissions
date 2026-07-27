from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        """
            - get first word
            - convert to dictionary
            - map that dictionary to the og word- {a:1, c:1, t:1} : "act"
            - except dictionaries can't bet keys, so convert to tuple
            -O(m x n) complexity?? length of word times number of words
        """

        master_dict = defaultdict(list)
    
        for string in strs:
            word_dict = defaultdict(int)
            for letter in string:
                word_dict[letter] += 1
            word_tuple = tuple(sorted(word_dict.items()))

            master_dict[word_tuple].append(string)
        
        return(list(master_dict.values()))

