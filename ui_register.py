
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(307, 378)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.password_register = QLineEdit(self.centralwidget)
        self.password_register.setObjectName(u"password_register")
        self.password_register.setGeometry(QRect(151, 132, 121, 21))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(67, 32, 161, 51))
        self.submit_register = QPushButton(self.centralwidget)
        self.submit_register.setObjectName(u"submit_register")
        self.submit_register.setGeometry(QRect(160, 290, 111, 24))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(71, 102, 61, 20))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(79, 134, 51, 16))
        self.username_register = QLineEdit(self.centralwidget)
        self.username_register.setObjectName(u"username_register")
        self.username_register.setGeometry(QRect(150, 100, 121, 21))
        self.confirm_password = QLineEdit(self.centralwidget)
        self.confirm_password.setObjectName(u"confirm_password")
        self.confirm_password.setGeometry(QRect(151, 165, 121, 21))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(19, 165, 111, 20))
        self.special_question = QComboBox(self.centralwidget)
        self.special_question.addItem("")
        self.special_question.addItem("")
        self.special_question.addItem("")
        self.special_question.addItem("")
        self.special_question.addItem("")
        self.special_question.addItem("")
        self.special_question.addItem("")
        self.special_question.addItem("")
        self.special_question.addItem("")
        self.special_question.setObjectName(u"special_question")
        self.special_question.setGeometry(QRect(150, 197, 121, 22))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 199, 111, 20))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 227, 111, 41))
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(150, 232, 121, 31))
        self.cancel_register = QPushButton(self.centralwidget)
        self.cancel_register.setObjectName(u"cancel_register")
        self.cancel_register.setGeometry(QRect(160, 320, 111, 24))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Register</span></p></body></html>", None))
        self.submit_register.setText(QCoreApplication.translate("MainWindow", u"Submit Credentials", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">Username</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">Password</p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">Confirm Password</p></body></html>", None))
        self.special_question.setItemText(0, QCoreApplication.translate("MainWindow", u"Select a question", None))
        self.special_question.setItemText(1, QCoreApplication.translate("MainWindow", u"Who was your childhood hero?", None))
        self.special_question.setItemText(2, QCoreApplication.translate("MainWindow", u"What was the name of your first pet?", None))
        self.special_question.setItemText(3, QCoreApplication.translate("MainWindow", u"What is your mother's maiden name?", None))
        self.special_question.setItemText(4, QCoreApplication.translate("MainWindow", u"What was the name of your first school?", None))
        self.special_question.setItemText(5, QCoreApplication.translate("MainWindow", u"What is your favorite book?", None))
        self.special_question.setItemText(6, QCoreApplication.translate("MainWindow", u"What is your favorite movie?", None))
        self.special_question.setItemText(7, QCoreApplication.translate("MainWindow", u"What was your dream job as a child?", None))
        self.special_question.setItemText(8, QCoreApplication.translate("MainWindow", u"What is the name of the town where you were born?", None))

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">Special Question</p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">Anser to<br/>Special Question</p></body></html>", None))
        self.cancel_register.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
    # retranslateUi

