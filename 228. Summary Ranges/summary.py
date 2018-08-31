#-*- coding: UTF-8 -*-

class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        res = []
        string = ""
        for i in range(len(nums)):
            if(i!=len(nums)-1):
                if(nums[i+1]-nums[i]==1 and string == ""):
                    string += str(nums[i])+"->"
                if(nums[i+1]-nums[i]>1):
                    if(string == ""):
                        res.append(str(nums[i]))
                    else:
                        string += str(nums[i])
                        res.append(string)
                        string = ""
            else:
                if(string == ""):
                    res.append(str(nums[i]))
                else:
                    string += str(nums[i])
                    res.append(string)
        return res

if __name__ == '__main__':
    solu = Solution()
    nums1 = [0,1,2,4,5,7]
    nums2 = [0,2,3,4,6,8,9]
    nums3 = [0,1,2,3,5,6,9,11,14,17,20,21,22]
    res1 = solu.summaryRanges(nums1)
    res2 = solu.summaryRanges(nums2)
    res3 = solu.summaryRanges(nums3)
    print(res1, res2, res3)