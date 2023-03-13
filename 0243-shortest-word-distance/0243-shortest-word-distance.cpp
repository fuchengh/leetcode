class Solution {
public:
    int shortestDistance(vector<string>& wordsDict, string word1, string word2) {
        int ans = INT_MAX;
        for(int i = 0; i < wordsDict.size(); i++) {
            if(wordsDict[i] == word1) { // start search
                for(int j = 0; j < wordsDict.size(); j++) {
                    if(wordsDict[j] == word2) {
                        ans = min(ans, abs(j - i));
                    }
                }
            }
        }
        return ans;
    }
};