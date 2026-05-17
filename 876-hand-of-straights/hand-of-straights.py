class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize != 0:
            return False
        d = {}
        hand.sort()
        for i in hand:
            d[i] = d.get(i,0) + 1
        i = 0
        print(d)
        while i<len(hand):
            if d[hand[i]] <= 0:
                i+=1
                continue
            k = 0
            while k<groupSize-1:
                if hand[i]+k+1 > hand[-1] or hand[i]+k+1 not in d or d[hand[i]+k+1]<d[hand[i]]:
                    return False
                d[hand[i]+k+1]-=d[hand[i]]
                k+=1
            d[hand[i]] = 0
            i+=1
        print(d)
        return True
                 

