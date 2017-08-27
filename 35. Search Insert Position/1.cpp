class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int num = nums.size();
        if(num==0) return 0;
        //注意边界条件
        if(target<=nums[0]) return 0;
        if(target==nums[num-1]) return num-1;
        if(target>nums[num-1]) return num;
        for(int i=0;i<num;i++)
        {
            if(target == nums[i]) return i;
            if(target>nums[i] && target<nums[i+1]) return i+1;
        }
    }
};
