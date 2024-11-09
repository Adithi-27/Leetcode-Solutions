class Solution {
public:
    int maxFrequency(std::vector<int>& nums, int k, int numOperations) {

        int max_num = *std::max_element(nums.begin(), nums.end());
        int size = max_num + k + 2;
        std::vector<int> freq(size, 0);

        for (int num : nums) {
            freq[num] += 1;
        }

        std::vector<int> pre(size, 0);
        pre[0] = freq[0];
        for (int i = 1; i < size; ++i) {
            pre[i] = pre[i - 1] + freq[i];
        }

        int result = 0;
        
        for (int x = 0; x < size; ++x) {
            if (freq[x] == 0 && numOperations == 0) {
                continue; 
            }

            int left = std::max(0, x - k);
            int right = std::min(size - 1, x + k);

            int totalInRange = pre[right] - (left > 0 ? pre[left - 1] : 0);
            
            int canAdjust = totalInRange - freq[x];
            
            int total = freq[x] + std::min(numOperations, canAdjust);
            
            result = std::max(result, total);
        }

        return result;
    }
};
