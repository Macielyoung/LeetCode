class Solution {
public:
    bool isValid(string s) {
        stack<char> stk;
        int len = s.length();
        for(int i=0;i<len;i++)
        {
            //将左括号压入栈中
            if(s[i]=='(' || s[i]=='[' || s[i]=='{')
            {
                stk.push(s[i]);
            }
            else{
                //若栈已空，则不匹配
                if(stk.empty()) return false;
                if(stk.top()=='(' && s[i]==')') stk.pop();
                else if(stk.top()=='[' && s[i]==']') stk.pop();
                else if(stk.top()=='{' && s[i]=='}') stk.pop();
                else return false;
            }
        }
        return stk.empty();
    }
};