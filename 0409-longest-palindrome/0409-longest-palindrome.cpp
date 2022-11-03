class Solution {
public:
    int longestPalindrome(string s) {
        unordered_map<char, int> freq;
        for(auto ch: s) freq[ch]++;
        
        int len = 0;
        bool central = false;
        
        for(auto [c, count]: freq) {
            if(count % 2 == 0) {
                len += count;
            } else {
                len += count - 1;
                central = true;
            }
        }
        if(central) len++;
        return len;
    }
};