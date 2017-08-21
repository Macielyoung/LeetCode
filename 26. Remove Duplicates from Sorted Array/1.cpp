class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int size = nums.size();
        //如果数组为空，则返回0
        if(size==0) return 0;
        int num=1;
        for(int i=1;i<size;i++)
        {
            //如果当前遍历到的数字与累加位数的数字不同，则赋值，并计数器加1
            if(nums[i] != nums[num-1])
            {
                num++;
                nums[num-1] = nums[i];
            }
        }
        return num;
    }
};
