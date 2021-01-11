from qtsgraphpy import QApplication, QTSGraphPy, sys, Qt


def PaintBox(p):
    # Начало рисования

    p.SetColor(Qt.blue)
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
    p.PutPixel(300, 300, 0, 5)
    p.SetTextStyle(12, 45, 1)
    p.OutTextXY(20, 20, "Привет Мир!")
    p.SetTextStyle(12, 0, 1)
    p.SetColor(Qt.red)
    p.OutTextXY(200, 130, "Кликните мышкой в окне...")
    p.SetColor(Qt.darkGreen)
    m = p.ReadMouseButton()
    if m == 1:
        p.OutTextXY(200, 150, "Нажата левая кнопка")
    elif m == 2:
        p.OutTextXY(200, 150, "Нажата правая кнопка")
    elif m == 3:
        p.OutTextXY(200, 150, "Нажата средняя кнопка")
    else:
        p.OutTextXY(200, 150, "Нажата неизвестная кнопка")

    # Конец рисования


if __name__ == "__main__":
    app = QApplication([])
    # Задаётся размер и положение окна
    # (w = 640, h = 480, x = -1, y = -1)
    # В случае отрицательного значения x или y, окно создаётся в центре экрана.
    w = QTSGraphPy(600, 600)

    w.pb = PaintBox

    w.show()
    sys.exit(app.exec_())
