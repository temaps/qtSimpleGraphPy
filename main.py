from qtsgraphpy import QApplication, QTSGraphPy, sys


def PaintBox(p):
    # Начало рисования

    p.SetColor(0xFF)
    p.Line(0, 0, 600, 600)
    p.Delay(1000)
    p.SetColor(0xFF0000)
    p.Line(0, 600, 600, 0)
    p.Rectangle(0, 0, 599, 599)
    p.OutTextXY(200, 70, "Нажмите любую клавишу...")
    k = p.ReadKey()
    p.SetColor(0xFFFF00)
    p.SetFillStyle(1, 0xFFFF)
    p.Circle(50, 50, 50)
    p.SetColor(0x999999)
    p.SetPenStyle(5)
    p.SetFillStyle(3, 0x00FF00FF)
    p.Ellipse(250, 280, 350, 320)
    p.SetColor(0xFF)
    p.OutTextXY(200, 100, "Нажата клавиша с кодом: " + str(k))

    # Конец рисования


if __name__ == "__main__":
    app = QApplication([])
    # Задаётся размер и положение окна
    # (w = 640, h = 480, x = -1, y = -1)
    # В случае отрицательного значения x или y, окно создаётся в центре экрана.
    window = QTSGraphPy(600, 600)

    window.pb = PaintBox
    window.show()
    sys.exit(app.exec_())
