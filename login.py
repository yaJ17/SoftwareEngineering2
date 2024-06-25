from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget
from PySide6.QtCore import QTimer
from ui_login import Ui_Login
from databases.database import DatabaseManager  # Adjust the import path as necessary
import sys
import subprocess

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

        # Call DatabaseManager to check login
        if self.db_manager.check_account_login(username, password):
            QMessageBox.information(self, "Login Successful", "Login Successful!")
            # Reset failed attempts on successful login
            self.failed_attempts = 0

            # Close the LoginWindow
            self.close()

            # Launch main.py using subprocess
            print(f"Launching main.py using {sys.executable}")
            try:
                proc = subprocess.Popen([sys.executable, 'main.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                out, err = proc.communicate(timeout=10)  # Adjust timeout as needed
                print(f"stdout: {out.decode()}")
                print(f"stderr: {err.decode()}")
            except subprocess.TimeoutExpired:
                print("Process timeout expired")
            except Exception as e:
                print(f"Error launching main.py: {e}")

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
