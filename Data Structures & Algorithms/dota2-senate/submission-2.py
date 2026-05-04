class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        cnt = i = 0

        while i < len(senate):
            c = senate[i]
            if c == 'R':
                if cnt < 0:
                    senate.append('D')
                cnt += 1
            if c == 'D':
                if cnt > 0:
                    senate.append('R')
                cnt -= 1
            i += 1
        
        print(senate)
        return 'Radiant' if cnt > 0 else 'Dire'