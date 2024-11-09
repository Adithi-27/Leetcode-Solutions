class Solution {
public:
    int maxFrequency(vector<int>& nums, int k, int numOperations) {
        int a = nums.size();
        map<int, int> freq;
        vector<pair<int, int>> events;
        
        // Build frequency map and event list
        for (int num : nums) {
            freq[num]++;
            events.push_back({num - k, 1});
            events.push_back({num + k + 1, -1});
        }
        
        // Collect all unique points
        set<int> points;
        for (auto& event : events) {
            points.insert(event.first);
        }
        for (auto& p : freq) {
            points.insert(p.first);
        }

        // Sort events
        sort(events.begin(), events.end());

        int idx = 0;
        int current_overlap = 0;
        int max_freq = 0;
        int actual_count = 0;
        
        // Traverse each point
        for (int x : points) {
            // Process events up to current point x
            while (idx < events.size() && events[idx].first <= x) {
                current_overlap += events[idx].second;
                idx++;
            }
            
            actual_count = freq.count(x) ? freq[x] : 0;
            int possible_freq = actual_count + min(numOperations, current_overlap - actual_count);
            max_freq = max(max_freq, possible_freq);
        }

        return max_freq;
    }
};
