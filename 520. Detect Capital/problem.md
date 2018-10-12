## Problem

Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

1. All letters in this word are capitals, like "USA".
2. All letters in this word are not capitals, like "leetcode".
3. Only the first letter in this word is capital if it has more than one letter, like "Google".

Otherwise, we define that this word doesn't use capitals in a right way.



**Example 1:**

```
Input: "USA"
Output: True
```



**Example 2:**

```
Input: "FlaG"
Output: False
```



**Note:** The input will be a non-empty word consisting of uppercase and lowercase latin letters.



## Solution

* 使用三个库函数：islower()表示全小写，isupper()表示全大写，istitle()表示首字母大写。
* 根据规则使用if else逻辑判断。