from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_register import Ui_MainWindow
from databases.database import DatabaseManager  # Adjust the import path as necessary
import sys
import re

class RegisterWindow(QMainWindow):
    def __init__(self):
        super(RegisterWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect buttons to their respective methods
        self.ui.submit_register.clicked.connect(self.handle_register)
        self.ui.cancel_register.clicked.connect(self.handle_cancel)

        # Initialize DatabaseManager instance
        key = b'[Xd\xee[\\\x90\x8c\xc8t\xba\xe4\xe0\rR\x87\xe6\xbe\xce\x8a\x02lC6\xf7G\x15O\xca\x182\xd0'
        self.db_manager = DatabaseManager('localhost', 'root', 'admin', key)
        self.db_manager.connect_to_database()
        self.db_manager.create_schema_and_tables()

        # Populate the special_question combobox with options
        self.populate_special_questions()

        # Show initial password requirements message box
        self.show_password_requirements()

    def populate_special_questions(self):
        self.ui.special_question.addItems([
            "Select a question",
            "What is your mother's maiden name?",
            "What was the name of your first pet?",
            "What was the make and model of your first car?",
            "In what city were you born?"
        ])

    def show_password_requirements(self):
        QMessageBox.information(
            self, "Password Requirements",
            "Registering would require a password with:\n"
            "• At least 8 characters\n"
            "• One uppercase letter\n"
            "• One lowercase letter\n"
            "• One number\n"
            "• One special character"
        )

    def handle_register(self):
        username = self.ui.username_register.text()
        password = self.ui.password_register.text()
        confirm_password = self.ui.confirm_password.text()
        question = self.ui.special_question.currentText()
        answer = self.ui.textEdit.toPlainText()

        # Check for empty fields
        if not username or not password or not confirm_password or not answer or question == "Select a question":
            QMessageBox.warning(self, "Registration Failed", "All fields are required and a valid security question must be selected.")
            return

        # Check if passwords match
        if password != confirm_password:
            QMessageBox.warning(self, "Registration Failed", "Passwords do not match.")
            return

        # Check password strength
        if not re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$", password):
            QMessageBox.warning(self, "Registration Failed",
                                "Password must be at least 8 characters long and include an uppercase letter, a lowercase letter, a number, and a special character.")
            return

        # Call DatabaseManager to add account
        try:
            self.db_manager.add_account(username, password, question, answer)
            QMessageBox.information(self, "Registration Successful", "Your account has been created successfully!")
        except Exception as e:
            QMessageBox.critical(self, "Registration Failed", f"An error occurred: {e}")

    def handle_cancel(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RegisterWindow()
    window.show()
    sys.exit(app.exec())
