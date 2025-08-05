/*
 * @lc app=leetcode id=155 lang=cpp
 *
 * [155] Min Stack
 */

// @lc code=start
class MinStack
{
  public:
    stack<int> vals;
    stack<int> mins;

    MinStack() {}

    void push(int val)
    {
        vals.push(val);
        // push to mins if val is <= mins.top()
        // making it a monotonic stack
        if (mins.empty() || mins.top() >= val)
            mins.push(val);
    }

    void pop()
    {
        int v = vals.top();
        if (!mins.empty() && mins.top() == v)
            mins.pop();
        vals.pop();
    }

    int top() { return vals.top(); }

    int getMin() { return mins.top(); }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
// @lc code=end
