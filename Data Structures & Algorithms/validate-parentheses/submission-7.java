class Solution {
    public boolean isValid(String s) {
        char[] parenthesis = s.toCharArray();

        Stack<Character> stack = new Stack<>();

        for (char c : parenthesis) {
            if (c == '{' || c == '[' || c == '(') {
                stack.push(c);
            }
            if (stack.isEmpty()) {
                return false;
            }
            if (c == ']') {
                if (stack.peek() != '[') {
                    return false;
                } else {
                    stack.pop();
                }
            } else if (c == '}') {
                if (stack.peek() != '{') {
                    return false;
                } else {
                    stack.pop();
                }
            } else if (c == ')') {
                if (stack.peek() != '(') {
                    return false;
                } else {
                    stack.pop();
                }
            }
        }
        return stack.isEmpty();
    }
}
