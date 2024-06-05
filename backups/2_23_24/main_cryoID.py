import sys, os
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5.QtCore import QTextCodec
codec = QTextCodec.codecForName("UTF-8")

from cryoID_v2_3 import Ui_cryoID
#from cryoID_v2_4 import Ui_cryoID
# alternatively can directly import from the ui file and skip the python file


class MainWindow(qtw.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Your code will go here
        self.ui = Ui_cryoID()
        self.ui.setupUi(self)
        #self.resize(1200, 800)   # can resize here too

        # select mrc file
        self.ui.browse_mrc_file_button.clicked.connect(self.SelectMRCfile)

        # select query file
        self.ui.browse_query_file_button.clicked.connect(self.SelectQueryinput)

        # select pool file
        self.ui.browse_pool_fil_button.clicked.connect(self.SelectSeqPool)

        # file menu actions
        self.ui.actionOpen.triggered.connect(self.open)

        # >>> stuff from OG cryoID <<<
        self.process = qtc.QProcess(self)   # QProcess object for external programs
        self.ui.gen_queries_button.clicked.connect(self.get_queries)
        self.ui.search_pool_button.clicked.connect(self.search_pool)
        self.ui.abort_button.clicked.connect(self.abortjob)

        self.ui.save_button.clicked.connect(self.testfxn)

        # Your code ends here
        self.show()

        self.setStyleSheet("QToolTip { color: white; background-color: gray; border: 1px; }")
        self.statusBar().showMessage('[Error messages go here]', 5000)

    def testfxn(self):
        self.process.start("calculator.py")

    def show_dialog(self):
        pass

    def SelectMRCfile(self):
        try:
            fname = QFileDialog.getOpenFileName(self, 'Select file', '.', 'density map(*.mrc *.cpp4)')
            fname_rel = os.path.relpath(fname[0], os.getcwd())
            self.ui.mrc_file_editbox.setText(fname_rel)
            self.statusBar().showMessage(f'{fname_rel}', 2000)
        except ValueError:
            self.statusBar().showMessage('Please specify a file!', 2000)
            return -1

    def SelectQueryinput(self):
        try:
            fname = QFileDialog.getOpenFileName(self, 'Select file', '.', 'query file(*.fasta *.pdb)')
            fname_rel = os.path.relpath(fname[0], os.getcwd())
            self.ui.query_file_editbox.setText(fname_rel)
            self.statusBar().showMessage(f'{fname_rel}', 2000)
        except ValueError:
            self.statusBar().showMessage('Please specify a file!', 2000)
            return -1

    def SelectSeqPool(self):
        try:
            fname = QFileDialog.getOpenFileName(self, 'Select file', '.', 'Protein pool file(*.fasta *.txt *.list)')
            fname_rel = os.path.relpath(fname[0], os.getcwd())
            self.ui.pool_file_editbox.setText(fname_rel)
        except ValueError:
            self.statusBar().showMessage('Please specify a file!', 2000)
            return -1

    def open(self):   # delete this later, prob came from one of the pyqt tutorials
        filename, _ = qtw.QFileDialog.getOpenFileName()
        if filename:
            with open(filename, 'r') as handle:
                text = handle.read()
            self.textedit.clear()
            self.textedit.insertPlainText(text)
            self.textedit.moveCursor(qtg.QTextCursor.Start)
            self.statusBar().showMessage(f'Editing {filename}')

    def abortjob(self):

        # send terminate signal to subprogress
        print("abort")   # comment this out later and change the print message :skull:
        self.statusBar().showMessage('Aborted', 2000)
        self.process.terminate()
        # self.process.kill()

    # realtime display of output/error on GUI
    def outputDisplay(self):

        cursor = self.ui.Infobox.textCursor()
        cursor.movePosition(cursor.End)
        output_text = codec.toUnicode(self.process.readAllStandardOutput())
        cursor.insertText(output_text)

    def errorDisplay(self):

        cursor = self.ui.errorbox.textCursor()
        cursor.movePosition(cursor.End)
        error_text = codec.toUnicode(self.process.readAllStandardError())
        cursor.insertText(error_text)

    def processError(self):

        if self.process.error() == 0:
            self.ui.errorbox.setText(
                'The process failed to start. Either the program is missing, or you may not have permissions to execute it')
            # elif self.process.error() == 1:
            # self.ui.errorbox.setText('The program crashed')
        else:
            self.ui.errorbox.setText(str(self.process.errorString()))

    # bound to get_queries
    def get_queries(self):    # get vs generate lol choose one
        print("gen queries")

        #self.ui.Infobox.clear()
        #self.ui.errorbox.clear()

        densitymap = self.ui.mrc_file_editbox.toPlainText()
        #print(densitymap)
        resolution = self.ui.resolution_editbox.toPlainText()
        symmetry = self.ui.symmetry_editbox.toPlainText()
        #advanced = self.ui.advanced_1.toPlainText()
        advanced = ""

        # check if densitymap is provided
        if densitymap:
            get_queries_argu = ['-m', densitymap]
        else:
            #self.ui.errorbox.setText('Please input your densitymap first!')
            return -1

        # if resolution or symmetry not provided, use default value
        if resolution:
            get_queries_argu += ['-r', resolution]
        if symmetry:
            get_queries_argu += ['-s', symmetry]

        # add advanced options
        if advanced:
            get_queries_argu += advanced.split()

        # if self.ui.command_button.isChecked():
        # print 'get_queries ' + ' '.join(get_queries_argu)

        # # self.process.start('get_queries', get_queries_argu)
        # print("get_queries_v2.py", get_queries_argu)
        print(get_queries_argu)
        #self.process.start("get_queries_v1_1.py", get_queries_argu)
        self.process.start("calculator.py")
        print("started?")

    # bound to search_pool
    def search_pool(self):
        print("search pool")

        #self.ui.Infobox.clear()
        #self.ui.errorbox.clear()

        seqpool = self.ui.pool_file_editbox.toPlainText()
        #print(seqpool)
        query_file = self.ui.query_file_editbox.toPlainText()
        #print(query_file)
        # output = self.ui.search_output.toPlainText()
        advanced = ""
        #advanced = self.ui.advanced_2.toPlainText()     # <- this is the options bar (or options dropdown thing in old pyqt) btw

        if not (seqpool and query_file):
            #self.ui.errorbox.setText('Please input the query file/protein pool file first!')
            return -1

        # if not output:
            # output = 'final_list'

        search_pool_argu = ['-q', query_file, '-p', seqpool]  # , '-o', output]

        # check whether do reverse too
        # if self.ui.search_reverse.isChecked():
        #    search_pool_argu.append('-r')

        # add advanced options
        if advanced:
            search_pool_argu += advanced.split()

        # if self.ui.command_button.isChecked():
        # print 'search_pool ' + ' '.join(search_pool_argu)

        # self.process.start('search_pool', search_pool_argu)
        print(search_pool_argu)
        self.process.start('search_pool_v1_1.py', search_pool_argu)

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())