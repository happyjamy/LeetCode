from string import ascii_lowercase
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        alpha_list = str(ascii_lowercase)
        alpha={}
        s=0
        for i in range(2,10):
            if i == 7 or i == 9:
                alpha[str(i)] = alpha_list[s:s+4]
                s+=4
            else:
                alpha[str(i)]=alpha_list[s:s+3]
                s+=3
                
        n=digits
        n_len=len(digits)
        ans=[]

        def dfs(index,result):
            if len(result) == n_len:
                if result == '':
                    return
                ans.append(result)
                return
            for i in range(index,n_len):
                for z in alpha[n[i]]:
                    dfs(i+1,result+z)
        dfs(0,'')
        return ans
        