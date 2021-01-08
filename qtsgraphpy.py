'''
"qtSimpleGraphPy" - Проект для изучения машинной графики
на основе последовательного рисования примитивов

Copyright (c) 2021 Проскурнев Артем Сергеевич

Этот файл — часть проекта qtSimpleGraphPy.

qtSimpleGraphPy - свободная программа: вы можете перераспространять ее и/или
изменять ее на условиях Стандартной общественной лицензии GNU в том виде,
в каком она была опубликована Фондом свободного программного обеспечения;
либо версии 3 лицензии, либо (по вашему выбору) любой более поздней
версии.

Весы распространяется в надежде, что она будет полезной,
но БЕЗО ВСЯКИХ ГАРАНТИЙ; даже без неявной гарантии ТОВАРНОГО ВИДА
или ПРИГОДНОСТИ ДЛЯ ОПРЕДЕЛЕННЫХ ЦЕЛЕЙ. Подробнее см. в Стандартной
общественной лицензии GNU.

Вы должны были получить копию Стандартной общественной лицензии GNU
вместе с этой программой. Если это не так, см.
<http://www.gnu.org/licenses/>.

This file is part of qtSimpleGraph.

qtSimpleGraph is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Vesi is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Vesi.  If not, see <http://www.gnu.org/licenses/>.
'''

import sys
from math import sin, cos
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
    IDMouseButton = -1
    IDPressedKey = -1
    EventKeyPressed = False
    EventMouseClicked = False

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

    def KeyPressed(self):
        QCoreApplication.processEvents(QEventLoop.AllEvents, 50)
        m = self.EventKeyPressed
        self.EventKeyPressed = False
        return m

    def keyPressEvent(self, event):
        self.ResetTimer.stop()
        self.EventKeyPressed = True
        self.IDPressedKey = event.key()
        self.ResetTimer.start(self.ResetInterval)

    def MouseClicked(self):
        QCoreApplication.processEvents(QEventLoop.AllEvents, 50)
        m = self.EventMouseClicked
        self.EventMouseClicked = False
        return m

    def mousePressEvent(self, event):
        self.ResetTimer.stop()
        self.EventMouseClicked = True
        if event.buttons() == Qt.LeftButton:
            self.IDMouseButton = 1
        elif event.buttons() == Qt.RightButton:
            self.IDMouseButton = 2
        elif event.buttons() == Qt.RightButton:
            self.IDMouseButton = 3
        self.ResetTimer.start(self.ResetInterval)

    def ReadKey(self):
        if self.IDPressedKey == -1:
            while not self.KeyPressed():
                self.Delay(1)
        t = self.IDPressedKey
        self.IDPressedKey = -1
        return t

    def ReadMouseButton(self):
        if self.IDMouseButton == -1:
            while not self.MouseClicked():
                self.Delay(1)
        t = self.IDMouseButton
        self.IDMouseButton = -1
        return t

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

    def OutTextXY(self, x, y, caption):
        painter = QPainter(self.Canvas)
        painter.setPen(self.Pen)
        b = self.TextDirection * 3.14159 / 180
        r = (x * x + y * y)**0.5
        sa = y / r
        ca = x / r
        sb = sin(b)
        cb = cos(b)
        xn = r * (ca * cb - sa * sb)
        yn = r * (sa * cb + sb * ca)
        painter.translate(x - xn, y - yn)
        painter.rotate(self.TextDirection)
        painter.drawText(x, y, caption)
        self.update()

    def PutPixel(self, x, y, c=0, PenWidth=1):
        painter = QPainter(self.Canvas)
        painter.setPen(QPen(QBrush(QColor(c)), PenWidth))
        painter.drawPoint(x, y)
        self.update()

    def Rectangle(self, x1, y1, x2, y2):
        painter = QPainter(self.Canvas)
        painter.setPen(self.Pen)
        painter.setBrush(self.Brush)
        painter.drawRect(x1, y1, abs(x2-x1), abs(y2-y1))
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
