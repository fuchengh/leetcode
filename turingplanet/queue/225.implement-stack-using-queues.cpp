/*
 * @lc app=leetcode id=225 lang=cpp
 *
 * [225] Implement Stack using Queues
 */

#include "lib/headers.h"

// @lc code=start
class MyStack
{
  public:
    queue<int> q;
    MyStack() {}

    void push(int x)
    {
        int to_move = q.size();
        q.push(x);
        // move first "to-move" nodes back to the q
        while (to_move--)
        {
            q.push(q.front());
            q.pop();
        }
    }

    int pop()
    {
        int v = q.front();
        q.pop();
        return v;
    }

    int top() { return q.front(); }

    bool empty() { return q.empty(); }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */
// @lc code=end
