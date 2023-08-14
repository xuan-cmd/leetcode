# 剑指 Offer 25. 合并两个排序的链表

输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

**示例1：**

```
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
```



## 题解1：

```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if (l1 == null ) return l2;//如果l1是空的，直接返回l2
        if (l2 == null ) return l1; //如果l2是空的，直接返回l1
        ListNode tmp = l1;
        ListNode head = l1;
        if(l2.val < l1.val){
             head = l2;
             tmp = l2;
             l2 = l2.next;
        } else{
              l1 = l1.next;
        }
        while((l1!=null) && (l2!=null)){
            
            if(l1.val <= l2.val){
                tmp.next = l1;
                l1 = l1.next;
                tmp = tmp.next;
            }
            else{
                tmp.next = l2;
                l2 = l2.next;
                tmp = tmp.next;
            }
        }
        if (l1 == null ) {
                tmp.next = l2; 
            }
            if (l2 == null ) {
                tmp.next = l1; 
            }
        return head;
    }
}
```

思路：创建一个head，用来返回头节点，创建一个tmp，用来指向需要返回列的最后一个，然后L1和L2都不等于null的时候进入循环，如果L1指向结点小于等于L2，就加入到tmp后，否则L2加入到tmp，最后跳出循环时，将非空的链表剩余的加入到tmp后

**注意**！！

题解1的写法，运行时间可以击败100%,但是内存只击败40%

然后发现大佬在最后一行return前，添加了System.gc()

垃圾回收机制，运行System.gc()只是提醒JVM的[垃圾回收器](https://so.csdn.net/so/search?q=垃圾回收器&spm=1001.2101.3001.7020)执行GC，但是不确定是否马上执行GC

然后运行时间就下降了，但是内存击败100%