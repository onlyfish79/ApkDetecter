# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'apkinfo_ui.ui'
#
# Created: Tue Jan 20 11:25:39 2015
#      by: PyQt4 UI code generator 4.11.3
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

class Ui_ApkInfo(object):
    def setupUi(self, ApkInfo):
        ApkInfo.setObjectName(_fromUtf8("ApkInfo"))
        ApkInfo.setWindowModality(QtCore.Qt.WindowModal)
        ApkInfo.setEnabled(True)
        ApkInfo.resize(621, 330)
        ApkInfo.setMinimumSize(QtCore.QSize(621, 330))
        ApkInfo.setMaximumSize(QtCore.QSize(621, 330))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("C:/Users/Andy/Desktop/20150117051304968_easyicon_net_512.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ApkInfo.setWindowIcon(icon)
        self.groupBox = QtGui.QGroupBox(ApkInfo)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 601, 311))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Aharoni"))
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.file_size = QtGui.QLabel(self.groupBox)
        self.file_size.setGeometry(QtCore.QRect(10, 27, 54, 12))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.file_size.setFont(font)
        self.file_size.setObjectName(_fromUtf8("file_size"))
        self.package_name = QtGui.QLabel(self.groupBox)
        self.package_name.setGeometry(QtCore.QRect(10, 63, 54, 12))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.package_name.setFont(font)
        self.package_name.setObjectName(_fromUtf8("package_name"))
        self.version = QtGui.QLabel(self.groupBox)
        self.version.setGeometry(QtCore.QRect(312, 28, 54, 12))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.version.setFont(font)
        self.version.setObjectName(_fromUtf8("version"))
        self.version_num = QtGui.QLabel(self.groupBox)
        self.version_num.setGeometry(QtCore.QRect(311, 64, 54, 12))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.version_num.setFont(font)
        self.version_num.setObjectName(_fromUtf8("version_num"))
        self.version_need = QtGui.QLabel(self.groupBox)
        self.version_need.setGeometry(QtCore.QRect(10, 101, 54, 12))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.version_need.setFont(font)
        self.version_need.setObjectName(_fromUtf8("version_need"))
        self.serial_num = QtGui.QLabel(self.groupBox)
        self.serial_num.setGeometry(QtCore.QRect(312, 100, 54, 12))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.serial_num.setFont(font)
        self.serial_num.setObjectName(_fromUtf8("serial_num"))
        self.publisher = QtGui.QLabel(self.groupBox)
        self.publisher.setGeometry(QtCore.QRect(10, 227, 54, 12))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.publisher.setFont(font)
        self.publisher.setObjectName(_fromUtf8("publisher"))
        self.issuer = QtGui.QLabel(self.groupBox)
        self.issuer.setGeometry(QtCore.QRect(10, 274, 54, 12))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.issuer.setFont(font)
        self.issuer.setObjectName(_fromUtf8("issuer"))
        self.apkmd5 = QtGui.QLabel(self.groupBox)
        self.apkmd5.setGeometry(QtCore.QRect(11, 143, 54, 12))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.apkmd5.setFont(font)
        self.apkmd5.setObjectName(_fromUtf8("apkmd5"))
        self.dexmd5 = QtGui.QLabel(self.groupBox)
        self.dexmd5.setGeometry(QtCore.QRect(10, 181, 54, 12))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        self.dexmd5.setFont(font)
        self.dexmd5.setObjectName(_fromUtf8("dexmd5"))
        self.edt_file = QtGui.QTextEdit(self.groupBox)
        self.edt_file.setEnabled(False)
        self.edt_file.setGeometry(QtCore.QRect(70, 18, 231, 28))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        font.setPointSize(10)
        self.edt_file.setFont(font)
        self.edt_file.setFrameShape(QtGui.QFrame.Box)
        self.edt_file.setObjectName(_fromUtf8("edt_file"))
        self.edt_package = QtGui.QTextEdit(self.groupBox)
        self.edt_package.setEnabled(False)
        self.edt_package.setGeometry(QtCore.QRect(70, 54, 231, 28))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        font.setPointSize(10)
        self.edt_package.setFont(font)
        self.edt_package.setFrameShape(QtGui.QFrame.Panel)
        self.edt_package.setObjectName(_fromUtf8("edt_package"))
        self.edt_version_need = QtGui.QTextEdit(self.groupBox)
        self.edt_version_need.setEnabled(False)
        self.edt_version_need.setGeometry(QtCore.QRect(70, 91, 231, 28))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        font.setPointSize(10)
        self.edt_version_need.setFont(font)
        self.edt_version_need.setFrameShape(QtGui.QFrame.Panel)
        self.edt_version_need.setObjectName(_fromUtf8("edt_version_need"))
        self.edt_version = QtGui.QTextEdit(self.groupBox)
        self.edt_version.setEnabled(False)
        self.edt_version.setGeometry(QtCore.QRect(360, 19, 231, 28))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        font.setPointSize(10)
        self.edt_version.setFont(font)
        self.edt_version.setFrameShape(QtGui.QFrame.Box)
        self.edt_version.setObjectName(_fromUtf8("edt_version"))
        self.edt_version_num = QtGui.QTextEdit(self.groupBox)
        self.edt_version_num.setEnabled(False)
        self.edt_version_num.setGeometry(QtCore.QRect(360, 55, 231, 28))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        font.setPointSize(10)
        self.edt_version_num.setFont(font)
        self.edt_version_num.setFrameShape(QtGui.QFrame.Panel)
        self.edt_version_num.setObjectName(_fromUtf8("edt_version_num"))
        self.edt_serial_num = QtGui.QTextEdit(self.groupBox)
        self.edt_serial_num.setEnabled(False)
        self.edt_serial_num.setGeometry(QtCore.QRect(360, 92, 231, 28))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        font.setPointSize(10)
        self.edt_serial_num.setFont(font)
        self.edt_serial_num.setFrameShape(QtGui.QFrame.Panel)
        self.edt_serial_num.setObjectName(_fromUtf8("edt_serial_num"))
        self.edt_apkmd5 = QtGui.QTextEdit(self.groupBox)
        self.edt_apkmd5.setEnabled(False)
        self.edt_apkmd5.setGeometry(QtCore.QRect(70, 132, 521, 28))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        font.setPointSize(10)
        self.edt_apkmd5.setFont(font)
        self.edt_apkmd5.setFrameShape(QtGui.QFrame.Panel)
        self.edt_apkmd5.setObjectName(_fromUtf8("edt_apkmd5"))
        self.edt_dexmd5 = QtGui.QTextEdit(self.groupBox)
        self.edt_dexmd5.setEnabled(False)
        self.edt_dexmd5.setGeometry(QtCore.QRect(70, 170, 521, 28))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        font.setPointSize(10)
        self.edt_dexmd5.setFont(font)
        self.edt_dexmd5.setFrameShape(QtGui.QFrame.Panel)
        self.edt_dexmd5.setObjectName(_fromUtf8("edt_dexmd5"))
        self.edt_publisher = QtGui.QTextEdit(self.groupBox)
        self.edt_publisher.setEnabled(False)
        self.edt_publisher.setGeometry(QtCore.QRect(70, 210, 521, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        font.setPointSize(10)
        self.edt_publisher.setFont(font)
        self.edt_publisher.setFrameShape(QtGui.QFrame.Panel)
        self.edt_publisher.setObjectName(_fromUtf8("edt_publisher"))
        self.edt_issuer = QtGui.QTextEdit(self.groupBox)
        self.edt_issuer.setEnabled(False)
        self.edt_issuer.setGeometry(QtCore.QRect(70, 260, 521, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        font.setPointSize(10)
        self.edt_issuer.setFont(font)
        self.edt_issuer.setFrameShape(QtGui.QFrame.Panel)
        self.edt_issuer.setObjectName(_fromUtf8("edt_issuer"))

        self.retranslateUi(ApkInfo)
        QtCore.QMetaObject.connectSlotsByName(ApkInfo)

    def retranslateUi(self, ApkInfo):
        ApkInfo.setWindowTitle(_translate("ApkInfo", "ApkInformation", None))
        self.groupBox.setTitle(_translate("ApkInfo", "文件信息", None))
        self.file_size.setText(_translate("ApkInfo", "文件大小", None))
        self.package_name.setText(_translate("ApkInfo", "文件包名", None))
        self.version.setText(_translate("ApkInfo", "版   本", None))
        self.version_num.setText(_translate("ApkInfo", "版本号", None))
        self.version_need.setText(_translate("ApkInfo", "系统要求", None))
        self.serial_num.setText(_translate("ApkInfo", "序列号", None))
        self.publisher.setText(_translate("ApkInfo", "发 行 者", None))
        self.issuer.setText(_translate("ApkInfo", "签 发 人", None))
        self.apkmd5.setText(_translate("ApkInfo", "APKMD5", None))
        self.dexmd5.setText(_translate("ApkInfo", "DEXMD5", None))

