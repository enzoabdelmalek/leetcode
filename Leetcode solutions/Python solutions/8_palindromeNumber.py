class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = list(str(x))
        ans = x[::-1]
        if ans == x :
            return True
        else :
            return False