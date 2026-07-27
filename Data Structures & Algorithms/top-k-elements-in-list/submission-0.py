from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numFrequencies = defaultdict(int)
        for num in nums:
            numFrequencies[num] += 1
        
        min_heap = []
        for key, value in numFrequencies.items():
            heapq.heappush(min_heap, (value, key))
            if(len(min_heap) > k):
                heapq.heappop(min_heap)

        top_elements = [pair[1] for pair in min_heap]
        return top_elements
        
        


        