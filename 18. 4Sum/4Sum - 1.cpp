class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        set<vector<int> > res;
        vector<vector<int> > ret;
        if(nums.size()<4) return ret;
        sort(nums.begin(), nums.end());
        //将4Sum转化为3Sum，进而再转化为2Sum
        for(int i=0;i<nums.size()-3;i++)
        {
            for(int j=i+1;j<nums.size()-2;j++)
            {
                int left = j+1;
                int right = nums.size()-1;
                while(left<right)
                {
                    int sum = nums[i] + nums[j] + nums[left] + nums[right];
                    if(sum == target)
                    {
                        vector<int> tmp;
                        tmp.push_back(nums[i]);
                        tmp.push_back(nums[j]);
                        tmp.push_back(nums[left]);
                        tmp.push_back(nums[right]);
                        res.insert(tmp);
                        ++left;
                        --right;
                    }
                    else if(sum < target) ++left;
                    else --right;
                }
            }
        }
        return vector<vector<int> > (res.begin(), res.end());
    }
};
