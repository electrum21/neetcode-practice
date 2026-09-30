class Solution:
    def isPalindrome(self, s: str) -> bool:
        stack = []
        for char in s:
            if char.isalnum():
                stack.append(char.lower())
        for char in s:
            if char.isalnum() and char.lower() == stack[-1]:
                stack.pop()
        return stack == []