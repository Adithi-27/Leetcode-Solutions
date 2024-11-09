class Solution {
public:
    int smallestNumber(int n, int t) {
        while (true) {
            int prod = 1;
            int temp = n;
            
            while (temp > 0) {
                int digit = temp % 10;
                prod  *= digit;
                temp /= 10;
            }
            if (prod % t == 0){
                return n;
            }
            n++;
        }
    }
};
