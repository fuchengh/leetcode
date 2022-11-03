class Solution {
public:
    int longestPalindrome(vector<string>& words) {
        unordered_map<string, int> freq;
        for(auto it: words) {
            freq[it]++;
        }
        
        int len = 0;
        bool central = false;
    
        for(auto [word, count]: freq) {
            if(word[0] == word[1]) {
                if(count % 2 == 0) {
                    len += count;
                } else {
                    len += count - 1;
                    central = true;
                }
            } else if (word[0] < word[1] && freq.count({word[1], word[0]})) {
                len += 2 * min(count, freq[{word[1], word[0]}]);
            }
        }
        
        if(central) len += 1;
        
        return len * 2;
    }
};