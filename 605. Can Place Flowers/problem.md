## Problem

1. Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

   Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number **n**, return if **n** new flowers can be planted in it without violating the no-adjacent-flowers rule.

   **Example 1:**

   ```
   Input: flowerbed = [1,0,0,0,1], n = 1
   Output: True
   ```

   

   **Example 2:**

   ```
   Input: flowerbed = [1,0,0,0,1], n = 2
   Output: False
   ```

   

   **Note:**

   1. The input array won't violate no-adjacent-flowers rule.
   2. The input array size is in the range of [1, 20000].
   3. **n** is a non-negative integer which won't exceed the input array size.



## Solution

* 根据规则判断，遍历数组，如果当前位置为0，且满足前一位和后一位也为0（如果是开头和结尾只需要满足单边即可），则可以种花，因此时间复杂度为O(n)，空间复杂度为O(1)。
* 优化方法：仍然遍历字符串，不过每次如果可以种花就可以跳过下一个位置，到达下个位置的下一个位置去判断，同时在遍历中判断种花数和要求数大小。
* 这道题的关键就是需要额外考虑开头和结尾两个位置，他们不需要两侧都空。