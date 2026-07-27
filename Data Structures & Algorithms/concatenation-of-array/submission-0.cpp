class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) 
    {
        vector<int> numsDoubled = nums;
        numsDoubled.insert(numsDoubled.end(), nums.begin(), nums.end());
        return numsDoubled;
    }
};