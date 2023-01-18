class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_dic = {}
        ans=[]
        for orin in strs:
            sort_orin = ''.join(sorted(orin))
            if sort_orin in ana_dic:
                ana_dic[sort_orin].append(orin)
            else:
                ana_dic[sort_orin]=[orin]


        return ana_dic.values()