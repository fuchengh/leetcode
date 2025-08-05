/*
 * @lc app=leetcode id=127 lang=cpp
 *
 * [127] Word Ladder
 */

// @lc code=start
class Solution
{
  public:
    int ladderLength(string beginWord, string endWord, vector<string> &wordList)
    {
        unordered_set<string> dict(wordList.begin(), wordList.end());

        if (!dict.count(endWord))  // not possible
            return 0;

        queue<string> q;
        q.push(beginWord);
        unordered_set<string> visited;
        visited.insert(beginWord);

        // start bfs
        int level = 0;
        while (!q.empty())
        {
            level++;
            int qsize = q.size();
            while (qsize--)
            {
                string cur = q.front();
                q.pop();
                // check if we reach the end
                if (cur == endWord)
                    return level;
                // add neighbor
                // try replacing cur[i] with a-z
                for (int i = 0; i < cur.size(); i++)
                {
                    char orig = cur[i];
                    for (int j = 0; j < 26; j++)
                    {
                        char replace = 'a' + j;
                        if (replace == orig)
                            continue;
                        cur[i] = replace;
                        // check if we can push into queue
                        if (!visited.count(cur) && dict.count(cur))
                        {
                            q.push(cur);
                            visited.insert(cur);
                        }
                    }
                    cur[i] = orig;
                }
            }
        }

        return 0;  // not found
    }
};
// @lc code=end
