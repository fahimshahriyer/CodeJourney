# Time:  O(n)
# Space: O(1)
#
# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
# 
# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
# 
# The replacement must be in-place, do not allocate extra memory.
# 
# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
# 1,2,3 -> 1,3,2
# 3,2,1 -> 1,2,3
# 1,1,5 -> 1,5,1

class Solution: 
    def nextPermutation(self,num):
        k, l = -1, 0
        for i in range(len(num)-1):
            if num[i] < num[i+1]:
                k = 1
        
        if k == -1:
            num.reverse()
            return
            
        for i in range(k + 1, len(num)):
            if num[i] > num[k]:
                l = i
        
        num[k], num[l] = num[l], num[k]
        num[k + 1:] = num[:k:-1]

if __name__ == "__main__":
    num = [1, 1, 5]
    Solution().nextPermutation(num)
    print (num)
    Solution().nextPermutation(num)
    print (num)
    Solution().nextPermutation(num)
    print (num)
