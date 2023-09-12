#剑指 Offer 17. 打印从1到最大的n位数

输入数字 `n`，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。

**示例 1:**

```
输入: n = 1
输出: [1,2,3,4,5,6,7,8,9]
```

 

这道题是分治算法

分治算法就是把大问题分解成小问题



##题解1

```java
class Solution {
    public int[] printNumbers(int n) {
        int num =(int) Math.pow(10,n) - 1;
        int[] a = new int[num];
        for(int i = 1; i <= num; i++){
            a[i-1] = i;
        }
        return a;
    }
}
```



## 题解2

这道题原来面试的时候是要考虑大数的

直接难哭，大佬yyds

```java
class Solution {
    int[] res;
    int count = 0;
    public int[] printNumbers(int n) {
        res = new int[(int)Math.pow(10,n)-1];
        for(int digit = 1; digit < n+1; digit++){
            for(char first = '1'; first <= '9'; first++){
                char[] num = new char[digit];
                num[0] = first;
                dfs(1,num,digit);
            }
        }
        return res;
    }
    private void dfs(int index, char[] num, int digit){
        if(index == digit){
            res[count++] = Integer.parseInt(String.valueOf(num));
            return;
        }
        for(char i = '0'; i<= '9'; i++){
            num[index] = i;
            dfs(index+1,num,digit);
        }
    }
}
```

