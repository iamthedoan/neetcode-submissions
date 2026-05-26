class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if nums == []:
            return 0

        nums = list(set(nums))
        nums.sort()
        counter = 1
        max_count = counter
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1] + 1:
                counter += 1
            else:
                # check if this is the longest seq
                if counter > max_count:
                    max_count = counter
                counter = 1

        if counter > max_count:
            max_count = counter
        return max_count