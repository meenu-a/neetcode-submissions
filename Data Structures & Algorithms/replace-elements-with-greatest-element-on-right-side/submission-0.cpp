class Solution {
public:
    vector<int> replaceElements(vector<int>& arr) 
    {
        int max_count = arr[arr.size()-1];
        arr[arr.size()-1] = -1;

        for(int i=arr.size()-2; i>=0; i--)
        {
            int result = arr[i];
            arr[i] = max_count;

            max_count = max(result, max_count);
        }

        return arr;
        
    }
};