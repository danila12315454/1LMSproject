import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QLabel, \
    QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import random
from datetime import datetime
import matplotlib.pyplot as plt


class UI_Design(object):
    def setupUi(self, Design):
        Design.setObjectName("Design")
        Design.resize(1047, 440)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        Design.setFont(font)
        self.tabWidget = QtWidgets.QTabWidget(Design)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1061, 601))
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(0, 0, 150, 20))
        self.comboBox.setObjectName("comboBox")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(160, 100, 800, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.textEdit = QtWidgets.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(160, 0, 800, 91))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(965, 100, 60, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_3.setGeometry(QtCore.QRect(107, 330, 100, 20))
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_4.setGeometry(QtCore.QRect(107, 360, 100, 20))
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_5.setGeometry(QtCore.QRect(107, 390, 100, 20))
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(0, 300, 100, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(0, 330, 100, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(0, 360, 100, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(0, 390, 100, 13))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(0, 240, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setKerning(False)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(114, 170, 11);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.lcdNumber = QtWidgets.QLCDNumber(self.tab)
        self.lcdNumber.setGeometry(QtCore.QRect(-110, 440, 64, 23))
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.tab)
        self.lcdNumber_2.setGeometry(QtCore.QRect(965, 30, 60, 60))
        self.lcdNumber_2.setDigitCount(2)
        self.lcdNumber_2.setProperty("intValue", 60)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.lineEdit_2 = QtWidgets.QTextEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(107, 300, 100, 20))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 731, 411))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pushButton = QtWidgets.QPushButton(self.tab_2)
        self.pushButton.setGeometry(QtCore.QRect(740, 0, 201, 31))
        self.pushButton.setObjectName("pushButton")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab_5)
        self.textEdit_2.setGeometry(QtCore.QRect(110, 70, 300, 341))
        self.textEdit_2.setObjectName("textEdit_2")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_6.setGeometry(QtCore.QRect(110, 30, 300, 31))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_6 = QtWidgets.QLabel(self.tab_5)
        self.label_6.setGeometry(QtCore.QRect(10, 35, 101, 21))
        self.label_6.setObjectName("label_6")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_3.setGeometry(QtCore.QRect(420, 30, 81, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_7.setGeometry(QtCore.QRect(609, 30, 261, 31))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_7 = QtWidgets.QLabel(self.tab_5)
        self.label_7.setGeometry(QtCore.QRect(520, 80, 47, 13))
        self.label_7.setObjectName("label_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_8.setGeometry(QtCore.QRect(570, 70, 300, 31))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_8 = QtWidgets.QLabel(self.tab_5)
        self.label_8.setGeometry(QtCore.QRect(510, 40, 101, 16))
        self.label_8.setObjectName("label_8")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_5)
        self.tableWidget_2.setGeometry(QtCore.QRect(510, 110, 361, 301))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_4.setGeometry(QtCore.QRect(880, 30, 81, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.tabWidget.addTab(self.tab_5, "")

        self.retranslateUi(Design)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Design)

    def retranslateUi(self, Design):
        _translate = QtCore.QCoreApplication.translate
        Design.setWindowTitle(_translate("Design", "Type Train"))
        """self.textEdit.setHtml(_translate("Design",
         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\"\
          \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
         "<html><head><meta name=\"qrichtext\" content=\"1\"\
          /><style type=\"text/css\">\n"
         "p, li { white-space: pre-wrap; }\n"
         "</style></head><body style=\" font-family:\'MS Shell Dlg 2\';\
          font-size:18pt;"
         " font-weight:400; font-style:normal;\">\n"
         "<p style=\"-qt-paragraph-type:empty; margin-top:0px;\
          margin-bottom:0px;"
         " margin-left:0px; margin-right:0px; -qt-block-indent:0;\
         text-indent:0px;"
         " font-size:2pt;\"><br /></p></body></html>"))"""
        self.pushButton_2.setText(_translate("Design", "Заново"))
        self.label.setText(_translate("Design", "Нажатия"))
        self.label_2.setText(_translate("Design", "Аккуратность"))
        self.label_3.setText(_translate("Design", "Верные слова"))
        self.label_4.setText(_translate("Design", "Неверные слова"))
        self.label_5.setText(_translate("Design", "26 СВМ"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab),
                                  _translate("Design", "Type test"))
        self.pushButton.setText(
            _translate("Design", "Показать статистику WPM/Day"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2),
                                  _translate("Design", "Records/Stats"))
        self.label_6.setText(_translate("Design", "Название сета:"))
        self.pushButton_3.setText(_translate("Design", "нарезать"))
        self.label_7.setText(_translate("Design", "Слово:"))
        self.label_8.setText(_translate("Design", "Название сета:"))
        self.pushButton_4.setText(_translate("Design", "Применить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5),
                                  _translate("Design", "Sets manager"))


class App(QWidget, UI_Design):
    def __init__(self):
        super().__init__()
        self.Create_db()
        self.setupUi(self)
        self.retranslateUi(self)
        self.pushButton.clicked.connect(self.CreateGraf)
        self.pushButton_2.clicked.connect(self.onpush)
        self.pushButton_3.clicked.connect(self.slice)
        self.pushButton_4.clicked.connect(self.rerite)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.TimeUpdate)
        self.timer.start(100)
        self.time = 60
        self.textEdit.setDisabled(True)
        self.testing = False
        self.linelen = 5
        self.rightWords = 0
        self.wrongWords = 0
        self.typenWord = ""
        self.righttaps = 0
        self.wrongtaps = 0
        self.information = ""
        self.reriterow = [0, 0]
        self.tableWidget_2.itemChanged.connect(self.item_changed)

        self.comboBox.addItems(["English", "Русский"])
        self.sets = []
        self.restoreCB()
        self.currentSet = self.sets[0]

        self.pixmap = QPixmap('unnamed.jpg')
        self.image = QLabel(self.tab)
        self.image.setGeometry(300, 230, 350, 200)
        # Отображаем содержимое QPixmap в объекте QLabel
        self.image.setPixmap(self.pixmap)

        self.onpush()
        self.StatsStart()
        self.RSstart()

    def StatsStart(self):
        connection = sqlite3.connect('Sets.db')

        cursor = connection.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS stats
                      (date TEXT, wpm INT, cw INT, iw INT, setused TEXT)''')
        connection.commit()
        connection.close()

    def restoreCB(self):
        for i in range(100):
            self.comboBox.removeItem(0)
        connection = sqlite3.connect('Sets.db')
        cursor = connection.cursor()
        arr = cursor.execute(
            f"SELECT name FROM sqlite_master WHERE type='table'").fetchall()
        self.sets = [arr[i][0] for i in range(len(arr)) if
                     arr[i][0] != "stats"]

        connection.close()
        del arr
        for i in self.sets:
            self.comboBox.addItem(i)

    def TimeUpdate(self):
        self.timer.start(10)
        if self.lineEdit.text() != "":
            self.testing = True
            self.textEdit.setDisabled(False)
            if self.lineEdit.text()[-1] == " ":
                self.numberW += 1
                self.currentline[
                    self.numberW % self.linelen] = f"<font color = \
                    blue>{self.words[self.numberW]}</font>"
                self.textEdit.setText(
                    "<p>" + " ".join(
                        self.currentline) + "</p>" + "<p>" + " ".join(
                        self.nextline) + "</p>")
                if self.lineEdit.text().rstrip(" ") == self.currentWord:
                    self.currentline[
                        self.numberW % self.linelen - 1] = f"<font color = \
                        green>{self.currentWord}</font>"
                    self.textEdit.setText(
                        "<p>" + " ".join(
                            self.currentline) + "</p>" + "<p>" + " ".join(
                            self.nextline) + "</p>")
                    self.rightWords += 1

                else:
                    self.currentline[
                        self.numberW % self.linelen - 1] = f"<font color = \
                        red>{self.currentWord}</font>"
                    self.textEdit.setText(
                        "<p>" + " ".join(
                            self.currentline) + "</p>" + "<p>" + " ".join(
                            self.nextline) + "</p>")
                    self.wrongWords += 1
                self.currentWord = self.words[self.numberW]
                self.lineEdit.setText("")
                if self.numberW % self.linelen == 0:
                    self.currentline = self.nextline
                    self.nextline = self.words[
                                    self.numberW + self.linelen:
                                    self.numberW + self.linelen * 2]
                    self.currentline[
                        self.numberW % self.linelen] = f"<font color = \
                        blue>{self.words[self.numberW]}</font>"
                    self.textEdit.setText(
                        "<p>" + " ".join(
                            self.currentline) + "</p>" + "<p>" + " ".join(
                            self.nextline) + "</p>")
            elif self.typenWord != self.lineEdit.text():
                if self.lineEdit.text() in self.currentWord:
                    self.typenWord = self.lineEdit.text()
                    self.righttaps += 1
                    self.currentline[
                        self.numberW % self.linelen] = f"<font color = \
                        blue>{self.words[self.numberW]}</font>"
                    self.textEdit.setText(
                        "<p>" + " ".join(
                            self.currentline) + "</p>" + "<p>" + " ".join(
                            self.nextline) + "</p>")
                else:
                    self.typenWord = self.lineEdit.text()
                    self.wrongtaps += 1
                    self.currentline[
                        self.numberW % self.linelen] = f"<font color = \
                        #FF33D1>{self.words[self.numberW]}</font>"
                    self.textEdit.setText(
                        "<p>" + " ".join(
                            self.currentline) + "</p>" + "<p>" + " ".join(
                            self.nextline) + "</p>")
        if self.testing:
            self.time -= 0.01
            self.lcdNumber_2.display(int(self.time))
        if int(self.time) == 0:
            self.lineEdit.setText("")
            self.time = 60
            self.testing = False
            self.lineEdit_4.setText(str(self.rightWords))
            self.lineEdit_5.setText(str(self.wrongWords))
            self.lineEdit.setEnabled(False)

            self.label_5.setText(f"{self.rightWords}СВМ")
            self.lineEdit_2.setText(
                f"<font color = green>{self.righttaps}\
                </font> | <font color = red>{self.wrongtaps}</font>")
            try:
                self.lineEdit_3.setText(str(int((self.righttaps / (
                        self.righttaps + self.wrongtaps)) * 100)) + "%")
            except ZeroDivisionError:
                self.lineEdit_3.setText("0" + "%")
            self.lineEdit_4.setText(str(self.rightWords))
            self.lineEdit_5.setText(str(self.wrongWords))
            connection = sqlite3.connect('Sets.db')

            cursor = connection.cursor()

            cursor.execute(
                f"INSERT INTO stats VALUES('{datetime.now()}', \
{self.rightWords}, {self.rightWords}, \
                {self.wrongWords}, '{self.currentSet}')")
            connection.commit()
            connection.close()
            self.RSstart()
        if self.comboBox.currentText() != self.currentSet:
            self.currentSet = self.comboBox.currentText()
            self.onpush()
        self.SetManagerReFresh()

    def onpush(self):
        connection = sqlite3.connect('Sets.db')
        cursor = connection.cursor()
        lengh = \
            cursor.execute(
                f"SELECT COUNT(*) FROM {self.currentSet}").fetchall()[
                0][0]
        self.words = [cursor.execute(f'''SELECT Word FROM {self.currentSet}
                WHERE id == {random.randint(1, lengh)}''').fetchall()[0][0] for
                      i in range(500)]
        connection.close()
        self.testing = False
        self.time = 60
        self.lcdNumber_2.display(int(self.time))
        self.currentline = self.words[0:self.linelen]
        self.nextline = self.words[self.linelen:self.linelen * 2]
        self.textEdit.setText(
            "<p>" + " ".join(self.currentline) + "</p>" + "<p>" + " ".join(
                self.nextline) + "</p>")
        self.numberW = 0
        self.currentWord = self.words[0]
        self.currentline[
            self.numberW % self.linelen] = f"<font color = \
            blue>{self.words[self.numberW]}</font>"
        self.textEdit.setText(
            "<p>" + " ".join(self.currentline) + "</p>" + "<p>" + " ".join(
                self.nextline) + "</p>")
        self.label_5.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")
        self.lineEdit_5.setText("")
        self.rightWords = 0
        self.wrongWords = 0
        self.righttaps = 0
        self.wrongtaps = 0
        self.lineEdit.setEnabled(True)

    def RSstart(self):
        connection = sqlite3.connect('Sets.db')
        cursor = connection.cursor()
        information = cursor.execute(
            "SELECT * FROM stats ORDER BY date ASC").fetchall()
        connection.close()
        self.tableWidget.setRowCount(len(information))
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(
            ["date", "wpm", "Correct Words", "Incorrect words", "used set"])
        for i in range(len(information)):
            for _ in range(len(information[0])):
                p = QTableWidgetItem(str(information[i][_]))
                p.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidget.setItem(i, _, p)
        self.tableWidget.resizeColumnsToContents()

    def Create_db(self):
        connection = sqlite3.connect('Sets.db')
        cursor = connection.cursor()
        try:
            cursor.execute(f"INSERT INTO StandartRU VALUES({1}, '{1}')")
        except BaseException:
            cursor.execute('''CREATE TABLE IF NOT EXISTS StandartRU
                      (id INT, Word TEXT)''')

            f = open("Russian.txt", "r", encoding="utf-8")
            _ = 1
            for i in f.read().split("\n"):
                cursor.execute(f"INSERT INTO StandartRU VALUES({_}, '{i}')")
                _ += 1
            f.close()
            connection.commit()

        try:
            cursor.execute(f"INSERT INTO StandartEN VALUES({1}, '{1}')")
        except BaseException:
            cursor.execute('''CREATE TABLE IF NOT EXISTS StandartEN
                      (id INT, Word TEXT)''')

            f = open("English.txt")
            _ = 1
            for i in f.read().split("\n"):
                cursor.execute(
                    f"INSERT INTO StandartEN VALUES({_}, '{i.split(':')[0]}')")
                _ += 1
            f.close()
            connection.commit()
        connection.close()

    def CreateGraf(self):
        connection = sqlite3.connect('Sets.db')
        cursor = connection.cursor()
        arr = [list(i) for i in cursor.execute(
            f"SELECT * FROM stats ORDER BY date ASC").fetchall()]
        dikt = {}
        for i in arr:
            try:
                dikt[int(i[0].split("-")[2].split(" ")[0])] += i[1]
                dikt[int(i[0].split("-")[2].split(" ")[0])] /= 2
            except BaseException:
                dikt[int(i[0].split("-")[2].split(" ")[0])] = i[1]
        x = [i for i in dikt]
        y = [dikt[i] for i in dikt]
        plt.plot(x, y)
        plt.show()

    def slice(self):
        connection = sqlite3.connect('Sets.db')
        cursor = connection.cursor()
        if self.lineEdit_6.text() != "" and self.lineEdit_6.text() not in \
                [i[0] for i in cursor.execute(f"SELECT name FROM sqlite_master\
                 WHERE type='table'").fetchall()] and \
                list(self.textEdit_2.toPlainText()) != []:
            try:
                cursor.execute(
                    f"INSERT INTO {self.lineEdit_6.text()} VALUES({1}, '{1}')")
            except BaseException:
                cursor.execute(
                    f'''CREATE TABLE IF NOT EXISTS {self.lineEdit_6.text()}
                                  (id INT, Word TEXT)''')
                _ = 1
                for i in set(self.textEdit_2.toPlainText().split()):
                    cursor.execute(
                        f"INSERT INTO {self.lineEdit_6.text()} VALUES({_},\
                         '{str(i)}')")
                    _ += 1
                del _
                connection.commit()
                self.restoreCB()
            self.lineEdit_6.setText("")
            self.textEdit_2.setText("")
        elif self.lineEdit_6.text() == "":
            QMessageBox.warning(self, 'Предупреждение',
                                'Вы должны выбрать имя сета!', QMessageBox.Ok)
        elif self.lineEdit_6.text() in [i[0] for i in cursor.execute(
                f"SELECT name FROM sqlite_master WHERE\
                 type='table'").fetchall()]:
            QMessageBox.warning(self, 'Предупреждение',
                                'Такое имя сета уже существует!',
                                QMessageBox.Ok)
        elif list(self.textEdit_2.toPlainText()) == []:
            QMessageBox.warning(self, 'Предупреждение',
                                'Вы должны ввести в поле хотя бы 1 слово!',
                                QMessageBox.Ok)
        connection.close()

    def SetManagerReFresh(self):
        connection = sqlite3.connect('Sets.db')
        cursor = connection.cursor()
        information = ""
        try:
            if int(self.lineEdit_8.text()) == 0:
                pass
            information = cursor.execute(f"""
                    SELECT * FROM {self.lineEdit_7.text()} 
                    WHERE Word == '{self.lineEdit_8.text()}' or \
                    id == {self.lineEdit_8.text()}""").fetchall()
        except BaseException:
            pass
        if not information:
            try:
                information = cursor.execute(f"""
                SELECT * FROM {self.lineEdit_7.text()}
                WHERE Word == '{self.lineEdit_8.text()}'""").fetchall()
            except BaseException:
                pass
        connection.close()
        if information != self.information:
            if information:
                if information != []:
                    self.tableWidget_2.setRowCount(len(information))
                    self.tableWidget_2.setColumnCount(2)
                    self.tableWidget_2.setHorizontalHeaderLabels(
                        ["id", "Word"])
                    for i in range(len(information)):
                        for _ in range(len(information[0])):
                            self.tableWidget_2.setItem(i, _, QTableWidgetItem(
                                str(information[i][_])))
                            if _ % 2 == 0:
                                p = QTableWidgetItem(str(information[i][_]))
                                p.setFlags(QtCore.Qt.ItemIsEnabled)
                                self.tableWidget_2.setItem(i, _, p)
                    self.tableWidget.resizeColumnsToContents()
            else:
                self.tableWidget_2.setRowCount(0)
        self.information = information

    def rerite(self):
        connection = sqlite3.connect('Sets.db')
        cursor = connection.cursor()
        cursor.execute(
            f"UPDATE {self.lineEdit_7.text()} SET Word = '{self.reriterow[1]}'\
             Where id == {self.reriterow[0]}")
        connection.commit()
        connection.close()

    def item_changed(self, item):
        try:
            int(item.text())
            self.reriterow[0] = item.text()
        except BaseException:
            self.reriterow[1] = item.text()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = App()
    myapp.show()
    sys.exit(app.exec())
