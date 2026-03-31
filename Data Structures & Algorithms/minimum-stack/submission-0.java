class MinStack {
    private Stack<Integer> stack;
    private Stack<Integer> minStack;

    public MinStack() {
        stack = new Stack<>();
        minStack = new Stack<>();
    }
    
    public void push(int val) {
        if(minStack.isEmpty() || minStack.peek() >= val) {
            minStack.push(val);
        }
        stack.push(val);
    }
    
    public void pop() {
        int top = stack.pop();
        if (!minStack.isEmpty() && minStack.peek() == top) {
            minStack.pop();
        }
    }
    
    public int top() {
        return stack.peek();
    }
    
    public int getMin() {
        return minStack.peek();
    }
}
