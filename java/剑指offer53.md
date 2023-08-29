#剑指 Offer 53 - I. 在排序数组中查找数字 I

统计一个数字在排序数组中出现的次数。

 

**示例 1:**

```
输入: nums = [5,7,7,8,8,10], target = 8
输出: 2
```

**示例 2:**

```
输入: nums = [5,7,7,8,8,10], target = 6
输出: 0
```

 

**提示：**

- `0 <= nums.length <= 105`
- `-109 <= nums[i] <= 109`
- `nums` 是一个非递减数组
- `-109 <= target <= 109`

## 题解1

```java
class Solution {
    public int search(int[] nums, int target) {
        int num = 0;
        for(int i:nums){
            if(i != target){
                continue;
            }
            if(i > target){
                break;
            }
            if(i == target){
                num ++;
            }
        }
        return num;
    }
}
```

思路：傻瓜写法，如果找到就++，如果大于就说明后面都没有了，就结束循环



## 题解2

二分写法

```java
class Solution {
    public int search(int[] nums, int target) {
        return helper(nums,target) - helper(nums,target - 1);
    }
    int helper(int[] nums, int target){
        int i = 0, j = nums.length - 1;
        while(i <= j){
            int m = (i + j) / 2;
            if(nums[m] <= target) i = m + 1;
            else j = m - 1;
        }
        return i;
    }
}
```

思路：

大佬解法~太强了！

找边界，用二分法找target的右边界和target-1的右边界，相减就是target的数量