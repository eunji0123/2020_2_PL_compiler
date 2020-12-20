from stack import *

class node:
    def __init__(self):
        self.data=None
        self.r_number=0
        self.parent=None
        self.child=list()

    def Data(self, data):
        self.data=data