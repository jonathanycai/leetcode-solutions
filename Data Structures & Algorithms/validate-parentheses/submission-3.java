class Solution {
    public boolean isValid(String s) {
        char[] chars = s.toCharArray();
        Stack<Character> stack = new Stack<>();

        if (chars.length % 2 != 0) {
            return false;
        }

        for (char c : chars) {
            if (c == '(' || c == '{' || c== '[') {
                stack.push(c);
            } else {
                if (stack.isEmpty()) {
                    return false;
                }
                if (c == ')') {
                    if (stack.peek() != '(') {
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
                } else if (c == ']') {
                    if (stack.peek() != '[') {
                        return false;
                    } else {
                        stack.pop();
                    }
                }
            }
        }
        return stack.isEmpty();
    }
}
