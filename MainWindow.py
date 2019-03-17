# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '扇贝网/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class myLabel(QtWidgets.QLabel):
    clicked = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)

    def mouseReleaseEvent(self, QMouseEvent):
        if QMouseEvent.button() == QtCore.Qt.LeftButton:
            self.clicked.emit()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1086, 579)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.firstPage = QtWidgets.QLabel(self.centralwidget)
        self.firstPage.setGeometry(QtCore.QRect(0, 0, 1086, 558))
        self.firstPage.setText("")
        self.firstPage.setPixmap(QtGui.QPixmap(":/pic/1.jpg"))
        self.firstPage.setScaledContents(True)
        self.firstPage.setObjectName("firstPage")
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(541, 330, 141, 38))
        self.startButton.setStyleSheet("QPushButton {\n"
                                       "opacity:0;\n"
                                       "border: none;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "background:rgba(4, 51, 46, 0.3)\n"
                                       "}")
        self.startButton.setText("")
        self.startButton.setCheckable(False)
        self.startButton.setAutoRepeat(False)
        self.startButton.setDefault(False)
        self.startButton.setObjectName("startButton")
        self.secondPage = QtWidgets.QLabel(self.centralwidget)
        self.secondPage.setGeometry(QtCore.QRect(0, 0, 1086, 558))
        self.secondPage.setStyleSheet("")
        self.secondPage.setText("")
        self.secondPage.setPixmap(QtGui.QPixmap(":/pic/3.jpg"))
        self.secondPage.setScaledContents(True)
        self.secondPage.setObjectName("secondPage")
        self.nextButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(472, 437, 141, 38))
        self.nextButton.setStyleSheet("QPushButton {\n"
                                      "opacity:0;\n"
                                      "border: none;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "background:rgba(4, 51, 46, 0.3)\n"
                                      "}")
        self.nextButton.setText("")
        self.nextButton.setCheckable(False)
        self.nextButton.setAutoRepeat(False)
        self.nextButton.setDefault(False)
        self.nextButton.setObjectName("nextButton")
        self.buttonWidget = QtWidgets.QWidget(self.centralwidget)
        self.buttonWidget.setEnabled(True)
        self.buttonWidget.setGeometry(QtCore.QRect(162, 210, 756, 101))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonWidget.sizePolicy().hasHeightForWidth())
        self.buttonWidget.setSizePolicy(sizePolicy)
        self.buttonWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonWidget.setAutoFillBackground(False)
        self.buttonWidget.setObjectName("buttonWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.buttonWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.GMATButton = QtWidgets.QPushButton(self.buttonWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.GMATButton.sizePolicy().hasHeightForWidth())
        self.GMATButton.setSizePolicy(sizePolicy)
        self.GMATButton.setMouseTracking(False)
        self.GMATButton.setAutoFillBackground(False)
        self.GMATButton.setStyleSheet("QPushButton {\n"
                                      "opacity:0;\n"
                                      "border: none;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "background-color:rgba(0,255,0,0.1);\n"
                                      "}")
        self.GMATButton.setText("")
        self.GMATButton.setCheckable(False)
        self.GMATButton.setAutoRepeat(False)
        self.GMATButton.setDefault(False)
        self.GMATButton.setObjectName("GMATButton")
        self.gridLayout.addWidget(self.GMATButton, 0, 0, 1, 1)
        self.mbaButton = QtWidgets.QPushButton(self.buttonWidget)
        self.mbaButton.setMinimumSize(QtCore.QSize(0, 51))
        self.mbaButton.setMouseTracking(False)
        self.mbaButton.setAutoFillBackground(False)
        self.mbaButton.setStyleSheet("QPushButton {\n"
                                     "opacity:0;\n"
                                     "border: none;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:hover {\n"
                                     "background-color:rgba(0,255,0,0.1);\n"
                                     "}")
        self.mbaButton.setText("")
        self.mbaButton.setCheckable(False)
        self.mbaButton.setAutoRepeat(False)
        self.mbaButton.setDefault(False)
        self.mbaButton.setObjectName("mbaButton")
        self.gridLayout.addWidget(self.mbaButton, 0, 1, 1, 1)
        self.examButton = QtWidgets.QPushButton(self.buttonWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.examButton.sizePolicy().hasHeightForWidth())
        self.examButton.setSizePolicy(sizePolicy)
        self.examButton.setMinimumSize(QtCore.QSize(0, 51))
        self.examButton.setMaximumSize(QtCore.QSize(16777215, 51))
        self.examButton.setMouseTracking(False)
        self.examButton.setAutoFillBackground(False)
        self.examButton.setStyleSheet("QPushButton {\n"
                                      "opacity:0;\n"
                                      "border: none;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "background-color:rgba(0,255,0,0.1);\n"
                                      "}")
        self.examButton.setText("")
        self.examButton.setCheckable(False)
        self.examButton.setAutoRepeat(False)
        self.examButton.setDefault(False)
        self.examButton.setObjectName("examButton")
        self.gridLayout.addWidget(self.examButton, 0, 2, 1, 1)
        self.level4Button = QtWidgets.QPushButton(self.buttonWidget)
        self.level4Button.setMinimumSize(QtCore.QSize(0, 51))
        self.level4Button.setMouseTracking(False)
        self.level4Button.setAutoFillBackground(False)
        self.level4Button.setStyleSheet("QPushButton {\n"
                                        "opacity:0;\n"
                                        "border: none;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "background-color:rgba(0,255,0,0.1);\n"
                                        "}")
        self.level4Button.setText("")
        self.level4Button.setCheckable(False)
        self.level4Button.setAutoRepeat(False)
        self.level4Button.setDefault(False)
        self.level4Button.setObjectName("level4Button")
        self.gridLayout.addWidget(self.level4Button, 0, 3, 1, 1)
        self.level6Button = QtWidgets.QPushButton(self.buttonWidget)
        self.level6Button.setMinimumSize(QtCore.QSize(0, 51))
        self.level6Button.setMouseTracking(False)
        self.level6Button.setAutoFillBackground(False)
        self.level6Button.setStyleSheet("QPushButton {\n"
                                        "opacity:0;\n"
                                        "border: none;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "background-color:rgba(0,255,0,0.1);\n"
                                        "}")
        self.level6Button.setText("")
        self.level6Button.setCheckable(False)
        self.level6Button.setAutoRepeat(False)
        self.level6Button.setDefault(False)
        self.level6Button.setObjectName("level6Button")
        self.gridLayout.addWidget(self.level6Button, 0, 4, 1, 1)
        self.professionalButton = QtWidgets.QPushButton(self.buttonWidget)
        self.professionalButton.setMinimumSize(QtCore.QSize(0, 51))
        self.professionalButton.setMouseTracking(False)
        self.professionalButton.setAutoFillBackground(False)
        self.professionalButton.setStyleSheet("QPushButton {\n"
                                              "opacity:0;\n"
                                              "border: none;\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:hover {\n"
                                              "background-color:rgba(0,255,0,0.1);\n"
                                              "}")
        self.professionalButton.setText("")
        self.professionalButton.setCheckable(False)
        self.professionalButton.setAutoRepeat(False)
        self.professionalButton.setDefault(False)
        self.professionalButton.setObjectName("professionalButton")
        self.gridLayout.addWidget(self.professionalButton, 1, 0, 1, 1)
        self.toeflButton = QtWidgets.QPushButton(self.buttonWidget)
        self.toeflButton.setMinimumSize(QtCore.QSize(0, 51))
        self.toeflButton.setMouseTracking(False)
        self.toeflButton.setAutoFillBackground(False)
        self.toeflButton.setStyleSheet("QPushButton {\n"
                                       "opacity:0;\n"
                                       "border: none;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "background-color:rgba(0,255,0,0.1);\n"
                                       "}")
        self.toeflButton.setText("")
        self.toeflButton.setCheckable(False)
        self.toeflButton.setAutoRepeat(False)
        self.toeflButton.setDefault(False)
        self.toeflButton.setObjectName("toeflButton")
        self.gridLayout.addWidget(self.toeflButton, 1, 1, 1, 1)
        self.greButton = QtWidgets.QPushButton(self.buttonWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.greButton.sizePolicy().hasHeightForWidth())
        self.greButton.setSizePolicy(sizePolicy)
        self.greButton.setMinimumSize(QtCore.QSize(0, 51))
        self.greButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.greButton.setMouseTracking(False)
        self.greButton.setAutoFillBackground(False)
        self.greButton.setStyleSheet("QPushButton {\n"
                                     "opacity:0;\n"
                                     "border: none;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:hover {\n"
                                     "background-color:rgba(0,255,0,0.1);\n"
                                     "}")
        self.greButton.setText("")
        self.greButton.setCheckable(False)
        self.greButton.setAutoRepeat(False)
        self.greButton.setDefault(False)
        self.greButton.setObjectName("greButton")
        self.gridLayout.addWidget(self.greButton, 1, 2, 1, 1)
        self.ieltsButton = QtWidgets.QPushButton(self.buttonWidget)
        self.ieltsButton.setMinimumSize(QtCore.QSize(0, 51))
        self.ieltsButton.setMouseTracking(False)
        self.ieltsButton.setAutoFillBackground(False)
        self.ieltsButton.setStyleSheet("QPushButton {\n"
                                       "opacity:0;\n"
                                       "border: none;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "background-color:rgba(0,255,0,0.1);\n"
                                       "}")
        self.ieltsButton.setText("")
        self.ieltsButton.setCheckable(False)
        self.ieltsButton.setAutoRepeat(False)
        self.ieltsButton.setDefault(False)
        self.ieltsButton.setObjectName("ieltsButton")
        self.gridLayout.addWidget(self.ieltsButton, 1, 3, 1, 1)
        self.randomButton = QtWidgets.QPushButton(self.buttonWidget)
        self.randomButton.setMinimumSize(QtCore.QSize(0, 51))
        self.randomButton.setMouseTracking(False)
        self.randomButton.setAutoFillBackground(False)
        self.randomButton.setStyleSheet("QPushButton {\n"
                                        "opacity:0;\n"
                                        "border: none;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "background-color:rgba(0,255,0,0.1);\n"
                                        "}")
        self.randomButton.setText("")
        self.randomButton.setCheckable(False)
        self.randomButton.setAutoRepeat(False)
        self.randomButton.setDefault(False)
        self.randomButton.setObjectName("randomButton")
        self.gridLayout.addWidget(self.randomButton, 1, 4, 1, 1)
        self.thirdPage = QtWidgets.QLabel(self.centralwidget)
        self.thirdPage.setGeometry(QtCore.QRect(0, 0, 1086, 558))
        self.thirdPage.setText("")
        self.thirdPage.setPixmap(QtGui.QPixmap(":/pic/4.jpg"))
        self.thirdPage.setScaledContents(True)
        self.thirdPage.setObjectName("thirdPage")
        self.nextButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.nextButton_2.setGeometry(QtCore.QRect(472, 485, 141, 38))
        self.nextButton_2.setStyleSheet("QPushButton {\n"
                                        "opacity:0;\n"
                                        "border: none;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "background:rgba(4, 51, 46, 0.3)\n"
                                        "}")
        self.nextButton_2.setText("")
        self.nextButton_2.setCheckable(False)
        self.nextButton_2.setAutoRepeat(False)
        self.nextButton_2.setDefault(False)
        self.nextButton_2.setObjectName("nextButton_2")
        self.checkBox_all = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_all.setGeometry(QtCore.QRect(1007, 25, 16, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_all.sizePolicy().hasHeightForWidth())
        self.checkBox_all.setSizePolicy(sizePolicy)
        self.checkBox_all.setMinimumSize(QtCore.QSize(0, 0))
        self.checkBox_all.setAutoFillBackground(False)
        self.checkBox_all.setStyleSheet("QCheckButton {\n"
                                        "border:0.5px;\n"
                                        "border-color: rgba(179, 179, 179, 1);\n"
                                        "background:rgba(255, 255, 255, 1);\n"
                                        "border-radius:2px;\n"
                                        "}\n"
                                        "\n"
                                        "QCheckButton::indicator:checkable {\n"
                                        "background:rgba(79, 138, 245, 1);\n"
                                        "}")
        self.checkBox_all.setText("")
        self.checkBox_all.setCheckable(True)
        self.checkBox_all.setChecked(False)
        self.checkBox_all.setAutoRepeat(False)
        self.checkBox_all.setObjectName("checkBox_all")
        self.lastPage = QtWidgets.QLabel(self.centralwidget)
        self.lastPage.setGeometry(QtCore.QRect(0, 0, 1086, 558))
        self.lastPage.setText("")
        self.lastPage.setPixmap(QtGui.QPixmap(":/pic/5.jpg"))
        self.lastPage.setScaledContents(True)
        self.lastPage.setObjectName("lastPage")
        self.vocabulary = QtWidgets.QLabel(self.centralwidget)
        self.vocabulary.setGeometry(QtCore.QRect(428, 120, 231, 91))
        font = QtGui.QFont()
        font.setFamily(".SF NS Text Condensed")
        font.setPointSize(70)
        font.setBold(True)
        font.setWeight(75)
        self.vocabulary.setFont(font)
        self.vocabulary.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.vocabulary.setAutoFillBackground(False)
        self.vocabulary.setStyleSheet("color: rgba(79, 155, 134, 1);")
        self.vocabulary.setScaledContents(False)
        self.vocabulary.setAlignment(QtCore.Qt.AlignCenter)
        self.vocabulary.setWordWrap(False)
        self.vocabulary.setObjectName("vocabulary")
        self.vocabularyContent = QtWidgets.QLabel(self.centralwidget)
        self.vocabularyContent.setGeometry(QtCore.QRect(268, 200, 551, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.vocabularyContent.setFont(font)
        self.vocabularyContent.setAlignment(QtCore.Qt.AlignCenter)
        self.vocabularyContent.setObjectName("vocabularyContent")
        self.checkboxes = QtWidgets.QWidget(self.centralwidget)
        self.checkboxes.setGeometry(QtCore.QRect(26, 80, 1031, 400))
        self.checkboxes.setObjectName("checkboxes")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.checkboxes)
        self.gridLayout_2.setContentsMargins(0, 5, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.checkBox_33 = QtWidgets.QCheckBox(self.checkboxes)
        self.checkBox_33.setObjectName("checkBox_33")
        self.gridLayout_2.addWidget(self.checkBox_33, 1, 3, 1, 1)
        self.checkBox_24 = QtWidgets.QCheckBox(self.checkboxes)
        self.checkBox_24.setObjectName("checkBox_24")
        self.gridLayout_2.addWidget(self.checkBox_24, 1, 2, 1, 1)
        self.checkBox_15 = QtWidgets.QCheckBox(self.checkboxes)
        self.checkBox_15.setObjectName("checkBox_15")
        self.gridLayout_2.addWidget(self.checkBox_15, 1, 1, 1, 1)
        self.checkBox_6 = QtWidgets.QCheckBox(self.checkboxes)
        self.checkBox_6.setObjectName("checkBox_6")
        self.gridLayout_2.addWidget(self.checkBox_6, 1, 0, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.checkboxes)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout_2.addWidget(self.checkBox_2, 0, 1, 1, 1)
        self.checkBox_1 = QtWidgets.QCheckBox(self.checkboxes)
        self.checkBox_1.setObjectName("checkBox_1")
        self.gridLayout_2.addWidget(self.checkBox_1, 0, 0, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(self.checkboxes)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout_2.addWidget(self.checkBox_4, 0, 3, 1, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(self.checkboxes)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout_2.addWidget(self.checkBox_3, 0, 2, 1, 1)
        self.checkBox_5 = QtWidgets.QCheckBox(self.checkboxes)
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout_2.addWidget(self.checkBox_5, 0, 4, 1, 1)
        self.checkBox_8 = QtWidgets.QCheckBox(self.checkboxes)
        self.checkBox_8.setObjectName("checkBox_8")
        self.gridLayout_2.addWidget(self.checkBox_8, 3, 0, 1, 1)
        self.checkBox_35 = QtWidgets.QCheckBox(self.checkboxes)
        self.checkBox_35.setObjectName("checkBox_35")
        self.gridLayout_2.addWidget(self.checkBox_35, 3, 3, 1, 1)
        self.checkBox_26 = QtWidgets.QCheckBox(self.checkboxes)
        self.checkBox_26.setObjectName("checkBox_26")
        self.gridLayout_2.addWidget(self.checkBox_26, 3, 2, 1, 1)
        self.checkBox_43 = QtWidgets.QCheckBox(self.checkboxes)
        self.checkBox_43.setObjectName("checkBox_43")
        self.gridLayout_2.addWidget(self.checkBox_43, 2, 4, 1, 1)
        self.checkBox_9 = QtWidgets.QCheckBox(self.checkboxes)
        self.checkBox_9.setObjectName("checkBox_9")
        self.gridLayout_2.addWidget(self.checkBox_9, 4, 0, 1, 1)
        self.checkBox_17 = QtWidgets.QCheckBox(self.checkboxes)
        self.checkBox_17.setObjectName("checkBox_17")
        self.gridLayout_2.addWidget(self.checkBox_17, 3, 1, 1, 1)
        self.checkBox_44 = QtWidgets.QCheckBox(self.checkboxes)
        self.checkBox_44.setObjectName("checkBox_44")
        self.gridLayout_2.addWidget(self.checkBox_44, 3, 4, 1, 1)
        self.checkBox_18 = QtWidgets.QCheckBox(self.checkboxes)
        self.checkBox_18.setObjectName("checkBox_18")
        self.gridLayout_2.addWidget(self.checkBox_18, 4, 1, 1, 1)
        self.checkBox_10 = QtWidgets.QCheckBox(self.checkboxes)
        self.checkBox_10.setObjectName("checkBox_10")
        self.gridLayout_2.addWidget(self.checkBox_10, 5, 0, 1, 1)
        self.checkBox_45 = QtWidgets.QCheckBox(self.checkboxes)
        self.checkBox_45.setObjectName("checkBox_45")
        self.gridLayout_2.addWidget(self.checkBox_45, 4, 4, 1, 1)
        self.checkBox_19 = QtWidgets.QCheckBox(self.checkboxes)
        self.checkBox_19.setObjectName("checkBox_19")
        self.gridLayout_2.addWidget(self.checkBox_19, 5, 1, 1, 1)
        self.checkBox_36 = QtWidgets.QCheckBox(self.checkboxes)
        self.checkBox_36.setObjectName("checkBox_36")
        self.gridLayout_2.addWidget(self.checkBox_36, 4, 3, 1, 1)
        self.checkBox_27 = QtWidgets.QCheckBox(self.checkboxes)
        self.checkBox_27.setObjectName("checkBox_27")
        self.gridLayout_2.addWidget(self.checkBox_27, 4, 2, 1, 1)
        self.checkBox_7 = QtWidgets.QCheckBox(self.checkboxes)
        self.checkBox_7.setObjectName("checkBox_7")
        self.gridLayout_2.addWidget(self.checkBox_7, 2, 0, 1, 1)
        self.checkBox_16 = QtWidgets.QCheckBox(self.checkboxes)
        self.checkBox_16.setObjectName("checkBox_16")
        self.gridLayout_2.addWidget(self.checkBox_16, 2, 1, 1, 1)
        self.checkBox_42 = QtWidgets.QCheckBox(self.checkboxes)
        self.checkBox_42.setObjectName("checkBox_42")
        self.gridLayout_2.addWidget(self.checkBox_42, 1, 4, 1, 1)
        self.checkBox_34 = QtWidgets.QCheckBox(self.checkboxes)
        self.checkBox_34.setObjectName("checkBox_34")
        self.gridLayout_2.addWidget(self.checkBox_34, 2, 3, 1, 1)
        self.checkBox_25 = QtWidgets.QCheckBox(self.checkboxes)
        self.checkBox_25.setObjectName("checkBox_25")
        self.gridLayout_2.addWidget(self.checkBox_25, 2, 2, 1, 1)
        self.checkBox_11 = QtWidgets.QCheckBox(self.checkboxes)
        self.checkBox_11.setObjectName("checkBox_11")
        self.gridLayout_2.addWidget(self.checkBox_11, 6, 0, 1, 1)
        self.checkBox_20 = QtWidgets.QCheckBox(self.checkboxes)
        self.checkBox_20.setObjectName("checkBox_20")
        self.gridLayout_2.addWidget(self.checkBox_20, 6, 1, 1, 1)
        self.checkBox_28 = QtWidgets.QCheckBox(self.checkboxes)
        self.checkBox_28.setObjectName("checkBox_28")
        self.gridLayout_2.addWidget(self.checkBox_28, 5, 2, 1, 1)
        self.checkBox_46 = QtWidgets.QCheckBox(self.checkboxes)
        self.checkBox_46.setObjectName("checkBox_46")
        self.gridLayout_2.addWidget(self.checkBox_46, 5, 4, 1, 1)
        self.checkBox_29 = QtWidgets.QCheckBox(self.checkboxes)
        self.checkBox_29.setObjectName("checkBox_29")
        self.gridLayout_2.addWidget(self.checkBox_29, 6, 2, 1, 1)
        self.checkBox_37 = QtWidgets.QCheckBox(self.checkboxes)
        self.checkBox_37.setObjectName("checkBox_37")
        self.gridLayout_2.addWidget(self.checkBox_37, 5, 3, 1, 1)
        self.checkBox_38 = QtWidgets.QCheckBox(self.checkboxes)
        self.checkBox_38.setObjectName("checkBox_38")
        self.gridLayout_2.addWidget(self.checkBox_38, 6, 3, 1, 1)
        self.checkBox_47 = QtWidgets.QCheckBox(self.checkboxes)
        self.checkBox_47.setObjectName("checkBox_47")
        self.gridLayout_2.addWidget(self.checkBox_47, 6, 4, 1, 1)
        self.checkBox_48 = QtWidgets.QCheckBox(self.checkboxes)
        self.checkBox_48.setObjectName("checkBox_48")
        self.gridLayout_2.addWidget(self.checkBox_48, 7, 4, 1, 1)
        self.checkBox_13 = QtWidgets.QCheckBox(self.checkboxes)
        self.checkBox_13.setObjectName("checkBox_13")
        self.gridLayout_2.addWidget(self.checkBox_13, 8, 0, 1, 1)
        self.checkBox_21 = QtWidgets.QCheckBox(self.checkboxes)
        self.checkBox_21.setObjectName("checkBox_21")
        self.gridLayout_2.addWidget(self.checkBox_21, 7, 1, 1, 1)
        self.checkBox_39 = QtWidgets.QCheckBox(self.checkboxes)
        self.checkBox_39.setObjectName("checkBox_39")
        self.gridLayout_2.addWidget(self.checkBox_39, 7, 3, 1, 1)
        self.checkBox_12 = QtWidgets.QCheckBox(self.checkboxes)
        self.checkBox_12.setObjectName("checkBox_12")
        self.gridLayout_2.addWidget(self.checkBox_12, 7, 0, 1, 1)
        self.checkBox_30 = QtWidgets.QCheckBox(self.checkboxes)
        self.checkBox_30.setObjectName("checkBox_30")
        self.gridLayout_2.addWidget(self.checkBox_30, 7, 2, 1, 1)
        self.checkBox_40 = QtWidgets.QCheckBox(self.checkboxes)
        self.checkBox_40.setObjectName("checkBox_40")
        self.gridLayout_2.addWidget(self.checkBox_40, 8, 3, 1, 1)
        self.checkBox_41 = QtWidgets.QCheckBox(self.checkboxes)
        self.checkBox_41.setObjectName("checkBox_41")
        self.gridLayout_2.addWidget(self.checkBox_41, 9, 3, 1, 1)
        self.checkBox_32 = QtWidgets.QCheckBox(self.checkboxes)
        self.checkBox_32.setObjectName("checkBox_32")
        self.gridLayout_2.addWidget(self.checkBox_32, 9, 2, 1, 1)
        self.checkBox_49 = QtWidgets.QCheckBox(self.checkboxes)
        self.checkBox_49.setObjectName("checkBox_49")
        self.gridLayout_2.addWidget(self.checkBox_49, 8, 4, 1, 1)
        self.checkBox_23 = QtWidgets.QCheckBox(self.checkboxes)
        self.checkBox_23.setObjectName("checkBox_23")
        self.gridLayout_2.addWidget(self.checkBox_23, 9, 1, 1, 1)
        self.checkBox_22 = QtWidgets.QCheckBox(self.checkboxes)
        self.checkBox_22.setObjectName("checkBox_22")
        self.gridLayout_2.addWidget(self.checkBox_22, 8, 1, 1, 1)
        self.checkBox_31 = QtWidgets.QCheckBox(self.checkboxes)
        self.checkBox_31.setObjectName("checkBox_31")
        self.gridLayout_2.addWidget(self.checkBox_31, 8, 2, 1, 1)
        self.checkBox_14 = QtWidgets.QCheckBox(self.checkboxes)
        self.checkBox_14.setObjectName("checkBox_14")
        self.gridLayout_2.addWidget(self.checkBox_14, 9, 0, 1, 1)
        self.checkBox_50 = QtWidgets.QCheckBox(self.checkboxes)
        self.checkBox_50.setObjectName("checkBox_50")
        self.gridLayout_2.addWidget(self.checkBox_50, 9, 4, 1, 1)
        self.fourthPage = QtWidgets.QLabel(self.centralwidget)
        self.fourthPage.setGeometry(QtCore.QRect(0, -3, 1086, 561))
        self.fourthPage.setText("")
        self.fourthPage.setPixmap(QtGui.QPixmap(":/pic/6.jpg"))
        self.fourthPage.setScaledContents(True)
        self.fourthPage.setObjectName("fourthPage")
        self.word = QtWidgets.QLabel(self.centralwidget)
        self.word.setGeometry(QtCore.QRect(99, 210, 301, 131))
        font = QtGui.QFont()
        font.setFamily(".SF NS Text Condensed")
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.word.setFont(font)
        self.word.setStyleSheet("color: rgba(79, 155, 134, 1)")
        self.word.setAlignment(QtCore.Qt.AlignCenter)
        self.word.setObjectName("word")
        self.wordNums = QtWidgets.QLabel(self.centralwidget)
        self.wordNums.setGeometry(QtCore.QRect(980, 14, 71, 40))
        font = QtGui.QFont()
        font.setFamily(".SF NS Symbols")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.wordNums.setFont(font)
        self.wordNums.setStyleSheet("color: rgba(51, 51, 51, 0.9)\n"
                                    "")
        self.wordNums.setAlignment(QtCore.Qt.AlignCenter)
        self.wordNums.setObjectName("wordNums")
        self.choiceWidget = QtWidgets.QWidget(self.centralwidget)
        self.choiceWidget.setGeometry(QtCore.QRect(490, 140, 541, 295))
        self.choiceWidget.setObjectName("choiceWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.choiceWidget)
        self.verticalLayout.setContentsMargins(40, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.choice_1 = myLabel(self.choiceWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.choice_1.sizePolicy().hasHeightForWidth())
        self.choice_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(".SF NS Text")
        font.setPointSize(20)
        self.choice_1.setFont(font)
        self.choice_1.setStyleSheet("QLabel {\n"
                                    "color: rgba(51, 51, 51, 0.95);\n"
                                    "}\n"
                                    "\n"
                                    "QLabel:hover {\n"
                                    "background-color:rgba(0,255,0,0.1);\n"
                                    "}\n"
                                    "\n"
                                    "\n"
                                    "")
        self.choice_1.setObjectName("choice_1")
        self.verticalLayout.addWidget(self.choice_1)
        self.choice_2 = myLabel(self.choiceWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.choice_2.sizePolicy().hasHeightForWidth())
        self.choice_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(".SF NS Text")
        font.setPointSize(20)
        self.choice_2.setFont(font)
        self.choice_2.setStyleSheet("QLabel {\n"
                                    "color: rgba(51, 51, 51, 0.95);\n"
                                    "}\n"
                                    "\n"
                                    "QLabel:hover {\n"
                                    "background-color:rgba(0,255,0,0.1);\n"
                                    "}\n"
                                    "\n"
                                    "\n"
                                    "")
        self.choice_2.setObjectName("choice_2")
        self.verticalLayout.addWidget(self.choice_2)
        self.choice_3 = myLabel(self.choiceWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.choice_3.sizePolicy().hasHeightForWidth())
        self.choice_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(".SF NS Text")
        font.setPointSize(20)
        self.choice_3.setFont(font)
        self.choice_3.setStyleSheet("QLabel {\n"
                                    "color: rgba(51, 51, 51, 0.95);\n"
                                    "}\n"
                                    "\n"
                                    "QLabel:hover {\n"
                                    "background-color:rgba(0,255,0,0.1);\n"
                                    "}\n"
                                    "\n"
                                    "\n"
                                    "")
        self.choice_3.setObjectName("choice_3")
        self.verticalLayout.addWidget(self.choice_3)
        self.choice_4 = myLabel(self.choiceWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.choice_4.sizePolicy().hasHeightForWidth())
        self.choice_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(".SF NS Text")
        font.setPointSize(20)
        self.choice_4.setFont(font)
        self.choice_4.setStyleSheet("QLabel {\n"
                                    "color: rgba(51, 51, 51, 0.95);\n"
                                    "}\n"
                                    "\n"
                                    "QLabel:hover {\n"
                                    "background-color:rgba(0,255,0,0.1);\n"
                                    "}\n"
                                    "\n"
                                    "\n"
                                    "")
        self.choice_4.setObjectName("choice_4")
        self.verticalLayout.addWidget(self.choice_4)
        self.choice_5 = myLabel(self.choiceWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.choice_5.sizePolicy().hasHeightForWidth())
        self.choice_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(".SF NS Text")
        font.setPointSize(20)
        self.choice_5.setFont(font)
        self.choice_5.setStyleSheet("QLabel {\n"
                                    "color: rgba(51, 51, 51, 0.95);\n"
                                    "}\n"
                                    "\n"
                                    "QLabel:hover {\n"
                                    "background-color:rgba(0,255,0,0.1);\n"
                                    "}\n"
                                    "\n"
                                    "\n"
                                    "")
        self.choice_5.setObjectName("choice_5")
        self.verticalLayout.addWidget(self.choice_5)
        self.lastPage.raise_()
        self.vocabularyContent.raise_()
        self.vocabulary.raise_()
        self.fourthPage.raise_()
        self.wordNums.raise_()
        self.choiceWidget.raise_()
        self.word.raise_()
        self.thirdPage.raise_()
        self.nextButton_2.raise_()
        self.checkboxes.raise_()
        self.checkBox_all.raise_()
        self.choice_1.raise_()
        self.choice_2.raise_()
        self.choice_3.raise_()
        self.choice_4.raise_()
        self.choice_5.raise_()
        self.secondPage.raise_()
        self.buttonWidget.raise_()
        self.nextButton.raise_()
        self.firstPage.raise_()
        self.startButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.startButton.clicked.connect(self.firstPage.close)
        self.startButton.clicked.connect(self.startButton.close)
        self.toeflButton.clicked.connect(self.nextButton.close)
        self.level6Button.clicked.connect(self.nextButton.close)
        self.level6Button.clicked.connect(self.secondPage.close)
        self.professionalButton.clicked.connect(self.buttonWidget.close)
        self.professionalButton.clicked.connect(self.secondPage.close)
        self.professionalButton.clicked.connect(self.nextButton.close)
        self.toeflButton.clicked.connect(self.buttonWidget.close)
        self.toeflButton.clicked.connect(self.secondPage.close)
        self.GMATButton.clicked.connect(self.buttonWidget.close)
        self.GMATButton.clicked.connect(self.nextButton.close)
        self.mbaButton.clicked.connect(self.secondPage.close)
        self.mbaButton.clicked.connect(self.nextButton.close)
        self.GMATButton.clicked.connect(self.secondPage.close)
        self.examButton.clicked.connect(self.buttonWidget.close)
        self.level6Button.clicked.connect(self.buttonWidget.close)
        self.examButton.clicked.connect(self.secondPage.close)
        self.level4Button.clicked.connect(self.nextButton.close)
        self.level4Button.clicked.connect(self.secondPage.close)
        self.level4Button.clicked.connect(self.buttonWidget.close)
        self.examButton.clicked.connect(self.nextButton.close)
        self.mbaButton.clicked.connect(self.buttonWidget.close)
        self.greButton.clicked.connect(self.buttonWidget.close)
        self.greButton.clicked.connect(self.secondPage.close)
        self.greButton.clicked.connect(self.nextButton.close)
        self.ieltsButton.clicked.connect(self.buttonWidget.close)
        self.ieltsButton.clicked.connect(self.secondPage.close)
        self.ieltsButton.clicked.connect(self.nextButton.close)
        self.randomButton.clicked.connect(self.buttonWidget.close)
        self.randomButton.clicked.connect(self.secondPage.close)
        self.randomButton.clicked.connect(self.nextButton.close)
        self.nextButton.clicked.connect(self.buttonWidget.close)
        self.nextButton.clicked.connect(self.secondPage.close)
        self.nextButton.clicked.connect(self.nextButton.close)
        self.nextButton_2.clicked.connect(self.thirdPage.close)
        self.nextButton_2.clicked.connect(self.checkboxes.close)
        self.nextButton_2.clicked.connect(self.nextButton_2.close)
        self.nextButton_2.clicked.connect(self.checkBox_all.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.vocabulary.setText(_translate("MainWindow", "100"))
        self.vocabularyContent.setText(_translate("MainWindow", "您的英语如果不是刚入门，就是忘得差不多了，加油啊！"))
        self.checkBox_33.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_24.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_15.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_6.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_2.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_1.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_4.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_3.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_5.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_8.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_35.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_26.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_43.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_9.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_17.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_44.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_18.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_10.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_45.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_19.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_36.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_27.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_7.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_16.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_42.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_34.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_25.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_11.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_20.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_28.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_46.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_29.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_37.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_38.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_47.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_48.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_13.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_21.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_39.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_12.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_30.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_40.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_41.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_32.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_49.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_23.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_22.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_31.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_14.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_50.setText(_translate("MainWindow", "CheckBox"))
        self.word.setText(_translate("MainWindow", "TextLabel"))
        self.wordNums.setText(_translate("MainWindow", "1/6"))
        self.choice_1.setText(_translate("MainWindow", "TextLabel"))
        self.choice_2.setText(_translate("MainWindow", "TextLabel"))
        self.choice_3.setText(_translate("MainWindow", "TextLabel"))
        self.choice_4.setText(_translate("MainWindow", "TextLabel"))
        self.choice_5.setText(_translate("MainWindow", "TextLabel"))


import shanbeircc_rc
