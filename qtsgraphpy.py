import sys
from PyQt5.QtWidgets import QWidget, QApplication, QDesktopWidget, QMainWindow
from PyQt5.QtGui import QPainter, QColor, QFont, QPixmap, QPen, QBrush
from PyQt5.QtCore import Qt, QTimer, QTime, QCoreApplication, QEventLoop

clRed = 0x00FF0000
clGreen = 0x0000FF00
clBlue = 0x000000FF
clBlack = 0x00000000
clWhite = 0x00FFFFFF
clYellow = 0x00FFFF00
clMagenta = 0x00FF00FF
clCyan = 0x0000FFFF


class QTSGraphPy(QMainWindow):
    pb = None
    TextDirection = 0

    def __init__(self, w=640, h=480, x=-1, y=-1):
        QMainWindow.__init__(self)
        if x < 0 or y < 0:
            desktop = QDesktopWidget()
            rect = desktop.availableGeometry(desktop.primaryScreen())
            center = rect.center()
            x = center.x() - w / 2
            y = center.y() - h / 2
        self.setGeometry(x, y, w, h)
        self.setWindowTitle("Рисунок")
        self.Canvas = QPixmap(self.size())
        self.Canvas.fill(Qt.white)
        self.DefaultColor = 0x00000000
        self.Pen = QPen(QBrush(QColor(self.DefaultColor)), 1)
        self.Font = QFont()
        self.Brush = QBrush(QColor(self.DefaultColor), 0)
        self.ResetInterval = 1000
        self.ResetTimer = QTimer()
        self.ResetTimer.timeout.connect(self.slotResetTimer)
        self.ResetTimer.start(self.ResetInterval)

        self.StartTimer = QTimer()
        self.StartTimer.timeout.connect(self.slotStartTimer)
        self.StartTimer.start(500)

    def Delay(self, ms=1000):
        dieTime = QTime.currentTime().addMSecs(ms)
        while QTime.currentTime() < dieTime:
            QCoreApplication.processEvents(QEventLoop.AllEvents, 50)

# -----------------------------------------------------
# События
# -----------------------------------------------------

    def slotResetTimer(self):
        self.ResetTimer.stop()
        self.EventKeyPressed = False
        self.EventMouseClicked = False

    def slotStartTimer(self):
        self.StartTimer.stop()
        self.pb(self)

    def paintEvent(self, event):
        p = QPainter(self)
        p.drawPixmap(0, 0, self.Canvas)

# -----------------------------------------------------
# Элементы
# -----------------------------------------------------

    def Circle(self, x, y, radius):
        painter = QPainter(self.Canvas)
        painter.setPen(self.Pen)
        painter.setBrush(self.Brush)
        painter.drawEllipse(x - radius, y - radius, radius * 2, radius * 2)
        self.update()

    def Ellipse(self, x1, y1, x2, y2):
        painter = QPainter(self.Canvas)
        painter.setPen(self.Pen)
        painter.setBrush(self.Brush)
        painter.drawEllipse(x1, y1, abs(x2-x1), abs(y2-y1))
        self.update()

    def Line(self, x1, y1, x2, y2):
        painter = QPainter(self.Canvas)
        painter.setPen(self.Pen)
        painter.drawLine(x1, y1, x2, y2)
        self.update()

    def SetColor(self, c):
        self.Pen.setColor(QColor(c))

    def SetFillStyle(self, Pattern, Color):
        self.Brush.setStyle(Qt.BrushStyle(Pattern))
        self.Brush.setColor(QColor(Color))

    def SetPenStyle(self, PenWidth, PenStyle=1):
        self.Pen.setWidth(PenWidth)
        self.Pen.setStyle(Qt.PenStyle(PenStyle))

    def SetPenWidth(self, PenWidth):
        self.Pen.setWidth(PenWidth)

    def SetTextStyle(self, idFont, Direction, CharSize):
        f = ""
        if idFont == 0:
            f = "serif"
        elif idFont == 1:
            f = "sans"
        elif idFont == 3:
            f = "mono"
        self.TextDirection = Direction
        self.Font.setFamily(f)
        self.Font.setPointSize(CharSize)
