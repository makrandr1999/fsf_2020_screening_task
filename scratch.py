import sys,os
from PyQt5.QtWidgets import *
from scratchGUI import *

class MyForm(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_load_input.clicked.connect(self.loadInputs)
        self.show()

    def loadInputs(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home/makishere/fossee2020')
        extension = os.path.splitext(fname[0])[1]
        supportedFileTypes=['.csv','.xlsx']
        if (extension in supportedFileTypes):
            f = open(fname[0], 'r')
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