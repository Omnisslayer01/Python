class Solution:
    def dailyTemperatures(self, temperatures):
        length=len(temperatures)
        output_list=[0]*length
        for i in range(0,length):
            for j in range(i+1,length):
                if temperatures[j]>temperatures[i]:
                    output_list[i]=(j-i)
                    break
                else:
                    continue
            
        

        print(output_list)
                    

Temp=Solution()
Temp.dailyTemperatures([73,74,75,71,69,72,76,73])

