class MyQueue {
public:
    vector<int> s1;
    vector<int> s2;
    int front;
    
    MyQueue() {
    }
    
    void push(int x) {
        if(s1.empty())
            front = x;
        s1.push_back(x);
    }
    
    int pop() {
        if(s2.empty()){
            while(!s1.empty()){
                s2.push_back(s1.back());
                s1.pop_back();
            }
        }
        int ret = s2.back();
        s2.pop_back();
        return ret;
    }
    
    int peek() {
        if(!s2.empty()) {
            return s2.back();
        }
        return front;
    }
    
    bool empty() {
        return s1.size() == 0 && s2.size() == 0;
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