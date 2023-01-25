import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = collections.Counter(nums)
        dic = dict(sorted(dic.items(), key=lambda x: x[1],reverse=True))

        return list(dic.keys())[0:k]
        
        