import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableView
from PySide6 import QtWidgets
from PySide6.QtGui import QStandardItemModel, QStandardItem
import os
from PySide6.QtCore import Qt
from PySide6.QtCore import QSize
from ui_main import Ui_MainWindow  # Replace 'your_ui_file' with the actual filename of your UI code
from databases.database import DatabaseManager

import xlwt

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
        self.ui.backup_button.clicked.connect(self.backup)
        self.ui.restore_button.clicked.connect(self.restore)
        key = b'[Xd\xee[\\\x90\x8c\xc8t\xba\xe4\xe0\rR\x87\xe6\xbe\xce\x8a\x02lC6\xf7G\x15O\xca\x182\xd0'
        self.db_manager = DatabaseManager('localhost', 'root', 'admin', key)
        self.db_manager.connect_to_database()
        self.db_manager.create_schema_and_tables()
        self.ui.prod_button.clicked.connect(self.show_production)

        # Populate the product table before showing the window
        self.populate_deadline_table()

        # Show the window after populating the table
        self.show()

    def show_dashboard(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.populate_deadline_table()

    def show_production(self):
        self.ui.stackedWidget.setCurrentIndex(5)
        self.populate_orders()

    def show_scheduling(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def show_inventory(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.populate_product_invent()
        self.populate_raw_invent()

    def show_reports(self):
        self.ui.stackedWidget.setCurrentIndex(8)

    def show_transaction(self):
        self.ui.stackedWidget.setCurrentIndex(6)

    def show_help(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def show_about(self):
        self.ui.stackedWidget.setCurrentIndex(7)

    def show_maintenance(self):
        self.ui.stackedWidget.setCurrentIndex(4)

    def logout(self):
        # Perform logout actions (e.g., closing the window or redirecting to login screen)
        self.close()

    def backup(self):
        # Perform logout actions (e.g., closing the window or redirecting to login screen)
        self.db_manager.backup_database_to_excel("data_backup.xlsx")

    def restore(self):
        # Perform logout actions (e.g., closing the window or redirecting to login screen)
        self.db_manager.restore_database_from_excel("data_backup.xlsx")

    def populate_deadline_table(self):
        # Call the populate_deadline function from database module
        deadline = self.db_manager.populate_deadline()
        print("hello")
        for row in deadline:
            print(row)
        
        # Define headers for the table
        headers = ['Name', 'Details', 'Date']
        
        # Create a QStandardItemModel and set headers
        model = QStandardItemModel(len(deadline), len(headers))
        model.setHorizontalHeaderLabels(headers)
        
        # Assuming deadline is a list of tuples or lists where each tuple/list is a row of data
        for row_index, row_data in enumerate(deadline):
            for column_index, data in enumerate(row_data):
                item = QStandardItem(str(data))
                model.setItem(row_index, column_index, item)
        
        # Set the model to the table view
        self.ui.prod_table.setModel(model)


        self.ui.prod_table.setEditTriggers(QTableView.NoEditTriggers)
        # Resize columns to fit content
        self.ui.prod_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

    def populate_orders(self):
        # Call populate_orders from DatabasecManager to fetch orders data
        orders = self.db_manager.populate_orders()

        # Define headers for the table
        headers = [ 'Quantity', 'Bag Type', 'Progress']

        # Create a QStandardItemModel and set headers
        model = QStandardItemModel(len(orders), len(headers))
        model.setHorizontalHeaderLabels(headers)

        # Populate the model with fetched data
        for row_index, row_data in enumerate(orders):
            for column_index, data in enumerate(row_data):
                item = QStandardItem(str(data))
                model.setItem(row_index, column_index, item)

        # Set the model to the prod_table in UI
        self.ui.product_table.setModel(model)
        self.ui.product_table.setEditTriggers(QTableView.NoEditTriggers)
        # Resize columns to fit content
        self.ui.product_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)


    def populate_product_invent(self):
        # Call populate_orders from DatabasecManager to fetch orders data
        orders = self.db_manager.populate_product()

        # Define headers for the table
        headers = [ 'Bag Type', 'Quantity', 'Product Price']

        # Create a QStandardItemModel and set headers
        model = QStandardItemModel(len(orders), len(headers))
        model.setHorizontalHeaderLabels(headers)

        # Populate the model with fetched data
        for row_index, row_data in enumerate(orders):
            for column_index, data in enumerate(row_data):
                item = QStandardItem(str(data))
                model.setItem(row_index, column_index, item)

        # Set the model to the prod_table in UI
        self.ui.product_inventory_table.setModel(model)
        self.ui.product_inventory_table.setEditTriggers(QTableView.NoEditTriggers)
        # Resize columns to fit content
        self.ui.product_inventory_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)


    def populate_raw_invent(self):
        # Call populate_orders from DatabasecManager to fetch orders data
        orders = self.db_manager.populate_raw_materials()

        # Define headers for the table
        headers = [ 'Material Name', 'Stocks', 'Cost']

        # Create a QStandardItemModel and set headers
        model = QStandardItemModel(len(orders), len(headers))
        model.setHorizontalHeaderLabels(headers)

        # Populate the model with fetched data
        for row_index, row_data in enumerate(orders):
            for column_index, data in enumerate(row_data):
                item = QStandardItem(str(data))
                model.setItem(row_index, column_index, item)

        # Set the model to the prod_table in UI
        self.ui.raw_inventory_table.setModel(model)
        self.ui.raw_inventory_table.setEditTriggers(QTableView.NoEditTriggers)
        # Resize columns to fit content
        self.ui.raw_inventory_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)















if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
