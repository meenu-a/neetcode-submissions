class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prod = [1]
        right_prod = [1]
        final = []
        c = 0

        for i in range (0, len(nums)-1):
            left_prod.append(left_prod[i] * nums[i])
        for i in range (len(nums)-1, 0, -1):
            right_prod.append(right_prod[c] * nums[i])
            c += 1
        right_prod.reverse()

        final = [(left_prod[i] * right_prod[i]) for i in range (0, len(left_prod))]
        return final
            