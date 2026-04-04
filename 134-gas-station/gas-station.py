class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        i = 0
        while i < (len(gas)):
            if gas[i]>=cost[i]:
                gasing = gas[i]-cost[i]
                itr = (i+1)%len(gas)
                found = True
                while itr!=i:
                    gasing+=gas[itr]
                    gasing-=cost[itr]
                    if gasing<0:
                        found = False
                        break
                    itr= (itr+1)%len(gas)
                if found:
                    return i
                i=itr-1
            i+=1
        return -1      
                

