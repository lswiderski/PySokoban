__author__ = 'neufrin'


class MapLoader:
    def __init__(self,mapname):
        self.load(mapname)
        self.mapName = mapname
        self.lastMapName = mapname
        self.lastMap = self.map

    def load(self,mapname):
        self.mapName = mapname
        fo = open("Content\\Levels\\"+mapname+".txt")
        self.map = fo.read().splitlines()
        fo.close()
        return self.map
