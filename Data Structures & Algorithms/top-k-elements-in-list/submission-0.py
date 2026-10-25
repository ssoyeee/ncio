class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = defaultdict(int)
        for n in nums:
            count_dict[n] += 1
        
        sorted_nums = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)
        return [x[0] for x in sorted_nums[:k]]