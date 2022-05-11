# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'responsavelViewXnOmLx.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(700, 425)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_4 = QFrame(Dialog)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.infoFoto = QFrame(self.frame_4)
        self.infoFoto.setObjectName(u"infoFoto")
        self.infoFoto.setMaximumSize(QSize(68, 68))
        self.infoFoto.setFrameShape(QFrame.StyledPanel)
        self.infoFoto.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.infoFoto)

        self.frame = QFrame(self.frame_4)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.infoSexo = QLabel(self.frame)
        self.infoSexo.setObjectName(u"infoSexo")

        self.gridLayout.addWidget(self.infoSexo, 1, 2, 1, 1)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 2, 2, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.infoResponsavel = QLabel(self.frame)
        self.infoResponsavel.setObjectName(u"infoResponsavel")

        self.gridLayout.addWidget(self.infoResponsavel, 3, 2, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.infoProfissao = QLabel(self.frame)
        self.infoProfissao.setObjectName(u"infoProfissao")

        self.gridLayout.addWidget(self.infoProfissao, 3, 1, 1, 1)

        self.infoNome = QLabel(self.frame)
        self.infoNome.setObjectName(u"infoNome")

        self.gridLayout.addWidget(self.infoNome, 1, 0, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.infoCPF = QLabel(self.frame)
        self.infoCPF.setObjectName(u"infoCPF")

        self.gridLayout.addWidget(self.infoCPF, 1, 1, 1, 1)

        self.infoEmail = QLabel(self.frame)
        self.infoEmail.setObjectName(u"infoEmail")

        self.gridLayout.addWidget(self.infoEmail, 3, 0, 1, 1)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 2, 1, 1, 1)


        self.horizontalLayout_2.addWidget(self.frame)


        self.verticalLayout.addWidget(self.frame_4)

        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 140))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_2.addWidget(self.label_7)

        self.infoEndereco = QLabel(self.frame_2)
        self.infoEndereco.setObjectName(u"infoEndereco")

        self.verticalLayout_2.addWidget(self.infoEndereco)

        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_2.addWidget(self.label_9)

        self.infoContato = QLabel(self.frame_2)
        self.infoContato.setObjectName(u"infoContato")

        self.verticalLayout_2.addWidget(self.infoContato)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(Dialog)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 50))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(70, 16777215))
        self.pushButton.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout.addWidget(self.frame_3)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.infoSexo.setText(QCoreApplication.translate("Dialog", u"infosexo", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Tipo de Responsabilidade", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Sexo", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Email", None))
        self.infoResponsavel.setText(QCoreApplication.translate("Dialog", u"inforesponsavel", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"CPF", None))
        self.infoProfissao.setText(QCoreApplication.translate("Dialog", u"infoprofissao", None))
        self.infoNome.setText(QCoreApplication.translate("Dialog", u"infonome", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Nome", None))
        self.infoCPF.setText(QCoreApplication.translate("Dialog", u"infocpf", None))
        self.infoEmail.setText(QCoreApplication.translate("Dialog", u"infoemail", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Profiss\u00e3o", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Endere\u00e7o", None))
        self.infoEndereco.setText(QCoreApplication.translate("Dialog", u"infoendereco", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Contato", None))
        self.infoContato.setText(QCoreApplication.translate("Dialog", u"infocontato", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Ok", None))
    # retranslateUi

