class Solution {
public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {
        int rows = image.size();
        int cols = image[0].size();
        set<tuple<int, int>> seen;
        seen.insert({sr, sc});
        deque<tuple<int, int>> q;
        q.push_back({sr, sc});
        int orig_color = image[sr][sc];
        
        while(!q.empty()) {
            auto [x, y] = q.front();
            q.pop_front();
            image[x][y] = color;
            vector<tuple<int, int>> dir = {{-1, 0}, {1, 0}, {0, 1}, {0, -1}};
            for(auto d: dir) {
                auto [dx, dy] = d;
                if(0 <= x+dx && x+dx < rows && 0 <= y+dy && y+dy < cols){
                    if(image[x+dx][y+dy] == orig_color && seen.find({x+dx, y+dy}) == seen.end()) q.push_back({x+dx, y+dy});
                }
                seen.insert({x+dx, y+dy});
            }
        }
        
        return image;
    }
};