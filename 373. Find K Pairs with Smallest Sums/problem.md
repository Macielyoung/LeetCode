## Problem

You are given two integer arrays **nums1** and **nums2** sorted in ascending order and an integer **k**.

Define a pair **(u,v)** which consists of one element from the first array and one element from the second array.

Find the k pairs **(u1,v1),(u2,v2) ...(uk,vk)** with the smallest sums.

**Example 1:**

```
Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]] 
Explanation: The first 3 pairs are returned from the sequence: 
             [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
```

**Example 2:**

```
Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [1,1],[1,1]
Explanation: The first 2 pairs are returned from the sequence: 
             [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
```

**Example 3:**

```
Input: nums1 = [1,2], nums2 = [3], k = 3
Output: [1,3],[2,3]
Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]
```



## Solution

* 直接使用sort对list来排序，空间复杂度太高。

* 使用堆排序。构建最小堆，首先把0行所有元素加入到heap中，然后取出堆顶元素，然后把当前元素的下一行元素加入到堆中，用来和行元素比较。

  ```
  num1 = [a, b, c],    num2 = [d, e, f]
  matrix = [[a,d], [a,e], [a,f],
  		  [b,d], [b,e], [b,f],
  		  [c,d], [c,e], [c,f]]
  ```

* 将元素组成看成上面的matrix，每行元素递增，每列元素也递增，然后求matrix前k小的元素。（转化题目）