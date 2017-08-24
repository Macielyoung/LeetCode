class Solution {
public:
    int strStr(string haystack, string needle) {
        int m = haystack.length();
        int n = needle.length();
        if (n==0) return 0;
        int *next = (int*)malloc(sizeof(int)*(n+1));
        //求next数组
        getNext(needle, next, n);
        int i=0,j=0;
        while(i<m && j<n)
        {
            //如果j = -1，或者当前字符匹配成功（即S[i] == P[j]），都令i++，j++ 
            if(j==-1 || haystack[i]==needle[j])
            {
                i++;
                j++;
            }
            else{
                //②如果j != -1，且当前字符匹配失败（即S[i] != P[j]），则令 i 不变，j = next[j]      
                //next[j]即为j所对应的next值
                j = next[j];
            }
        }
        if(j<n) return -1;
        else return i-j;        
    }
    
    void getNext(string needle, int* next, int n)
    {
        int i=0, j=-1;
        next[0] = -1;
        while(i<n)
        {
            if(j==-1 || needle[i]==needle[j])
            {
                j++;
                i++;
                next[i] = j;
            }
            else{
                j = next[j];
            }
        }
    }
};
