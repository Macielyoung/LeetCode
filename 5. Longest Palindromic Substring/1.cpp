class Solution {
public:
    string longestPalindrome(string s) {
        //动态规划
        int n = s.size();
        if(n==0) return "";
        if(n==1) return s;
        int start = 0, max = 1;
        bool table[1000][1000] = {false};
        for(int i=0;i<n;i++)
        {
            table[i][i] = true;
        }
        for(int i=0;i<n-1;i++)
        {
            if(s[i]==s[i+1])
            {
                table[i][i+1] = true;
                start = i;
                max = 2;
            }
        }
        for(int len=3;len<=n;len++)
        {
            for(int i=0;i<n-len+1;i++)
            {
                int j=i+len-1;
                if(s[i]==s[j] && table[i+1][j-1])
                {
                    table[i][j] = true;
                    start = i;
                    max = len;
                }
            }
        }
        return s.substr(start, max);
    }
};