
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = {}
        for i in tasks:
            d[i] = d.get(i,0)+1
        sorted_dict = sorted(d.items(), key=lambda x: x[1], reverse=True)
        maxi = sorted_dict[0][1]
        count_max = 1
        for i in range(1,len(sorted_dict)):
            if sorted_dict[i][1] != maxi:
                break
            count_max+=1
                
        minimum = (n+1)*(maxi-1)+count_max
        
        return max(len(tasks),minimum)
                



        