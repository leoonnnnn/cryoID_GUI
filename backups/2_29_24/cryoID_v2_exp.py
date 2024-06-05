# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cryoID_v2_exp.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_cryoID(object):
    def setupUi(self, cryoID):
        cryoID.setObjectName("cryoID")
        cryoID.resize(970, 607)
        font = QtGui.QFont()
        font.setPointSize(12)
        cryoID.setFont(font)
        cryoID.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(cryoID)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.top_widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.top_widget.sizePolicy().hasHeightForWidth())
        self.top_widget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.top_widget.setFont(font)
        self.top_widget.setObjectName("top_widget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.top_widget)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.top_widget_left = QtWidgets.QWidget(self.top_widget)
        self.top_widget_left.setObjectName("top_widget_left")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.top_widget_left)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_2.addItem(spacerItem1)
        self.gen_queries_button = QtWidgets.QPushButton(self.top_widget_left)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gen_queries_button.sizePolicy().hasHeightForWidth())
        self.gen_queries_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.gen_queries_button.setFont(font)
        self.gen_queries_button.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.gen_queries_button.setObjectName("gen_queries_button")
        self.verticalLayout_2.addWidget(self.gen_queries_button)
        spacerItem2 = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_6.addWidget(self.top_widget_left)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.top_widget_right = QtWidgets.QWidget(self.top_widget)
        self.top_widget_right.setObjectName("top_widget_right")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.top_widget_right)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top_widget_right_1 = QtWidgets.QWidget(self.top_widget_right)
        self.top_widget_right_1.setStyleSheet("/*background-color: rgb(145, 145, 145);")
        self.top_widget_right_1.setObjectName("top_widget_right_1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.top_widget_right_1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.density_map_label = QtWidgets.QLabel(self.top_widget_right_1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.density_map_label.setFont(font)
        self.density_map_label.setObjectName("density_map_label")
        self.horizontalLayout.addWidget(self.density_map_label)
        spacerItem4 = QtWidgets.QSpacerItem(73, 15, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.mrc_file_editbox = QtWidgets.QLineEdit(self.top_widget_right_1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mrc_file_editbox.setFont(font)
        self.mrc_file_editbox.setObjectName("mrc_file_editbox")
        self.horizontalLayout.addWidget(self.mrc_file_editbox)
        spacerItem5 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.browse_mrc_file_button = QtWidgets.QPushButton(self.top_widget_right_1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.browse_mrc_file_button.setFont(font)
        self.browse_mrc_file_button.setStyleSheet("/*image: url(:/newPrefix/upload-sign-svgrepo-com.svg);\n"
"image-position: right; */")
        self.browse_mrc_file_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("svg_assets/upload-sign-svgrepo-com.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.browse_mrc_file_button.setIcon(icon)
        self.browse_mrc_file_button.setObjectName("browse_mrc_file_button")
        self.horizontalLayout.addWidget(self.browse_mrc_file_button)
        spacerItem6 = QtWidgets.QSpacerItem(68, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.verticalLayout.addWidget(self.top_widget_right_1)
        self.mid_widget_right_2 = QtWidgets.QWidget(self.top_widget_right)
        self.mid_widget_right_2.setStyleSheet("/*background-color: rgb(145, 145, 145);")
        self.mid_widget_right_2.setObjectName("mid_widget_right_2")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.mid_widget_right_2)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.protein_pool_file_label = QtWidgets.QLabel(self.mid_widget_right_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.protein_pool_file_label.setFont(font)
        self.protein_pool_file_label.setObjectName("protein_pool_file_label")
        self.horizontalLayout_14.addWidget(self.protein_pool_file_label)
        spacerItem7 = QtWidgets.QSpacerItem(55, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem7)
        self.pool_file_editbox = QtWidgets.QLineEdit(self.mid_widget_right_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pool_file_editbox.setFont(font)
        self.pool_file_editbox.setObjectName("pool_file_editbox")
        self.horizontalLayout_14.addWidget(self.pool_file_editbox)
        spacerItem8 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem8)
        self.browse_pool_fil_button = QtWidgets.QPushButton(self.mid_widget_right_2)
        self.browse_pool_fil_button.setText("")
        self.browse_pool_fil_button.setIcon(icon)
        self.browse_pool_fil_button.setObjectName("browse_pool_fil_button")
        self.horizontalLayout_14.addWidget(self.browse_pool_fil_button)
        spacerItem9 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem9)
        self.verticalLayout.addWidget(self.mid_widget_right_2)
        spacerItem10 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem10)
        self.top_widget_right_4 = QtWidgets.QWidget(self.top_widget_right)
        self.top_widget_right_4.setStyleSheet("/*background-color: rgb(85, 85, 85);")
        self.top_widget_right_4.setObjectName("top_widget_right_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.top_widget_right_4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem11 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem11)
        self.gq_methods_button = QtWidgets.QPushButton(self.top_widget_right_4)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.gq_methods_button.setFont(font)
        self.gq_methods_button.setObjectName("gq_methods_button")
        self.horizontalLayout_5.addWidget(self.gq_methods_button)
        spacerItem12 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem12)
        self.verticalLayout.addWidget(self.top_widget_right_4)
        self.horizontalLayout_6.addWidget(self.top_widget_right, 0, QtCore.Qt.AlignLeft)
        self.gridLayout.addWidget(self.top_widget, 0, 0, 1, 1)
        self.bot_widget = QtWidgets.QWidget(self.centralwidget)
        self.bot_widget.setObjectName("bot_widget")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.bot_widget)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        spacerItem13 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem13)
        self.abort_button = QtWidgets.QPushButton(self.bot_widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.abort_button.setFont(font)
        self.abort_button.setStyleSheet("background-color: rgb(206, 0, 0);")
        self.abort_button.setObjectName("abort_button")
        self.horizontalLayout_16.addWidget(self.abort_button)
        spacerItem14 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem14)
        self.status_label = QtWidgets.QLabel(self.bot_widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.status_label.setFont(font)
        self.status_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.status_label.setObjectName("status_label")
        self.horizontalLayout_16.addWidget(self.status_label)
        spacerItem15 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem15)
        self.status_label_ = QtWidgets.QLabel(self.bot_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.status_label_.sizePolicy().hasHeightForWidth())
        self.status_label_.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.status_label_.setFont(font)
        self.status_label_.setStyleSheet("background-color: rgb(186, 186, 186);")
        self.status_label_.setObjectName("status_label_")
        self.horizontalLayout_16.addWidget(self.status_label_)
        spacerItem16 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem16)
        self.save_button = QtWidgets.QPushButton(self.bot_widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.save_button.setFont(font)
        self.save_button.setStyleSheet("background-color: rgb(0, 204, 0);")
        self.save_button.setObjectName("save_button")
        self.horizontalLayout_16.addWidget(self.save_button)
        spacerItem17 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem17)
        self.gridLayout.addWidget(self.bot_widget, 1, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.widget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.horizontalLayout_2.addWidget(self.plainTextEdit)
        self.verticalScrollBar = QtWidgets.QScrollBar(self.widget)
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.horizontalLayout_2.addWidget(self.verticalScrollBar)
        self.gridLayout.addWidget(self.widget, 2, 0, 1, 1)
        cryoID.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(cryoID)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 970, 28))
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
        self.dockWidget = QtWidgets.QDockWidget(cryoID)
        self.dockWidget.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.dockWidgetContents)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label, 0, QtCore.Qt.AlignTop)
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem18)
        self.dockWidget.setWidget(self.dockWidgetContents)
        cryoID.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)
        self.dockWidget_2 = QtWidgets.QDockWidget(cryoID)
        self.dockWidget_2.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.dockWidget_2.setObjectName("dockWidget_2")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.dockWidgetContents_2)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.checkBox = QtWidgets.QCheckBox(self.dockWidgetContents_2)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_4.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.dockWidgetContents_2)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout_4.addWidget(self.checkBox_2)
        self.checkBox_3 = QtWidgets.QCheckBox(self.dockWidgetContents_2)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout_4.addWidget(self.checkBox_3)
        self.checkBox_4 = QtWidgets.QCheckBox(self.dockWidgetContents_2)
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout_4.addWidget(self.checkBox_4)
        self.checkBox_5 = QtWidgets.QCheckBox(self.dockWidgetContents_2)
        self.checkBox_5.setObjectName("checkBox_5")
        self.verticalLayout_4.addWidget(self.checkBox_5)
        spacerItem19 = QtWidgets.QSpacerItem(20, 212, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem19)
        self.dockWidget_2.setWidget(self.dockWidgetContents_2)
        cryoID.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_2)
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
        self.actionChimeraX = QtWidgets.QAction(cryoID)
        self.actionChimeraX.setObjectName("actionChimeraX")
        self.actionMRCs = QtWidgets.QAction(cryoID)
        self.actionMRCs.setObjectName("actionMRCs")
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
        self.menuView.addAction(self.actionMRCs)
        self.menuView.addAction(self.actionChimeraX)
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
        self.gen_queries_button.setText(_translate("cryoID", "Run"))
        self.density_map_label.setText(_translate("cryoID", "Density Map"))
        self.mrc_file_editbox.setText(_translate("cryoID", "your_cryoEM_map.mrc"))
        self.browse_mrc_file_button.setToolTip(_translate("cryoID", "<html><head/><body><p>Browse files and select the cryoEM density map you would like to analyze.</p></body></html>"))
        self.protein_pool_file_label.setText(_translate("cryoID", "Candidate Pool"))
        self.pool_file_editbox.setText(_translate("cryoID", "your_pool_file"))
        self.gq_methods_button.setText(_translate("cryoID", "Options"))
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
        self.label_2.setText(_translate("cryoID", "side menu"))
        self.label.setText(_translate("cryoID", "(just testing)"))
        self.label_4.setText(_translate("cryoID", "View MRCs"))
        self.checkBox.setText(_translate("cryoID", "placeholder1.mrc"))
        self.checkBox_2.setText(_translate("cryoID", "placeholder2.mrc"))
        self.checkBox_3.setText(_translate("cryoID", "placeholder3.mrc"))
        self.checkBox_4.setText(_translate("cryoID", "placeholder4.mrc"))
        self.checkBox_5.setText(_translate("cryoID", "placeholder5.mrc"))
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
        self.actionChimeraX.setText(_translate("cryoID", "ChimeraX"))
        self.actionMRCs.setText(_translate("cryoID", "MRCs"))
from svg_assets import resources


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    cryoID = QtWidgets.QMainWindow()
    ui = Ui_cryoID()
    ui.setupUi(cryoID)
    cryoID.show()
    sys.exit(app.exec_())
