## Probelm

Given a List of words, return the words that can be typed using letters of **alphabet** on only one row's of American keyboard like the image below.

![American keyboard](https://leetcode.com/static/images/problemset/keyboard.png)

**Example 1:**

```
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
```



**Note:**

1. You may use one character in the keyboard more than once.
2. You may assume the input string will only contain letters of alphabet.



## Solution

* 使用一个映射表，把单词分别映射到对应的行，如果都在一行即可输出。