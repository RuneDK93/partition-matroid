# partition-matroid
A Sage based class for creating partition matroids with tuneable capacities.

## Partition Matroids

A matroid is defined by:

$M = (E,I)$

with ground set $E$ and family of independent sets $I$. 

For a partition matroid the ground set $E$ is partitioned into disjoint sets $E_1,E_2...E_l$ and an family of independent sets is defined by:

$I = ( X \subseteq E: |X \cap E_i \le k_i|  \ \forall i = 1,...,l )$

So the cardinality / size of the intersection of an independent set with each partition $E_i$ must be at max the capacity $k_i$.

For more background see:
https://math.mit.edu/~goemans/18433S09/matroid-notes.pdf
