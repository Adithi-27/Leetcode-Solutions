class Solution {
private:
    bool isStrictlyIncreasing(vector<int>& nums, int start, int k) {
        for (int a = start; a < start + k - 1; a++) {
            if (nums[a] >= nums[a + 1]) {
                return false;
            }
        }
        return true;
    }
    
public:
    bool hasIncreasingSubarrays(vector<int>& arr, int len) {
        int size = arr.size();
        
        if (size < 2 * len) {
            return false;
        }
        
        for (int pos = 0; pos <= size - 2 * len; pos++) {
            if (isStrictlyIncreasing(arr, pos, len) && 
                isStrictlyIncreasing(arr, pos + len, len)) {
                return true;
            }
        }
        
        return false;
    }
};
