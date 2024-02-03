# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cryoID_v2_1.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_cryoID(object):
    def setupUi(self, cryoID):
        cryoID.setObjectName("cryoID")
        cryoID.resize(879, 544)
        self.centralwidget = QtWidgets.QWidget(cryoID)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 821, 191))
        self.groupBox.setStyleSheet("")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gen_queries_button = QtWidgets.QPushButton(self.groupBox)
        self.gen_queries_button.setGeometry(QtCore.QRect(70, 60, 121, 51))
        self.gen_queries_button.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.gen_queries_button.setObjectName("gen_queries_button")
        self.density_map_label = QtWidgets.QLabel(self.groupBox)
        self.density_map_label.setGeometry(QtCore.QRect(290, 30, 60, 14))
        self.density_map_label.setObjectName("density_map_label")
        self.resolution_label = QtWidgets.QLabel(self.groupBox)
        self.resolution_label.setGeometry(QtCore.QRect(290, 70, 141, 21))
        self.resolution_label.setObjectName("resolution_label")
        self.symmetry_label = QtWidgets.QLabel(self.groupBox)
        self.symmetry_label.setGeometry(QtCore.QRect(290, 100, 91, 16))
        self.symmetry_label.setObjectName("symmetry_label")
        self.browse_mrc_file_button = QtWidgets.QPushButton(self.groupBox)
        self.browse_mrc_file_button.setGeometry(QtCore.QRect(640, 20, 113, 32))
        self.browse_mrc_file_button.setStyleSheet("image: url(:/newPrefix/upload-sign-svgrepo-com.svg);\n"
"image-position: right;")
        self.browse_mrc_file_button.setObjectName("browse_mrc_file_button")
        self.gq_methods_button = QtWidgets.QPushButton(self.groupBox)
        self.gq_methods_button.setGeometry(QtCore.QRect(360, 130, 281, 51))
        self.gq_methods_button.setObjectName("gq_methods_button")
        self.res_units_label = QtWidgets.QLabel(self.groupBox)
        self.res_units_label.setGeometry(QtCore.QRect(550, 70, 71, 21))
        self.res_units_label.setObjectName("res_units_label")
        self.mrc_file_editbox = QtWidgets.QTextEdit(self.groupBox)
        self.mrc_file_editbox.setGeometry(QtCore.QRect(360, 30, 261, 21))
        self.mrc_file_editbox.setObjectName("mrc_file_editbox")
        self.resolution_editbox = QtWidgets.QTextEdit(self.groupBox)
        self.resolution_editbox.setGeometry(QtCore.QRect(430, 70, 111, 21))
        self.resolution_editbox.setObjectName("resolution_editbox")
        self.symmetry_editbox = QtWidgets.QTextEdit(self.groupBox)
        self.symmetry_editbox.setGeometry(QtCore.QRect(430, 100, 111, 21))
        self.symmetry_editbox.setObjectName("symmetry_editbox")
        self.symmetry_editbox.raise_()
        self.resolution_editbox.raise_()
        self.mrc_file_editbox.raise_()
        self.gen_queries_button.raise_()
        self.density_map_label.raise_()
        self.resolution_label.raise_()
        self.symmetry_label.raise_()
        self.browse_mrc_file_button.raise_()
        self.gq_methods_button.raise_()
        self.res_units_label.raise_()
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 220, 821, 211))
        self.groupBox_2.setStyleSheet("")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.search_pool_button = QtWidgets.QPushButton(self.groupBox_2)
        self.search_pool_button.setGeometry(QtCore.QRect(70, 70, 121, 51))
        self.search_pool_button.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.search_pool_button.setObjectName("search_pool_button")
        self.sp_options_button = QtWidgets.QPushButton(self.groupBox_2)
        self.sp_options_button.setGeometry(QtCore.QRect(360, 130, 281, 51))
        self.sp_options_button.setObjectName("sp_options_button")
        self.browse_query_file_button = QtWidgets.QPushButton(self.groupBox_2)
        self.browse_query_file_button.setGeometry(QtCore.QRect(640, 30, 113, 32))
        self.browse_query_file_button.setObjectName("browse_query_file_button")
        self.browse_pool_fil_button = QtWidgets.QPushButton(self.groupBox_2)
        self.browse_pool_fil_button.setGeometry(QtCore.QRect(640, 80, 113, 32))
        self.browse_pool_fil_button.setObjectName("browse_pool_fil_button")
        self.query_file_label = QtWidgets.QLabel(self.groupBox_2)
        self.query_file_label.setGeometry(QtCore.QRect(290, 40, 61, 16))
        self.query_file_label.setObjectName("query_file_label")
        self.protein_pool_file_label = QtWidgets.QLabel(self.groupBox_2)
        self.protein_pool_file_label.setGeometry(QtCore.QRect(260, 80, 81, 16))
        self.protein_pool_file_label.setObjectName("protein_pool_file_label")
        self.query_file_editbox = QtWidgets.QTextEdit(self.groupBox_2)
        self.query_file_editbox.setGeometry(QtCore.QRect(360, 40, 261, 21))
        self.query_file_editbox.setObjectName("query_file_editbox")
        self.pool_file_editbox = QtWidgets.QTextEdit(self.groupBox_2)
        self.pool_file_editbox.setGeometry(QtCore.QRect(360, 80, 261, 21))
        self.pool_file_editbox.setObjectName("pool_file_editbox")
        self.pool_file_editbox.raise_()
        self.query_file_editbox.raise_()
        self.search_pool_button.raise_()
        self.sp_options_button.raise_()
        self.browse_query_file_button.raise_()
        self.browse_pool_fil_button.raise_()
        self.query_file_label.raise_()
        self.protein_pool_file_label.raise_()
        self.abort_button = QtWidgets.QPushButton(self.centralwidget)
        self.abort_button.setGeometry(QtCore.QRect(50, 430, 201, 61))
        self.abort_button.setStyleSheet("background-color: rgb(206, 0, 0);")
        self.abort_button.setObjectName("abort_button")
        self.status_label = QtWidgets.QLabel(self.centralwidget)
        self.status_label.setGeometry(QtCore.QRect(320, 440, 51, 31))
        self.status_label.setObjectName("status_label")
        self.status_label_ = QtWidgets.QLabel(self.centralwidget)
        self.status_label_.setGeometry(QtCore.QRect(370, 440, 381, 31))
        self.status_label_.setStyleSheet("background-color: rgb(186, 186, 186);")
        self.status_label_.setObjectName("status_label_")
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setGeometry(QtCore.QRect(770, 440, 51, 31))
        self.save_button.setStyleSheet("background-color: rgb(0, 204, 0);")
        self.save_button.setObjectName("save_button")
        cryoID.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(cryoID)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 879, 22))
        self.menubar.setObjectName("menubar")
        self.menucryoID = QtWidgets.QMenu(self.menubar)
        self.menucryoID.setObjectName("menucryoID")
        self.menuMore_Options = QtWidgets.QMenu(self.menubar)
        self.menuMore_Options.setObjectName("menuMore_Options")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        cryoID.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(cryoID)
        self.statusbar.setObjectName("statusbar")
        cryoID.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(cryoID)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(cryoID)
        self.actionOpen.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.actionOpen.setObjectName("actionOpen")
        self.actionRecent = QtWidgets.QAction(cryoID)
        self.actionRecent.setObjectName("actionRecent")
        self.actionTBD = QtWidgets.QAction(cryoID)
        self.actionTBD.setObjectName("actionTBD")
        self.actionNonesofar = QtWidgets.QAction(cryoID)
        self.actionNonesofar.setObjectName("actionNonesofar")
        self.actionResults_window = QtWidgets.QAction(cryoID)
        self.actionResults_window.setObjectName("actionResults_window")
        self.actionProgress_bar = QtWidgets.QAction(cryoID)
        self.actionProgress_bar.setObjectName("actionProgress_bar")
        self.actionPreviewer = QtWidgets.QAction(cryoID)
        self.actionPreviewer.setObjectName("actionPreviewer")
        self.action_L_oad_save = QtWidgets.QAction(cryoID)
        self.action_L_oad_save.setObjectName("action_L_oad_save")
        self.actionPhenix = QtWidgets.QAction(cryoID)
        self.actionPhenix.setObjectName("actionPhenix")
        self.menucryoID.addSeparator()
        self.menucryoID.addAction(self.actionNew)
        self.menucryoID.addAction(self.actionOpen)
        self.menucryoID.addAction(self.actionRecent)
        self.menucryoID.addAction(self.action_L_oad_save)
        self.menuMore_Options.addSeparator()
        self.menuMore_Options.addAction(self.actionTBD)
        self.menuMore_Options.addAction(self.actionPhenix)
        self.menuHelp.addAction(self.actionNonesofar)
        self.menuView.addAction(self.actionResults_window)
        self.menuView.addAction(self.actionProgress_bar)
        self.menuView.addAction(self.actionPreviewer)
        self.menubar.addAction(self.menucryoID.menuAction())
        self.menubar.addAction(self.menuMore_Options.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(cryoID)
        QtCore.QMetaObject.connectSlotsByName(cryoID)

    def retranslateUi(self, cryoID):
        _translate = QtCore.QCoreApplication.translate
        cryoID.setWindowTitle(_translate("cryoID", "MainWindow"))
        self.gen_queries_button.setToolTip(_translate("cryoID", "<html><head/><body><p>Specify your cryoEM density map, resolution limit, and symmetry in the fields to the right, then click on this button to generate query sequences from your chosen cryoEM map.</p></body></html>"))
        self.gen_queries_button.setText(_translate("cryoID", "Generate Queries"))
        self.density_map_label.setText(_translate("cryoID", "Density Map"))
        self.resolution_label.setText(_translate("cryoID", "High Resolution Limit"))
        self.symmetry_label.setText(_translate("cryoID", "Symmetry"))
        self.browse_mrc_file_button.setToolTip(_translate("cryoID", "<html><head/><body><p>Browse files and select the cryoEM density map you would like to analyze.</p></body></html>"))
        self.browse_mrc_file_button.setText(_translate("cryoID", "Browse Files"))
        self.gq_methods_button.setText(_translate("cryoID", "Options"))
        self.res_units_label.setText(_translate("cryoID", "Angstroms"))
        self.mrc_file_editbox.setToolTip(_translate("cryoID", "<html><head/><body><p>Use the Browse button to the right to locate and select the cryoEM density map you would like to analyze.</p></body></html>"))
        self.mrc_file_editbox.setHtml(_translate("cryoID", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">your_cryoEM_map.mrc</p></body></html>"))
        self.resolution_editbox.setHtml(_translate("cryoID", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3.2</p></body></html>"))
        self.symmetry_editbox.setHtml(_translate("cryoID", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Any</p></body></html>"))
        self.search_pool_button.setToolTip(_translate("cryoID", "<html><head/><body><p>Specify your query set file and your candidate protein pool file in the fields to the right, then click on this button to identify the candidate proteins that align best with your query sequences.</p></body></html>"))
        self.search_pool_button.setText(_translate("cryoID", "Search Pool"))
        self.sp_options_button.setText(_translate("cryoID", "Options"))
        self.browse_query_file_button.setText(_translate("cryoID", "Browse Files"))
        self.browse_pool_fil_button.setText(_translate("cryoID", "Browse Files"))
        self.query_file_label.setText(_translate("cryoID", "Query File"))
        self.protein_pool_file_label.setText(_translate("cryoID", "Protein Pool File"))
        self.query_file_editbox.setHtml(_translate("cryoID", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">your_query_file</p></body></html>"))
        self.pool_file_editbox.setHtml(_translate("cryoID", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">your_pool_file</p></body></html>"))
        self.abort_button.setToolTip(_translate("cryoID", "<html><head/><body><p>Abort the current job</p></body></html>"))
        self.abort_button.setText(_translate("cryoID", "Abort"))
        self.status_label.setText(_translate("cryoID", "Status"))
        self.status_label_.setText(_translate("cryoID", "  -/-"))
        self.save_button.setToolTip(_translate("cryoID", "<html><head/><body><p>Saves most recent progress that can be loaded and resumed at a later time. (Ctrl+S)</p></body></html>"))
        self.save_button.setWhatsThis(_translate("cryoID", "<html><head/><body><p><br/></p></body></html>"))
        self.save_button.setText(_translate("cryoID", "Save"))
        self.menucryoID.setTitle(_translate("cryoID", "File"))
        self.menuMore_Options.setTitle(_translate("cryoID", "More Options"))
        self.menuHelp.setTitle(_translate("cryoID", "Help"))
        self.menuView.setTitle(_translate("cryoID", "View"))
        self.actionNew.setText(_translate("cryoID", "New"))
        self.actionOpen.setText(_translate("cryoID", "Open"))
        self.actionRecent.setText(_translate("cryoID", "Recent"))
        self.actionTBD.setText(_translate("cryoID", "COOT"))
        self.actionNonesofar.setText(_translate("cryoID", "TBD"))
        self.actionResults_window.setText(_translate("cryoID", "Results window"))
        self.actionProgress_bar.setText(_translate("cryoID", "Progress bar"))
        self.actionPreviewer.setText(_translate("cryoID", "Previewer"))
        self.action_L_oad_save.setText(_translate("cryoID", "Load save"))
        self.actionPhenix.setText(_translate("cryoID", "Phenix"))
#import file_upload_rc   #manually commented this out for now, TLDR generated cuz of the image i added. 
# the above import doesnt work currently bc file_upload.qrc is nested under another directory
# can easily fix it manually, but trying to fix it in Designer so you don't need to do this everytime you make a change
# another solution is moving the assets into the same directory (kinda unorganized tho)