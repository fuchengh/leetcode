class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int, int> freq;
        for(auto n: nums) {
            if(freq.count(n)) return true;
            freq[n]++;
        }
        return false;
    }
};