class Solution {
public:
    vector<int> findSubstring(string s, vector<string>& words) {
        int len_s = s.size();
        int len_w = words[0].size();
        int num = words.size();
        map<string, int> str, tmp;
        for(int i=0;i<num;i++)
        {
            str[words[i]]++;
        }
        vector<int> index;
        for(int i=0;i<len_s-len_w*num+1;i++)
        {
            tmp.clear();
            int j=0;
            for(;j<num;j++)
            {
                string word = s.substr(i+j*len_w, len_w);
                if(str.find(word) == str.end()) break;
                tmp[word]++;
                if(str[word] < tmp[word]) break;
            }
            if(j>=num) index.push_back(i);
        }
        return index;
    }
};