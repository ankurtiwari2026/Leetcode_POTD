class Solution {
public:
    int bagOfTokensScore(vector<int>& tokens, int power) {
        int n =tokens.size();
        int i=0,j=n-1;
        sort(begin(tokens),end(tokens));
        int score=0;
        int maxs=0;
        while(i<=j){
            if(power>=tokens[i]){
                power-=tokens[i];
                score+=1;
                i++;
                maxs=max(maxs,score);
            }
            else if(score>=1){
                power+=tokens[j];
                j--;
                score-=1;
            }
            else{
                return maxs;
            }
        }return maxs;
        }
        

        
    
};