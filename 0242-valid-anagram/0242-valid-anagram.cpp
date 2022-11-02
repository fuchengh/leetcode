class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> seen;
        
        if(s.length() != t.length()) return false;
        
        for(auto it: s) {
            if(seen.find(it) != seen.end()) seen[it]++;
            else seen[it] = 1;
        }
        for(auto it: t) {
            if(seen[it] == 0) return false;
            seen[it]--;
        }
        
        return true;
    }
};