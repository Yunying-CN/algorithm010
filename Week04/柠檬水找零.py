class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dic={}
        dic[5]=0
        dic[10]=0
        for bill in bills:
            if bill == 5:
                dic[5]+=1
            elif bill ==10:
                if dic[5]<1:
                    return False
                else:
                    dic[5]-=1
                    dic[10]+=1
            elif bill == 20:
                if dic[10]>0 and dic[5]>0:
                    dic[10]-=1
                    dic[5]-=1
                elif dic[5]>3:
                    dic[5]-=3
                else:
                    return False
        return True