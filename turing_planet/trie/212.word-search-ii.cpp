/*
 * @lc app=leetcode id=212 lang=cpp
 *
 * [212] Word Search II
 */

// @lc code=start
class Trie
{
  public:
    unordered_map<char, Trie *> child;
    string                      word = "";
};

class Solution
{
  public:
    vector<string> res;

    bool VALID(int i, int j, int maxI, int maxJ)
    {
        return (i >= 0 && j >= 0 && i < maxI && j < maxJ);
    }

    void dfs(vector<vector<char>> &board, int r, int c, Trie *root)
    {
        if (!root)
            return;
        Trie *cur = root;
        if (cur->word.size() != 0)
        {
            res.push_back(cur->word);
            cur->word = "";  // already used this word
        }
        // continue dfs
        char orig   = board[r][c];
        board[r][c] = '#';
        for (auto [nextR, nextC] :
             vector<pair<int, int>>{{r - 1, c}, {r + 1, c}, {r, c - 1}, {r, c + 1}})
        {
            if (VALID(nextR, nextC, board.size(), board[0].size()))
            {
                if (board[nextR][nextC] != '#' && cur->child[board[nextR][nextC]])
                    dfs(board, nextR, nextC, cur->child[board[nextR][nextC]]);
            }
        }
        board[r][c] = orig;
    }

    vector<string> findWords(vector<vector<char>> &board, vector<string> &words)
    {
        Trie *root = new Trie();
        // add wordlist into trie
        for (string &s : words)
        {
            Trie *cur = root;
            for (char c : s)
            {
                if (!cur->child[c])
                    cur->child[c] = new Trie();
                cur = cur->child[c];
            }
            cur->word = s;
        }
        // start searching on board
        for (int i = 0; i < board.size(); i++)
        {
            for (int j = 0; j < board[0].size(); j++)
            {
                if (root->child[board[i][j]])
                    dfs(board, i, j, root->child[board[i][j]]);
            }
        }
        return res;
    }
};
// @lc code=end
