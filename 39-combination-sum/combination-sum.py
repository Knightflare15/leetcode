class Solution:
    arr = []
    def RcombinationSum(self, candidates: List[int], target: int,att) -> List[List[int]]:
        if target == 0:
            self.arr.append(att[:])
            return
        if target<0:
            return    
        for i in range(len(candidates)):
            att.append(candidates[i]) 
            self.RcombinationSum(candidates[i:],target-candidates[i],att)
            att.pop()
        return
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.arr.clear()
        self.RcombinationSum(candidates,target,[])
        return self.arr



            

        
                
