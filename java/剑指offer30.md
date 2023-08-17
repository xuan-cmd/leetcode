#剑指 Offer 30. 包含min函数的栈

定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。

 

**示例:**

```
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.min();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.min();   --> 返回 -2.
```

 

**提示：**

1. 各函数的调用总次数不超过 20000 次

## 错误解法：

```java
class MinStack {

    /** initialize your data structure here. */
    Stack<Integer> stack1;
    Stack<Integer> stack2;
    int min;

    public MinStack() {
        stack1 = new Stack<Integer>();
        stack2 = new Stack<Integer>();
    }
    
    public void push(int x) {
        stack1.push(x);
        
    }
    
    public void pop() {
        stack1.pop();
    }
    
    public int top() {
        return stack1.peek();
    }
    
    public Integer min() {
        stack2 = new Stack<Integer>();
        if (stack1.size()==0){
            return null;
        }else{
            int min = stack1.peek();
            while(stack1.size()!=0){
                if(stack1.peek()<min){
                    min = stack1.peek();
                }
                stack2.push(stack1.pop());
            }
            while(stack2.size()!=0){
                stack1.push(stack2.pop());
            }
            return min;
        }
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.min();
 */
```

超时了

## 题解1：

```java
class MinStack {

    /** initialize your data structure here. */
    Stack<Integer> stack1;
    Stack<Integer> stack2;

    public MinStack() {
        stack1 = new Stack<Integer>();
        stack2 = new Stack<Integer>();
    }
    
    public void push(int x) {
        stack1.push(x);
        if(stack2.empty()||stack2.peek()>=x){
            stack2.push(x);
        }
    }
    
    public void pop() {
        if(stack1.pop().equals(stack2.peek())){
            stack2.pop();
        }
    }
    
    public int top() {
        return stack1.peek();
    }
    
    public Integer min() {
            return stack2.peek();
        }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.min();
 */
```

大佬的解法就是yyds，设置一个辅助的栈，然后严格存储栈顶就是最小的，原来以为，要记录第一个小和第二个小，因为第一个小的出去了，下一次就要输出第二个小的了，那万一第一个就是最小的，怎么记录倒数第二小的，但是发现这种情况是不存在的，辅助栈空的时候，主栈也空了。

需要注意的是，不能用== ，要用equals

object1.equals(object2)为true，则表示equals1和equals2实际上是引用同一个对象。