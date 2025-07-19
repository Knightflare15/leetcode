from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        maxF= max(counter[i] for i in counter)
        maxC = 0 
        for i in counter:
            if counter[i] == maxF:
                maxC+=1
        part_count = maxF - 1
        part_length = n + 1
        empty_slots = part_count * part_length + maxC
        return max(len(tasks),empty_slots)
                



        