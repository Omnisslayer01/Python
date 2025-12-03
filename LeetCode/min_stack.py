class MinStack:

    def __init__(self):
        self.list=[]
        
    def push(self, val: int) -> None:
        if len(self.list)==0:
            self.list.append([val,val])
        
        elif val<self.list[-1][1]:
            self.list.append([val,val])
        else:
            self.list.append([val,self.list[-1][1]])
        
    def pop(self) -> None:
        self.list.pop()
        
    def top(self) -> int:
        return self.list[-1][0]
        
    def getMin(self) -> int:
        return self.list[-1][1]
    


        


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(4)
obj.push(5)
obj.push(3)
obj.push(4)
obj.pop()

print(obj.list)
param_3 = obj.top()
param_4 = obj.getMin()

print(param_3)
print(param_4)