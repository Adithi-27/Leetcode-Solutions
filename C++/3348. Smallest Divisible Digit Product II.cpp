int __FAST_IO__ = []() { std::ios::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0); return 0; }();

int f[10]{0}, D[4] = {2, 3, 5, 7};
class Solution {
    void Add(long long x) {
        for (int d : D) while (x > 1 && x % d == 0) x /= d, f[d]++;
    }

    void Del(long long x) {
        for (int d : D) while (x > 1 && x % d == 0) x /= d, f[d]--;
    }

    string Calc() {
        int g[10];
        memcpy(g, f, sizeof f);
        string str;
        while (g[3] >= 2) g[3]-=2, str.push_back('9');
        while (g[2] >= 3) g[2]-=3, str.push_back('8');
        while (g[7] >= 1) g[7]-=1, str.push_back('7');
        while (g[2] >= 1 && g[3] >= 1) g[2]--, g[3]--, str.push_back('6');
        while (g[5] >= 1) g[5]--, str.push_back('5');
        while (g[2] >= 2) g[2]-=2, str.push_back('4');
        while (g[3] >= 1) g[3]--, str.push_back('3');
        while (g[2] >= 1) g[2]--, str.push_back('2');
        reverse(str.begin(), str.end());
        return str;
    }
public:
    string smallestNumber(string num, long long t) {
        memset(f, 0, sizeof f);
        for (int d : D) while (t > 1 && t % d == 0) t /= d, f[d]++;
        if (t > 1) return "-1";

        int n = num.size();
        for (int i = 0; i < n; ++i) {
            long long x = num[i] - '0';
            if (x == 0) {
                for (; i < n; ++i) num[i] = '1';
            } else {
                Del(x);
            }
        }

        if (Calc().length() == 0) return num;

        for (int i = n - 1; i >= 0; --i) {
            Add(num[i] - '0');
            if (num[i] == '9') continue;

            for (int j = num[i] - '0' + 1; j <= 9; ++j) {
                Del(j);

                string back = Calc();
                // cout << i << " " << back << endl;
                if (back.size() < n - i) {
                    num[i] = j + '0';
                    return num.substr(0, i + 1) + string(n - i - 1 - back.size(), '1') + back;
                }
    
                Add(j);
            }
            
        }
        string back = Calc();
        return string(max<int>(0LL, n + 1 - back.length()), '1') + back;
    }
};
