class stack:
    def __init__(self):
        self.stack_list=[]
        self.current_index=-1
        self.capacity=5

    def push(self,n):
        if self.current_index==self.capacity-1:
            print("Stack Overflow")
            raise Exception("Stack Overflow")
        self.current_index+=1
        self.stack_list.append(n)
        return n
    
    def pop(self):
        if self.current_index==-1:
            print("There is nothing to pop")
            raise Exception("Stack Underflow")
        self.current_index-=1
        return self.stack_list.pop()
        
        
        
    def peek(self):
        return self.stack_list[self.current_index]
    
    def isEmpty(self):
        if len(self.stack_list)==0 and self.current_index==-1:
            return True
        else:
            return False
            
    
    def size(self):
        return len(self.stack_list)
    
    def isFull(self):
        if self.current_index==self.capacity-1:
            return True
        else:
            return False


s=stack()


