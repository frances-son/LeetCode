# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, h = 1, n
        result = -1
        
        while l <= h:
            mid = (l + h) // 2
            if isBadVersion(mid):
                result = mid
                h = mid - 1
            else:
                l = mid + 1
        
        return result