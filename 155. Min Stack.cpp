#include <stack>
class MinStack {
private:
    stack <int> s;
    stack <int> mins;
public:
    /** initialize your data structure here. */
    MinStack() {
    }
    
    void push(int x) {
        if (s.empty())
        {
            s.push(x);
            mins.push(x);
        }
        else
        {
            s.push(x);
            if (x <= mins.top())
                mins.push(x);
        }
    }
    
    void pop() {
        if (s.top() == mins.top())
        {
            s.pop();
            mins.pop();
        }
        else
            s.pop();
    }
    
    int top() {
        return s.top();
    }
    
    int getMin() {
        return mins.top();
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */
