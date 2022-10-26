# partition-matroid
A SageMath based class for creating partition matroids with tuneable capacities.

Sage contains examples of creating partition matroids with capacity 1 for each partition. I have created this modified class to allow tuneable capacities. 

The partitions and capicity for each partition can be specified when creating the matroid.

## Partition Matroids

A matroid is defined by:

$M = (E,I)$

with ground set $E$ and family of independent sets $I$. 

For a partition matroid the ground set $E$ is partitioned into disjoint sets $E_1,E_2...E_l$ and the family of independent sets is defined by:

$I = ( X \subseteq E: |X \cap E_i \le k_i|  \ \forall i = 1,...,l )$

So the cardinality / size of the intersection of an independent set with each partition $E_i$ must be at max the capacity $k_i$.

For more background see:
https://math.mit.edu/~goemans/18433S09/matroid-notes.pdf

## Using the class

To use the class specify the desired partitions and capacities for each partition:

'p = [[0,1],[2,3]] # Partitions'
'k = [1,1]         # Capacities'

Then create a partition matroid:

M = PartitionMatroid(partition=p, capacity=k) # Matroid

Check the ground set or independent sets of the matroid with:

M.groundset()
M.independent_sets()

## Dependencies
You need SageMath installed:
https://www.sagemath.org

Tested with SageMath version 9.7 and Python version 3.8.2
