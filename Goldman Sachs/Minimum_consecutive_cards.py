class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        mp = dict()
        mini=float('inf')
        for index,val in enumerate(cards):
            if val in mp:
                if index-mp[val]<mini:
                    mini=abs(mp[val]-index)+1
            mp[val]=index    
        if mini==float('inf'):
            return -1
        return mini        
                
                    

                 