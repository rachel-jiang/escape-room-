"""from panda3d.core import loadPrcFile
loadPrcFile("config/conf.prc")

from direct.showbase.ShowBase import ShowBase

class MyGame(ShowBase):
	def__init__(self):
		super().__init__()

		m = loader.loadModel("room1.egg")
		env.reparentTo(self.render)


game=MyGame()
game.run()"""

from direct.showbase.ShowBase import ShowBase
from panda3d.core import loadPrcFile
loadPrcFile("config/conf.prc")


class MyApp(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)

        # Load the environment model.
        #self.scene = self.loader.loadModel("room1.obj")
        self.scene = self.loader.loadModel("room1_color.obj")
        # Reparent the model to render.
        self.scene.reparentTo(self.render)
        # Apply scale and position transforms on the model.
        self.scene.setScale(0.5, 0.5, 0.5)
        self.scene.setPos(-8, 42, 0)


app = MyApp()
app.run()