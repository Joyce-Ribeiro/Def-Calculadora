from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPainterPath
import sys
import math

def chama_log_tela():
    log_tela.show()
    log_tela.setWindowTitle('Logarítmica')

def chama_Afim_tela():
    afim_tela.show()
    afim_tela.setWindowTitle('Afim')

def chama_Quad_tela():
    quad_tela.show()
    quad_tela.setWindowTitle('Quadrática')

def selct_afim_compF():
    valorF = afim_tela.spnF.value()
    afim_tela.lblF.setText(str(valorF))
    return valorF

def selct_afim_compA():
    valorA = afim_tela.spnA.value()
    afim_tela.lblA.setText(str(valorA))
    return valorA

def selct_afim_compB():
    valorB = afim_tela.spnB.value()
    afim_tela.lblB.setText(str(valorB))
    return valorB

def selct_afim_compX():
    valorX=afim_tela.lbl_resAfim.text()
    return valorX

def selct_log_A():
    valorA=log_tela.spnAlog.value()
    log_tela.lblLogA.setText(str(valorA))

def select_log_B():
    valorB = log_tela.spnBase.value()
    log_tela.lblLogB.setText(str(valorB))

def selct_quad_compC():
    valorC = quad_tela.spnC.value()
    quad_tela.lblCQu.setText(str(valorC))
    quad_tela.lblCQ.setText(str(valorC))

def selct_quad_compA():
    valorA = quad_tela.spnA.value()
    quad_tela.lblAQu.setText(str(valorA))
    quad_tela.lblAQ.setText(str(valorA))

def selct_quad_compB():
    valorB = quad_tela.spnB.value()
    quad_tela.lblBQu.setText(str(valorB))
    quad_tela.lblBQ.setText(str(valorB))

def calc_a():
    f = str(afim_tela.lblF.text())
    a = str(afim_tela.lblA.text())
    b = str(afim_tela.lblB.text())
    if f != 'f(x)   ' and a != 'A' and b != 'B':
        f= int(str(f))
        b=int(str(b))
        a=int(str(a))
        if f == 0:
            raiz = b/a
        else:

            n1 = f - b
            raiz = n1 / a

        afim_tela.lbl_resAfim.setText(str(raiz))

def calc_quad():
    if quad_tela.lblCQ.text()!= "C" and quad_tela.lblAQ.text()!= "A" and quad_tela.lblBQ.text()!="B":
        c = (quad_tela.lblCQ.text())
        a = (quad_tela.lblAQ.text())
        b = (quad_tela.lblBQ.text())
        c= int(str(c))
        b=int(str(b))
        a=int(str(a))

        delta = (b ** 2) - 4 * a * c
        raizdelta = delta ** 0.5
        x1=(-b+ raizdelta)//(2*a)
        x2=(-b- raizdelta)//(2*a)

        quad_tela.lblDeltQ.setText(str(delta))
        quad_tela.lblBX.setText(str(b))
        quad_tela.lblAX.setText(str(a))
        quad_tela.lblBX_2.setText(str(b))
        quad_tela.lblAX_2.setText(str(a))
        quad_tela.DeltaX.setText(str(delta))
        quad_tela.DeltaX_2.setText(str(delta))
        quad_tela.X1.setText(str(x1))
        quad_tela.X1_2.setText(str(x2))

def calc_log():
    a=float(str(log_tela.lblLogA.text()))
    b=float(str(log_tela.lblLogB.text()))
    f = math.log(a, b)
    log_tela.lblLogRes.setText(str(f))


class GraficoAfim(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 280, 270)
        self.setWindowTitle('Gráfico Afim')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawLines(qp)
        qp.end()

    def drawLines(self, qp):
        pen = QPen(Qt.black, 2, Qt.SolidLine)

        qp.setPen(pen)
        qp.drawLine(140, 10, 140, 260)
        pen = QPen(Qt.black, 2, Qt.SolidLine)

        qp.setPen(pen)
        qp.drawLine(20, 130, 250, 130)
        a = selct_afim_compA()
        b = selct_afim_compB()
        y = b

        if a < 0:
            if y < 0:
                pen = QPen(Qt.red, 2, Qt.SolidLine)

                qp.setPen(pen)
                qp.drawLine(30, 40, 180, 250)
            if y > 0:
                pen = QPen(Qt.red, 2, Qt.SolidLine)

                qp.setPen(pen)
                qp.drawLine(40, 20, 280, 200)
            if y == 0:
                pen = QPen(Qt.red, 2, Qt.SolidLine)

                qp.setPen(pen)
                qp.drawLine(10, 10, 270, 250)

        else:
            if y > 0:
                pen = QPen(Qt.red, 2, Qt.SolidLine)

                qp.setPen(pen)
                qp.drawLine(30, 180, 250, 40)

            if y < 0:
                pen = QPen(Qt.red, 2, Qt.SolidLine)

                qp.setPen(pen)
                qp.drawLine(50, 240, 270, 80)
            if y == 0:
                pen = QPen(Qt.red, 2, Qt.SolidLine)

                qp.setPen(pen)
                qp.drawLine(270, 10, 10, 250)

class ExampleQ(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 380, 250)
        self.setWindowTitle('Bézier curve')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing)
        self.drawBezierCurve(qp)
        qp.end()

    def drawBezierCurve(self, qp):
        path = QPainterPath()
        path.moveTo(30, 30)
        path.cubicTo(30, 30, 200, 350, 350, 30)

        qp.drawPath(path)

#DEFININDO TELAS#
app= QtWidgets.QApplication([])
def_menu = uic.loadUi("Def.ui")
def_menu.setWindowTitle('Def calculadora')
afim_tela = uic.loadUi("Afim_tela.ui")
quad_tela = uic.loadUi("Quad_tela.ui")
log_tela = uic.loadUi("Log_tela.ui")


#DEFININDO BOTOES#

def_menu.btnAfim.clicked.connect(chama_Afim_tela)
def_menu.btnQuad.clicked.connect(chama_Quad_tela)
def_menu.btnLog.clicked.connect(chama_log_tela)
afim_tela.btnCAfim.clicked.connect(calc_a)
log_tela.btncalcLog.clicked.connect(calc_log)

#quad_tela.btnCalcQ.clicked.connect(chama_Afim.calc_quad)

afim_tela.spnA.valueChanged.connect(selct_afim_compA)
afim_tela.spnB.valueChanged.connect(selct_afim_compB)
afim_tela.spnF.valueChanged.connect(selct_afim_compF)


quad_tela.spnA.valueChanged.connect(selct_quad_compA)
quad_tela.spnB.valueChanged.connect(selct_quad_compB)
quad_tela.spnC.valueChanged.connect(selct_quad_compC)
quad_tela.btnCalcQ.clicked.connect(calc_quad)

log_tela.spnAlog.valueChanged.connect(selct_log_A)
log_tela.spnBase.valueChanged.connect(select_log_B)


#INICIALIZANDO PROGRAMA#

def_menu.show()
app.exec()

app1 = QtWidgets.QApplication(sys.argv)
ex = GraficoAfim()
ex.show()
app1.exec_()
#afim_tela.btngrafic.clicked.connect()