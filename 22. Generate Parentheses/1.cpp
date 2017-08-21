class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> res;
        add(res, "", n, 0);
        return res;
    }
    
    void add(vector<string> &ret, string str, int left, int right)
    {
        //如果左右括号个数都是0，则表示所有括号都已插入，可以返回结果
        if(left==0 && right==0)
        {
            ret.push_back(str);
            return;
        }
        //右括号个数大于0，添加右括号，同时左括号个数不变，右括号个数减1
        if(right > 0)
        {
            add(ret, str+")", left, right-1);
        }
        //左括号个数大于0，添加左括号，同时左括号个数减1，右括号个数加1
        if(left > 0)
        {
            add(ret, str+"(", left-1, right+1);
        }
    }
};