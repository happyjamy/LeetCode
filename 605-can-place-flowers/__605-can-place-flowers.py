class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        if len(flowerbed) >= 3:
            for i in range(len(flowerbed)):
                if i != 0 and i != len(flowerbed)-1:
                    if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] ==0:
                        flowerbed[i] = 1 
                        n-=1

                elif i ==0:
                    if flowerbed[i] == 0 and flowerbed[i+1] ==0:
                        flowerbed[i] = 1
                        n-=1

                else:
                    if flowerbed[i] == 0 and flowerbed[i-1] ==0:
                        flowerbed[i] = 1
                        n-=1

                if n <=0:
                    return(True)
                    break
            else:
                return(False)
            
        elif len(flowerbed) == 1:
            if flowerbed[0]== 0 :
                n-=1
            if n>0:
                return False
            else:
                return True
                
        else:
            if flowerbed[0] ==0 and flowerbed[1] ==0:
                n-=1
                
            if n>0:
                return False
            else:
                return True
            
                
            
            
            
                    
