
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
        Login.setWindowTitle(QCoreApplication.translate("Login", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("Login", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Rexie Maris <br/>Bag Enterprise</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Login", u"<html><head/><body><p align=\"right\">Username</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Login", u"<html><head/><body><p align=\"right\">Password</p></body></html>", None))
        self.forgot_pass_button.setText(QCoreApplication.translate("Login", u"Forgot Password", None))
        self.login_exit_button.setText(QCoreApplication.translate("Login", u"Exit", None))
        self.login_button.setText(QCoreApplication.translate("Login", u"Login", None))
        self.restore_button_login.setText(QCoreApplication.translate("Login", u"Restore", None))
    # retranslateUi

