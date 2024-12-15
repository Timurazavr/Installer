import sys
import ctypes
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QApplication
from time import sleep
from services import (
    get_name_project,
    get_path_program,
    install_project,
    is_admin,
    resource_path,
)


class Installer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setObjectName("MainWindow")
        self.resize(750, 500)
        self.setWindowIcon(QtGui.QIcon(resource_path("image\\icon.ico")))

        self.welcome_screen()

        self.path = get_path_program()

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
        self.backgroundPictureLabel.setPixmap(
            QtGui.QPixmap(resource_path("image\\background.png"))
        )
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
                f'Он установит на ваш компьютер {get_name_project()}, для продолжения нажмите "далее" или "отмена" для прекращения установки.',
            )
        )
        self.backButton.setText(_translate("MainWindow", "Назад"))
        self.cancelButton.setText(_translate("MainWindow", "Отмена"))
        self.nextButton.setText(_translate("MainWindow", "Далее"))

        self.cancelButton.clicked.connect(sys.exit)
        self.nextButton.clicked.connect(self.path_screen)

    def path_screen(self):
        self.centralwidget = QtWidgets.QWidget(parent=self)
        self.centralwidget.setObjectName("centralwidget")
        self.theneLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.theneLabel.setGeometry(QtCore.QRect(20, 40, 591, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.theneLabel.setFont(font)
        self.theneLabel.setObjectName("theneLabel")
        self.pathLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.pathLabel.setGeometry(QtCore.QRect(20, 125, 661, 100))
        self.pathLabel.setWordWrap(True)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pathLabel.setFont(font)
        self.pathLabel.setObjectName("pathLabel")
        self.licenseCheck = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.licenseCheck.setGeometry(QtCore.QRect(20, 450, 381, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.licenseCheck.setFont(font)
        self.licenseCheck.setObjectName("licenseCheck")
        self.tagCheck = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.tagCheck.setGeometry(QtCore.QRect(20, 290, 431, 31))
        self.tagCheck.setFont(font)
        self.tagCheck.setChecked(True)
        self.tagCheck.setTristate(False)
        self.tagCheck.setObjectName("tagCheck")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pathButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pathButton.setGeometry(QtCore.QRect(690, 160, 50, 30))
        self.pathButton.setFont(font)
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
            _translate("MainWindow", "Пользовательское соглашение (его нет)")
        )
        self.theneLabel.setText(_translate("MainWindow", "Расположение программы:"))
        self.pathLabel.setText(_translate("MainWindow", self.path))
        self.tagCheck.setText(_translate("MainWindow", "Создать ярлык"))
        self.pathButton.setText(_translate("MainWindow", "."))
        self.backButton.setText(_translate("MainWindow", "Назад"))
        self.cancelButton.setText(_translate("MainWindow", "Отмена"))
        self.nextButton.setText(_translate("MainWindow", "Далее"))

        self.backButton.clicked.connect(self.welcome_screen)
        self.cancelButton.clicked.connect(sys.exit)
        self.pathButton.clicked.connect(self.dialog_file_choice)
        self.nextButton.clicked.connect(self.complete)

    def dialog_file_choice(self):
        result = QtWidgets.QFileDialog.getExistingDirectory(
            self, "Выберите папку", get_path_program()
        )
        if result:
            self.path = result.replace("/", "\\").rstrip("\\") + "\\"
            self.pathLabel.setText(self.path)

    def complete(self):
        if not self.licenseCheck.isChecked():
            error = QtWidgets.QMessageBox(self)
            error.setWindowTitle("Ошибка")
            error.setText("Для продолжения примите Пользовательское соглашение")
            error.show()
            return

        self.checked = self.tagCheck.isChecked()

        self.centralwidget = QtWidgets.QWidget(parent=self)
        self.centralwidget.setObjectName("centralwidget")
        self.progressBar = QtWidgets.QProgressBar(parent=self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(25, 150, 700, 40))
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setValue(0)
        self.themeLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.themeLabel.setGeometry(QtCore.QRect(25, 50, 500, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.themeLabel.setFont(font)
        self.themeLabel.setObjectName("themeLabel")
        self.setCentralWidget(self.centralwidget)

        _translate = QtCore.QCoreApplication.translate
        self.themeLabel.setText(_translate("MainWindow", "Идет установка:"))

        self.timer, self.counter = QtCore.QTimer(), 0
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.timerRun)
        self.timer.start()

    def timerRun(self):
        self.counter += 20
        self.progressBar.setValue(self.counter)
        if self.counter == 100:
            self.timer.stop()
            sleep(0.5)

            install_project(self.path, self.checked)

            self.centralwidget = QtWidgets.QWidget(parent=self)
            self.centralwidget.setObjectName("centralwidget")
            self.themeLabel = QtWidgets.QLabel(parent=self.centralwidget)
            self.themeLabel.setGeometry(QtCore.QRect(350, 0, 400, 300))
            font = QtGui.QFont()
            font.setPointSize(18)
            self.themeLabel.setFont(font)
            self.themeLabel.setWordWrap(True)
            self.themeLabel.setObjectName("themeLabel")
            self.backgroundPictureLabel = QtWidgets.QLabel(parent=self.centralwidget)
            self.backgroundPictureLabel.setGeometry(QtCore.QRect(0, 0, 340, 500))
            self.backgroundPictureLabel.setPixmap(
                QtGui.QPixmap(resource_path("image\\background.png"))
            )
            self.backgroundPictureLabel.setObjectName("backgroundPictureLabel")
            self.finishButton = QtWidgets.QPushButton(parent=self.centralwidget)
            self.finishButton.setGeometry(QtCore.QRect(580, 430, 150, 50))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.finishButton.setFont(font)
            self.finishButton.setObjectName("finishButton")
            self.setCentralWidget(self.centralwidget)

            _translate = QtCore.QCoreApplication.translate
            self.themeLabel.setText(
                _translate(
                    "MainWindow",
                    "Установка завершена! Можете закрыть окно и приступить к использованию!",
                )
            )
            self.finishButton.setText(_translate("MainWindow", "Финиш"))

            self.finishButton.clicked.connect(sys.exit)


if __name__ == "__main__":
    if not is_admin():
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, " ".join(sys.argv), None, 1
        )
        sys.exit()
    app = QApplication(sys.argv)
    window = Installer()
    window.show()
    sys.exit(app.exec())
