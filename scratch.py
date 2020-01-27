import sys,os,xlrd,json
from PyQt5.QtWidgets import *
from scratchGUI import *

class mydict(dict):
        def __str__(self):
            return json.dumps(self)

class MyForm(QMainWindow,Ui_MainWindow):

    def __init__(self,parent=None):
        super(MyForm, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_load_input.clicked.connect(self.loadInputs)
        self.ui.btn_validate.clicked.connect(self.validate)
        self.ui.btn_submit.clicked.connect(self.submit)
        self.show()
    def dispMessage(self,text,informativeText,WindowTitle):
            msg = QMessageBox()
            # msg.setIcon(QMessageBox.Critical)
            msg.setText(text)
            msg.setInformativeText(informativeText)
            msg.setWindowTitle(WindowTitle)
            msg.exec_()   
    def validate(self):
        tablenames=['table_fin','table_ten','table_bce','table_cleat']
        for sheet_name in self.sheet_names:
            tablename=self.sheets_dict[sheet_name]['table_name']
            print(self.validateNumeric(tablename))
            # self.validateNumeric(tablename)
        # self.dispMessage('lol','lol','lol')    
    def validateID(self,tablename):
        table = (self.findChild(QTableWidget,tablename)) 
        allRows = table.rowCount()
        ids=[]
        for row in range(0,allRows):
            y=table.item(row,0).text()
            # print(y)
            ids.append(y)
        s =set()
        for x in ids:
            if x in s: return False
            s.add(x)
        return True

    def validateNumeric(self,tablename):
        table = (self.findChild(QTableWidget,tablename))
        allRows = table.rowCount()
        # int flag=0;
        tablecols=table.columnCount()
        for i in range(0,allRows): 
            for j in range(tablecols): 
                try:
                    float(table.item(i,j).text())
                    # return True
                except ValueError:
                    return False        
            
        return True            

    def submit(self):

        # pass
        for sheet_name in self.sheet_names:
            # print(sheet_name)
            tablename=self.sheets_dict[sheet_name]['table_name']   
            table = (self.findChild(QTableWidget,tablename))
            allRows = table.rowCount()
            # int flag=0;
            tablecols=table.columnCount()
            for i in range(allRows):
                filename=sheet_name+'_'+table.item(i,0).text()+'.txt'
                dicts = {}
                for j in range(tablecols): 
                    # print(i,j) 
                    dicts[table.horizontalHeaderItem(j).text()] =table.item(i,j).text()
                with open(filename, 'w') as file:

                    file.write(json.dumps(dicts))    
                # print(filename)


            

    def loadData(self,path):
        self.wb = xlrd.open_workbook(path) 
        self.sheet_names = self.wb.sheet_names()
        no_of_sheets=len(self.sheet_names)
        for i in range(no_of_sheets):
            self.loadIntoTable(self.wb.sheet_by_index(i),self.sheet_names[i]);

    def loadIntoTable(self,curr_sheet,sheet_name):       
        self.sheets_dict={ 'FinPlate': {'table_name': 'table_fin', 'cols': '7'}, 
         'TensionMember': {'table_name': 'table_ten', 'cols': '5'},'BCEndPlate': {'table_name': 'table_bce', 'cols': '8'},
         'CleatAngle': {'table_name': 'table_cleat', 'cols': '7'}}
        tablename=self.sheets_dict[sheet_name]['table_name']
        tablecols=int(self.sheets_dict[sheet_name]['cols'])
        table = (self.findChild(QTableWidget,tablename))          
        table.setRowCount(curr_sheet.nrows-1)
        for i in range(1,curr_sheet.nrows): 
            for j in range(int(tablecols)):
                y=curr_sheet.cell_value(i,j)
                if j==0:
                    y=int(y)
                table.setItem(i-1,j,QTableWidgetItem(str(y)))

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