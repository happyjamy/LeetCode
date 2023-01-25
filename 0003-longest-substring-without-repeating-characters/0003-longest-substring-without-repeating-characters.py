class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_length=0
        start,max_length=0,0
        used={}
        for i,v in enumerate(s):
            if v in used and start <= used[v]:
                start=used[v]+1
            else:
                max_length=max(max_length,i-start+1)
            
            used[v]=i

        return max_length
        