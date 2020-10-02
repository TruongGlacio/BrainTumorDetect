# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1248, 311)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(450, 220, 381, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.hboxlayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.hboxlayout.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")
        self.pushButton_trainingData = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_trainingData.setEnabled(False)
        self.pushButton_trainingData.setMaximumSize(QtCore.QSize(120, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_trainingData.setFont(font)
        self.pushButton_trainingData.setObjectName("pushButton_trainingData")
        self.hboxlayout.addWidget(self.pushButton_trainingData)
        self.pushButton_segmentation = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_segmentation.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_segmentation.sizePolicy().hasHeightForWidth())
        self.pushButton_segmentation.setSizePolicy(sizePolicy)
        self.pushButton_segmentation.setMaximumSize(QtCore.QSize(120, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_segmentation.setFont(font)
        self.pushButton_segmentation.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_segmentation.setObjectName("pushButton_segmentation")
        self.hboxlayout.addWidget(self.pushButton_segmentation)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(9, 10, 1221, 32))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_FolerPath = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_FolerPath.setFont(font)
        self.label_FolerPath.setObjectName("label_FolerPath")
        self.horizontalLayout.addWidget(self.label_FolerPath)
        self.lineEdit_FolderPath = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_FolderPath.setFont(font)
        self.lineEdit_FolderPath.setObjectName("lineEdit_FolderPath")
        self.horizontalLayout.addWidget(self.lineEdit_FolderPath)
        self.pushButton_OpenFileBroswer = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_OpenFileBroswer.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_OpenFileBroswer.sizePolicy().hasHeightForWidth())
        self.pushButton_OpenFileBroswer.setSizePolicy(sizePolicy)
        self.pushButton_OpenFileBroswer.setMinimumSize(QtCore.QSize(20, 30))
        self.pushButton_OpenFileBroswer.setMaximumSize(QtCore.QSize(150, 40))
        self.pushButton_OpenFileBroswer.setBaseSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_OpenFileBroswer.setFont(font)
        self.pushButton_OpenFileBroswer.setObjectName("pushButton_OpenFileBroswer")
        self.horizontalLayout.addWidget(self.pushButton_OpenFileBroswer)
        self.label_NotifyStatus = QtWidgets.QLabel(self.centralwidget)
        self.label_NotifyStatus.setGeometry(QtCore.QRect(20, 120, 1181, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_NotifyStatus.setFont(font)
        self.label_NotifyStatus.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_NotifyStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.label_NotifyStatus.setObjectName("label_NotifyStatus")
        self.radioButton_trainingMode = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_trainingMode.setGeometry(QtCore.QRect(50, 60, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_trainingMode.setFont(font)
        self.radioButton_trainingMode.setCheckable(True)
        self.radioButton_trainingMode.setChecked(True)
        self.radioButton_trainingMode.setObjectName("radioButton_trainingMode")
        self.radioButtonDetectedMode = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonDetectedMode.setGeometry(QtCore.QRect(50, 160, 121, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButtonDetectedMode.setFont(font)
        self.radioButtonDetectedMode.setObjectName("radioButtonDetectedMode")
        self.checkBox_BratsData = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_BratsData.setGeometry(QtCore.QRect(70, 190, 111, 20))
        self.checkBox_BratsData.setCheckable(False)
        self.checkBox_BratsData.setChecked(False)
        self.checkBox_BratsData.setObjectName("checkBox_BratsData")
        self.checkBox_TrainingWithMultiLabel = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_TrainingWithMultiLabel.setGeometry(QtCore.QRect(70, 90, 141, 17))
        self.checkBox_TrainingWithMultiLabel.setObjectName("checkBox_TrainingWithMultiLabel")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_trainingData.setText(_translate("MainWindow", "Training Data"))
        self.pushButton_segmentation.setText(_translate("MainWindow", "Segmentation"))
        self.label_FolerPath.setText(_translate("MainWindow", "Folder path :"))
        self.lineEdit_FolderPath.setText(_translate("MainWindow", "Type image Path in here"))
        self.pushButton_OpenFileBroswer.setText(_translate("MainWindow", "...."))
        self.label_NotifyStatus.setText(_translate("MainWindow", "While training data, please wait until finished"))
        self.radioButton_trainingMode.setText(_translate("MainWindow", "Training Mode"))
        self.radioButtonDetectedMode.setText(_translate("MainWindow", "Detect Mode"))
        self.checkBox_BratsData.setText(_translate("MainWindow", "Using Brats data"))
        self.checkBox_TrainingWithMultiLabel.setText(_translate("MainWindow", "Training With Multi Label"))
