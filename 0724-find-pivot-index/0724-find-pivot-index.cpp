class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int total_sum = accumulate(nums.begin(), nums.end(), 0);
        int left = 0;
        printf("%d\n", total_sum);
        
        for(int i = 0; i < nums.size(); i++) {
            if(i >= 1) {
                left += nums[i-1];
            }
            int right = total_sum - left - nums[i];
            if(right == left) return i;
        }
        return -1;
    }
};