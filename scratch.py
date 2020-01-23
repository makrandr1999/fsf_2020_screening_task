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

    def loadData(self,path):
        self.wb = xlrd.open_workbook(path) # 
        sheet_names = self.wb.sheet_names()
        no_of_sheets=len(sheet_names)
        for i in range(no_of_sheets):
            self.loadIntoTable(self.wb.sheet_by_index(i),sheet_names[i]);

    def loadIntoTable(self,curr_sheet,sheet_name):       
        sheets_dict={ 'FinPlate': {'table_name': 'table_fin', 'cols': '7'}, 
         'TensionMember': {'table_name': 'table_ten', 'cols': '5'},'BCEndPlate': {'table_name': 'table_bce', 'cols': '8'},
         'CleatAngle': {'table_name': 'table_cleat', 'cols': '7'}}
        tablename=sheets_dict[sheet_name]['table_name']
        tablecols=int(sheets_dict[sheet_name]['cols'])
        table = (self.findChild(QTableWidget,tablename))          
        table.setRowCount(curr_sheet.nrows-1)
        for i in range(1,curr_sheet.nrows): 
            for j in range(int(tablecols)): 
                table.setItem(i-1,j,QTableWidgetItem(str(curr_sheet.cell_value(i,j))))  

    def loadInputs(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home/makishere/fossee2020')
        extension = os.path.splitext(fname[0])[1]
        # print(fname[0])
        supportedFileTypes=['.csv','.xlsx']
        if (extension in supportedFileTypes):
            self.loadData(fname[0])
            # self.addDummyData(fname[0])

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("File Type Not Supported")
            msg.setInformativeText('Please load a CSV or an xlsx file')
            msg.setWindowTitle("Error")
            msg.exec_()

            # app.exec_()
      
                


if __name__=="__main__":   
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())