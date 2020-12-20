from node import *
from stack import *

class parsetree:
    nonterminal=['prog', 'decls', 'decl', 'block', 'slist', 'stat', 'cond', 'expr', 'term', 'fact']

    print_data=['word', 'num', 'IF', 'THEN', 'ESLE', 'WHILE', 'EXIT', '=', '>', '==', '+', '*']

# reduce_log=['r2', 'r22', 'r20', 'r18', 'r13', 'r10', 'r22', 'r20', 'r18', 'r13', 'r9', 'r22', 'r20', 'r22', 'r19', 'r13', 'r9', 'r7', 'r0'] #parsing table에서 accept 나올 때까지 했던 reduce 연산

    handle={'r0': ['prog', ['word', '(', ')', 'block']], 'r1': ['decls', ['decls', 'decl']], 'r2': ['decls', [' ']], 'r3': ['decl', ['vtype', 'word', ';']], 'r4': ['vtype', ['int']], 'r5': ['vtype', ['char']], 'r6': ['vtype', [' ']], 'r7': ['block', ['{', 'decls', 'slist', '}']], 'r8': ['block', [' ']], 'r9': ['slist', ['slist', 'stat']], 'r10': ['slist', ['stat']], 'r11': ['stat', ['IF', 'cond', 'THEN', 'block', 'ELSE', 'block']], 'r12': ['stat', ['WHILE', 'cond', 'block']], 'r13': ['stat', ['word', '=', 'expr', ';']], 'r14': ['stat', ['EXIT', 'expr', ';']], 'r15': ['stat', [' ']], 'r16': ['cond', ['expr', '>', 'expr']], 'r17': ['cond', ['expr', '==', 'epxr']], 'r18': ['expr', ['term']], 'r19': ['expr', ['term', '+', 'term']], 'r20': ['term', ['fact']], 'r21': ['term', ['fact', '*', 'fact']], 'r22': ['fact', ['num']], 'r23': ['fact', ['word']]} #value [A, [B, C, D]] == A->B C D

    def __init__(self):
        self.stack=stack()
        self.root=None
    
    def maketree(self, reduce_log):
        for i in reduce_log:
            # print(i)
            data=parsetree.handle.get(i)
            root=node()
            root.Data(data[0])

            data[1].reverse() #A->B C D 일때 D C B 순서대로 입력받기

            for j in data[1]:
                if j in parsetree.nonterminal:
                    temp=self.stack.peek()
                    self.stack.pop()
                else:
                    temp=node()
                    temp.Data(j)
        
                temp.parnet=root
                root.child.append(temp)
    
            root.child.reverse()
            # for j in root.child:
            #     print("parent=  "+ root.data + " child= ", j.data)

            self.stack.push(root)
            self.root=root
        # self.numbering(self.root)
        return self

    # def numbering(self, root):
    #     # print('root', root.data, root.r_number)
    #     if root.child==False:
    #         return

    #     for i in root.child:
    #         i.r_number=root.r_number+root.child.index(i)
    #         if i.r_number>self.max_reg:
    #             self.max_reg=i.r_number
    #         self.numbering(i)
    #         # print('child', i.data, i.r_number)
            