import os
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from pyqtgraph.graphicsItems.PlotItem import PlotItem
from pyqtgraph.imageview import ImageView


class mainWindow(QMainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.load_ui()
        self.mainWindow_setup()


    def load_ui(self):
        path = os.path.join(os.path.dirname(__file__), "form.ui")
        uic.loadUi(path, self)

    def mainWindow_setup(self):
         self.setWindowTitle("ploting the crosssections")


class mainWindow2(QMainWindow):
    def __init__(self):
        super(mainWindow2, self).__init__()
        self.load_ui()
        self.mainWindow_setup()


    def load_ui(self):
        path = os.path.join(os.path.dirname(__file__), "second_app.ui")
        uic.loadUi(path, self)

    def mainWindow_setup(self):
         self.setWindowTitle("ploting the crosssections")
         self.graphicsView_5.getView().invertY(False)
         self.graphicsView_6.getView().invertY(False)
         self.graphicsView_7.getView().invertY(False)
         self.graphicsView_8.getView().invertY(False)



# same as ImageView but with coordinates
class myImageView(ImageView):
    def __init__(self, *args, **kwargs):
        super().__init__(view=PlotItem(), *args, **kwargs)
        self.setPredefinedGradient('flame')
        # self.getView().invertY(False)