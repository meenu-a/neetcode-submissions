class Solution {
public:
    int removeElement(vector<int>& nums, int val) 
    {
        int first = 0;
        int last = nums.size()-1;

        while(first <= last)
        {
            if(nums[first] == val)
            {
                nums[first] = nums[last];
                last--;
            }
            else
            {
                first++;
            }
        }

        return first;
    }
};