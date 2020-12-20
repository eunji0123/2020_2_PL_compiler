class Symbol_table:
    def __init__(self, tokens: list):
        self.tokens = tokens
        self.length = len(tokens)
        self.symbol_table = []

    def make_table(self):
        i = 0
        # count the number of open parenthesis and close parenthesis
        open_count = 0
        close_count = 0

        while i+2 < self.length:
            if self.tokens[i][1] == '{':
                open_count += 1
                
            elif self.tokens[i][1] == '}':
                close_count += 1
                
            elif self.tokens[i][0] == 'vtype':
                name = self.tokens[i+1][1]
                symbol_type = self.tokens[i][1] # if function, add it later
                # size based on type
                if symbol_type == 'int':
                    size = 4
                else: # symbol_type == 'char'
                    size = 1
                
                # ), =, ; : variable
                # especially, ) : function parameter
                # ( : function
                if self.tokens[i+2][1] in [';', '=']:
                    if open_count > close_count:
                        scope = 'block local'
                    elif open_count == close_count:
                        scope = 'global'

                elif self.tokens[i+2][1] == ')':
                    scope = 'function parameter'

                elif self.tokens[i+2][1] == '(':
                    symbol_type = 'function, ' + symbol_type
                    scope = 'global'

                self.symbol_table.append((name, symbol_type, scope, size))

            i += 1

            
                    
            
                    
