class Solution {
public:
    bool isPalindrome(string s) {
        int l = 0;
        int r = s.length()-1;
        
        while (l < r) {
            while(!isalnum(s[l]) && l < r) l += 1;
            while(!isalnum(s[r]) && l < r) r -= 1;
            if(tolower(s[l]) != tolower(s[r])) return false;
            
            l += 1;
            r -= 1;
        }
        return true;
    }
};