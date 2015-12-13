__author__ = 'neufrin'
import MainMenu
import Credits
import FinishedLevel
import SelectLevel
import Level


screens = {"level" : Level.Level(),
           "mainmenu" : MainMenu.MainMenu(),
           "finishedlevel" : FinishedLevel.FinishedLevel(),
           "selectlevel" : SelectLevel.SelectLevel(),
           "credits" : Credits.Credits(),
          }