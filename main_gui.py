import sys
import os
import subprocess
from pathlib import Path
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PyQt5.QtCore import QTextCodec
codec = QTextCodec.codecForName("UTF-8")

from gui_skin import Ui_cryoID
# alternatively for the import, could skip the python file and just use the ui file (check tutorial for steps)

from chimerax_launcher import launch_chimerax


class MainWindow(qtw.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Your code will go here
        self.ui = Ui_cryoID()
        self.ui.setupUi(self)
        #self.resize(1200, 800)   # can resize here too

        self.selected_files = []   # files selected from input and result files

        ### Main window signals & slots
        # select mrc file
        self.ui.browse_mrc_file_button.clicked.connect(self.SelectMRCfile)
        # select pool file
        self.ui.browse_pool_fil_button.clicked.connect(self.SelectSeqPool)
        # abort button, nothing to abort right now
        self.ui.abort_button.clicked.connect(self.abortjob)   # just do equivalent of ctrl+C in linux?

        ### Menu (top) bar signals & slots
        # File > Open, will likely remove later or change it to an open folder/set home folder button
        self.ui.actionOpen.triggered.connect(self.open)    # DEPRECATE THIS
        # View > ChimeraX (same as the sidebar button)
        self.ui.actionChimeraX.triggered.connect(lambda: launch_chimerax(self.selected_files))

        ### Side bar signals & slots
        # View selected files in ChimeraX
        self.ui.view_in_chimera_button.clicked.connect(lambda: launch_chimerax(self.selected_files))
        # Initial file fetch, defaults to cwd
        self.fetch_files(os.getcwd())
        # change inputs folder
        self.ui.change_folder_button_inputs.clicked.connect(lambda: self.select_folder("inputs"))
        # change results folder
        self.ui.change_folder_button_results.clicked.connect(lambda: self.select_folder("results"))

        # no clue if this is even needed anymore, might be from original cryoID gui
        self.process = qtc.QProcess(self)   # QProcess object for external programs

        # # testing new placeholder function (printing custom message when button is clicked)
        # self.ui.run_button.clicked.connect(lambda: self.placeholder_fxn('run button'))
        # self.ui.abort_button.clicked.connect(lambda: self.placeholder_fxn('abort button'))

        # testing 2nd placeholder function (print name of button clicked), also helps during development
        self.ui.run_button.clicked.connect(self.placeholder_fxn_2)
        self.ui.abort_button.clicked.connect(self.placeholder_fxn_2)

        # self.set_up_body()

        # Your code ends here
        self.show()

        self.setStyleSheet("QToolTip { color: white; background-color: gray; border: 1px; }")
        self.statusBar().showMessage('[Error messages go here]', 5000)

    ##### Main window functions
    # might combine these 2 functions if they end up rly similar
    def SelectMRCfile(self):
        try:
            fname = qtw.QFileDialog.getOpenFileName(self, 'Select file', '.', 'density map(*.mrc *.cpp4)')
            fname_rel = os.path.relpath(fname[0], os.getcwd())
            self.ui.mrc_file_editbox.setText(fname_rel)
            self.statusBar().showMessage(f'{fname_rel}', 2000)
        except ValueError:
            self.statusBar().showMessage('Please specify a file!', 2000)
            return -1

    def SelectSeqPool(self):
        try:
            fname = qtw.QFileDialog.getOpenFileName(self, 'Select file', '.', 'Protein pool file(*.fasta *.txt *.list)')
            fname_rel = os.path.relpath(fname[0], os.getcwd())
            self.ui.pool_file_editbox.setText(fname_rel)
            self.statusBar().showMessage(f'{fname_rel}', 2000)
        except ValueError:
            self.statusBar().showMessage('Please specify a file!', 2000)
            return -1

    # abort the running job
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

    # from old cryoID, may or may not need this. Delete get_queries tho, actualy dont need that one.
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

    ##### Menu (top) bar functions
    def open(self):    # from a tutorial, remove later or just use the style of the 3 other open file fxns
        filename, _ = qtw.QFileDialog.getOpenFileName()
        if filename:
            with open(filename, 'r') as handle:
                text = handle.read()
            self.textedit.clear()
            self.textedit.insertPlainText(text)
            self.textedit.moveCursor(qtg.QTextCursor.Start)
            self.statusBar().showMessage(f'Editing {filename}')

    def placeholder_fxn(self, name):     # rename this variable to msg
        # prints message passed from signal, which can be custom set (currently just the name of the button)
        print(name)   # to pycharm command line
        self.statusBar().showMessage(name + " clicked", 2000)   # to the gui

    def placeholder_fxn_2(self, name):
        # prints name of signal connected to this slot (ie the name of the button clicked)
        sender = self.sender()
        senderName = sender.objectName()
        print(senderName)   # to pycharm command line
        self.statusBar().showMessage(senderName + " clicked", 2000)    # to the gui

    ##### Side bar functions
    # Most likely will delete this one
    # For displaying file tree
    # this one still needs work, prob shouldnt do it like this, delete this later
    def set_up_body(self):

        # Body
        body_frame = qtw.QFrame()
        body_frame.setFrameShape(qtw.QFrame.NoFrame)
        body_frame.setFrameShadow(qtw.QFrame.Plain)
        body_frame.setLineWidth(0)
        body_frame.setMidLineWidth(0)
        body_frame.setContentsMargins(0, 0, 0, 0)
        body_frame.setSizePolicy(qtw.QSizePolicy.Expanding, qtw.QSizePolicy.Expanding)
        body = qtw.QHBoxLayout()
        body.setContentsMargins(0, 0, 0, 0)
        body.setSpacing(0)
        body_frame.setLayout(body)

        # side_bar
        self.side_bar = qtw.QFrame()
        self.side_bar.setFrameShape(qtw.QFrame.StyledPanel)
        self.side_bar.setFrameShadow(qtw.QFrame.Plain)
        self.side_bar.setStyleSheet(f'''
            background-color: black;
        ''')
        side_bar_layout = qtw.QHBoxLayout()
        side_bar_layout.setContentsMargins(5, 10, 5, 0)
        side_bar_layout.setSpacing(0)
        side_bar_layout.setAlignment(qtc.Qt.AlignTop | qtc.Qt.AlignCenter)

        # setup labels
        folder_label = qtw.QLabel()
        folder_label.setPixmap(qtg.QPixmap("./src/icons/folder-icon-blue.svg").scaled(qtc.QSize(25, 25)))
        folder_label.setAlignment(qtc.Qt.AlignmentFlag.AlignTop)
        #folder_label.setFont(self.window_font)
        folder_label.mousePressEvent = self.show_hide_tab
        side_bar_layout.addWidget(folder_label)
        self.side_bar.setLayout(side_bar_layout)

        body.addWidget(self.side_bar)

        # split view
        self.hsplit = qtw.QSplitter(qtc.Qt.Horizontal)

        # frame and layout to hold tree view (file manager)
        self.tree_frame = qtw.QFrame()
        self.tree_frame.setLineWidth(1)
        self.tree_frame.setMaximumWidth(400)
        self.tree_frame.setMinimumWidth(200)
        self.tree_frame.setBaseSize(100, 0)
        self.tree_frame.setContentsMargins(0, 0, 0, 0)
        tree_frame_layout = qtw.QVBoxLayout()
        tree_frame_layout.setContentsMargins(0, 0, 0, 0)
        tree_frame_layout.setSpacing(0)
        self.tree_frame.setStyleSheet('''
            QFrame {
                background-color: #21252b;
                border-radius: 5px;
                border: none;
                padding: 5px;
                color: #D3D3D3;
            }
            QFrame:hover {
                color: white;
            }
        ''')

        # Create file system model to show in tree view
        self.model = qtw.QFileSystemModel()
        self.model.setRootPath(os.getcwd())
        # File system filters
        self.model.setFilter(qtc.QDir.NoDotAndDotDot | qtc.QDir.AllDirs | qtc.QDir.Files)

        # Tree View
        self.tree_view = qtw.QTreeView()
        self.tree_view.setFont(qtg.QFont("FiraCode", 13))
        self.tree_view.setModel(self.model)
        self.tree_view.setRootIndex(self.model.index(os.getcwd()))
        self.tree_view.setSelectionMode(qtw.QTreeView.SingleSelection)
        self.tree_view.setSelectionBehavior(qtw.QTreeView.SelectRows)
        self.tree_view.setEditTriggers(qtw.QTreeView.NoEditTriggers)
        # add custom context menu
        self.tree_view.setContextMenuPolicy(qtc.Qt.CustomContextMenu)
        self.tree_view.customContextMenuRequested.connect(self.tree_view_context_menu)
        # handling click
        self.tree_view.clicked.connect(self.tree_view_clicked)
        self.tree_view.setIndentation(10)
        self.tree_view.setSizePolicy(qtw.QSizePolicy.Expanding, qtw.QSizePolicy.Expanding)
         # Hide header and hide other columns except for name
        self.tree_view.setHeaderHidden(True) # hiding header
        self.tree_view.setColumnHidden(1, True)
        self.tree_view.setColumnHidden(2, True)
        self.tree_view.setColumnHidden(3, True)

        # setup layout
        tree_frame_layout.addWidget(self.tree_view)
        self.tree_frame.setLayout(tree_frame_layout)


        # Tab Widget to add editor to
        self.tab_view = qtw.QTabWidget()
        self.tab_view.setContentsMargins(0, 0, 0, 0)
        self.tab_view.setTabsClosable(True)
        self.tab_view.setMovable(True)
        self.tab_view.setDocumentMode(True)
        # self.tab_view.tabsClos

        # add tree view and tab view
        self.hsplit.addWidget(self.tree_frame)
        self.hsplit.addWidget(self.tab_view)


        body.addWidget(self.hsplit)
        body_frame.setLayout(body)


        self.setCentralWidget(body_frame)

    def show_hide_tab(self):
        ...

    def tree_view_context_menu(self, pos):
        ...


    def tree_view_clicked(self, index: qtc.QModelIndex):
        path = self.model.filePath(index)
        p = Path(path)
        self.set_new_tab(p)

    ##### New side bar functions
    # Select the folder to display files from, currently only for results folder
    def select_folder(self, name=None):
        default_folder = os.getcwd()    # TODO: change the default folder to wherever the model building code saves the results
        folder = qtw.QFileDialog.getExistingDirectory(self, "Select Folder", default_folder)
        if folder:
            self.fetch_files(folder, name)

    # Fetch files and display them
    def fetch_files(self, folder, name=None):
        # Update label to display the selected folder
        parent_folder = os.path.basename(os.path.dirname(folder))
        current_folder = os.path.basename(folder)
        # print(folder); print(parent_folder); print(current_folder)    # debugging
        if name == "inputs":
            # display parent and current directory
            self.ui.inputs_folder_label.setText(os.path.join(parent_folder, current_folder).replace("\\","/"))
            # self.ui.inputs_folder_label.setText(current_folder)
        elif name == "results":
            self.ui.results_folder_label.setText(os.path.join(parent_folder, current_folder).replace("\\","/"))
            # self.ui.results_folder_label.setText(current_folder)

        # Fetch files from the selected folder
        files = os.listdir(folder)

        # Clear existing items
        if name == "inputs":
            current_widget = self.ui.file_list_widget_inputs
        elif name == "results":
            current_widget = self.ui.file_list_widget_results
        else:
            return     # early return, should never happen. works without this, but extra safety net
        current_widget.clear()
        self.selected_files.clear()

        # Add files to list widget with checkboxes
        for file in files:
            if os.path.isfile(os.path.join(folder, file)):
                file_abspath = os.path.join(folder, file).replace("\\", "/")
                #print(file_abspath)    # debug
                checkbox = qtw.QCheckBox(file)
                item = qtw.QListWidgetItem()
                current_widget.addItem(item)
                current_widget.setItemWidget(item, checkbox)
                checkbox.stateChanged.connect(lambda state, file_abspath=file_abspath: self.update_selected_files(state, file_abspath))

    # Add files to selected files list when checked, and remove when unchecked
    def update_selected_files(self, state, file):
        if state == 2:  # Checked
            self.selected_files.append(file)
            print(file)   # debug
            print(self.selected_files)
        elif state == 0:  # Unchecked
            self.selected_files.remove(file)
            print(file)  # debug


    ##### Drag and drop
    #TODO:


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())