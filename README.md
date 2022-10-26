# partition-matroid
A Sage based class for creating partition matroids with tuneable capacities.

## Partition Matroids

A matroid is defined by:

$M = (E,I)$

with ground set $E$ and family of independent sets $I$. 

For a partition matroid the ground set $E$ is partitioned into disjoint sets $E_1,E_2...E_l$ and an independent set $X$ must follow:

$I = \{ X \in E: |X \cap E_i \le k_i| \} $ 

for all $i = 1,...,l$


So the size of the intersection of the independent set with each partition $E_i$ must be at max $k_i$.

For more background see:
https://math.mit.edu/~goemans/18433S09/matroid-notes.pdf
