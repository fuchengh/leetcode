class Solution {
public:
    bool isValid(string s) {
        vector<char> stack;
        for(int i = 0; i < s.length(); i++){
            char ch = s[i];
            if(ch == '(' || ch == '[' || ch == '{') {
                stack.push_back(ch);
            }
            else {
                // check if stack is empty
                if(stack.empty()) return false;
                // check if top is a valid left parentheses
                char top = stack.back();
                if(ch == ')') {
                    if(top != '(') {
                        return false;
                    }
                } else if (ch == ']') {
                    if (top != '[') {
                        return false;
                    }
                } else if (ch == '}') {
                    if (top != '{') return false;
                }
                stack.pop_back();
            }
        }
        // check if stack is not empty
        if(!stack.empty()) return false;
        return true;
    }
};