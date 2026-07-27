from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_frequencies = Counter(nums)
        frequency_arr = [[] for _ in range (len(nums) + 1)]

        for key,value in num_frequencies.items():
            frequency_arr[value].append(key)
        
        top_k = []
        for i in range (len(frequency_arr)-1, 0, -1):
            for num in frequency_arr[i]:
                top_k.append(num)
                if(len(top_k)) == k:
                    return top_k


        
        


        