# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'alunoFVvrbM.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTableView, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(807, 576)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frmTop = QFrame(Form)
        self.frmTop.setObjectName(u"frmTop")
        self.frmTop.setMaximumSize(QSize(16777215, 50))
        self.frmTop.setFrameShape(QFrame.StyledPanel)
        self.frmTop.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frmTop)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frmTop)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.txtLocalizar = QLineEdit(self.frmTop)
        self.txtLocalizar.setObjectName(u"txtLocalizar")

        self.horizontalLayout_2.addWidget(self.txtLocalizar)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.frmTop)

        self.tblListagem = QTableView(Form)
        self.tblListagem.setObjectName(u"tblListagem")

        self.verticalLayout.addWidget(self.tblListagem)

        self.frmButton = QFrame(Form)
        self.frmButton.setObjectName(u"frmButton")
        self.frmButton.setMaximumSize(QSize(16777215, 50))
        self.frmButton.setFrameShape(QFrame.StyledPanel)
        self.frmButton.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frmButton)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.btnNovo = QPushButton(self.frmButton)
        self.btnNovo.setObjectName(u"btnNovo")

        self.horizontalLayout.addWidget(self.btnNovo)

        self.btnEdit = QPushButton(self.frmButton)
        self.btnEdit.setObjectName(u"btnEdit")

        self.horizontalLayout.addWidget(self.btnEdit)

        self.btnDelete = QPushButton(self.frmButton)
        self.btnDelete.setObjectName(u"btnDelete")

        self.horizontalLayout.addWidget(self.btnDelete)

        self.btnSelecao = QPushButton(self.frmButton)
        self.btnSelecao.setObjectName(u"btnSelecao")

        self.horizontalLayout.addWidget(self.btnSelecao)

        self.btnListagem = QPushButton(self.frmButton)
        self.btnListagem.setObjectName(u"btnListagem")

        self.horizontalLayout.addWidget(self.btnListagem)


        self.verticalLayout.addWidget(self.frmButton)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Localizar", None))
        self.btnNovo.setText(QCoreApplication.translate("Form", u"Insere Novo", None))
        self.btnEdit.setText(QCoreApplication.translate("formResponsavel", u"Edita", None))
        self.btnDelete.setText(QCoreApplication.translate("Form", u"Apaga", None))
        self.btnSelecao.setText(QCoreApplication.translate("Form", u"Imprime sele\u00e7\u00e3o", None))
        self.btnListagem.setText(QCoreApplication.translate("Form", u"Imprime listagem", None))
    # retranslateUi

