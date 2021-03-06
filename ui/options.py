# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'options.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_OptionsGroup(object):
    def setupUi(self, OptionsGroup):
        OptionsGroup.setObjectName(_fromUtf8("OptionsGroup"))
        OptionsGroup.resize(752, 602)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(OptionsGroup.sizePolicy().hasHeightForWidth())
        OptionsGroup.setSizePolicy(sizePolicy)
        self.gridLayout = QtGui.QGridLayout(OptionsGroup)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.chkApplyStyles = QtGui.QCheckBox(OptionsGroup)
        self.chkApplyStyles.setChecked(True)
        self.chkApplyStyles.setObjectName(_fromUtf8("chkApplyStyles"))
        self.gridLayout.addWidget(self.chkApplyStyles, 10, 0, 1, 2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.rbZoomManual = QtGui.QRadioButton(OptionsGroup)
        self.rbZoomManual.setText(_fromUtf8(""))
        self.rbZoomManual.setObjectName(_fromUtf8("rbZoomManual"))
        self.horizontalLayout.addWidget(self.rbZoomManual)
        self.zoomSpin = QtGui.QSpinBox(OptionsGroup)
        self.zoomSpin.setEnabled(False)
        self.zoomSpin.setMaximumSize(QtCore.QSize(70, 16777215))
        self.zoomSpin.setObjectName(_fromUtf8("zoomSpin"))
        self.horizontalLayout.addWidget(self.zoomSpin, QtCore.Qt.AlignLeft)
        self.lblZoomRange = QtGui.QLabel(OptionsGroup)
        self.lblZoomRange.setObjectName(_fromUtf8("lblZoomRange"))
        self.horizontalLayout.addWidget(self.lblZoomRange)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout, 7, 1, 1, 1)
        self.label_5 = QtGui.QLabel(OptionsGroup)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.chkClipTiles = QtGui.QCheckBox(OptionsGroup)
        self.chkClipTiles.setObjectName(_fromUtf8("chkClipTiles"))
        self.gridLayout.addWidget(self.chkClipTiles, 3, 0, 1, 2)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.btnResetToInspectionDefaults = QtGui.QPushButton(OptionsGroup)
        self.btnResetToInspectionDefaults.setObjectName(_fromUtf8("btnResetToInspectionDefaults"))
        self.gridLayout_2.addWidget(self.btnResetToInspectionDefaults, 2, 3, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 2, 0, 1, 1)
        self.btnResetToAnalysisDefaults = QtGui.QPushButton(OptionsGroup)
        self.btnResetToAnalysisDefaults.setObjectName(_fromUtf8("btnResetToAnalysisDefaults"))
        self.gridLayout_2.addWidget(self.btnResetToAnalysisDefaults, 1, 3, 1, 1)
        self.btnResetToBasemapDefaults = QtGui.QPushButton(OptionsGroup)
        self.btnResetToBasemapDefaults.setObjectName(_fromUtf8("btnResetToBasemapDefaults"))
        self.gridLayout_2.addWidget(self.btnResetToBasemapDefaults, 0, 3, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 11, 0, 1, 2)
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setHorizontalSpacing(6)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem2, 1, 3, 1, 1)
        self.chkLimitNrOfTiles = QtGui.QCheckBox(OptionsGroup)
        self.chkLimitNrOfTiles.setChecked(True)
        self.chkLimitNrOfTiles.setObjectName(_fromUtf8("chkLimitNrOfTiles"))
        self.gridLayout_5.addWidget(self.chkLimitNrOfTiles, 1, 0, 1, 1)
        self.spinNrOfLoadedTiles = QtGui.QSpinBox(OptionsGroup)
        self.spinNrOfLoadedTiles.setEnabled(True)
        self.spinNrOfLoadedTiles.setMinimumSize(QtCore.QSize(0, 21))
        self.spinNrOfLoadedTiles.setMinimum(1)
        self.spinNrOfLoadedTiles.setMaximum(9999)
        self.spinNrOfLoadedTiles.setProperty("value", 20)
        self.spinNrOfLoadedTiles.setObjectName(_fromUtf8("spinNrOfLoadedTiles"))
        self.gridLayout_5.addWidget(self.spinNrOfLoadedTiles, 1, 1, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblNumberTilesInCurrentExtent = QtGui.QLabel(OptionsGroup)
        self.lblNumberTilesInCurrentExtent.setObjectName(_fromUtf8("lblNumberTilesInCurrentExtent"))
        self.gridLayout_5.addWidget(self.lblNumberTilesInCurrentExtent, 1, 2, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_5, 1, 0, 1, 2)
        spacerItem3 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem3, 9, 0, 1, 1)
        self.chkMergeTiles = QtGui.QCheckBox(OptionsGroup)
        self.chkMergeTiles.setChecked(False)
        self.chkMergeTiles.setObjectName(_fromUtf8("chkMergeTiles"))
        self.gridLayout.addWidget(self.chkMergeTiles, 2, 0, 1, 2)
        self.rbAutoZoom = QtGui.QRadioButton(OptionsGroup)
        self.rbAutoZoom.setChecked(True)
        self.rbAutoZoom.setObjectName(_fromUtf8("rbAutoZoom"))
        self.gridLayout.addWidget(self.rbAutoZoom, 5, 1, 1, 1)
        self.rbZoomMax = QtGui.QRadioButton(OptionsGroup)
        self.rbZoomMax.setChecked(False)
        self.rbZoomMax.setObjectName(_fromUtf8("rbZoomMax"))
        self.gridLayout.addWidget(self.rbZoomMax, 6, 1, 1, 1)

        self.retranslateUi(OptionsGroup)
        QtCore.QMetaObject.connectSlotsByName(OptionsGroup)

    def retranslateUi(self, OptionsGroup):
        OptionsGroup.setWindowTitle(_translate("OptionsGroup", "Options", None))
        OptionsGroup.setTitle(_translate("OptionsGroup", "Options", None))
        self.chkApplyStyles.setToolTip(_translate("OptionsGroup", "Apply a build-in, predefined QGIS style made for OpenMapTiles (instead of random QGIS default style)", None))
        self.chkApplyStyles.setText(_translate("OptionsGroup", "Apply predefined OpenMapTiles style", None))
        self.lblZoomRange.setText(_translate("OptionsGroup", "TextLabel", None))
        self.label_5.setText(_translate("OptionsGroup", "Zoom", None))
        self.chkClipTiles.setText(_translate("OptionsGroup", "Clip each tile at bounds", None))
        self.btnResetToInspectionDefaults.setText(_translate("OptionsGroup", "Inspection Defaults", None))
        self.btnResetToAnalysisDefaults.setText(_translate("OptionsGroup", "Analysis Defaults", None))
        self.btnResetToBasemapDefaults.setText(_translate("OptionsGroup", "Base Map Defaults", None))
        self.chkLimitNrOfTiles.setToolTip(_translate("OptionsGroup", "<html><head/><body><p>If this option is enabled, only the specified number of tiles will be loaded from the selected source. </p><p>Cached tiles are not affected by this limit. Therefore, there may be more tiles visible when loading is complete.</p></body></html>", None))
        self.chkLimitNrOfTiles.setText(_translate("OptionsGroup", "Loaded tile limit", None))
        self.lblNumberTilesInCurrentExtent.setText(_translate("OptionsGroup", "(Current extent: n tiles)", None))
        self.chkMergeTiles.setText(_translate("OptionsGroup", "Merge Tiles (slow)", None))
        self.rbAutoZoom.setText(_translate("OptionsGroup", "Auto (scale based)", None))
        self.rbZoomMax.setText(_translate("OptionsGroup", "Max. Zoom", None))

