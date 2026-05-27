class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        prev_left = None
        prev_right = None

        res = []
        while left < right:
            if prev_right == right:
                right -= 1
            if prev_left == left:
                left += 1
            else:
                num_sum = numbers[left] + numbers[right]
                if num_sum > target:
                    prev_right = right
                    right -= 1
                elif num_sum < target:
                    prev_left = left
                    left += 1
                else:
                    return [left+1, right+1]
        
        return res