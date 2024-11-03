#include <vector>
#include <queue>
#include <limits>
#include <algorithm>

using namespace std;

class Solution {
public:
    int minTimeToReach(vector<vector<int>>& moveTime) {
        int c = moveTime.size();
        int e = moveTime[0].size();

        vector<vector<vector<int>>> d(c, vector<vector<int>>(e, vector<int>(2, INT_MAX)));
        d[0][0][0] = 0;

        priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> pq;
        pq.push({0, 0, 0, 0});

        vector<pair<int, int>> directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

        while (!pq.empty()) {
            vector<int> current = pq.top();
            pq.pop();

            int t = current[0];
            int i = current[1];
            int j = current[2];
            int p = current[3];

            if (t > d[i][j][p]) continue;

            for (auto dir : directions) {
                int ci = i + dir.first;
                int cj = j + dir.second;

                if (ci >= 0 && ci < c && cj >= 0 && cj < e) {
                    int ct = max(t, moveTime[ci][cj]) + (p == 0 ? 1 : 2);
                    if (ct < d[ci][cj][1 - p]) {
                        d[ci][cj][1 - p] = ct;
                        pq.push({ct, ci, cj, 1 - p});
                    }
                }
            }
        }

        return min(d[c - 1][e - 1][0], d[c - 1][e - 1][1]);
    }
};
