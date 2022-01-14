class Solution:
    def sortedSquares(self, nums):
        n = len(nums)
        left = 0
        right = n - 1
        result = [0] * n

        for i in range(n - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                square = nums[left]
                left += 1
            else:
                square = nums[right]
                right -= 1
            result[i] = square * square
        return result
