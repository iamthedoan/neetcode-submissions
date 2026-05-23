class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        out = [0] * k
        tracker = {}

        for i in nums:
            tracker[i] = 1 + tracker.get(i,0)

        sorted_tracker = dict(sorted(tracker.items(), key=lambda x:x[1], reverse=True))
        tracker_keys = list(sorted_tracker.keys())

        for i in range(k):
            out[i] = tracker_keys[i]
        
        return out