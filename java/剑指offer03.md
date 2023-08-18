#剑指 Offer 03. 数组中重复的数字

找出数组中重复的数字。


在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

**示例 1：**

```
输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3 
```

## 题解1

```java
class Solution {
    public Integer findRepeatNumber(int[] nums) {
        int num = nums.length;
        int [] nums_num = new int [num] ;
        for (int i = 0; i < num; i++){
            if(nums_num[nums[i]] == 1){
                return nums[i];
            }else{
                nums_num[nums[i]] = 1;
            }
        }
        return null;
    }
}
```

思路：数组默认值为0，如果出现就赋值1，如果再遇到1，就是重复了，然后就return。



## 题解2

参考大佬

哈希表

```java
class Solution {
    public Integer findRepeatNumber(int[] nums) {
        HashSet<Integer>sites = new HashSet<Integer>();
        int num = nums.length;
        for (int i = 0; i < num; i++){
            if(sites.contains(nums[i])){
                return nums[i];
            }else{
                sites.add(nums[i]);
            }
            
        }
        return null;
    }
}
```



## 题解3

原地交换，参考的大佬，没想到我还是入坑了

错误代码

```java
class Solution {
    public int findRepeatNumber(int[] nums) {
        int num = nums.length;
        for (int i = 0; i < num; i++){
            if(nums[i] == i){
                continue;
            }
            System.out.println(i);
            System.out.println(nums[nums[i]]);
            System.out.println(nums[i]);
            System.out.println("----");
            if(nums[nums[i]] == nums[i]){
                return nums[i];
            }
            int tmp =  nums[i];
            nums[i] = nums[tmp];
            nums[tmp] = tmp;
        }
        return -1;
    }
}
```

错误的点在于循环的地方，这样循环每次会送一个到该去的索引的地方， 但是有个问题是，如果后面的数字换到前面了，他就会一直到不了索引的地方

正确的代码：

```java
class Solution {
    public int findRepeatNumber(int[] nums) {
        int i = 0;
        while(i < nums.length) {
            if(nums[i] == i) {
                i++;
                continue;
            }
            if(nums[nums[i]] == nums[i]) return nums[i];
            int tmp = nums[i];
            nums[i] = nums[tmp];
            nums[tmp] = tmp;
        }
        return -1;
    }
}
```

这个点在于，只有当第索引和值相当了，才会+，就不会出现上面漏数字的情况