# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'musicPlayer.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def clickFile(self):
        fileDialog = QtWidgets.QFileDialog()
        address = fileDialog.getExistingDirectory(MainWindow, "import music")
        print(address)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(446, 512)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        self.buttonFile = QtWidgets.QPushButton(self.frame_4)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/folder.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonFile.setIcon(icon)
        self.buttonFile.setIconSize(QtCore.QSize(20, 20))
        self.buttonFile.setObjectName("buttonFile")
        self.horizontalLayout_4.addWidget(self.buttonFile)
        self.buttonFile.clicked.connect(self.clickFile)

        self.buttonSettings = QtWidgets.QPushButton(self.frame_4)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("resources/settings.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonSettings.setIcon(icon1)
        self.buttonSettings.setObjectName("buttonSettings")
        self.horizontalLayout_4.addWidget(self.buttonSettings)
        self.gridLayout.addWidget(self.frame_4, 0, 0, 1, 1)

        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.buttonBack = QtWidgets.QPushButton(self.frame_2)
        self.buttonBack.setMinimumSize(QtCore.QSize(0, 100))
        self.buttonBack.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("resources/Back.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonBack.setIcon(icon2)
        self.buttonBack.setIconSize(QtCore.QSize(40, 40))
        self.buttonBack.setObjectName("buttonBack")
        self.horizontalLayout.addWidget(self.buttonBack)

        self.buttonPlay = QtWidgets.QPushButton(self.frame_2)
        self.buttonPlay.setMinimumSize(QtCore.QSize(0, 100))
        self.buttonPlay.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("resources/play.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonPlay.setIcon(icon3)
        self.buttonPlay.setIconSize(QtCore.QSize(40, 40))
        self.buttonPlay.setObjectName("buttonPlay")
        self.horizontalLayout.addWidget(self.buttonPlay)

        self.buttonNext = QtWidgets.QPushButton(self.frame_2)
        self.buttonNext.setMinimumSize(QtCore.QSize(0, 100))
        self.buttonNext.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("resources/next.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonNext.setIcon(icon4)
        self.buttonNext.setIconSize(QtCore.QSize(40, 40))
        self.buttonNext.setObjectName("buttonNext")
        self.horizontalLayout.addWidget(self.buttonNext)

        self.gridLayout.addWidget(self.frame_2, 3, 0, 1, 2)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalSlider = QtWidgets.QSlider(self.frame_3)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout_2.addWidget(
            self.horizontalSlider, 0, QtCore.Qt.AlignBottom)
        self.gridLayout.addWidget(self.frame_3, 2, 0, 1, 2)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(0, 200))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.imageLabel = QtWidgets.QLabel(self.frame)
        self.imageLabel.setObjectName("imageLabel")
        self.verticalLayout_2.addWidget(self.imageLabel)
        self.gridLayout.addWidget(self.frame, 1, 0, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 446, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.buttonFile.setText(_translate("MainWindow", "File"))
        self.buttonSettings.setText(_translate("MainWindow", "Settings"))
        self.imageLabel.setText(_translate("MainWindow", "Image"))


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

    def resizeEvent(self, event):
        width = self.width()
        height = self.height()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
