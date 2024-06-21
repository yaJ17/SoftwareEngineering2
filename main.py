import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QSize
from ui_main import Ui_MainWindow  # Replace 'your_ui_file' with the actual filename of your UI code



# import database

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(QSize(908, 463))  # Set the fixed size of the window

        # Connect button clicks to their respective functions
        self.ui.dash_button.clicked.connect(self.show_dashboard)
        self.ui.prod_button.clicked.connect(self.show_production)
        self.ui.sched_button.clicked.connect(self.show_scheduling)
        self.ui.invent_button.clicked.connect(self.show_inventory)
        self.ui.rep_button.clicked.connect(self.show_reports)
        self.ui.transac_button.clicked.connect(self.show_transaction)
        self.ui.help_button.clicked.connect(self.show_help)
        self.ui.about_button.clicked.connect(self.show_about)
        self.ui.maintenance_button.clicked.connect(self.show_maintenance)
        self.ui.logout_button.clicked.connect(self.logout)


    def show_dashboard(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def show_production(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def show_scheduling(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def show_inventory(self):
        self.ui.stackedWidget.setCurrentIndex(6)

    def show_reports(self):
        self.ui.stackedWidget.setCurrentIndex(8)

    def show_transaction(self):
        self.ui.stackedWidget.setCurrentIndex(5)

    def show_help(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def show_about(self):
        self.ui.stackedWidget.setCurrentIndex(7)

    def show_maintenance(self):
        self.ui.stackedWidget.setCurrentIndex(4)

    def logout(self):
        # Perform logout actions (e.g., closing the window or redirecting to login screen)
        self.close()
'''
    def populate_product_table(self):
        # Call the populate_product function from database module
        product_data = database.populate_product()

        # Assuming product_data is a list of tuples or lists where each tuple/list is a row of data
        self.ui.prod_table.setRowCount(len(product_data))

        for row_index, row_data in enumerate(product_data):
            for column_index, data in enumerate(row_data):
                item = QTableWidgetItem(str(data))  # Convert data to string if necessary
                self.ui.prod_table.setItem(row_index, column_index, item)
'''






if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
