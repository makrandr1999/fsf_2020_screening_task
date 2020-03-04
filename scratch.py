import sys,os,xlrd,json,csv
from PyQt5.QtWidgets import *
from scratchGUI import *
import openpyxl
from openpyxl import Workbook
from pathlib import Path


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
            msg.setText(text)
            msg.setInformativeText(informativeText)
            msg.setWindowTitle(WindowTitle)
            msg.exec_()   
    def validate(self):
        try:
            tablenames=['table_fin','table_ten','table_bce','table_cleat']
            for sheet_name in self.sheet_names:
                tablename=self.sheets_dict[sheet_name]['table_name']
                isUnique=self.validateID(tablename)
                isNumeric=self.validateNumeric(tablename)
                if not isNumeric:
                    self.dispMessage("Value Error","Please ensure that all values are numeric","Error")
                    return False
                if not isUnique:
                    self.dispMessage("ID's aren't unique","Please ensure that all ID values are unique","Error")
                    return False

            self.dispMessage("Successfully Validated the input values!"," ","Success!")    
            return True
        except AttributeError:
            self.dispMessage("Input File not loaded"," " ,"Error")

    def validateID(self,tablename):
        table = (self.findChild(QTableWidget,tablename)) 
        allRows = table.rowCount()
        ids=[]
        for row in range(0,allRows):
            y=table.item(row,0).text()
            ids.append(y)
        s =set()
        for x in ids:
            if x in s: return False
            s.add(x)
        return True

    def validateNumeric(self,tablename):
        table = (self.findChild(QTableWidget,tablename))
        allRows = table.rowCount()
        tablecols=table.columnCount()
        for i in range(0,allRows): 
            for j in range(tablecols): 
                try:
                    float(table.item(i,j).text())
                except ValueError:
                    return False        
            
        return True            

    def submit(self):
        if not self.validate():
            return
        try:
            cwd = os.getcwd()
            for sheet_name in self.sheet_names:
                path = os.path.join(cwd,sheet_name)
                os.mkdir(path)  
                tablename=self.sheets_dict[sheet_name]['table_name']   
                table = (self.findChild(QTableWidget,tablename))
                allRows = table.rowCount()
                tablecols=table.columnCount()
                for i in range(allRows):
                    filename=sheet_name+'_'+table.item(i,0).text()+'.txt'
                    dicts = {}
                    for j in range(tablecols): 
                        dicts[table.horizontalHeaderItem(j).text()] =table.item(i,j).text()
                    with open(os.path.join(path,filename), 'w') as file:
                        file.write(json.dumps(dicts))
            self.dispMessage("Successfully generated the text files!"," ","Success!")    
                            

        except Exception as e:
            self.dispMessage(str(e)," ", "Something went wrong!")                 


            

    def loadData(self,path):
        self.wb = xlrd.open_workbook(path) 
        self.sheet_names = self.wb.sheet_names()
        no_of_sheets=len(self.sheet_names)
        for i in range(no_of_sheets):
            self.loadIntoTable(self.wb.sheet_by_index(i),self.sheet_names[i]);

    def loadIntoTable(self,curr_sheet,sheet_name):    
        try:   
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
        except Exception as e:
            self.dispMessage(str(e)," ", "Something went wrong!")    
                    

    def loadInputs(self):
        try:

            fname = QFileDialog.getOpenFileName(self, 'Open file', '/home/makishere/fossee2020',"Excel files(*.xlsx);;CSV files (*.csv)")
            extension = os.path.splitext(fname[0])[1]   
            if fname[0]:
                self.loadData(Path(fname[0]))
        except Exception as e:
            self.dispMessage(str(e)," ", "Something went wrong!")    
                


if __name__=="__main__":   
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())