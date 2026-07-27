class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        """
            - get first word
            - convert to dictionary
            - map that dictionary to the og word- {a:1, c:1, t:1} : "act"
            - except dictionaries can't bet keys, so convert to tuple
            -O(m x n) complexity?? length of word times number of words
        """

        master_dict = {}
    
        for string in strs:
            word_dict = {}
            for letter in string:
                if letter in word_dict:
                    word_dict[letter] += 1
                else:
                    word_dict[letter] = 1
            word_tuple = tuple(sorted(word_dict.items()))

            if word_tuple in master_dict:
                master_dict[word_tuple].append(string)
            else:
                master_dict[word_tuple] = [string]
        
        return(list(master_dict.values()))

