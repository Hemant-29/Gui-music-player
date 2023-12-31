# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'musicPlayer.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import os
from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
from sound import Play
import cover


class Ui_MainWindow(object):

    def updateText(self):
        self.labelTitle.setText(
            f"<span style='font-size:14pt;font-weight:300;'>{self.music.title}</span>\
                <span style='color:#595959;'>{self.music.artist}</span>")
        # <span style='font-size:14pt; font-weight:600; color:#ff0000;'>Hello</span>

    def setIcon(self, icon):
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(icon),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonPlay.setIcon(icon1)
        self.buttonPlay.setIconSize(QtCore.QSize(40, 40))

    def clickFile(self):
        fileDialog = QtWidgets.QFileDialog()
        address = fileDialog.getExistingDirectory(MainWindow, "import music")
        self.musicAddresses = []
        self.musicIndex = 0
        files = []
        try:
            files = os.listdir(address)
        except FileNotFoundError:
            None

        for item in files:
            if ('.' in item) and (item.split('.')):
                exten = item.split('.')[-1]

            if exten in ["mp3", "wav"]:
                self.musicFiles.append(item)
                self.musicAddresses.append(address+"/"+item)
        print(self.musicFiles)

        # music found; calling function
        if len(self.musicFiles) >= 1:
            print(self.musicFiles[self.musicIndex])
            print("music found, calling function")
            self.play_music(audio_file=self.musicAddresses[self.musicIndex])
            print("audio_file ", self.musicAddresses[self.musicIndex])

        else:
            print('no music found')

    def clickNext(self):
        if self.musicIndex < len(self.musicAddresses)-1:
            self.musicIndex += 1
        else:
            self.musicIndex = 0

        self.play_music(audio_file=self.musicAddresses[self.musicIndex])
        self.updateText()

    def clickPrev(self):
        if self.musicIndex > 0:
            self.musicIndex -= 1
        else:
            self.musicIndex = len(self.musicAddresses)-1
        self.play_music(audio_file=self.musicAddresses[self.musicIndex])
        self.updateText()

    def clickPlay(self):
        if self.music.isPlaying is True:
            self.pause_music()
        else:
            self.resume_music()

    def play_music(self, audio_file):
        self.music.play_audio(audio_file, 0)
        self.music.elapsed_time = 0
        self.updateText()
        self.setIcon("resources/pause.png")
        self.setCover(audio_file)

    def pause_music(self):
        self.setIcon("resources/play.png")
        self.music.pause_audio()

    def resume_music(self):
        self.setIcon("resources/pause.png")
        self.music.resume_audio()

    def setStyle(style, name):
        name.setStyleSheet("background-color:white; border-radius:25px")

    def setCover(self, address):
        bytes_data = cover.extract(address)

        # Create a QImage from the bytes data
        qimage = QtGui.QImage.fromData(bytes_data)
        # Create a QPixmap from the QImage
        pixmap = QtGui.QPixmap.fromImage(qimage)
        self.imageLabel.setPixmap(pixmap)

    def setupUi(self, MainWindow):
        self.music = Play()
        self.musicAddresses = []  # contains file addresses
        self.musicFiles = []  # contains file names
        self.musicIndex = 0
        self.cover = "resources/cover3.png"

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(0, 0))
        self.frame.setMaximumSize(QtCore.QSize(400, 400))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.imageLabel = QtWidgets.QLabel(self.frame)
        self.imageLabel.setText("")
        self.imageLabel.setPixmap(QtGui.QPixmap(self.cover))
        self.imageLabel.setScaledContents(True)
        self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.imageLabel.setWordWrap(True)
        self.imageLabel.setObjectName("imageLabel")

        self.verticalLayout_2.addWidget(
            self.imageLabel, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.gridLayout.addWidget(
            self.frame, 4, 0, 1, 2, QtCore.Qt.AlignHCenter)
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
        self.horizontalLayout_4.addWidget(
            self.buttonFile, 0, QtCore.Qt.AlignLeft)
        self.buttonFile.clicked.connect(self.clickFile)
        self.setStyle(self.buttonFile)

        self.buttonSettings = QtWidgets.QPushButton(self.frame_4)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("resources/settings.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonSettings.setIcon(icon1)
        self.buttonSettings.setObjectName("buttonSettings")
        self.setStyle(self.buttonSettings)
        self.horizontalLayout_4.addWidget(
            self.buttonSettings, 0, QtCore.Qt.AlignLeft)
        self.gridLayout.addWidget(
            self.frame_4, 0, 0, 1, 1, QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
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
        self.buttonBack.clicked.connect(self.clickPrev)
        self.setStyle(self.buttonBack)

        self.buttonPlay = QtWidgets.QPushButton(self.frame_2)
        self.buttonPlay.setMinimumSize(QtCore.QSize(0, 100))
        self.buttonPlay.setText("")
        self.setIcon("resources/play.png")
        self.buttonPlay.setObjectName("buttonPlay")
        self.horizontalLayout.addWidget(self.buttonPlay)
        self.buttonPlay.clicked.connect(self.clickPlay)
        self.setStyle(self.buttonPlay)

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
        self.buttonNext.clicked.connect(self.clickNext)
        self.setStyle(self.buttonNext)

        self.gridLayout.addWidget(
            self.frame_2, 7, 0, 1, 2, QtCore.Qt.AlignVCenter)
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
        self.gridLayout.addWidget(
            self.frame_3, 6, 0, 1, 2, QtCore.Qt.AlignBottom)
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.labelTitle = QtWidgets.QLabel(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.labelTitle.sizePolicy().hasHeightForWidth())
        self.labelTitle.setSizePolicy(sizePolicy)
        self.labelTitle.setObjectName("labelTitle")
        self.verticalLayout_3.addWidget(self.labelTitle)
        self.gridLayout.addWidget(
            self.frame_5, 5, 0, 1, 2, QtCore.Qt.AlignVCenter)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 424, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.buttonFile.setText(_translate("MainWindow", "File"))
        self.buttonSettings.setText(_translate("MainWindow", "Settings"))
        self.labelTitle.setText(_translate(
            "MainWindow", "Press file to import music"))


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 100, 389, 705)  # Initial size
        self.setWindowTitle("Music")
        self.setStyleSheet("background-color:#ffffff;")
        windowIcon = QtGui.QIcon()
        windowIcon.addPixmap(QtGui.QPixmap("resources/sound-waves.png"))
        self.setWindowIcon(windowIcon)

    def resizeEvent(self, event):
        # Get the new width and height
        imageDim = int(self.height()/2)
        ui.frame.setMaximumSize(QtCore.QSize(
            imageDim, imageDim))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
