# 反转链表

定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

 **示例:**

```
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
```



题解1：

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
    public ListNode reverseList(ListNode head) {
        LinkedList<Integer> stack = new LinkedList<Integer>();
        while(head!=null){
            stack.add(head.val);
            head = head.next;
        }
        int num = stack.size();
        ListNode tmp = null;
        for(int i = 0 ;i< num ;i++){
            ListNode newnode = new ListNode(stack.removeLast());
            if (tmp == null){
                tmp = newnode;
            }
            else {
                ListNode cur = tmp;
                while(cur.next != null) {
                    cur = cur.next;
                }
                cur.next = newnode;
            }
        }
        return tmp;
    }
}
```

很普通有点麻烦的做法



题解2：参考力扣大佬的写法

**迭代**

```java
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode pre = null, cur = head;
        while(cur!=null){
            ListNode tmp = cur.next;
            cur.next = pre;
            pre = cur;
            cur = tmp;
        }
        return pre;
    }
}
```

题解3：参考力扣大佬的写法

递归

```java
class Solution {
    public ListNode reverseList(ListNode head) {
        return recur(head,null);
    }
    private ListNode recur(ListNode cur, ListNode pre){
        if (cur == null ) return pre;
        ListNode res = recur(cur.next, cur);
        cur.next = pre;
        return res;
    }
}
```

