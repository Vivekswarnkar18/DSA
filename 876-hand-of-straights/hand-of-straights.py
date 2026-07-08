from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n=len(hand)
        hand.sort()
        count=Counter(hand)
        if len(hand)%groupSize!=0:
            return False
        for num in hand:
            if count[num]==0:
                continue
            for i in range(groupSize):
                if count[num + i] == 0:
                    return False

               
                count[num + i] -= 1

        return True

            
           


        