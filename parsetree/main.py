from tree import *

reduce_log=['r2', 'r22', 'r20', 'r18', 'r13', 'r10', 'r22', 'r20', 'r18', 'r13', 'r9', 'r22', 'r20', 'r22', 'r19', 'r13', 'r9', 'r7', 'r0'] #parsing table에서 accept 나올 때까지 했던 reduce 연산

tree=parsetree(reduce_log)
root=tree.maketree()