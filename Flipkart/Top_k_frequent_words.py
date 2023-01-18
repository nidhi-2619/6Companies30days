class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        d=dict()
        for i in words:
            if i in d: 
                d[i] += 1
            else:
                d[i] = 1
     
        d = sorted(d.items(), key = lambda i: (-i[1], i[0]))
       
        return [i[0] for i in d[:k]]