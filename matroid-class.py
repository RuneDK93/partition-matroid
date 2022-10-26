from collections import Counter
class PartitionMatroid(sage.matroids.matroid.Matroid):
    def __init__(self,partition,capacity):
        self.partition = partition
        self.k = capacity
        assert sum(k) > 0, 'The capicity should be larger than zero for at least 1 partition'
        assert len(partition) == len(k), 'The number of specified capacities should match the number of partitions'
       
        E = set()
        for P in partition:
            E.update(P)
        self.E = frozenset(E)    
        
    def groundset(self):
        return self.E
     
    def _rank(self,X):
        X2 = set(X)
        used_indices = []
        rk = 0
        while X2:
            e = X2.pop()
            for i in range(len(self.partition)):
                if e in self.partition[i]:
                    # Count number of uses for each partition i
                    # The number of allowed uses is determined by k
                    if Counter(used_indices)[i]<self.k[i]:
                        used_indices.append(i)
                        rk = rk + 1 
                    break # Break if partition i has been used too many times
        return rk
    
p = [[0,1],[2,3]] # Partitions
k = [1,1]         # Capacities

M = PartitionMatroid(partition=p, capacity=k) # Matroid
