import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QApplication


class Installer(QMainWindow):
    def setupUi(self, MainWindow: QMainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 500)
        MainWindow.setWindowIcon(QtGui.QIcon("image/icon.ico"))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.themeLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.themeLabel.setGeometry(QtCore.QRect(350, 10, 400, 200))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.themeLabel.setFont(font)
        self.themeLabel.setWordWrap(True)
        self.themeLabel.setObjectName("themeLabel")
        self.descriptionLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.descriptionLabel.setGeometry(QtCore.QRect(350, 170, 400, 141))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.descriptionLabel.setFont(font)
        self.descriptionLabel.setWordWrap(True)
        self.descriptionLabel.setObjectName("descriptionLabel")
        self.backgroundPictureLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.backgroundPictureLabel.setGeometry(QtCore.QRect(0, 0, 340, 500))
        self.backgroundPictureLabel.setPixmap(QtGui.QPixmap("image/background.png"))
        self.backgroundPictureLabel.setObjectName("backgroundPictureLabel")
        self.backButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(490, 440, 120, 50))
        self.backButton.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.backButton.setFont(font)
        self.backButton.setObjectName("backButton")
        self.cancelButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.cancelButton.setGeometry(QtCore.QRect(350, 440, 120, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cancelButton.setFont(font)
        self.cancelButton.setObjectName("cancelButton")
        self.nextButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(620, 440, 120, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nextButton.setFont(font)
        self.nextButton.setObjectName("nextButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Установщик"))
        self.themeLabel.setText(
            _translate("MainWindow", "Вас приветствует мастер установки!")
        )
        self.descriptionLabel.setText(
            _translate(
                "MainWindow",
                'Он установит на ваш компьютер {}, для продолжения нажмите "далее" или "отмена" для прекращения установки.',
            )
        )
        self.backButton.setText(_translate("MainWindow", "Назад"))
        self.cancelButton.setText(_translate("MainWindow", "Отмена"))
        self.nextButton.setText(_translate("MainWindow", "Далее"))

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.cancelButton.clicked.connect(self.cancelRun)

    def cancelRun(self):
        exit()

    def nextRun(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Installer()
    window.show()
    sys.exit(app.exec())
