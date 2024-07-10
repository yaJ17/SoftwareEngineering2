# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_loginMeaDKq.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(307, 378)
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(255, 251, 247, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(127, 125, 123, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush3)
        brush4 = QBrush(QColor(170, 167, 165, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        brush5 = QBrush(QColor(213, 213, 213, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        Login.setPalette(palette)
        self.centralwidget = QWidget(Login)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(77, 30, 161, 111))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 162, 61, 20))
        self.username_login = QLineEdit(self.centralwidget)
        self.username_login.setObjectName(u"username_login")
        self.username_login.setGeometry(QRect(129, 160, 121, 21))
        self.password_login = QLineEdit(self.centralwidget)
        self.password_login.setObjectName(u"password_login")
        self.password_login.setGeometry(QRect(130, 192, 121, 21))
        self.password_login.setEchoMode(QLineEdit.EchoMode.Password)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(58, 194, 51, 16))
        self.forgot_pass_button = QPushButton(self.centralwidget)
        self.forgot_pass_button.setObjectName(u"forgot_pass_button")
        self.forgot_pass_button.setGeometry(QRect(140, 270, 111, 24))
        self.login_exit_button = QPushButton(self.centralwidget)
        self.login_exit_button.setObjectName(u"login_exit_button")
        self.login_exit_button.setGeometry(QRect(140, 300, 111, 24))
        self.login_button = QPushButton(self.centralwidget)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setGeometry(QRect(140, 240, 111, 24))
        self.restore_button_login = QPushButton(self.centralwidget)
        self.restore_button_login.setObjectName(u"restore_button_login")
        self.restore_button_login.setGeometry(QRect(140, 330, 111, 24))
        Login.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Login)
        self.statusbar.setObjectName(u"statusbar")
        Login.setStatusBar(self.statusbar)

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Rexie Login", None))
        self.label.setText(QCoreApplication.translate("Login", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Rexie Maris <br/>Bag Enterprise</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Login", u"<html><head/><body><p align=\"right\">Username</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Login", u"<html><head/><body><p align=\"right\">Password</p></body></html>", None))
        self.forgot_pass_button.setText(QCoreApplication.translate("Login", u"Forgot Password", None))
        self.login_exit_button.setText(QCoreApplication.translate("Login", u"Exit", None))
        self.login_button.setText(QCoreApplication.translate("Login", u"Login", None))
        self.restore_button_login.setText(QCoreApplication.translate("Login", u"Recovery", None))
    # retranslateUi

