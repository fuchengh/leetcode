class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int major = -1;
        int count = 0;
        
        for(auto n: nums) {
            if(count == 0) {
                major = n;
                count = 1;
            } else if (n != major) {
                count--;
            } else {
                count++;
            }
        }
        return major;
    }
};