class Solution:
    def dailyTemperatures(self, temperatures):
        length=len(temperatures)
        output_list=[0*(length-1)]
        for i in range(0,length):
            for j in range(i+1,length):
                if temperatures[j]>temperatures[i]:
                    output_list.append(j-i)
                    break
                elif i>length-2 and j==length-1:
                    output_list.append(0)
                    continue
                elif i==length-2 and j==length-1:
                    output_list.append(0)
                    continue
                
                else:
                    continue
            
        if i==length-1:
            output_list.append(0)

        print(output_list)
                    

Temp=Solution()
Temp.dailyTemperatures([55,38,53,81,61,93,97,32,43,78])
