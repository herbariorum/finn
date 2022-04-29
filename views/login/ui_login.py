# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginbkpgaTuux.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(350, 500)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frmTop")
        self.frame.setMaximumSize(QSize(16777215, 40))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.lblTitleLogin = QLabel(self.frame)
        self.lblTitleLogin.setObjectName(u"lblTitleLogin")
        self.lblTitleLogin.setMinimumSize(QSize(300, 0))
        self.lblTitleLogin.setMaximumSize(QSize(300, 16777215))
        self.lblTitleLogin.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lblTitleLogin)

        self.btnTitleExit = QPushButton(self.frame)
        self.btnTitleExit.setObjectName(u"btnTitleExit")
        
        self.btnTitleExit.setLayoutDirection(Qt.LeftToRight)
        self.btnTitleExit.setFlat(True)

        self.horizontalLayout.addWidget(self.btnTitleExit, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 50, 0, 0)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"lblLogo")
        self.label.setMaximumSize(QSize(16777215, 130))
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, -1, 0)
        self.txtUsuario = QLineEdit(self.frame_3)
        self.txtUsuario.setObjectName(u"txtUsuario")
        self.txtUsuario.setMinimumSize(QSize(250, 0))
        self.txtUsuario.setMaximumSize(QSize(250, 16777215))
        self.txtUsuario.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.txtUsuario, 0, Qt.AlignHCenter)

        self.txtPassword = QLineEdit(self.frame_3)
        self.txtPassword.setObjectName(u"txtPassword")
        self.txtPassword.setMinimumSize(QSize(250, 0))
        self.txtPassword.setMaximumSize(QSize(250, 16777215))
        self.txtPassword.setEchoMode(QLineEdit.Password)
        self.txtPassword.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.txtPassword, 0, Qt.AlignHCenter)

        self.btnVerificar = QPushButton(self.frame_3)
        self.btnVerificar.setObjectName(u"btnVerificar")
        self.btnVerificar.setMinimumSize(QSize(100, 0))
        self.btnVerificar.setMaximumSize(QSize(100, 16777215))

        self.verticalLayout_3.addWidget(self.btnVerificar, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lblTitleLogin.setText(QCoreApplication.translate("Form", u"Login", None))
        self.btnTitleExit.setText(QCoreApplication.translate("Form", u"X", None))
        self.label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.txtUsuario.setPlaceholderText(QCoreApplication.translate("Form", u"Email", None))
        self.txtPassword.setPlaceholderText(QCoreApplication.translate("Form", u"Password", None))
        self.btnVerificar.setText(QCoreApplication.translate("Form", u"Verificar", None))
    # retranslateUi

