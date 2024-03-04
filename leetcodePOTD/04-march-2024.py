class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        n=len(tokens)
        left,right=0,n-1
        maxscore=0
        score=0
        while left <=right:
            if power>=tokens[left]:
                power-=tokens[left]
                score+=1
                maxscore=max(maxscore,score)
                left+=1
            elif score>0:
                power+=tokens[right]
                score-=1
                right-=1
            else:
                break
        return maxscore                