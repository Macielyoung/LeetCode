## Problem

Given a text file `file.txt`, print just the 10th line of the file.

**Example:**

Assume that `file.txt` has the following content:

```
Line 1
Line 2
Line 3
Line 4
Line 5
Line 6
Line 7
Line 8
Line 9
Line 10
```

Your script should output the tenth line, which is:

```
Line 10
```

**Note:**

1. If the file contains less than 10 lines, what should you output?
2. There's at least three different solutions. Try to explore all possibilities.



## Solution

* 使用awk指令。语法：`awk '{pattern + action}' {filenames}`

  ```
  1. awk '{ if (FNR==10) print $0 }' file.txt
  2. awk NR==10 file.txt
  ```

  FNR : 表示当前记录数，但是作用域只在一个文件中，如果重新打开文件，FNR会从1开始；

  NR : 也表示当前记录数。

* 使用sed指令。语法：`sed [options] 'command' file(s)`

  ```
  sed -n 10p file.txt
  ```

   

* `