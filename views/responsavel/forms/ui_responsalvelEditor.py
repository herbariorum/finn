# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'responsalvelEditorduJSyP.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QComboBox,
    QDialog, QDialogButtonBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(634, 355)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(70, 70))
        self.frame_6.setMaximumSize(QSize(70, 70))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.lblFoto = QLabel(self.frame_6)
        self.lblFoto.setObjectName(u"lblFoto")
        self.lblFoto.setGeometry(QRect(2, 2, 64, 64))
        self.lblFoto.setMinimumSize(QSize(64, 64))

        self.horizontalLayout.addWidget(self.frame_6)

        self.frame_2 = QFrame(self.frame_5)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 70))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(20)
        self.lblID = QLabel(self.frame_2)
        self.lblID.setObjectName(u"lblID")

        self.gridLayout.addWidget(self.lblID, 1, 0, 1, 1)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)

        self.txtCPF = QLineEdit(self.frame_2)
        self.txtCPF.setObjectName(u"txtCPF")
        self.txtCPF.setMaximumSize(QSize(150, 16777215))

        self.gridLayout.addWidget(self.txtCPF, 1, 2, 1, 1)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.txtNome = QLineEdit(self.frame_2)
        self.txtNome.setObjectName(u"txtNome")
        self.txtNome.setMaximumSize(QSize(300, 16777215))

        self.gridLayout.addWidget(self.txtNome, 1, 1, 1, 1)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)


        self.horizontalLayout.addWidget(self.frame_2)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 70))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)

        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 0, 1, 1, 1)

        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 0, 2, 1, 1)

        self.cbxTipoResponsavel = QComboBox(self.frame_3)
        self.cbxTipoResponsavel.addItem("")
        self.cbxTipoResponsavel.addItem("")
        self.cbxTipoResponsavel.addItem("")
        self.cbxTipoResponsavel.addItem("")
        self.cbxTipoResponsavel.addItem("")
        self.cbxTipoResponsavel.addItem("")
        self.cbxTipoResponsavel.addItem("")
        self.cbxTipoResponsavel.setObjectName(u"cbxTipoResponsavel")

        self.gridLayout_2.addWidget(self.cbxTipoResponsavel, 1, 0, 1, 1)

        self.cbxSexo = QComboBox(self.frame_3)
        self.cbxSexo.addItem("")
        self.cbxSexo.addItem("")
        self.cbxSexo.setObjectName(u"cbxSexo")

        self.gridLayout_2.addWidget(self.cbxSexo, 1, 1, 1, 1)

        self.txtEmail = QLineEdit(self.frame_3)
        self.txtEmail.setObjectName(u"txtEmail")

        self.gridLayout_2.addWidget(self.txtEmail, 1, 2, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 0))
        self.frame_4.setMaximumSize(QSize(16777215, 150))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_7 = QLabel(self.frame_4)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 0, 0, 1, 1)

        self.label_8 = QLabel(self.frame_4)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_3.addWidget(self.label_8, 0, 1, 1, 1)

        self.txtProfissao = QLineEdit(self.frame_4)
        self.txtProfissao.setObjectName(u"txtProfissao")

        self.gridLayout_3.addWidget(self.txtProfissao, 1, 0, 1, 1)

        self.chbAtivo = QCheckBox(self.frame_4)
        self.chbAtivo.setObjectName(u"chbAtivo")

        self.gridLayout_3.addWidget(self.chbAtivo, 1, 1, 1, 2)

        self.label_9 = QLabel(self.frame_4)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_3.addWidget(self.label_9, 2, 0, 1, 1)

        self.txtEndereco = QLineEdit(self.frame_4)
        self.txtEndereco.setObjectName(u"txtEndereco")

        self.gridLayout_3.addWidget(self.txtEndereco, 3, 0, 1, 2)

        self.label_10 = QLabel(self.frame_4)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_3.addWidget(self.label_10, 4, 0, 1, 1)

        self.txtContato = QLineEdit(self.frame_4)
        self.txtContato.setObjectName(u"txtContato")

        self.gridLayout_3.addWidget(self.txtContato, 5, 0, 1, 3)


        self.verticalLayout_2.addWidget(self.frame_4)


        self.verticalLayout.addWidget(self.frame)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        # self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lblFoto.setText("")
        self.lblID.setText("")
        self.label_3.setText(QCoreApplication.translate("Dialog", u"CPF", None))
#if QT_CONFIG(tooltip)
        self.txtCPF.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Forne\u00e7a apenas n\u00fameros.</p><p>Ex. 69639339399</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("Dialog", u"ID", None))
#if QT_CONFIG(tooltip)
        self.txtNome.setToolTip(QCoreApplication.translate("Dialog", u"Nome do respons\u00e1vel pelo aluno", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("Dialog", u"NOME", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Sexo", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Email", None))
        self.cbxTipoResponsavel.setItemText(0, QCoreApplication.translate("Dialog", u"PAI", None))
        self.cbxTipoResponsavel.setItemText(1, QCoreApplication.translate("Dialog", u"M\u00c3E", None))
        self.cbxTipoResponsavel.setItemText(2, QCoreApplication.translate("Dialog", u"AV\u00d4", None))
        self.cbxTipoResponsavel.setItemText(3, QCoreApplication.translate("Dialog", u"AV\u00d3", None))
        self.cbxTipoResponsavel.setItemText(4, QCoreApplication.translate("Dialog", u"PADRASTRO", None))
        self.cbxTipoResponsavel.setItemText(5, QCoreApplication.translate("Dialog", u"MADASTRA", None))
        self.cbxTipoResponsavel.setItemText(6, QCoreApplication.translate("Dialog", u"OUTROS", None))

        self.cbxSexo.setItemText(0, QCoreApplication.translate("Dialog", u"Masculino", None))
        self.cbxSexo.setItemText(1, QCoreApplication.translate("Dialog", u"Feminino", None))

        self.label_7.setText(QCoreApplication.translate("Dialog", u"Profiss\u00e3o", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Status", None))
#if QT_CONFIG(tooltip)
        self.txtProfissao.setToolTip(QCoreApplication.translate("Dialog", u"Preencha a profiss\u00e3o atual do respons\u00e1vel", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.chbAtivo.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:700;\">Ativo</span> - caso o respons\u00e1vel esteja com aluno(s) matriculado</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.chbAtivo.setText(QCoreApplication.translate("Dialog", u"Ativo", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Endere\u00e7o(s)", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"Contato(s)", None))
        # self.lblEndereco.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        # self.lblContato.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
    # retranslateUi

