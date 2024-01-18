import sys, os
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog

from cryoID_v2 import Ui_cryoID
# alternatively skip the python file and just use the ui file


class MainWindow(qtw.QMainWindow):

    # custom signals
    file_selection_error = qtc.pyqtSignal(str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Your code will go here
        self.ui = Ui_cryoID()
        self.ui.setupUi(self)

        # select mrc file
        self.ui.browse_mrc_file_button.clicked.connect(self.SelectMRCfile)

        # select query file
        self.ui.browse_query_file_button.clicked.connect(self.SelectMRCfile)

        # select pool file
        self.ui.browse_pool_fil_button.clicked.connect(self.SelectMRCfile)

        # file menu actions
        self.ui.actionOpen.triggered.connect(self.open)

        # Your code ends here
        self.show()

    def SelectMRCfile(self):

        try:
            fname = QFileDialog.getOpenFileName(self, 'Select file', '.', 'density map(*.mrc *.cpp4)')
            fname_rel = os.path.relpath(fname[0], os.getcwd())
            self.ui.mrc_file_edit.setText(fname_rel)
        except ValueError:
            self.file_selection_error.emit('')   # artifact from cryoID code, it was an error message saying to select a file
            return -1

    def SelectQueryinput(self):
        fname = QFileDialog.getOpenFileName(self, 'Select file', '.', 'query file(*.fasta *.pdb)')
        fname_rel = os.path.relpath(fname[0], os.getcwd())
        self.ui.query_file_edit.setText(fname_rel)

    def SelectSeqPool(self):
        fname = QFileDialog.getOpenFileName(self, 'Select file', '.', 'Protein pool file(*.fasta *.txt *.list)')
        fname_rel = os.path.relpath(fname[0], os.getcwd())
        self.ui.pool_file_edit.setText(fname_rel)

    def open(self):
        filename, _ = qtw.QFileDialog.getOpenFileName()
        if filename:
            with open(filename, 'r') as handle:
                text = handle.read()
            self.textedit.clear()
            self.textedit.insertPlainText(text)
            self.textedit.moveCursor(qtg.QTextCursor.Start)
            self.statusBar().showMessage(f'Editing {filename}')

    # def generate_queries(self):
    #     filename = self.ui.query_file_edit.text()
    #
    #     if username == 'user' and password == 'pass':
    #         qtw.QMessageBox.information(self, 'Success', 'You are logged in')
    #     else:
    #         qtw.QMessageBox.critical(self, 'Fail', 'You did not log in')

    # TODO
    # COLORS
    # color hierarchy of buttons, make sure they make sense
    # think about names of buttosn (and everything else too)
    # allow users to save sessions (i.e. if you get interrupted in the middle of a long job)

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())