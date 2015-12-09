__author__ = 'neufrin'


class MapLoader:

    def load(self,mapname):
        self.mapName = mapname
        fo = open("Content\\Levels\\"+mapname+".txt")
        self.map = fo.read().splitlines()
        fo.close()
        return self.map
