import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ducks import models

class DuckService():

	def createNewDuck(self):
		return models.Duck()