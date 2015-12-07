__author__ = 'neufrin'
import Block

class Box(Block.Block):
    def __init__(self, x, y,mode):
         if(mode == "$" ):
            super(Box, self,).__init__("$", x, y)
         elif(mode == "*"):
            super(Box, self,).__init__("*", x, y)

    def setOn(self):
        self.setSprite("*")

    def setOff(self):
        self.setSprite("$")


