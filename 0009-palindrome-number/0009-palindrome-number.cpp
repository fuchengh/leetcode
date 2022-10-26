class Solution {
public:
    bool isPalindrome(int x) {
        string str_x = to_string(x);
        reverse(str_x.begin(), str_x.end());
        return str_x == to_string(x);
    }
};