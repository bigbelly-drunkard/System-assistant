# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'update_ui.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget#centralwidget{background:#F7FAFF}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_min = QtWidgets.QPushButton(self.widget)
        self.pushButton_min.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_min.setStyleSheet("QPushButton{background:Transparent;color:blank;}QPushButton:hover{background-color:rgba(0,0,0, 0.1);}")
        self.pushButton_min.setText("")
        self.pushButton_min.setObjectName("pushButton_min")
        self.horizontalLayout.addWidget(self.pushButton_min)
        self.pushButton_close = QtWidgets.QPushButton(self.widget)
        self.pushButton_close.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_close.setStyleSheet("QPushButton{background:Transparent;color:blank;}QPushButton:hover{background-color:rgba(0,0,0, 0.1);}")
        self.pushButton_close.setText("")
        self.pushButton_close.setObjectName("pushButton_close")
        self.horizontalLayout.addWidget(self.pushButton_close)
        self.verticalLayout.addWidget(self.widget)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setStyleSheet("QTextEdit{background:Transparent}")
        self.textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.progressBar = QtWidgets.QProgressBar(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.progressBar.setFont(font)
        self.progressBar.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.progressBar.setAcceptDrops(False)
        self.progressBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.progressBar.setStyleSheet("QProgressBar::chunk{background:qlineargradient(spread:pad,x1:0,y1:0,x2:1,y2:0,stop:0 #36d1dc,stop:1 #5b86e5);}")
        self.progressBar.setProperty("value", 66)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_2.addWidget(self.progressBar)
        self.verticalLayout.addWidget(self.widget_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "软件升级中，请稍后..."))
        self.label_2.setText(_translate("MainWindow", "更新进度："))
        self.progressBar.setFormat(_translate("MainWindow", "%p%"))