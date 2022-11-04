class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        int i = 0;
        vector<vector<int>> res;
        
        for(;i < intervals.size(); i++) {
            auto intv = intervals[i];
            int start = intv[0], end = intv[1];
            if(start < newInterval[0]) {
                res.push_back(intv);
            } else {
                break;
            }
        }
        // merge newInterval
        if(res.empty() || res[res.size()-1][1] < newInterval[0])
            res.push_back(newInterval);
        else
            res[res.size()-1][1] = max(res[res.size()-1][1], newInterval[1]);
        
        // merge remaining intervals
        for(; i < intervals.size(); i++) {
            auto newIntv = intervals[i];
            if(res[res.size()-1][1] < newIntv[0]) {
                res.push_back(newIntv);
            } else {
                res[res.size()-1][1] = max(res[res.size()-1][1], newIntv[1]);
            }
        }
        return res;
    }
};