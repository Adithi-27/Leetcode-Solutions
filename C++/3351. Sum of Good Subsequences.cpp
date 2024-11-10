class Solution {
public:
    int sumOfGoodSubsequences(vector<int>& nums) {
        const int M = 1e9 + 7;
        long long res = 0;
        vector<long long> count(100001, 0);
        vector<long long> sum_of_subsequences(100001, 0);
        
        auto input_nums = nums;
        
        for (auto cur_num : nums) {
            long long cur_count = 1;
            long long cur_sum = cur_num;
            
            
            if (cur_num > 0) {
                cur_count = (cur_count + count[cur_num - 1]) % M;
            }
            
            
            if (cur_num < 100000) {
                cur_count = (cur_count + count[cur_num + 1]) % M;
            }
            
            
            if (cur_num > 0) {
                cur_sum = (cur_sum + sum_of_subsequences[cur_num - 1] + ((long long)count[cur_num - 1] * cur_num) % M) % M;
            }
            
            
            if (cur_num < 100000) {
                cur_sum = (cur_sum + sum_of_subsequences[cur_num + 1] + ((long long)count[cur_num + 1] * cur_num) % M) % M;
            }
            
            
            res = (res + cur_sum) % M;
            
            
            count[cur_num] = (count[cur_num] + cur_count) % M;
            sum_of_subsequences[cur_num] = (sum_of_subsequences[cur_num] + cur_sum) % M;
        }
        
        return res;
    }
};
