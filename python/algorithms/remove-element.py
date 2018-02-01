# Time:  O(n)
# Space: O(1)
#
# Given an array and a value, remove all instances of that value in place and return the new length.
# 
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.

class Solution:
    def removeElement(self, A, element):
        """
        
        Arguments:
            A {[list]}
            elem {[int]}
        
        Returns:
            [int]
        """

        i, last = 0, len(A) - 1
        while i <= last:
            if A[i] == element:
                A[i], A[last] = A[last], A[i]
                last -= 1
            else:
                i += 1
        return last + 1
    
if __name__ == "__main__":
    print(Solution().removeElement([1, 2, 3, 4, 5, 2, 2], 2))