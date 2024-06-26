from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_login import Ui_Login
from databases.database import DatabaseManager  # Adjust the import path as necessary
import sys
from main import MainWindow  # Import MainWindow from main.py
from PySide6.QtCore import QTimer
class LoginWindow(QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.ui = Ui_Login()
        self.ui.setupUi(self)

        # Connect buttons to their respective methods
        self.ui.login_button.clicked.connect(self.handle_login)
        self.ui.forgot_pass_button.clicked.connect(self.handle_forgot_password)
        self.ui.login_exit_button.clicked.connect(self.handle_exit)

        # Initialize DatabaseManager instance
        key = b'[Xd\xee[\\\x90\x8c\xc8t\xba\xe4\xe0\rR\x87\xe6\xbe\xce\x8a\x02lC6\xf7G\x15O\xca\x182\xd0'
        self.db_manager = DatabaseManager('localhost', 'root', 'admin', key)
        self.db_manager.connect_to_database()
        self.db_manager.create_schema_and_tables()
        # Initialize variables
        self.failed_attempts = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.enable_login)

    def handle_login(self):
        username = self.ui.username_login.text()
        password = self.ui.password_login.text()

        if self.db_manager.check_username_exists(username):

            # Call DatabaseManager to check login
            if self.db_manager.check_account_login(username, password):
                QMessageBox.information(self, "Login Successful", "Login Successful!")
                # Reset failed attempts on successful login
                self.failed_attempts = 0

                username_id = self.db_manager.get_username_id(username, password)
                # Pass username and username_id to the main window
                self.main_window = MainWindow(username=username, username_id=username_id)
                self.main_window.show()
                self.close()  # Close the login window
            else:
                QMessageBox.warning(self, "Login Failed", "Invalid username or password")
                self.failed_attempts += 1
                if self.failed_attempts >= 5:
                    self.disable_login()
        else:

            if self.db_manager.check_account_login_by_id(username, password):
                QMessageBox.information(self, "Login Successful", "Login Successful!")
                # Reset failed attempts on successful login
                self.failed_attempts = 0

                # Pass username and username_id to the main window
                userName = self.db_manager.get_username_by_id_and_password(username, password)
                self.main_window = MainWindow(username=userName, username_id=username)
                self.main_window.show()
                self.close()  # Close the login window
            else:
                QMessageBox.warning(self, "Login Failed", "Invalid username or password")
                self.failed_attempts += 1
                if self.failed_attempts >= 5:
                    self.disable_login()

    def disable_login(self):
        # Disable textboxes and login button
        self.ui.username_login.setEnabled(False)
        self.ui.password_login.setEnabled(False)
        self.ui.login_button.setEnabled(False)

        # Show message box
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Too Many Attempts")
        msg_box.setText("Too many failed login attempts! You cannot attempt to login for 3 minutes.")
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.exec()

        # Start a timer to enable login after 3 minutes (180000 ms)
        self.timer.start(180000)

    def enable_login(self):
        # Enable textboxes and login button
        self.ui.username_login.setEnabled(True)
        self.ui.password_login.setEnabled(True)
        self.ui.login_button.setEnabled(True)

        # Stop the timer
        self.timer.stop()

        # Reset failed attempts
        self.failed_attempts = 0

    def handle_forgot_password(self):
        QMessageBox.information(self, "Forgot Password", "Forgot Password functionality is not implemented yet.")

    def handle_exit(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
