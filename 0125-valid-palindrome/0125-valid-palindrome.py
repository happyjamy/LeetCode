from collections import deque
class Solution:
    def isPalindrome(self, s: str) -> bool:
        checked_str=deque()
        for i in s:
            if i.isalnum() :
                checked_str.append(i.lower())
        
        while len(checked_str) > 1:
            if checked_str.popleft() != checked_str.pop():
                return False
        return True


