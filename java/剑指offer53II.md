#剑指 Offer 53 - II. 0～n-1中缺失的数字

一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。

 

**示例 1:**

```
输入: [0,1,3]
输出: 2
```

**示例 2:**

```
输入: [0,1,2,3,4,5,6,7,9]
输出: 8
```

 

**限制：**

```
1 <= 数组长度 <= 10000
```

##题解1

```java
class Solution {
    public Integer missingNumber(int[] nums) {
        int m = nums.length;
        int i = 0;
        int flag = 0;
        for(i = 0; i < m; i++){
            if(nums[i] != i){
                flag = 1;
                break;
            }
        }
        if(flag == 1){
            return nums[i]-1;
        }else{
            return nums[i-1]+1;
        }
    }
}
```

思路：遍历解法，但是例子有特殊情况，就是输入是nums=[0]，这时候要返回1，所以用一个flag来判断是中间有断的话，就返回断点的-1，就是失去的，如果没有断，就是最后一个丢失，就+1.



## 题解2

二分法

```java
class Solution {
    public Integer missingNumber(int[] nums) {
        int i = 0;
        int j = nums.length - 1;
        while(i <= j){
            int m = (i + j) / 2;
            if(nums[m] == m){
                i = m + 1;
            }else{
                j = m - 1;
            }
        }
        return i;
    }
}
```

原来想让判定条件为m - i == nums[m] - nums[i]

但是这种是不行的，因为i和m在一起的时候，是判定不出来的，无法区分应该以断点为分界两侧的子数组，