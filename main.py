import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QImage
from PyQt5.QtCore import *
import imageio
import numpy as np
import matplotlib.pyplot as plt


# ESTA ES LA CLASE PRINCIPAL
class pantalla(QMainWindow):

    def __init__(self):
        # Estas dos lineas son obligatorias
        super().__init__()
        uic.loadUi("interfaz.ui", self)

        # Aqui cargo la primera imagen
        rgb = imageio.imread('imageio:astronaut.png')[:, 50:550, :]
        #rgb = img*255
        rgb = np.minimum(rgb, 255)
        rgb = np.maximum(rgb, 0)
        h, w, _ = rgb.shape
        im = QtGui.QImage(rgb.astype(np.uint8), w, h, 3 *
                          w, QtGui.QImage.Format_RGB888)
        pix = QtGui.QPixmap.fromImage(im)
        self.label.setPixmap(pix)

        # Aqui cargo la seguna imagen
        rgb = imageio.imread('imageio:coffee.png')[:, 50:550, :]
        #rgb = img*255
        rgb = np.minimum(rgb, 255)
        rgb = np.maximum(rgb, 0)
        h, w, _ = rgb.shape
        im = QtGui.QImage(rgb.astype(np.uint8), w, h, 3 *
                          w, QtGui.QImage.Format_RGB888)
        pix = QtGui.QPixmap.fromImage(im)
        self.label_2.setPixmap(pix)
        self.boton.clicked.connect(self.getItem)

    # Funcion para saber cual es la opcion elegida

    def getItem(self):
        opc = self.opciones.currentText()
        # Hace alguna de las operaciones con pixeles
        img = realizarOperacion(opc)
        # Muestra el resultado
        mostrarResultado(self, img)


def mostrarResultado(self, img):
    rgb = img*255
    rgb = np.minimum(rgb, 255)
    rgb = np.maximum(rgb, 0)
    h, w, _ = rgb.shape
    im = QtGui.QImage(rgb.astype(np.uint8), w, h, 3 *
                      w, QtGui.QImage.Format_RGB888)
    pix = QtGui.QPixmap.fromImage(im)
    self.label_3.setPixmap(pix)


def cuasiSumaRGB_Clamp(img1, img2):
    return np.clip(img1 + img2, 0, 1)


def realizarOperacion(opc):
    if opc == "Suma Clampeada RGB":
        return cuasiSumaRGB_Clamp(img1, img2)


#img1 = imageio.imread('imageio:coffee.png')[:, 50:550, :]/255
#img2 = imageio.imread('imageio:astronaut.png')[56:456, 6:506, :]/255


# esto inicia la app
if __name__ == "__main__":
    app = QApplication(sys.argv)
    GUI = pantalla()
    GUI.show()
    sys.exit(app.exec_())
