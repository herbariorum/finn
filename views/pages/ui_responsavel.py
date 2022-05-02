# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'responsavelWwkolS.ui'
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

class Ui_formResponsavel(object):
    def setupUi(self, formResponsavel):
        if not formResponsavel.objectName():
            formResponsavel.setObjectName(u"formResponsavel")
        formResponsavel.resize(751, 543)
        self.verticalLayout = QVBoxLayout(formResponsavel)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frmTop = QFrame(formResponsavel)
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

        self.frmTabela = QFrame(formResponsavel)
        self.frmTabela.setObjectName(u"frmTabela")
        self.frmTabela.setFrameShape(QFrame.StyledPanel)
        self.frmTabela.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frmTabela)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tblListagem = QTableView(self.frmTabela)
        self.tblListagem.setObjectName(u"tblListagem")
        

        self.verticalLayout_2.addWidget(self.tblListagem)


        self.verticalLayout.addWidget(self.frmTabela)

        self.frmButton = QFrame(formResponsavel)
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


        self.retranslateUi(formResponsavel)

        QMetaObject.connectSlotsByName(formResponsavel)
    # setupUi

    def retranslateUi(self, formResponsavel):
        formResponsavel.setWindowTitle(QCoreApplication.translate("formResponsavel", u"Form", None))
        self.label.setText(QCoreApplication.translate("formResponsavel", u"Localizar", None))
        self.btnNovo.setText(QCoreApplication.translate("formResponsavel", u"Insere Novo", None))
        self.btnDelete.setText(QCoreApplication.translate("formResponsavel", u"Apaga", None))
        self.btnSelecao.setText(QCoreApplication.translate("formResponsavel", u"Imprime sele\u00e7\u00e3o", None))
        self.btnListagem.setText(QCoreApplication.translate("formResponsavel", u"Imprime listagem", None))
    # retranslateUi

