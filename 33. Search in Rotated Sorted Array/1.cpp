class Solution {
public:
    int search(vector<int>& nums, int target) {
        int n = nums.size();
        if(n==0) return -1;
        int left = 0, right = n-1;
        while(left<=right)
        {
            int mid = (left + right) / 2;
            if(nums[mid]==target) return mid;
            //如果中间的数小于最右边的数，说明右半段是有序的
            if(nums[mid] < nums[right])
            {
                if(nums[mid] < target && nums[right] >= target)
                {
                    left = mid+1;
                }
                else{
                    right = mid-1;
                }
            }
            //如果中间的数大于最右边的数，说明左半段是有序的
            else{
                if(nums[left] <= target && nums[mid] > target)
                {
                    right = mid-1;
                }
                else{
                    left = mid+1;
                }
            }
        }
        return -1;
    }
};