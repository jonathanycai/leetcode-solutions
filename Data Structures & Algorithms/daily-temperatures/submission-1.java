class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int[] dist = new int[temperatures.length];
        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i < temperatures.length; i++) {
            int t = temperatures[i];
            while (!stack.isEmpty() && t > temperatures[stack.peek()]) {
                int index = stack.pop();
                dist[index] = i - index;
            }
            stack.push(i);
        }

        return dist;
    }
}
