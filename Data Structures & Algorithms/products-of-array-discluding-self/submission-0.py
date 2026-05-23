class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            pdt = 1
            for j in range(len(nums)):
                if i != j:
                    pdt = pdt * nums[j]

            res.append(pdt)
        return res