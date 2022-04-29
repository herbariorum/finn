# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashobardoldfGZ.ui'
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
    QListView, QMainWindow, QSizePolicy, QStackedWidget,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(250, 0))
        self.frame.setMaximumSize(QSize(250, 16777215))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frmTopLeft = QFrame(self.frame)
        self.frmTopLeft.setObjectName(u"frmTopLeft")
        self.frmTopLeft.setMinimumSize(QSize(0, 50))
        self.frmTopLeft.setFrameShape(QFrame.StyledPanel)
        self.frmTopLeft.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frmTopLeft)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 0, 0, 0)
        self.lblIconLogo = QLabel(self.frmTopLeft)
        self.lblIconLogo.setObjectName(u"lblIconLogo")
        self.lblIconLogo.setMinimumSize(QSize(32, 0))
        self.lblIconLogo.setMaximumSize(QSize(32, 16777215))

        self.horizontalLayout_2.addWidget(self.lblIconLogo)


        self.lblTextLogo = QLabel(self.frmTopLeft)
        self.lblTextLogo.setObjectName(u"lblTextLogo")
        self.lblTextLogo.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lblTextLogo)


        self.verticalLayout.addWidget(self.frmTopLeft)

        self.listView = QListView(self.frame)
        self.listView.setObjectName(u"listView")
        self.listView.setFrameShape(QFrame.NoFrame)

        self.verticalLayout.addWidget(self.listView)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frmTopRight = QFrame(self.frame_2)
        self.frmTopRight.setObjectName(u"frmTopRight")
        self.frmTopRight.setMinimumSize(QSize(0, 50))
        self.frmTopRight.setFrameShape(QFrame.NoFrame)
        self.frmTopRight.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3 = QHBoxLayout(self.frmTopRight)
        self.lblTopIcon = QLabel(self.frmTopRight)
        self.lblTopIcon.setObjectName(u"topicon")

        self.horizontalLayout_3.addWidget(self.lblTopIcon)
        
        self.lblTopTitle = QLabel(self.frmTopRight)
        self.lblTopTitle.setObjectName(u"lblTopTitle")

        self.horizontalLayout_3.addWidget(self.lblTopTitle)

        self.verticalLayout_2.addWidget(self.frmTopRight)

        self.pages = QStackedWidget(self.frame_2)
        self.pages.setObjectName(u"pages")

        self.verticalLayout_2.addWidget(self.pages)


        self.horizontalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lblIconLogo.setText("")
        self.lblTextLogo.setText(QCoreApplication.translate("MainWindow", u"FINNANCE V.01", None))
        self.lblTopTitle.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

