# 剑指 Offer 18. 删除链表的节点

给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。

返回删除后的链表的头节点。

- 题目保证链表中节点的值互不相同
- 若使用 C 或 C++ 语言，你不需要 `free` 或 `delete` 被删除的节点

**注意：**此题对比原题有改动

**示例 1:**

```
输入: head = [4,5,1,9], val = 5
输出: [4,1,9]
解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.
```

**示例 2:**

```
输入: head = [4,5,1,9], val = 1
输出: [4,5,9]
解释: 给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.
```

 ## 题解1

```java
class Solution {
    public ListNode deleteNode(ListNode head, int val) {
        ListNode first = head;
        ListNode pre = null, cur = head;
        while(cur.val != val){
            pre = cur ;
            cur = cur.next;
        }
        if (first == cur){
            return first.next;
        }
        pre.next = cur.next;
        return first;
    }
}
```

思路：分两种，要删除是第一个节点和后面节点的情况

因为最后返回头节点，所以有一个first指针一直指向第一个节点

如果删除的是第一个节点，就返回first指针的下一个节点

如果删除的是后面的节点，first指针不动，pre指针指向要删除节点的前面，cur指向要删除的节点，找到要删除的节点以后，让pre.next = cur .next