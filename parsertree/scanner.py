class Scanner:
    parenthesis = ['(', ')', '{', '}']
    vtype = ['int', 'char']
    statement = ['IF', 'THEN', 'ELSE', 'WHILE', 'EXIT']
    operator = ['=', '>', '==', '+', '*']
    
    def __init__(self, source: str):
        self.source = source # source file
        self.tokens = [] # store tokens into the list 'tokens'
        self.length = len(source) # length of the source file

    def scan(self):
        ch = 0 # points to the next character

        while ch < self.length:
            # strip out white spaces
            if self.source[ch] == ' ' or self.source[ch] == '\n':
                ch += 1

            # semicolon
            elif self.source[ch] == ';':
                self.tokens.append(('semicolon', self.source[ch]))
                ch += 1
                
            # num
            elif self.source[ch].isdigit():
                num = ''
                while self.source[ch].isdigit():
                    num += self.source[ch]
                    ch += 1
                self.tokens.append(('num', num))

            # word
            elif self.source[ch].isalpha():
                word = ''
                while self.source[ch].isalpha():
                    word += self.source[ch]
                    ch += 1
                # vtype
                if word in Scanner.vtype:
                    self.tokens.append(('vtype', word))
                # statement
                elif word in Scanner.statement:
                    self.tokens.append(('statement', word))
                # word
                else:
                    self.tokens.append(('word', word))

            # parenthesis
            elif self.source[ch] in Scanner.parenthesis:
                self.tokens.append(('parenthesis', self.source[ch]))
                ch += 1

            # operator
            elif self.source[ch] in Scanner.operator:
                # '==' operator
                if self.source[ch+1] == '=':
                    self.tokens.append(('operator', '=='))
                    ch += 2
                # other operators
                else:
                    self.tokens.append(('operator', self.source[ch]))
                    ch += 1
            # 에러 발생 시 어떻게 할지 생각해보기
            else:
                print("Rejected. The input is not valid.")
