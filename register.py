from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QComboBox
from PySide6.QtCore import Qt
from ui_register import Ui_MainWindow  # Adjust the import path as necessary
from databases.database import DatabaseManager  # Adjust the import path as necessary
import sys
import re

class RegisterWindow(QMainWindow):
    def __init__(self):
        super(RegisterWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Initialize DatabaseManager instance
        key = b'[Xd\xee[\\\x90\x8c\xc8t\xba\xe4\xe0\rR\x87\xe6\xbe\xce\x8a\x02lC6\xf7G\x15O\xca\x182\xd0'
        self.db_manager = DatabaseManager('localhost', 'root', 'admin', key)
        self.db_manager.connect_to_database()
        self.db_manager.create_schema_and_tables()


        # Connect buttons to their respective methods
        self.ui.submit_register.clicked.connect(self.handle_register)
        self.ui.cancel_register.clicked.connect(self.handle_cancel)

        # Show password requirements upon loading
        self.show_password_requirements()



    def show_password_requirements(self):
        QMessageBox.information(
            self,
            "Password Requirements",
            "Registering would require a password with:\n"
            "• at least 8 characters\n"
            "• one uppercase letter\n"
            "• one lowercase letter\n"
            "• one number\n"
            "• one special character"
        )

    def handle_register(self):
        Username = self.ui.username_register.text()
        password = self.ui.password_register.text()
        confirm_password = self.ui.confirm_password.text()
        special_question = self.ui.special_question.currentText()
        answer = self.ui.textEdit.toPlainText()

        # Validate input fields
        if not Username or not password or not confirm_password or not answer or special_question == "Select a question":
            QMessageBox.warning(self, "Invalid Input", "All fields must be filled out and a question selected.")
            return

        if password != confirm_password:
            QMessageBox.warning(self, "Password Mismatch", "Passwords do not match.")
            return

        # Validate password criteria
        if not re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$", password):
            QMessageBox.warning(self, "Invalid Password", "Password does not meet the required criteria.")
            return

        # Add account to the database
        self.db_manager.add_account(Username, password, special_question, answer)
        QMessageBox.information(self, "Registration Successful", "Account has been successfully created.")
        self.close()


    def handle_cancel(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RegisterWindow()
    window.show()
    sys.exit(app.exec())
