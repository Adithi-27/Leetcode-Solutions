class Solution {
public:
    bool isBalanced(string num) {
        int eSum = 0;
        int oSum = 0;
        for (int i = 0; i < num.length(); ++i) {
            if (i % 2 == 0) {
                eSum += num[i] - '0';
                
            } else {
                oSum += num[i] - '0';
            }
        }
        return eSum == oSum;
    }
};
