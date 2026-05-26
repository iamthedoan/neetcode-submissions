class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_set = set(numbers)

        res = []
        for i in num_set:
            comp = target - i
            if comp in num_set and comp != i:
                res.append(numbers.index(i) + 1)
                res.append(numbers.index(target - i) + 1)
                res.sort()
                return res

        return res