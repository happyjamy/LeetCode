class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        num=[]
        st=[]
        for i in logs :
            if (i.split()[1]).isdigit():
                num.append(i)
            else:
                st.append(i)
        
        st.sort(key= lambda x:(x.split()[1:], x.split()[0]))
        
        return st+num