class MyQueue {
public:
    vector<int> stack;
    
    MyQueue() {
    }
    
    void push(int x) {
        this->stack.push_back(x);
    }
    
    int pop() {
        vector<int> tmp;
        for(int i = this->stack.size()-1; i > 0; i--) {
            int top = this->stack.back();
            this->stack.pop_back();
            tmp.push_back(top);
        }
        int ret = this->stack.back();
        this->stack.pop_back();
        while(tmp.size() > 0) {
            int top = tmp.back();
            tmp.pop_back();
            this->stack.push_back(top);
        }
        return ret;
    }
    
    int peek() {
        return this->stack[0];
    }
    
    bool empty() {
        return this->stack.size() == 0;
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */