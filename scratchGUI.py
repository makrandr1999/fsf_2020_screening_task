# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scratch.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(498, 447)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.frame)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_fin = QtWidgets.QWidget()
        self.tab_fin.setObjectName("tab_fin")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_fin)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.table_fin = QtWidgets.QTableWidget(self.tab_fin)
        self.table_fin.setGridStyle(QtCore.Qt.SolidLine)
        self.table_fin.setRowCount(0)
        self.table_fin.setObjectName("table_fin")
        self.table_fin.setColumnCount(7)
        item = QtWidgets.QTableWidgetItem()
        self.table_fin.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_fin.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_fin.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_fin.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_fin.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_fin.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_fin.setHorizontalHeaderItem(6, item)
        # self.table_fin.setColumnWidth(1, 80)
        self.table_fin.horizontalHeader().setCascadingSectionResizes(True)
        self.table_fin.horizontalHeader().setDefaultSectionSize(150)
        self.table_fin.horizontalHeader().setStretchLastSection(True)
        self.table_fin.verticalHeader().setDefaultSectionSize(40)
        # self.table_fin.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.verticalLayout_2.addWidget(self.table_fin)
        self.tabWidget.addTab(self.tab_fin, "")
        self.tab_ten = QtWidgets.QWidget()
        self.tab_ten.setObjectName("tab_ten")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_ten)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.table_ten = QtWidgets.QTableWidget(self.tab_ten)
        self.table_ten.setObjectName("table_ten")
        self.table_ten.horizontalHeader().setDefaultSectionSize(250)
        self.table_ten.verticalHeader().setDefaultSectionSize(40)
        self.table_ten.setColumnCount(5)
        self.table_ten.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_ten.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_ten.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_ten.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_ten.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_ten.setHorizontalHeaderItem(4, item)
        self.table_ten.horizontalHeader().setDefaultSectionSize(150)
        self.table_ten.horizontalHeader().setStretchLastSection(True)
        self.table_ten.verticalHeader().setCascadingSectionResizes(True)
        self.verticalLayout_6.addWidget(self.table_ten)
        self.tabWidget.addTab(self.tab_ten, "")
        self.tab_bce = QtWidgets.QWidget()
        self.tab_bce.setObjectName("tab_bce")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_bce)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.table_bce = QtWidgets.QTableWidget(self.tab_bce)
        self.table_bce.verticalHeader().setDefaultSectionSize(40)
        self.table_bce.horizontalHeader().setDefaultSectionSize(150)
        self.table_bce.setObjectName("table_bce")
        self.table_bce.setColumnCount(8)
        self.table_bce.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_bce.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_bce.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_bce.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_bce.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_bce.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_bce.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_bce.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_bce.setHorizontalHeaderItem(7, item)
        self.table_bce.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_4.addWidget(self.table_bce)
        self.tabWidget.addTab(self.tab_bce, "")
        self.tab_cleat = QtWidgets.QWidget()
        self.tab_cleat.setObjectName("tab_cleat")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_cleat)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.table_cleat = QtWidgets.QTableWidget(self.tab_cleat)
        self.table_cleat.horizontalHeader().setDefaultSectionSize(150)
        self.table_cleat.setGridStyle(QtCore.Qt.SolidLine)
        self.table_cleat.setObjectName("table_cleat")
        self.table_cleat.verticalHeader().setDefaultSectionSize(40)
        self.table_cleat.setColumnCount(7)
        self.table_cleat.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_cleat.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_cleat.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_cleat.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_cleat.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_cleat.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_cleat.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_cleat.setHorizontalHeaderItem(6, item)
        self.table_cleat.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_5.addWidget(self.table_cleat)
        self.tabWidget.addTab(self.tab_cleat, "")
        self.verticalLayout_3.addWidget(self.tabWidget)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.frame_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setLineWidth(0)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_load_input = QtWidgets.QPushButton(self.frame_2)
        self.btn_load_input.setObjectName("btn_load_input")
        self.gridLayout.addWidget(self.btn_load_input, 0, 0, 1, 1)
        self.btn_validate = QtWidgets.QPushButton(self.frame_2)
        self.btn_validate.setObjectName("btn_validate")
        self.gridLayout.addWidget(self.btn_validate, 0, 1, 1, 1)
        self.btn_submit = QtWidgets.QPushButton(self.frame_2)
        self.btn_submit.setObjectName("btn_submit")
        self.gridLayout.addWidget(self.btn_submit, 0, 2, 1, 1)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Scratch"))
        item = self.table_fin.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.table_fin.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Connection Type"))
        item = self.table_fin.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Axial Load"))
        item = self.table_fin.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Shear Load"))
        item = self.table_fin.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Bolt Diameter"))
        item = self.table_fin.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Bolt Grade"))
        item = self.table_fin.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Plate Thickness"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_fin), _translate("MainWindow", "FinPlate"))
        item = self.table_ten.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.table_ten.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Member Length"))
        item = self.table_ten.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Tensile Load"))
        item = self.table_ten.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Support Condition at End1 "))
        item = self.table_ten.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Support Condition at End2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_ten), _translate("MainWindow", "TensionMember"))
        item = self.table_bce.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.table_bce.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "End Plate "))
        item = self.table_bce.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "End Plate type"))
        item = self.table_bce.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Shear Load"))
        item = self.table_bce.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Axial Load"))
        item = self.table_bce.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Moment Load"))
        item = self.table_bce.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Bolt diameter"))
        item = self.table_bce.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Plate thickness"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_bce), _translate("MainWindow", "BCEndPlate"))
        item = self.table_cleat.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.table_cleat.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Angle leg 1"))
        item = self.table_cleat.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Angle log 1"))
        item = self.table_cleat.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Angle leg 2"))
        item = self.table_cleat.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Angle Thickness"))
        item = self.table_cleat.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Shear Load"))
        item = self.table_cleat.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Bolt grade"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_cleat), _translate("MainWindow", "CleatAngle"))
        self.btn_load_input.setText(_translate("MainWindow", "Load Inputs"))
        self.btn_validate.setText(_translate("MainWindow", "Validate"))
        self.btn_submit.setText(_translate("MainWindow", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

