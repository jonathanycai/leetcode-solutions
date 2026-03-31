class Solution {
    public boolean isValid(String s) {
    
        char[] chars = s.toCharArray();
        Stack<Character> stack = new Stack<>();
        HashMap<Character, Character> map = new HashMap<>();
        map.put('}', '{');
        map.put(')', '(');
        map.put(']', '[');

        if (chars.length % 2 != 0) {
            return false;
        }


        for (char c : chars) {
            if (!map.containsKey(c)) {
                stack.push(c);
                continue;
            } else {
                if (stack.empty() || stack.peek() != map.get(c)) {
                    return false;
                }
                stack.pop();
            }
        }

        return stack.empty();
    }
}
