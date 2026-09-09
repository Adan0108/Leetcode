# # Min Stack
#
# svg
#
# **MediumTopicsCompany TagssvgHints**
#
# Design a stack class that supports the `push`, `pop`, `top`, and `getMin` operations.
#
# - `MinStack()` initializes the stack object.
# - `void push(int val)` pushes the element `val` onto the stack.
# - `void pop()` removes the element on the top of the stack.
# - `int top()` gets the top element of the stack.
# - `int getMin()` retrieves the minimum element in the stack.
#
# Each function should run in `O(1)` time.
#
# **Example 1:**
#
# ```java
# Input: ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]
#
# Output: [null,null,null,null,0,null,2,1]
#
# Explanation:
# MinStack minStack = new MinStack();
# minStack.push(1);
# minStack.push(2);
# minStack.push(0);
# minStack.getMin(); // return 0
# minStack.pop();
# minStack.top();    // return 2
# minStack.getMin(); // return 1
# ```
#
# **Constraints:**
#
# - `-2^31 <= val <= 2^31 - 1`.
# - `pop`, `top` and `getMin` will always be called on **non-empty** stacks.
# - At most `3∗104` calls will be made to `push`, `pop`, `top`, and `getMin`.

class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            #keep track of the minimum up to that point
            #for example stack = [-2, 0, -3]
            #after push all in [(-2, -2), (0, -2), (-3, -3)]
            #if pop the -3 which is min, when [(-2, -2), (0, -2)]
            #-2 is still minimum
            current_min = self.stack[-1][1]
            self.stack.append((val, min(val, current_min)))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]