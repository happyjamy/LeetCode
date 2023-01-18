from collections import Counter
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words=''
        banned=set(banned)
        count_arr=[]
        
        for i in paragraph:
            if i.isalnum():
                words+=i.lower()
            else:
                words+=' '
                    
        for i in words.split() :
            if i in banned:
                continue
            else:
                count_arr.append(i)
        
        count = Counter(count_arr)
        return count.most_common(1)[0][0]
        
        
        