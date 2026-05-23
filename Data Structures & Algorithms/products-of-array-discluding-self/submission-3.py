class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_pdt = 0
        numZero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                if total_pdt == 0:
                    total_pdt = nums[i]
                else:
                    total_pdt = total_pdt * nums[i]
            else:
                numZero += 1

        res = []

        if numZero > 1:
            return [0] * len(nums)
        for i in range(len(nums)):
            if numZero == 1 and nums[i] != 0:
                res.append(0)
            elif numZero == 1 and nums[i] == 0:
                res.append(total_pdt)
            else:
                res.append(int(total_pdt/nums[i]))

        return res