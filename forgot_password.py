from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtCore import Qt
from ui_forgot_password import Ui_MainWindow  # Adjust the import path as necessary
from databases.database import DatabaseManager  # Adjust the import path as necessary
import sys
import re

class ForgotPasswordWindow(QMainWindow):
    def __init__(self):
        super(ForgotPasswordWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Initialize DatabaseManager instance
        key = b'[Xd\xee[\\\x90\x8c\xc8t\xba\xe4\xe0\rR\x87\xe6\xbe\xce\x8a\x02lC6\xf7G\x15O\xca\x182\xd0'
        self.db_manager = DatabaseManager('localhost', 'root', 'admin', key)
        self.db_manager.connect_to_database()
        self.db_manager.create_schema_and_tables()
        self.ui.stackedWidget.setCurrentIndex(1)
        # Connect buttons to their respective methods
        self.ui.confirm_FP.clicked.connect(self.handle_confirm)
        self.ui.submit_register.clicked.connect(self.handle_submit)
        self.ui.cancel_FP.clicked.connect(self.handle_FP_cancel)
        self.ui.FP_cancel2.clicked.connect(self.handle_FP_cancel)
    def handle_confirm(self):
        username = self.ui.username_FP.text()
        special_question = self.ui.special_question_FP.currentText()
        answer = self.ui.answer_FP.toPlainText()

        # Validate input fields
        if not username or not special_question or not answer or special_question == "Select a question":
            QMessageBox.warning(self, "Invalid Input", "All fields must be filled out and a question selected.")
            return

        # Validate user credentials
        if not self.db_manager.validate_user_for_reset(username, special_question, answer):
            QMessageBox.warning(self, "Invalid Credentials", "Username, special question, or answer is incorrect.")
            return

        # If validation is successful, proceed to the next widget
        self.show_password_requirements()
        self.ui.stackedWidget.setCurrentIndex(0)

    def handle_submit(self):
        new_password = self.ui.new_pass_FP.text()
        confirm_password = self.ui.confirm_new_pass_FP.text()

        # Validate input fields
        if not new_password or not confirm_password:
            QMessageBox.warning(self, "Invalid Input", "Both password fields must be filled out.")
            return

        if new_password != confirm_password:
            QMessageBox.warning(self, "Password Mismatch", "Passwords do not match.")
            return

        # Validate password criteria
        if not re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$", new_password):
            QMessageBox.warning(self, "Invalid Password", "Password does not meet the required criteria.")
            return

        # Update password in the database
        username = self.ui.username_FP.text()
        self.db_manager.update_password(username, new_password)
        QMessageBox.information(self, "Success", "Password has been successfully reset.")
        self.close()
        self.load_login_window()

    def load_login_window(self):
        from login import LoginWindow  # Adjust the import path as necessary
        self.login_window = LoginWindow()
        self.login_window.show()

    def handle_FP_cancel(self):
        from login import LoginWindow  # Adjust the import path as necessary
        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()

    def show_password_requirements(self):
        QMessageBox.information(
            self,
            "Password Requirements",
            "Your Password Requires the following:\n"
            "• at least 8 characters\n"
            "• one uppercase letter\n"
            "• one lowercase letter\n"
            "• one number\n"
            "• one special character"
        )

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ForgotPasswordWindow()
    window.show()
    sys.exit(app.exec())
