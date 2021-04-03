from PyQt5.QtWidgets import QFileDialog, QLabel
import numpy as np
import os
from .models import ImgData


class MainController():
    def __init__(self, widget):
        self.widget = widget
        self._create_connections()
        self.data = ImgData()

    
    def _create_connections(self):
        #buttons
        self.widget.pushButton.clicked.connect(self.loadData)


    #slots
    def loadData(self):
        posSlice, scaleSlice, imgSlice = self.data.get_slice_parallel()
        self.widget.graphicsView.setImage(imgSlice, pos=posSlice, scale=scaleSlice)

        posPerp, scalePerp, imgPerp = self.data.get_slice_perp()
        self.widget.graphicsView_2.setImage(imgPerp, pos=posPerp, scale=scalePerp)

        posPerp2, scalePerp2, imgPerp2 = self.data.get_slice_perp2()
        self.widget.graphicsView_3.setImage(imgPerp2, pos=posPerp2, scale=scalePerp2)