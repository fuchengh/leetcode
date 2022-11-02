class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int cur_min = pow(10, 4)+1;
        int cur_max = -1;
        
        for(int i = 0; i < prices.size(); i++){
            int p = prices[i];
            cur_min = min(cur_min, p);
            cur_max = max(cur_max, p-cur_min);
        }
        return cur_max;
    }
};