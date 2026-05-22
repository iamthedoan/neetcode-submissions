class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_copy = []
        
        for n in nums:
            if n in nums_copy:
                return True
            else:
                nums_copy.append(n)
            
        
        return False

        