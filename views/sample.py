# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerxhTtoJ.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QPushButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(515, 284)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.loginBtn = QPushButton(Form)
        self.loginBtn.setObjectName(u"loginBtn")

        self.horizontalLayout.addWidget(self.loginBtn)

        self.btnCancela = QPushButton(Form)
        self.btnCancela.setObjectName(u"btnCancela")

        self.horizontalLayout.addWidget(self.btnCancela)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.loginBtn.setText(QCoreApplication.translate("Form", u"Login", None))
        self.btnCancela.setText(QCoreApplication.translate("Form", u"Cancela", None))
    # retranslateUi

