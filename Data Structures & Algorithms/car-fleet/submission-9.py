class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)]
        pair.sort(reverse = True)
        stack = []

        for p, s in pair:
            time = (target - p) / s
            if stack and time <= stack[-1]:
                continue
            stack.append(time)

        return len(stack)