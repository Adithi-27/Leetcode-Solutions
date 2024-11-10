class Solution {
public:
    bool canFindTwoIncreasingSubarrays(vector<int>& inc, int k, int n) {
        for (int a = 0; a + 2 * k - 1 < n; ++a) {
            if (inc[a] >= k && inc[a + k] >= k) {
                return true;
            }
        }
        return false;
    }

    int maxIncreasingSubarrays(vector<int>& nums) {
        int n = nums.size();
        vector<int> inc(n, 1);

        for (int a = n - 2; a >= 0; --a) {
            if (nums[a] < nums[a + 1]) {
                inc[a] = inc[a + 1] + 1;
            }
        }

        int l = 1, r = n / 2, res = 0;

        while (l <= r) {
            int m = l + (r - l) / 2;
            if (canFindTwoIncreasingSubarrays(inc, m, n)) {
                res = m;
                l = m + 1;
            } else {
                r = m - 1;
            }
        }

        return res;
    }
};
