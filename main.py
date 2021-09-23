from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QPen
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPainterPath
from PyQt5.QtWidgets import QDialog
import sys
import math

def chama_log_tela():
    log_tela.show()
    log_tela.setWindowTitle('Logarítmica')

def chama_exp_tela():
    exp_tela.show()
    exp_tela.setWindowTitle('Exponencial')

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
    return valorA
def select_log_B():
    valorB = log_tela.spnBase.value()
    log_tela.lblLogB.setText(str(valorB))
    return valorB

def selct_quad_compC():
    valorC = quad_tela.spnC.value()
    quad_tela.lblCQu.setText(str(valorC))
    quad_tela.lblCQ.setText(str(valorC))
    return valorC
def selct_quad_compA():
    valorA = quad_tela.spnA.value()
    quad_tela.lblAQu.setText(str(valorA))
    quad_tela.lblAQ.setText(str(valorA))
    return valorA
def selct_quad_compB():
    valorB = quad_tela.spnB.value()
    quad_tela.lblBQu.setText(str(valorB))
    quad_tela.lblBQ.setText(str(valorB))
    return valorB

def selct_exp_comf():
    valorF= exp_tela.spnfExp.value()
    exp_tela.lblfExp.setText(str(valorF))
    return valorF
def selct_exp_comb():
    valorB = exp_tela.spnbExp.value()
    exp_tela.lblbExp.setText(str(valorB))
    return valorB
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
        if delta>0 or delta==0:
            raizdelta = delta ** 0.5
            x1=(-b+ raizdelta)//(2*a)
            x2=(-b- raizdelta)//(2*a)
        else:
            x1=0
            x2=0

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

class GraficoAfim(QDialog):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 280, 270)
        self.setWindowTitle('Gráfico Afim')


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

class GraficoQuad(QDialog):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 380, 250)
        self.setWindowTitle('Gráfico Quadrática')

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing)
        self.drawBezierCurve(qp)
        qp.end()

    def drawBezierCurve(self, qp):
        a = selct_quad_compA()
        b = selct_quad_compB()
        c = selct_quad_compC()

        delta = (b ** 2) - 4 * a * c

        if delta > 0 or delta == 0:
            raizdelta = delta ** 0.5
            x1 = (-b + raizdelta) // (2 * a)
            x2 = (-b - raizdelta) // (2 * a)
        else:
            x1 = 0
            x2 = 0

        pen1 = QPen(Qt.black, 2, Qt.SolidLine)

        qp.setPen(pen1)
        qp.drawLine(190, 0, 190, 300)

        pen2 = QPen(Qt.black, 2, Qt.SolidLine)

        qp.setPen(pen2)
        qp.drawLine(0, 130, 400, 130)
        if a > 0:
            if delta > 0:
                if x1 < 0 and x2 > 0 or x1 > 0 and x2 < 0:
                    pen = QPen(Qt.red, 2, Qt.SolidLine)
                    qp.setPen(pen)
                    path = QPainterPath()
                    path.moveTo(80, 10)
                    path.cubicTo(100, 80, 200, 300, 300, 10)
                    qp.drawPath(path)
                if x1 > 0 and x2 > 0:
                    pen = QPen(Qt.red, 2, Qt.SolidLine)
                    qp.setPen(pen)
                    path = QPainterPath()
                    path.moveTo(220, 10)
                    path.cubicTo(200, 100, 230, 300, 300, 10)
                    qp.drawPath(path)
                if x1 < 0 and x2 < 0:
                    pen = QPen(Qt.red, 2, Qt.SolidLine)
                    qp.setPen(pen)
                    path = QPainterPath()
                    path.moveTo(80, 10)
                    path.cubicTo(90, 80, 100, 300, 180, 10)
                    qp.drawPath(path)
            if delta == 0:
                if x1 < 0:
                    pen = QPen(Qt.red, 2, Qt.SolidLine)
                    qp.setPen(pen)
                    path = QPainterPath()
                    path.moveTo(60, 10)
                    path.cubicTo(70, 80, 120, 240, 110, 10)
                    qp.drawPath(path)
                if x1 > 0:
                    pen = QPen(Qt.red, 2, Qt.SolidLine)
                    qp.setPen(pen)
                    path = QPainterPath()
                    path.moveTo(210, 10)
                    path.cubicTo(190, 100, 300, 230, 290, 10)
                    qp.drawPath(path)
                if x1 == 0:
                    pen = QPen(Qt.red, 2, Qt.SolidLine)
                    qp.setPen(pen)
                    path = QPainterPath()
                    path.moveTo(150, 10)
                    path.cubicTo(150, 100, 200, 230, 250, 10)
                    qp.drawPath(path)
        if a < 0:
            if delta > 0:
                if x1 < 0 and x2 > 0 or x1 > 0 and x2 < 0:
                    pen = QPen(Qt.red, 2, Qt.SolidLine)
                    qp.setPen(pen)
                    path = QPainterPath()
                    path.moveTo(100, 230)
                    path.cubicTo(210, 0, 200, 40, 250, 230)
                    qp.drawPath(path)
                if x1 > 0 and x2 > 0:
                    pen = QPen(Qt.red, 2, Qt.SolidLine)
                    qp.setPen(pen)
                    path = QPainterPath()
                    path.moveTo(200, 230)
                    path.cubicTo(210, 0, 300, 40, 300, 230)
                    qp.drawPath(path)
                if x1 < 0 and x2 < 0:
                    pen = QPen(Qt.red, 2, Qt.SolidLine)
                    qp.setPen(pen)
                    path = QPainterPath()
                    path.moveTo(80, 230)
                    path.cubicTo(140, 0, 190, 40, 170, 230)
                    qp.drawPath(path)
            if delta == 0:
                if x1 < 0:
                    pen = QPen(Qt.red, 2, Qt.SolidLine)
                    qp.setPen(pen)
                    path = QPainterPath()
                    path.moveTo(60, 230)
                    path.cubicTo(70, 80, 120, 115, 110, 230)
                    qp.drawPath(path)
                if x1 > 0:
                    pen = QPen(Qt.red, 2, Qt.SolidLine)
                    qp.setPen(pen)
                    path = QPainterPath()
                    path.moveTo(210, 230)
                    path.cubicTo(190, 100, 300, 95, 290, 230)
                    qp.drawPath(path)
                if x1 == 0:
                    pen = QPen(Qt.red, 2, Qt.SolidLine)
                    qp.setPen(pen)
                    path = QPainterPath()
                    path.moveTo(140, 230)
                    path.cubicTo(150, 100, 220, 95, 250, 230)
                    qp.drawPath(path)

class GraficoExp(QDialog):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 380, 250)
        self.setWindowTitle('Bézier curve')

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing)
        self.drawBezierCurve(qp)
        qp.end()

    def drawBezierCurve(self, qp):
        f = selct_exp_comf()
        b = selct_exp_comb()
        a = f ** (1 / b)
        a = math.ceil(a)
        pen1 = QPen(Qt.black, 2, Qt.SolidLine)

        qp.setPen(pen1)
        qp.drawLine(190, 0, 190, 300)

        pen2 = QPen(Qt.black, 2, Qt.SolidLine)

        qp.setPen(pen2)
        qp.drawLine(0, 130, 400, 130)
        if a > 1:
            pen = QPen(Qt.red, 2, Qt.SolidLine)
            qp.setPen(pen)
            path = QPainterPath()
            path.moveTo(30, 120)
            path.cubicTo(30, 120, 200, 150, 260, 30)

            qp.drawPath(path)
        if a > 0 and a < 1:
            pen = QPen(Qt.red, 2, Qt.SolidLine)
            qp.setPen(pen)
            path = QPainterPath()
            path.moveTo(120, 30)
            path.cubicTo(130, 40, 200, 140, 350, 125)

            qp.drawPath(path)

class GraficoLog(QDialog):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 380, 250)
        self.setWindowTitle('Gráfico Logaritmica')

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing)
        self.drawBezierCurve(qp)
        qp.end()

    def drawBezierCurve(self, qp):
        a = selct_log_A()
        pen1 = QPen(Qt.black, 2, Qt.SolidLine)

        qp.setPen(pen1)
        qp.drawLine(190, 0, 190, 300)

        pen2 = QPen(Qt.black, 2, Qt.SolidLine)

        qp.setPen(pen2)
        qp.drawLine(0, 130, 400, 130)
        if a > 0 and a < 1:
            pen = QPen(Qt.red, 2, Qt.SolidLine)
            qp.setPen(pen)
            path = QPainterPath()
            path.moveTo(200, 30)
            path.cubicTo(200, 200, 200, 200, 350, 230)
            qp.drawPath(path)
        if a > 1:
            pen = QPen(Qt.red, 2, Qt.SolidLine)
            qp.setPen(pen)
            path = QPainterPath()
            path.moveTo(340, 30)
            path.cubicTo(150, 70, 205, 230, 195, 230)

            qp.drawPath(path)

def calc_exp():
    f = str(exp_tela.lblfExp.text())
    b = str(exp_tela.lblbExp.text())
    if f!= "f(x)" and b!="B":
        f= int(f)
        b=(int(b))
        a=f ** (1/b)
        a=math.ceil(a)
        exp_tela.lblaExp.setText(str(a))

def exibeGraficoAfim():
    ex = GraficoAfim()
    ex.exec()

def exibeGraficoQuad():
    ex = GraficoQuad()
    ex.exec()
def exibeGraficoExp():
    ex = GraficoExp()
    ex.exec()

def exibeGraficoLog():
    ex = GraficoLog()
    ex.exec()


#DEFININDO TELAS#
app = QtWidgets.QApplication(sys.argv)
def_menu = uic.loadUi("Def.ui")
def_menu.setWindowTitle('Def calculadora')
afim_tela = uic.loadUi("Afim_tela.ui")
quad_tela = uic.loadUi("Quad_tela.ui")
log_tela = uic.loadUi("Log_tela.ui")
exp_tela = uic.loadUi("Exp_tela.ui")


#DEFININDO BOTOES#
afim_tela.btngrafic.clicked.connect(exibeGraficoAfim)
quad_tela.btngrafic_3.clicked.connect(exibeGraficoQuad)
exp_tela.btngrafic_4.clicked.connect(exibeGraficoExp)
log_tela.btngrafic_2.clicked.connect(exibeGraficoLog)


def_menu.btnAfim.clicked.connect(chama_Afim_tela)
def_menu.btnQuad.clicked.connect(chama_Quad_tela)
def_menu.btnLog.clicked.connect(chama_log_tela)
def_menu.btnExp.clicked.connect(chama_exp_tela)
afim_tela.btnCAfim.clicked.connect(calc_a)
log_tela.btncalcLog.clicked.connect(calc_log)
exp_tela.btncalcExp.clicked.connect(calc_exp)


afim_tela.spnA.valueChanged.connect(selct_afim_compA)
afim_tela.spnB.valueChanged.connect(selct_afim_compB)
afim_tela.spnF.valueChanged.connect(selct_afim_compF)


quad_tela.spnA.valueChanged.connect(selct_quad_compA)
quad_tela.spnB.valueChanged.connect(selct_quad_compB)
quad_tela.spnC.valueChanged.connect(selct_quad_compC)
quad_tela.btnCalcQ.clicked.connect(calc_quad)

log_tela.spnAlog.valueChanged.connect(selct_log_A)
log_tela.spnBase.valueChanged.connect(select_log_B)

exp_tela.spnfExp.valueChanged.connect(selct_exp_comf)
exp_tela.spnbExp.valueChanged.connect(selct_exp_comb)


#INICIALIZANDO PROGRAMA#

def_menu.show()
sys.exit(app.exec_())