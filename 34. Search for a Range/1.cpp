class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int n = nums.size();
        vector<int> res(2, -1);
        int left = 0;
        int right = n-1;
        while(left<=right)
        {
            int mid = (left + right) / 2;
            if(nums[mid]>target)
            {
                right = mid-1;
            }
            else if(nums[mid]<target)
            {
                left = mid+1; 
            }
            else{
                res[0] = mid;
                res[1] = mid;
                int j = mid-1;
                while(j>=0 && nums[j]==target)
                {
                    res[0] = j;
                    j--;
                }
                int i = mid+1;
                while(i<n && nums[i]==target)
                {
                    res[1] = i;
                    i++;
                }
                break;
            }
        }
        return res;
    }
};