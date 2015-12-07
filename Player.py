__author__ = 'neufrin'

__author__ = 'neufrin'
import Block

class Player(Block.Block):
    def __init__(self, x, y):
        super(Player, self,).__init__("@", x, y)