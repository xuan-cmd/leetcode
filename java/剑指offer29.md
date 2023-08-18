#剑指 Offer 29. 顺时针打印矩阵

输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

 

**示例 1：**

```
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
```

**示例 2：**

```
输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]
```



## 题解1

完全没思路只能说，完全学习大佬

```java
class Solution {
    public int[] spiralOrder(int[][] matrix) {
        if (matrix.length == 0) return new int[0]; //如果矩阵是空的，就返回长度为0的int
        int l = 0, t = 0 , r = matrix[0].length-1, b = matrix.length-1;
        int x = 0;
        int [] res = new int [(r+1)*(b+1)];
        while(true){
            for (int i = l;i <= r;i++){
                res[x++] = matrix[t][i];
            }
            t = t + 1;
            if(t > b) break;
            for (int i = t;i <= b;i++){
                res[x++] = matrix[i][r];
            }
            r = r-1;
            if(l>r) break;
            for (int i = r;i >= l;i--){
                res[x++] = matrix[b][i];
            }
            b = b-1;
            if(t > b) break;
            for( int i = b;i >= t;i--){
                res[x++] = matrix[i][l];
            }
            l = l +1;
            if(l>r) break;
        }
        return res;
    }
}
```

