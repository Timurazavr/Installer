import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QApplication
import ctypes


class Installer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setObjectName("MainWindow")
        self.resize(750, 500)
        self.setWindowIcon(QtGui.QIcon("image/icon.ico"))

        self.welcome_screen()

    def welcome_screen(self):
        self.centralwidget = QtWidgets.QWidget(parent=self)
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
        self.cancelButton.setFont(font)
        self.cancelButton.setObjectName("cancelButton")
        self.nextButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(620, 440, 120, 50))
        self.nextButton.setFont(font)
        self.nextButton.setObjectName("nextButton")
        self.setCentralWidget(self.centralwidget)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Установщик"))
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

        self.cancelButton.clicked.connect(self.cancelRun)
        self.nextButton.clicked.connect(self.path_screen)

    def cancelRun(self):
        exit()

    def path_screen(self):
        self.centralwidget = QtWidgets.QWidget(parent=self)
        self.centralwidget.setObjectName("centralwidget")
        self.licenseCheck = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.licenseCheck.setGeometry(QtCore.QRect(20, 450, 381, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.licenseCheck.setFont(font)
        self.licenseCheck.setObjectName("licenseCheck")
        self.theneLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.theneLabel.setGeometry(QtCore.QRect(20, 40, 591, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.theneLabel.setFont(font)
        self.theneLabel.setObjectName("theneLabel")
        self.pathLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.pathLabel.setGeometry(QtCore.QRect(20, 160, 661, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pathLabel.setFont(font)
        self.pathLabel.setObjectName("pathLabel")
        self.tagCheck = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.tagCheck.setGeometry(QtCore.QRect(20, 290, 431, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tagCheck.setFont(font)
        self.tagCheck.setChecked(True)
        self.tagCheck.setTristate(False)
        self.tagCheck.setObjectName("tagCheck")
        self.pathButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pathButton.setGeometry(QtCore.QRect(690, 160, 50, 30))
        self.pathButton.setObjectName("pathButton")
        self.backButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(490, 440, 120, 50))
        self.backButton.setFont(font)
        self.backButton.setObjectName("backButton")
        self.cancelButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.cancelButton.setGeometry(QtCore.QRect(350, 440, 120, 50))
        self.cancelButton.setFont(font)
        self.cancelButton.setObjectName("cancelButton")
        self.nextButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(620, 440, 120, 50))
        self.nextButton.setFont(font)
        self.nextButton.setObjectName("nextButton")
        self.setCentralWidget(self.centralwidget)

        _translate = QtCore.QCoreApplication.translate
        self.licenseCheck.setText(
            _translate("MainWindow", "Пользаваьельское соглашение (его нет)")
        )
        self.theneLabel.setText(_translate("MainWindow", "Расположение программы:"))
        self.pathLabel.setText(_translate("MainWindow", "путь"))
        self.tagCheck.setText(
            _translate("MainWindow", "Создать ярлык на рабочем столе")
        )
        self.pathButton.setText(_translate("MainWindow", "."))
        self.backButton.setText(_translate("MainWindow", "Назад"))
        self.cancelButton.setText(_translate("MainWindow", "Отмена"))
        self.nextButton.setText(_translate("MainWindow", "Далее"))

        self.backButton.clicked.connect(self.welcome_screen)
        self.cancelButton.clicked.connect(self.cancelRun)


if __name__ == "__main__":
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, " ".join(sys.argv), None, 0
    )
    app = QApplication(sys.argv)
    window = Installer()
    window.show()
    sys.exit(app.exec())
