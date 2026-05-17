class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        checkx, checky , checkz = False,False,False
        for i in triplets:
            if not checkx and i[0]==target[0] and i[1]<=target[1] and i[2]<=target[2]:
                checkx = True
            if not checky and i[0]<=target[0] and i[1]==target[1] and i[2]<=target[2]:
                checky = True
            if not checkz and i[0]<=target[0] and i[1]<=target[1] and i[2] == target[2]:
                checkz = True

        return checkx and checky and checkz
        