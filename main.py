import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtGui
from PyQt5.QtCore import *
import imageio
import numpy as np
from funciones import *


class pantalla(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("interfaz.ui", self)

        self.boton.clicked.connect(self.getItem)

    def getItem(self):
        opc = self.opciones.currentText()
        img = realizarOperacion(opc)
        mostrarResultado(self, img)


def mostrarResultado(self, rgb):
    rgb = np.clip(rgb, 0, 255)
    h, w, _ = rgb.shape
    im = QtGui.QImage(rgb.astype(np.uint8), w, h, 3 *
                      w, QtGui.QImage.Format_RGB888)
    pix = QtGui.QPixmap.fromImage(im)
    self.label_3.setPixmap(pix)


def realizarOperacion(opc):
    if opc == "Suma Clampeada RGB":
        return cuasiSumaRGB_Clamp(img1, img2)*255
    elif opc == "Suma Promediada RGB":
        return cuasiSumaRGB_Prom(img1, img2)*255
    elif opc == "Resta Clampeada RGB":
        return cuasiRestaRGB_Clamp(img1, img2)*255
    elif opc == "Resta Promediada RGB":
        return cuasiRestaRGB_Prom(img1, img2)*255
    elif opc == "Suma Clampeada YIQ":
        YA, IA, QA = pasar_a_YIQ(img1)
        YB, IB, QB = pasar_a_YIQ(img2)
        YC, IC, QC = cuasiSumaYIQ_Clamp(YA, IA, QA, YB, IB, QB)
        return pasar_a_RGB(YC, IC, QC)
    elif opc == "Resta Clampeada YIQ":
        YA, IA, QA = pasar_a_YIQ(img1)
        YB, IB, QB = pasar_a_YIQ(img2)
        YC, IC, QC = cuasiRestaYIQ_Clamp(YA, IA, QA, YB, IB, QB)
        return pasar_a_RGB(YC, IC, QC)
    elif opc == "Suma Promediada YIQ":
        YA, IA, QA = pasar_a_YIQ(img1)
        YB, IB, QB = pasar_a_YIQ(img2)
        YC, IC, QC = cuasiSumaYIQ_Prom(YA, IA, QA, YB, IB, QB)
        return pasar_a_RGB(YC, IC, QC)
    elif opc == "Resta Promediada YIQ":
        YA, IA, QA = pasar_a_YIQ(img1)
        YB, IB, QB = pasar_a_YIQ(img2)
        YC, IC, QC = cuasiRestaYIQ_Prom(YA, IA, QA, YB, IB, QB)
        return pasar_a_RGB(YC, IC, QC)
    elif opc == "Producto":
        return productoRGB(img1, img2)*255
    elif opc == "Cociente":
        return cocienteRGB(img1, img2)*255
    elif opc == "Resta en Valor Absoluto":
        return restaAbsoluta(img1, img2)*255
    elif opc == "If darker":
        return ifDarker(img1, img2)*255
    elif opc == "If ligther":
        return ifLigther(img1, img2)*255


img1 = normalizar_RGB(imageio.imread(
    'imageio:coffee.png')[:, 50:550, :])
img2 = normalizar_RGB(imageio.imread(
    'imageio:astronaut.png')[56:456, 6:506, :])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    GUI = pantalla()
    GUI.show()
    sys.exit(app.exec_())
