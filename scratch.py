import sys,os,xlrd
from PyQt5.QtWidgets import *
from scratchGUI import *

class MyForm(QMainWindow,Ui_MainWindow):

    def __init__(self,parent=None):
        super(MyForm, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_load_input.clicked.connect(self.loadInputs)
        self.show()

    def addDummyData(self,path):
        # for i in range(10):
        #     for j in range(10):
        #         self.ui.tableWidget.setItem(i,j,QTableWidgetItem(str(i))) 
        wb = xlrd.open_workbook(path) 
        sheet = wb.sheet_by_index(0) 
        sheet_names = wb.sheet_names()
        self.ui.tableWidget.setRowCount(sheet.nrows)

        # print(sheet_names)  
        # For row 0 and column 0 
        # sheet.cell_value(0, 0) 
        # self.ui.tableWidget.setItem(0,0,QTableWidgetItem(str(0)))  
        for i in range(1,sheet.nrows): 
            for j in range(7): 
                # print(sheet.cell_value(i,j),i,j)
                self.ui.tableWidget.setItem(i-1,j,QTableWidgetItem(str(sheet.cell_value(i,j))))  
                # self.ui.tableWidget.setItem(i-1,j,QTableWidgetItem(str(0)))






    def loadInputs(self):
        self.addDummyData('/home/makishere/fossee2020/Input_values.xlsx')
        # fname = QFileDialog.getOpenFileName(self, 'Open file', '/home/makishere/fossee2020')
        # extension = os.path.splitext(fname[0])[1]
        # # print(fname[0])
        # supportedFileTypes=['.csv','.xlsx']
        # if (extension in supportedFileTypes):
        #     self.addDummyData(fname[0])

        # else:
        #     msg = QMessageBox()
        #     msg.setIcon(QMessageBox.Critical)
        #     msg.setText("File Type Not Supported")
        #     msg.setInformativeText('Please load a CSV or an xlsx file')
        #     msg.setWindowTitle("Error")
        #     msg.exec_()

            # app.exec_()
      
                


if __name__=="__main__":   
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())