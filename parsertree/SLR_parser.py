class Parser:
    # state, non-terminal, goto
    goto = [[3, 'block', 4],
            [5, 'decls', 7],
            [7, 'decl', 10], [7, 'vtype', 17], [7, 'slist', 9], [7, 'stat', 11],
            [9, 'stat', 21],
            [12, 'cond', 23], [12, 'expr', 24], [12, 'term', 25], [12, 'fact', 26],
            [13, 'cond', 29], [13, 'expr', 24], [13, 'term', 25], [13, 'fact', 26],
            [15, 'expr', 31], [15, 'term', 25], [15, 'fact', 26],
            [29, 'slist', 38],
            [30, 'expr', 39], [30, 'term', 25], [30, 'fact', 26],
            [33, 'block', 42],
            [34, 'expr', 43], [34, 'term', 25], [34, 'fact', 26],
            [35, 'expr', 44], [35, 'term', 25], [35, 'fact', 26],
            [36, 'term', 45], [36, 'fact', 26],
            [37, 'fact', 46],
            [48, 'block', 49]]

    action = [[0,'word','s',1],
              [1,'(','s',2],
              [2,')','s',3],
              [3,'{','s',5],[3,'eps','s',6],
              [4,'$','Accept'],
              [5,'eps','s',8],
              [6,'word','r',8],[6,'IF','r',8],[6,'ELSE','r',8],[6,'WHILE','r',8],[6,'EXIT','r',8],[6,'eps','r',8],[6,'$','r',8],
              [7,'word','s',14],[7,'int','s',18],[7,'char','s',19],[7,'IF','s',12],[7,'WHILE','s',13],[7,'EXIT','s',15],[7,'eps','s',16],
              [8,'word','r',2],[8,'int','r',2],[8,'char','r',2],[8,'IF','r',2],[8,'WHILE','r',2],[8,'EXIT','r',2],[8,'eps','r',2],
              [9,'word','s',14],[9,'}','s',20],[9,'IF','s',12],[9,'WHILE','s',13],[9,'EXIT','s',15],[9,'eps','s',22],
              [10,'word','r',1],[10,'int','r',1],[10,'char','r',1],[10,'IF','r',1],[10,'WHILE','r',1],[10,'EXIT','r',1],[10,'eps','r',1],
              [11,'word','r',10],[11,'IF','r',10],[11,'WHILE','r',10],[11,'EXIT','r',10],[11,'eps','r',10],
              [12,'word','s',28],[12,'num','s',27],
              [13,'word','s',28],[13,'num','s',27],
              [14,'=','s',30],
              [15,'word','s',28],[15,'num','s',27],
              [16,'word','r',15],[16,'num','r',6],[16,'IF','r',15],[16,'WHILE','r',15],[16,'EXIT','r',15],[16,'eps','r',15],
              [17,'word','s',32],[18,'word','r',4],[19,'word','r',5],
              [20,'word','r',7],[20,'IF','r',7],[20,'ELSE','r',7],[20,'WHILE','r',7],[20,'EXIT','r',7],[20,'eps','r',7],[20,'$','r',7],
              [21,'word','r',9],[21,'IF','r',9],[21,'WHILE','r',9],[21,'EXIT','r',9],[21,'eps','r',9],
              [22,'word','r',15],[22,'IF','r',15],[22,'WHILE','r',15],[22,'EXIT','r',15],[22,'eps','r',15],
              [23,'THEN','s',33],[24,'>','s',34],[24,'==','s',35],
              [25,'{','r',18],[25,'THEN','r',18],[25,'>','r',18],[25,'==','r',18],[25,'+','s',36],[25,';','r',18],[25,'eps','r',18],
              [26,'{','r',20],[26,'THEN','r',20],[26,'>','r',20],[26,'==','r',20],[26,'*','s',37],[26,';','r',20],[26,'eps','r',20],
              [27,'{','r',22],[27,'THEN','r',22],[27,'>','r',22],[27,'==','r',22],[27,'+','r',22],[27,'*','r',22],[27,';','r',22],[27,'eps','r',22],
              [28,'{','r',23],[28,'THEN','r',23],[28,'>','r',23],[28,'==','r',23],[28,'+','r',23],[28,'*','r',23],[28,';','r',23],[28,'eps','r',23],
              [29,'{','s',5],[29,'eps','s',6],
              [30,'word','s',28],[30,'num','s',27],
              [31,';','s',40],[32,';','s',41],[33,'{','s',5],[33,'eps','s',6],
              [34,'word','s',28],[34,'num','s',27],[35,'word','s',28],[35,'num','s',27],[36,'word','s',28],[36,'num','s',27],
              [37,'word','s',28],[37,'num','s',27],
              [38,'word','r',12],[38,'IF','r',12],[38,'WHILE','r',12],[38,'EXIT','r',12],[38,'eps','r',12],
              [39,';','s',47],[40,'word','r',14],[40,'IF','r',14],[40,'WHILE','r',14],[40,'EXIT','r',14],[40,'eps','r',14],
              [41,'word','r',3],[41,'int','r',3],[41,'char','r',3],[41,'IF','r',3],[41,'WHILE','r',3],[41,'EXIT','r',3],[41,'eps','r',3],
              [42,'ELSE','s',48],[43,'{','r',16],[43,'THEN','r',16],[43,'eps','r',16],[44,'{','r',17],[44,'THEN','r',17],[44,'eps','r',17],
              [45,'{','r',19],[45,'THEN','r',19],[45,'>','r',19],[45,'==','r',19],[45,';','r',19],[45,'eps','r',19],
              [46,'{','r',21],[46,'THEN','r',21],[46,'>','r',21],[46,'==','r',21],[46,'+','r',21],[46,';','r',21],[46,'eps','r',21],
              [47,'word','r',13],[47,'IF','r',13],[47,'WHILE','r',13],[47,'EXIT','r',13],[47,'eps','r',13],
              [48,'{','s',5],[48,'eps','s',6],
              [49,'word','r',11],[49,'IF','r',11],[49,'WHILE','r',11],[49,'EXIT','r',11],[49,'eps','r',11]]
    
    def __init__(self, tokens: list):
        self.tokens = tokens
        self.stack = ['$', 0]
        self.input_list = ['$']
        self.log=list()

    # lexer: tokens ----(terminal)---> parser: input stack
    # terminals: 'word', 'num', parenthesis, operator, statement, semicolon
    def make_input(self):
        i = len(self.tokens)
        for j in range(i-1, -1, -1):
            if self.tokens[j][0] == 'vtype':
                self.input_list.append(self.tokens[j][1])
            elif self.tokens[j][0] == 'word':
                self.input_list.append('word')
            elif self.tokens[j][0] == 'num':
                self.input_list.append('num')
            else:
                self.input_list.append(self.tokens[j][1])
        print()       
        print(self.input_list)

    def parsing(self):
        s_top = self.stack.pop()
        i_top = self.input_list.pop()
        
        if self.action_goto_table(s_top, i_top) == -1:
            print(self.stack)
            print(self.input_list)
            print()
            self.parsing()
        elif self.action_goto_table(s_top, i_top) == 0:
            print("Accept!")
        elif self.action_goto_table(s_top, i_top) == -2:
            print("Grammatically incorrect!")

    def action_goto_table(self, s_top, i_top):
        for i in range(len(Parser.action)):
            if Parser.action[i][0] == s_top and Parser.action[i][1] == i_top:
                # accept
                if Parser.action[i][2] == 'Accept':
                    return 0
                # shift
                if Parser.action[i][2] == 's':
                    self.stack.append(s_top)
                    self.stack.append(i_top)
                    self.stack.append(Parser.action[i][3])
                    return -1
                # reduce
                elif Parser.action[i][2] == 'r':
                    self.input_list.append(i_top)
                    if Parser.action[i][3] == 0:
                        while True:
                            if self.stack.pop() == 'word':
                                break
                        self.stack.append('prog')
                        self.log.append('r0')
                    elif Parser.action[i][3] == 1:
                        while True:
                            if self.stack.pop() == 'decls':
                                break
                        self.stack.append('decls')
                        self.log.append('r1')
                    elif Parser.action[i][3] == 2:
                        while True:
                            if self.stack.pop() == 'eps':
                                break
                        self.stack.append('decls')
                        self.log.append('r2')
                    elif Parser.action[i][3] == 3:
                        while True:
                            if self.stack.pop() == 'vtype':
                                break
                        self.stack.append('decl')
                        self.log.append('r3')
                    elif Parser.action[i][3] == 4:
                        while True:
                            if self.stack.pop() == 'int':
                                break
                        self.stack.append('vtype')
                        self.log.append('r4')
                    elif Parser.action[i][3] == 5:
                        while True:
                            if self.stack.pop() == 'char':
                                break
                        self.stack.append('vtype')
                        self.log.append('r5')
                    elif Parser.action[i][3] == 6:
                        while True:
                            if self.stack.pop() == 'eps':
                                break
                        self.stack.append('vtype')
                        self.log.append('r6')
                    elif Parser.action[i][3] == 7:
                        while True:
                            if self.stack.pop() == '{':
                                break
                        self.stack.append('block')
                        self.log.append('r7')
                    elif Parser.action[i][3] == 8:
                        while True:
                            if self.stack.pop() == 'eps':
                                break
                        self.stack.append('block')
                        self.log.append('r8')
                    elif Parser.action[i][3] == 9:
                        while True:
                            if self.stack.pop() == 'slist':
                                break
                        self.stack.append('slist')
                        self.log.append('r9')
                    elif Parser.action[i][3] == 10:
                        while True:
                            if self.stack.pop() == 'stat':
                                break
                        self.stack.append('slist')
                        self.log.append('r10')
                    elif Parser.action[i][3] == 11:
                        while True:
                            if self.stack.pop() == 'IF':
                                break
                        self.stack.append('stat')
                        self.log.append('r11')
                    elif Parser.action[i][3] == 12:
                        while True:
                            if self.stack.pop() == 'WHILE':
                                break
                        self.stack.append('stat')
                        self.log.append('r12')
                    elif Parser.action[i][3] == 13:
                        while True:
                            if self.stack.pop() == 'word':
                                break
                        self.stack.append('stat')
                        self.log.append('r13')
                    elif Parser.action[i][3] == 14:
                        while True:
                            if self.stack.pop() == 'EXIT':
                                break
                        self.stack.append('stat')
                        self.log.append('r14')
                    elif Parser.action[i][3] == 15:
                        while True:
                            if self.stack.pop() == 'eps':
                                break
                        self.stack.append('stat')
                        self.log.append('r15')
                    elif Parser.action[i][3] == 16:
                        while True:
                            if self.stack.pop() == '>':
                                break
                        while True:
                            if self.stack.pop() == 'expr':
                                break
                        self.stack.append('cond')
                        self.log.append('r16')
                    elif Parser.action[i][3] == 17:
                        while True:
                            if self.stack.pop() == '==':
                                break
                        while True:
                            if self.stack.pop() == 'expr':
                                break
                        self.stack.append('cond')
                        self.log.append('r17')
                    elif Parser.action[i][3] == 18:
                        while True:
                            if self.stack.pop() == 'term':
                                break
                        self.stack.append('expr')
                        self.log.append('r18')
                    elif Parser.action[i][3] == 19:
                        while True:
                            if self.stack.pop() == '+':
                                break
                        while True:
                            if self.stack.pop() == 'term':
                                break
                        self.stack.append('expr')
                        self.log.append('r19')
                    elif Parser.action[i][3] == 20:
                        while True:
                            if self.stack.pop() == 'fact':
                                break
                        self.stack.append('term')
                        self.log.append('r20')
                    elif Parser.action[i][3] == 21:
                        while True:
                            if self.stack.pop() == '*':
                                break
                        while True:
                            if self.stack.pop() == 'fact':
                                break
                        self.stack.append('term')
                        self.log.append('r21')
                    elif Parser.action[i][3] == 22:
                        while True:
                            if self.stack.pop() == 'num':
                                break
                        self.stack.append('fact')
                        self.log.append('r22')
                    elif Parser.action[i][3] == 23:
                        while True:
                            if self.stack.pop() == 'word':
                                break
                        self.stack.append('fact')
                        self.log.append('r23')

                    for j in range(len(Parser.goto)):
                        if Parser.goto[j][0] == self.stack[-2] and Parser.goto[j][1] == self.stack[-1]:
                            self.stack.append(Parser.goto[j][2])
                    return -1

            elif Parser.action[i][0] == s_top and Parser.action[i][1] == 'eps':
                # accept
                if Parser.action[i][2] == 'Accept':
                        return 0
                # shift
                if Parser.action[i][2] == 's':
                    self.input_list.append(i_top)
                    self.stack.append(s_top)
                    self.stack.append('eps')
                    self.stack.append(Parser.action[i][3])
                    return -1
                # reduce
                elif Parser.action[i][2] == 'r':
                    self.input_list.append(i_top)
                    if Parser.action[i][3] == 0:
                        while True:
                            if self.stack.pop() == 'word':
                                break
                        self.stack.append('prog')
                    elif Parser.action[i][3] == 1:
                        while True:
                            if self.stack.pop() == 'decls':
                                break
                        self.stack.append('decls')
                    elif Parser.action[i][3] == 2:
                        while True:
                            if self.stack.pop() == 'eps':
                                break
                        self.stack.append('decls')
                    elif Parser.action[i][3] == 3:
                        while True:
                            if self.stack.pop() == 'vtype':
                                break
                        self.stack.append('decl')
                    elif Parser.action[i][3] == 4:
                        while True:
                            if self.stack.pop() == 'int':
                                break
                        self.stack.append('vtype')
                    elif Parser.action[i][3] == 5:
                        while True:
                            if self.stack.pop() == 'char':
                                break
                        self.stack.append('vtype')
                    elif Parser.action[i][3] == 6:
                        while True:
                            if self.stack.pop() == 'eps':
                                break
                        self.stack.append('vtype')
                    elif Parser.action[i][3] == 7:
                        while True:
                            if self.stack.pop() == '{':
                                break
                        self.stack.append('block')
                    elif Parser.action[i][3] == 8:
                        while True:
                            if self.stack.pop() == 'eps':
                                break
                        self.stack.append('block')
                    elif Parser.action[i][3] == 9:
                        while True:
                            if self.stack.pop() == 'slist':
                                break
                        self.stack.append('slist')
                    elif Parser.action[i][3] == 10:
                        while True:
                            if self.stack.pop() == 'stat':
                                break
                        self.stack.append('slist')
                    elif Parser.action[i][3] == 11:
                        while True:
                            if self.stack.pop() == 'IF':
                                break
                        self.stack.append('stat')
                    elif Parser.action[i][3] == 12:
                        while True:
                            if self.stack.pop() == 'WHILE':
                                break
                        self.stack.append('stat')
                    elif Parser.action[i][3] == 13:
                        while True:
                            if self.stack.pop() == 'word':
                                break
                        self.stack.append('stat')
                    elif Parser.action[i][3] == 14:
                        while True:
                            if self.stack.pop() == 'EXIT':
                                break
                        self.stack.append('stat')
                    elif Parser.action[i][3] == 15:
                        while True:
                            if self.stack.pop() == 'eps':
                                break
                        self.stack.append('stat')
                    elif Parser.action[i][3] == 16:
                        while True:
                            if self.stack.pop() == '>':
                                break
                        while True:
                            if self.stack.pop() == 'expr':
                                break
                        self.stack.append('cond')
                    elif Parser.action[i][3] == 17:
                        while True:
                            if self.stack.pop() == '==':
                                break
                        while True:
                            if self.stack.pop() == 'expr':
                                break
                        self.stack.append('cond')
                    elif Parser.action[i][3] == 18:
                        while True:
                            if self.stack.pop() == 'term':
                                break
                        self.stack.append('expr')
                    elif Parser.action[i][3] == 19:
                        while True:
                            if self.stack.pop() == '+':
                                break
                        while True:
                            if self.stack.pop() == 'term':
                                break
                        self.stack.append('expr')
                    elif Parser.action[i][3] == 20:
                        while True:
                            if self.stack.pop() == 'fact':
                                break
                        self.stack.append('term')
                    elif Parser.action[i][3] == 21:
                        while True:
                            if self.stack.pop() == '*':
                                break
                        while True:
                            if self.stack.pop() == 'fact':
                                break
                        self.stack.append('term')
                    elif Parser.action[i][3] == 22:
                        while True:
                            if self.stack.pop() == 'num':
                                break
                        self.stack.append('fact')
                    elif Parser.action[i][3] == 23:
                        while True:
                            if self.stack.pop() == 'word':
                                break
                        self.stack.append('fact')

                    for j in range(len(Parser.goto)):
                        if Parser.goto[j][0] == self.stack[-2] and Parser.goto[j][1] == self.stack[-1]:
                            self.stack.append(Parser.goto[j][2])
                        
                    return -1
          
        return -2
                
                    
                                

