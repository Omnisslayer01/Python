
class Solution:
    def isPalindrome(self, x: int) -> bool:
        my_list=list(str(x))
        
        rev_list=my_list.copy()
        rev_list.reverse()
        print(rev_list)
        print(my_list)
        for i in range(0,len(my_list)):
            if(my_list[i]==rev_list[i]):
                continue
            else:
                return False
            
        return True
        

                       
sol=Solution()
print(sol.isPalindrome(12321))
        