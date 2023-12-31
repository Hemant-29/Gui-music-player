# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'musicplayer.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import time
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from sound import Play
import cover


class BackEnd():
    def __init__(self):
        self.music = Play()
        self.musicAddresses = []  # contains file addresses
        self.musicFiles = []  # contains file names
        self.musicIndex = 0
        self.cover = "resources/cover3.png"
        self.repeating = "all"
        self.ended = False
        self.currentTime = 0
        self.sliderPressed = False
        self.gotoPosition = 0

    def updateText(self):
        if self.music.title != "None":
            title = self.music.title
        else:
            title = self.musicFiles[self.musicIndex]
        ui.labelTitle.setText(
            f"<span style='font-size:14pt;font-weight:300;'>{title}</span>\
                <span style='color:#595959;'>{self.music.artist}</span>")
        # <span style='font-size:14pt; font-weight:600; color:#ff0000;'>Hello</span>

    def setIconPlay(self, icon):
        iconMap = QtGui.QIcon()
        iconMap.addPixmap(QtGui.QPixmap(icon),
                          QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ui.buttonPlay.setIcon(iconMap)
        ui.buttonPlay.setIconSize(QtCore.QSize(40, 40))

    def setIconRepeat(self, icon):
        iconMap = QtGui.QIcon()
        iconMap.addPixmap(QtGui.QPixmap(icon),
                          QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ui.buttonRepeat.setIcon(iconMap)
        ui.buttonRepeat.setIconSize(QtCore.QSize(25, 25))

    def movedSlider(self, value):
        if self.sliderPressed:
            self.gotoPosition = int((value/100)*self.music.duration)
            self.currentTime = self.music.elapsed_time

    def pressedSlider(self):
        self.sliderPressed = True

    def releasedSlider(self):
        self.sliderPressed = False
        self.music.goto(self.gotoPosition)
        self.currentTime = self.music.elapsed_time

    def clickFile(self):
        fileDialog = QtWidgets.QFileDialog()
        address = fileDialog.getExistingDirectory(MainWindow, "import music")
        self.musicAddresses = []
        self.musicIndex = 0
        self.musicFiles = []
        try:
            files = os.listdir(address)
        except FileNotFoundError:
            None
        else:

            for item in files:
                if ('.' in item) and (item.split('.')):
                    exten = item.split('.')[-1]

                if exten in ["mp3", "wav"]:
                    self.musicFiles.append(item)
                    self.musicAddresses.append(address+"/"+item)
        print(self.musicFiles)

        # music found; calling function
        if len(self.musicFiles) >= 1:
            print("music found, calling function")
            self.play_music(audio_file=self.musicAddresses[self.musicIndex])

        else:
            print('no music found')

    def clickRepeat(self):
        list = ["all", "one", "none"]
        indx = list.index(self.repeating)
        indx += 1
        if indx == 3:
            indx = 0
        self.repeating = list[indx]
        self.setIconRepeat(f"resources/repeat_{self.repeating}.png")
        # print(f"resources/repeat_{self.repeating}.png")

    def clickNext(self):
        if self.musicIndex < len(self.musicAddresses)-1:
            self.musicIndex += 1
        else:
            self.musicIndex = 0

        try:
            self.play_music(audio_file=self.musicAddresses[self.musicIndex])
            self.updateText()
        except IndexError:
            None
        self.currentTime = 0

    def clickPrev(self):
        if self.musicIndex > 0:
            self.musicIndex -= 1
        else:
            self.musicIndex = len(self.musicAddresses)-1
        try:
            self.play_music(audio_file=self.musicAddresses[self.musicIndex])
            self.updateText()
        except IndexError:
            None
        self.currentTime = 0

    def clickPlay(self):
        if self.music.isPlaying is True:
            self.pause_music()
        elif len(self.musicAddresses) == 0:
            self.clickFile()
        else:
            self.resume_music()

    def clickVolume(self):
        if not ui.hasVolumeSlider:
            ui.popupSlider()
            ui.hasVolumeSlider = True
        else:
            ui.delPopupSlider()

    def play_music(self, audio_file):
        self.music.play_audio(audio_file, 0)
        self.music.elapsed_time = 0
        self.updateText()
        self.setIconPlay("resources/pause.png")
        self.setCover(audio_file)
        self.currentTime = -1
        self.ended = False

    def pause_music(self):
        self.setIconPlay("resources/play.png")
        self.music.pause_audio()
        self.currentTime = self.music.elapsed_time

    def resume_music(self):
        print("audio_file", self.music.audio_file)
        self.setIconPlay("resources/pause.png")
        self.music.resume_audio()
        self.startTime = time.time()

    def setCover(self, address):
        bytes_data = cover.extract(address)

        # Create a QImage from the bytes data
        qimage = QtGui.QImage.fromData(bytes_data)
        # Create a QPixmap from the QImage
        pixmap = QtGui.QPixmap.fromImage(qimage)
        ui.labelImage.setPixmap(pixmap)

    def convert_to_mins(self, timeInSeconds):
        mins = int((timeInSeconds)//60)
        secs = int((timeInSeconds) % 60)
        return f"{mins}:{secs}"

    def periodic_function(self):
        if self.music.isPlaying is True:
            self.currentTime += 1

        if (self.currentTime) > self.music.duration:
            self.ended = True

        ui.labelTime.setText(self.convert_to_mins(
            self.currentTime) + '/'+self.convert_to_mins(self.music.duration))

        if self.ended:
            self.currentTime = 0
            if self.repeating == "all":
                self.clickNext()
            elif self.repeating == "one":
                self.play_music(
                    audio_file=self.musicAddresses[self.musicIndex])
            else:
                if self.musicIndex >= len(self.musicFiles)-1:
                    None
                else:
                    self.clickNext()

        if self.music.duration != 0:
            percentage = int((self.currentTime/self.music.duration)*100)
            if not backend.sliderPressed:
                ui.horizontalSlider.setProperty("value", percentage)


class Ui_MainWindow(object):
    def setStyle(self, name):
        eval(name).setStyleSheet("background-color:white; border-radius:25px")

        if name == "self.horizontalSlider":
            eval(name).setStyleSheet("QSlider::groove:horizontal {"
                                     "background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #16113d, stop:1 #a5419e);"
                                     "border: 1px solid #999999;"
                                     "height: 6px;"
                                     "margin: 2px 0;"
                                     "}"
                                     "QSlider::handle:horizontal {"
                                     "background: white;"
                                     "border: 1px solid black;"
                                     "width: 15px;"
                                     "height: 15px;"
                                     "margin: -1px 0;"
                                     "border-radius: 25px;"
                                     "}"
                                     "QSlider::handle:horizontal:active {"
                                     "background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 white, stop:1 white);"
                                     "}")

    def setupUi(self, MainWindow):
        self.hasVolumeSlider = False
        MainWindow.setObjectName("MainWindow")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setContentsMargins(11, -1, 0, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.buttonArrow = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.buttonArrow.sizePolicy().hasHeightForWidth())
        self.buttonArrow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources//left.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonArrow.setIcon(icon)
        self.buttonArrow.setObjectName("pushButton_3")
        self.horizontalLayout_4.addWidget(self.buttonArrow)
        # self.buttonArrow.clicked.connect(self.clickPrev)
        self.setStyle("self.buttonArrow")

        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.buttonFile = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.buttonFile.sizePolicy().hasHeightForWidth())
        self.buttonFile.setSizePolicy(sizePolicy)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("resources//folder.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonFile.setIcon(icon1)
        self.buttonFile.setIconSize(QtCore.QSize(20, 20))
        self.buttonFile.setObjectName("buttonFile")
        self.horizontalLayout_4.addWidget(self.buttonFile)
        self.buttonFile.clicked.connect(backend.clickFile)
        self.setStyle("self.buttonFile")

        self.buttonSettings = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.buttonSettings.sizePolicy().hasHeightForWidth())
        self.buttonSettings.setSizePolicy(sizePolicy)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("resources//settings.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonSettings.setIcon(icon2)
        self.buttonSettings.setObjectName("buttonSettings")
        self.horizontalLayout_4.addWidget(self.buttonSettings)
        self.setStyle("self.buttonSettings")

        self.verticalLayout.addWidget(self.frame_4, 0, QtCore.Qt.AlignTop)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")

        self.labelImage = QtWidgets.QLabel(self.frame)
        self.labelImage.setText("")
        self.labelImage.setPixmap(QtGui.QPixmap("resources/cover3.png"))
        self.labelImage.setScaledContents(True)
        self.labelImage.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.labelImage)
        self.labelImage.setMaximumSize(200, 200)

        self.verticalLayout.addWidget(self.frame)
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
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labelTitle = QtWidgets.QLabel(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.labelTitle.sizePolicy().hasHeightForWidth())
        self.labelTitle.setSizePolicy(sizePolicy)
        self.labelTitle.setScaledContents(False)
        self.labelTitle.setWordWrap(False)
        self.labelTitle.setObjectName("labelTitle")
        self.horizontalLayout_3.addWidget(self.labelTitle)
        self.verticalLayout.addWidget(self.frame_5)
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
        self.horizontalLayout_2.setContentsMargins(11, 11, 10, -1)
        self.horizontalLayout_2.setSpacing(7)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.horizontalSlider = QtWidgets.QSlider(self.frame_3)
        self.horizontalSlider.setProperty("value", 69)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout_2.addWidget(self.horizontalSlider)
        self.setStyle("self.horizontalSlider")
        self.horizontalSlider.sliderPressed.connect(backend.pressedSlider)
        self.horizontalSlider.sliderReleased.connect(backend.releasedSlider)
        self.horizontalSlider.valueChanged.connect(backend.movedSlider)
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setSingleStep(1)

        self.labelTime = QtWidgets.QLabel(self.frame_3)
        self.labelTime.setMinimumSize(QtCore.QSize(0, 0))
        self.labelTime.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelTime.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.labelTime.setObjectName("labelTime")
        self.horizontalLayout_2.addWidget(self.labelTime)

        self.verticalLayout.addWidget(self.frame_3)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(300, 0))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.buttonRepeat = QtWidgets.QPushButton(self.frame_2)
        self.buttonRepeat.setMinimumSize(QtCore.QSize(0, 40))
        self.buttonRepeat.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("resources//repeat_all.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonRepeat.setIcon(icon3)
        self.buttonRepeat.setIconSize(QtCore.QSize(25, 25))
        self.buttonRepeat.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(
            self.buttonRepeat, 0, QtCore.Qt.AlignLeft)
        self.buttonRepeat.clicked.connect(backend.clickRepeat)
        self.setStyle("self.buttonRepeat")

        self.buttonBack = QtWidgets.QPushButton(self.frame_2)
        self.buttonBack.setMinimumSize(QtCore.QSize(0, 50))
        self.buttonBack.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("resources//Back.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonBack.setIcon(icon4)
        self.buttonBack.setIconSize(QtCore.QSize(40, 40))
        self.buttonBack.setObjectName("buttonBack")
        self.horizontalLayout.addWidget(
            self.buttonBack, 0, QtCore.Qt.AlignRight)
        self.buttonBack.clicked.connect(backend.clickPrev)
        self.setStyle("self.buttonBack")

        self.buttonPlay = QtWidgets.QPushButton(self.frame_2)
        self.buttonPlay.setMinimumSize(QtCore.QSize(0, 50))
        self.buttonPlay.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("resources//play.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonPlay.setIcon(icon5)
        self.buttonPlay.setIconSize(QtCore.QSize(40, 40))
        self.buttonPlay.setObjectName("buttonPlay")
        self.horizontalLayout.addWidget(
            self.buttonPlay, 0, QtCore.Qt.AlignHCenter)
        self.buttonPlay.clicked.connect(backend.clickPlay)
        self.setStyle("self.buttonPlay")

        self.buttonNext = QtWidgets.QPushButton(self.frame_2)
        self.buttonNext.setMinimumSize(QtCore.QSize(0, 50))
        self.buttonNext.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("resources//next.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonNext.setIcon(icon6)
        self.buttonNext.setIconSize(QtCore.QSize(40, 40))
        self.buttonNext.setObjectName("buttonNext")
        self.horizontalLayout.addWidget(
            self.buttonNext, 0, QtCore.Qt.AlignLeft)
        self.buttonNext.clicked.connect(backend.clickNext)
        self.setStyle("self.buttonNext")

        self.buttonVol = QtWidgets.QPushButton(self.frame_2)
        self.buttonVol.setMinimumSize(QtCore.QSize(0, 40))
        self.buttonVol.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(
            "resources//speaker-filled-audio-tool.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonVol.setIcon(icon7)
        self.buttonVol.setIconSize(QtCore.QSize(25, 25))
        self.buttonVol.setObjectName("pushButton")
        self.horizontalLayout.addWidget(
            self.buttonVol, 0, QtCore.Qt.AlignRight)
        self.buttonVol.clicked.connect(backend.clickVolume)
        self.setStyle("self.buttonVol")

        self.verticalLayout.addWidget(self.frame_2)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 1)
        self.gridLayout_2.addLayout(self.verticalLayout, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.buttonArrow.setText(_translate("MainWindow", "Back"))
        self.buttonFile.setText(_translate("MainWindow", "File"))
        self.buttonSettings.setText(_translate("MainWindow", "Settings"))
        self.labelTitle.setText(_translate(
            "MainWindow", "press File to import music"))

    def popupSlider(self):
        self.volumeSlider = QtWidgets.QSlider(MainWindow)
        print("Volume slider added")
        self.volumeSlider.setProperty("value", 69)
        x = ui.buttonVol.pos().x()+20
        y = MainWindow.height()-200
        print(x, y)
        self.volumeSlider.setGeometry(x, y, 20, 100)
        self.volumeSlider.setOrientation(QtCore.Qt.Vertical)
        self.volumeSlider.setObjectName("volumeSlider")
        self.volumeSlider.show()

    def delPopupSlider(self):
        if ui.hasVolumeSlider:
            self.volumeSlider.setParent(None)
            self.volumeSlider.deleteLater()
            ui.hasVolumeSlider = False


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.move(1000, 100)  # Initial size
        self.setWindowTitle("Music")
        self.setStyleSheet("background-color:#ffffff;")
        windowIcon = QtGui.QIcon()
        windowIcon.addPixmap(QtGui.QPixmap("resources/sound-waves.png"))
        self.setWindowIcon(windowIcon)

        # Call periodic function #
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(backend.periodic_function)
        self.timer.start(1000)  # Update every second

        self.stacked_widget = QtWidgets.QStackedWidget()
        self.main_menu_widget = QtWidgets.QWidget()
        self.stacked_widget.addWidget(self.main_menu_widget)

    def resizeEvent(self, event):
        # Get the new width and height
        resize_factor = 2
        imageDim = int(self.height()/resize_factor)
        if self.height() >= 900 and self.width() >= 1800:
            ui.labelImage.setMaximumSize(700, 700)
        else:
            ui.labelImage.setMaximumSize(imageDim, imageDim)
        ui.delPopupSlider()

    def mousePressEvent(self, event) -> None:
        if event.button() == QtCore.Qt.LeftButton:
            ui.delPopupSlider()

    def switch_to_list_menu(self):
        self.stacked_widget()

#


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    backend = BackEnd()
    MainWindow = MainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
