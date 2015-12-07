__author__ = 'neufrin'
import Block

class Box(Block.Block):
    def __init__(self, x, y):
        super(Box, self,).__init__("$", x, y)
