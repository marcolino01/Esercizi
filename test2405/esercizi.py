from collections import Counter


def longest_palindrome(s: str) -> int:
    pass



"""You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and 
nums2 respectively. Write a function to merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a 
length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should """

def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> list[int]:
    nums1 : list[int] = nums1[:m]
    nums2 : list[int] = nums2[:n]
    nums1 += nums2
    nums1.sort()
    for i in nums1:
        if i == 0:
            nums1.remove(i)

    return nums1


"""Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

- push(x: int) -> None: Pushes element x to the top of the stack.
- pop() -> None Removes the element on the top of the stack and returns it.
- pop() -> None Returns the element on the top of the stack.
- empty() -> None Returns true if the stack is empty, false otherwise."""


class Queue:

    def __init__(self) -> None:
        pass
      


class MyStack:

    def __init__(self, queue : list[int]= []):
        self.queue : list[int] = queue
    
    def push(self,x: int):
        self.queue.insert(0, x)

    def pop(self):
        x = self.queue.pop(0)
        return x

    def top(self):
        return self.queue[0]

    def empty(self):
        if len(self.queue) > 0:
            return False
        else:
            return True
        
"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', write a function to determine if the input string is valid.

An input string is valid if: 

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type."""

"""def is_valid_parenthesis(s: str) -> bool:

    for i in s:
        if i == "(":
            return True
        else:
            return False
        
    for i in s:"""

def longest_palindrome(s: str) -> int:
    from collections import Counter

    max=1
    diz : dict = Counter(s)
    lista : list = []

    for value in diz.values():
        if value % 2 == 0:
            lista.append(value)
        else:
            if value>max:
                max=value
                lista.append(max-1)
            else:
                lista.append(value)
        
            
    
    return sum(lista)

print(longest_palindrome("abccccdd"))



def is_valid_parenthesis(s: str) -> bool:
    diz={"(":0,"[":0,"{":0}
    for i in s:
        if i == diz.keys():
            diz[i] += 1
        elif i==")":
            diz["("]-=1
        elif i=="]":
            diz["[]"]-=1
        elif i=="}":
            diz["{"]-=1
    return diz