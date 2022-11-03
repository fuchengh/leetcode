class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int ans = -pow(10, 4);
        int cur = 0;
        for(auto n: nums) {
            cur = max(n, cur+n);
            ans = max(ans, cur);
        }
        return ans;
    }
};