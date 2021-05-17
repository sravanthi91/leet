"""Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
Example 4:

Input: x = 0
Output: 0
 

Constraints:

-231 <= x <= 231 - 1

"""

class Solution:
    def reverse(self, x: int) -> int:
        if(x>0):
            s=1
        else:
            s=-1 
        reverse=0
        x=abs(x)
        while(x!=0):
            r=x%10
            reverse=reverse*10+r
            x=x//10
        reverse=s*reverse
        if(reverse>=-2**31 and reverse<=2**31-1):
            return reverse
        else:
            return 0
        return reverse
