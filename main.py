from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QWidget
from PySide6.QtCore import QDate
from PySide6.QtWidgets import QMainWindow, QApplication, QLabel, QToolTip
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QTableWidgetItem, QTableWidget, QHeaderView, QMessageBox, QFileDialog
import pandas as pd
import sys
import os
import threading
import time
from PySide6.QtWidgets import QApplication, QMainWindow, QTableView
from PySide6 import QtWidgets
from PySide6.QtGui import QStandardItemModel, QStandardItem, QColor, QBrush, QDesktopServices
from PySide6.QtCore import Qt
from PySide6.QtCore import QSize
from ui_main import Ui_MainWindow  # Replace 'your_ui_file' with the actual filename of your UI code
from databases.database import DatabaseManager
import difflib
from PySide6.QtWidgets import QPushButton
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle
import datetime
from PySide6.QtCore import QDate, QDateTime, QUrl
from register import RegisterWindow
from mysql.connector import Error  # Import the Error class
current_date = datetime.date.today()


class MainWindow(QMainWindow):
    def __init__(self, username, username_id):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(QSize(908, 463))  # Set the fixed size of the window
        self.ui.stackedWidget.setCurrentIndex(0)
        self.current_date = datetime.date.today()
        self.ui.order_deadline_dateEdit.setDate(QDate(current_date.year, current_date.month, current_date.day))
        self.ui.add_deadline_date.setDate(QDate(current_date.year, current_date.month, current_date.day))

        self.ui.report_start.setDate(QDate(current_date.year, current_date.month, current_date.day))
        self.ui.report_end.setDate(QDate(current_date.year, current_date.month, current_date.day))
        self.ui.user_logs_start.setDate(QDate(current_date.year, current_date.month, current_date.day))
        self.ui.user_logs_end.setDate(QDate(current_date.year, current_date.month, current_date.day))
        # close

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
        self.ui.cancel_add_deadline.clicked.connect(self.cancel_add_dl)
        self.ui.cancel_edit_deadline.clicked.connect(self.cancel_edit_dl)
        self.ui.add_deadline_button.clicked.connect(self.add_dl)
        self.ui.save_add_deadline.clicked.connect(self.save_added_deadline)
        self.ui.save_edit_deadline.clicked.connect(self.save_edited_deadline)
        self.ui.archive_edit_deadline.clicked.connect(self.archive_deadline)
        self.ui.user_logs_button.clicked.connect(self.show_user_logs)
        self.ui.generate_user_logs.clicked.connect(self.generate_user_logs_pdf_clicked)
        self.ui.back_user_logs.clicked.connect(self.show_reports)
        self.ui.weekly_calendar.clicked.connect(self.show_weekly_scheduling)
        self.ui.daily_calendar.clicked.connect(self.show_daily_scheduling)
        self.ui.daily_calendar.clicked.connect(self.populate_today)
        self.ui.return_calendar.clicked.connect(self.show_scheduling)
        self.ui.return_calendar_2.clicked.connect(self.show_scheduling)
        self.ui.quick_raw.clicked.connect(self.show_add_raw_material)
        self.ui.quick_stock.clicked.connect(self.show_add_finished_product)
        self.ui.add_order_button.clicked.connect(self.show_add_order)
        self.ui.cancel_add_order.clicked.connect(self.show_production)
        self.ui.edit_cancel_button.clicked.connect(self.show_production)

        self.ui.add_product_button.clicked.connect(self.show_add_finished_product)
        self.ui.add_inventory_button.clicked.connect(self.show_add_raw_material)
        self.ui.cancel_add_invProduct.clicked.connect(self.show_inventory)
        self.ui.cancel_add_raw.clicked.connect(self.show_inventory)
        self.ui.cancel_update_product.clicked.connect(self.show_inventory)
        self.ui.cancel_edit_raw.clicked.connect(self.show_inventory)

        self.ui.prod_report_btn.clicked.connect(self.generate_product_pdf_clicked)
        self.ui.stocks_report_btn.clicked.connect(self.generate_stock_pdf_clicked)
        self.ui.inventory_report_btn.clicked.connect(self.generate_inventory_pdf_clicked)
        self.ui.sales_report_btn.clicked.connect(self.generate_sales_pdf_clicked)

        self.ui.save_add_order.clicked.connect(self.save_add_production_action)
        self.ui.save_add_raw.clicked.connect(self.save_add_material_invent)
        self.ui.save_add_invProduct.clicked.connect(self.save_add_finish_product_invent)

        key = b'[Xd\xee[\\\x90\x8c\xc8t\xba\xe4\xe0\rR\x87\xe6\xbe\xce\x8a\x02lC6\xf7G\x15O\xca\x182\xd0'
        self.db_manager = DatabaseManager('localhost', 'root', 'admin', key)
        self.db_manager.connect_to_database()
        self.db_manager.create_schema_and_tables()

        self.ui.specify_report_date.stateChanged.connect(self.specific_date)
        self.ui.specify_user_logs_date.stateChanged.connect(self.specific_user_logs)

        self.ui.prod_button.clicked.connect(self.show_production)
        self.ui.search_bar.returnPressed.connect(self.perform_search)
        self.ui.edit_save_button.clicked.connect(self.save_edit_order)
        self.ui.update_edit_raw.clicked.connect(self.save_edit_material)
        self.ui.update_products.clicked.connect(self.save_edit_product)
        self.ui.void_order.clicked.connect(self.void_production)
        self.ui.archive_raw.clicked.connect(self.void_material)
        self.ui.Archive_finished_product.clicked.connect(self.void_product)
        # Populate the product table before showing the window
        self.populate_deadline_table()
        self.populate_history_DB()
        self.populate_dashboard_weekly()
        self.data = {}
        self.register_window = None
        # calendar
        self.ui.calendarWidget.clicked.connect(self.date_clicked)
        self.schedules_table = QTableWidget(self)
        self.clicked_date = None

        # Connect instruct_button to open_user_manual method
        self.ui.instruct_button.clicked.connect(self.open_user_manual)

        self.ui.username_label.setText(username)
        self.ui.username_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.ui.username_id.setText(username_id)
        self.ui.username_id.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        self.ui.add_account.clicked.connect(self.show_register_window)
        id, user = self.db_manager.get_account_username()
        self.username = username
        self.username_id = username_id
        if self.username != user and self.username_id != id:
            self.ui.add_account.setEnabled(False)
        # Show the window after populating the table
        self.ui.toolButton.setToolTip("""
                    <div style="
                        width: 200px; 
                        height: 200px; 
                        word-wrap: break-word; 
                        white-space: normal; 
                        padding: 50px; 
                        text-align: left;
                        ">
                        <br>
                        <b>Deadline setting parameters</b><br>
                        <b>Production Report:</b> deadline date.<br>
                        <b>Inventory, Stocks, Sales Reports:</b> entry creation date.
                        <br>
                    </div>
                """)

        self.start_automatic_backup()

        #buttons for add quantity
        self.ui.cancel_order_plus.clicked.connect(self.show_production)
        self.ui.cancel_raw_plus.clicked.connect(self.show_inventory)
        self.ui.cancel_product_plus.clicked.connect(self.show_inventory)
        self.ui.save_order_plus.clicked.connect(self.save_order_plus_action)
        self.ui.save_raw_plus.clicked.connect(self.save_plus_raw_inv_action)
        self.ui.save_product_plus.clicked.connect(self.save_prod_plus_action)

        self.show()


    def start_automatic_backup(self):
        backup_dir = os.path.join(os.getcwd(), "Backup", "Automatic")
        os.makedirs(backup_dir, exist_ok=True)

        def automatic_backup():
            while True:
                # Wait for 10 seconds before the next backup
                time.sleep(3600)
                # List all existing backup files
                backup_files = sorted(
                    [f for f in os.listdir(backup_dir) if f.startswith("auto_backup_")],
                    key=lambda x: os.path.getmtime(os.path.join(backup_dir, x))
                )

                # If there are already 5 backup files, delete the oldest one
                if len(backup_files) >= 5:
                    os.remove(os.path.join(backup_dir, backup_files[0]))

                # Create the new backup file path
                timestamp = time.strftime("%Y%m%d_%H%M%S")
                backup_file = os.path.join(backup_dir, f"auto_backup_{timestamp}.xlsx")

                # Perform the backup
                self.db_manager.backup_database_to_excel(backup_file)

        backup_thread = threading.Thread(target=automatic_backup)
        backup_thread.daemon = True
        backup_thread.start()

    def open_user_manual(self):

        # Directory of the current script
        current_dir = os.path.dirname(os.path.realpath(__file__))

        # Path to the User Manual PDF
        pdf_path = os.path.join(current_dir, "User Manual.pdf")

        # Check if the PDF file exists
        if not os.path.exists(pdf_path):
            QMessageBox.warning(self, "File Not Found", "User Manual.pdf not found in the application directory.")
            return
        # Open the PDF file with the default PDF viewer
        url = QUrl.fromLocalFile(pdf_path)
        QDesktopServices.openUrl(url)

        # User log
        action = f"Opened the user manual."
        self.db_manager.add_user_log(self.username, self.username_id, action)

    def open_report(self, filename):
        # Directory of the current script
        current_dir = os.path.dirname(os.path.realpath(__file__))

        # Path to the User Manual PDF
        pdf_path = os.path.join(current_dir, filename)

        # Check if the PDF file exists
        if not os.path.exists(pdf_path):
            QMessageBox.warning(self, "File Not Found", "User Manual.pdf not found in the application directory.")
            return

        # Open the PDF file with the default PDF viewer
        url = QUrl.fromLocalFile(pdf_path)
        QDesktopServices.openUrl(url)

    def show_register_window(self):
        print(self.username, self.username_id)
        self.register_window = RegisterWindow()
        self.register_window.show()

    def show_dashboard(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.populate_deadline_table()
        self.populate_dashboard_weekly()

    def show_production(self):
        self.ui.stackedWidget.setCurrentIndex(9)
        self.populate_orders()
        self.ui.client_name_entry.setText("")
        self.ui.bag_type_entry.setText("")
        self.ui.order_quantity_spinBox.setValue(0)
        self.ui.order_deadline_dateEdit.setDate(QDate.currentDate())
        self.ui.order_priority_spinBox.setValue(0)
        self.ui.add_order_notes.setText("")
    def show_add_order(self):
        self.ui.stackedWidget.setCurrentIndex(10)

    def show_edit_order(self):
        self.ui.stackedWidget.setCurrentIndex(11)

    def show_scheduling(self):
        self.ui.stackedWidget.setCurrentIndex(12)

    def show_weekly_scheduling(self):
        self.ui.stackedWidget.setCurrentIndex(13)
        self.populate_weekly_table()

    def show_daily_scheduling(self):
        self.ui.stackedWidget.setCurrentIndex(14)

    def show_inventory(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.populate_product_invent()
        self.populate_raw_invent()

    def show_add_raw_material(self):
        self.ui.stackedWidget.setCurrentIndex(4)

    def show_edit_material(self):
        self.ui.stackedWidget.setCurrentIndex(5)

    def show_add_finished_product(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def edit_finished_product(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def show_reports(self):
        self.ui.stackedWidget.setCurrentIndex(16)

    def show_transaction(self):
        self.ui.stackedWidget.setCurrentIndex(6)
        self.populate_table_transac()

    def show_help(self):
        self.ui.stackedWidget.setCurrentIndex(7)

    def show_about(self):
        self.ui.stackedWidget.setCurrentIndex(15)

    def show_maintenance(self):
        self.ui.stackedWidget.setCurrentIndex(8)



    def logout(self):
        action = f"Logged out."
        self.db_manager.add_user_log(self.username, self.username_id, action)
        self.username = None
        self.username_id = None

        self.close()
        self.show_login_window()

    def closeEvent(self, event):
        action = f"Logged out."
        self.db_manager.add_user_log(self.username, self.username_id, action)
        event.accept()  # Close the window if user confirms

    def show_login_window(self):
        from login import LoginWindow
        self.login_window = LoginWindow()
        self.login_window.show()

    def show_user_logs(self):
        self.ui.stackedWidget.setCurrentIndex(19)
        self.populate_user_logs()

    def populate_user_logs(self):
        transac = self.db_manager.populate_user_logs()
        print("hello")
        for row in transac:
            print(row)

        # Define headers for the table
        headers = ['USER ID', 'USERNAME', 'ACTION', 'TIMESTAMP']
        self.ui.user_logs_table.setRowCount(len(transac))
        self.ui.user_logs_table.setColumnCount(len(headers))

        # Set the headers for the table
        self.ui.user_logs_table.setHorizontalHeaderLabels(headers)

        # Populate the table with fetched data
        for row_index, row_data in enumerate(transac):
            for column_index, data in enumerate(row_data):
                item = QTableWidgetItem(str(data))
                self.ui.user_logs_table.setItem(row_index, column_index, item)
        # Set the edit triggers (disable editing)
        self.ui.user_logs_table.setEditTriggers(QTableWidget.NoEditTriggers)

        # Resize columns to fit content
        self.ui.user_logs_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.user_logs_table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

    def backup(self):
        # Create the backup directory if it doesn't exist
        backup_dir = os.path.join(os.getcwd(), "Backup", "Manual")
        os.makedirs(backup_dir, exist_ok=True)

        # Specify the backup file path
        backup_file = os.path.join(backup_dir, "data_backup.xlsx")

        # Perform the backup
        self.db_manager.backup_database_to_excel(backup_file)

        action = f"Created system backup at {backup_file}."
        self.db_manager.add_user_log(self.username, self.username_id, action)

    def restore(self):
        # Open file dialog to select the backup file
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("Excel files (*.xlsx)")
        file_dialog.setFileMode(QFileDialog.ExistingFile)

        if file_dialog.exec_():
            selected_files = file_dialog.selectedFiles()
            if selected_files:
                input_file = selected_files[0]
                self.db_manager.overwrite_restore(input_file)

                action = f"Restored the system data from {input_file}."
                self.db_manager.add_user_log(self.username, self.username_id, action)

    def populate_deadline_table(self):
        # Call the populate_deadline function from database module
        deadline = self.db_manager.populate_deadline()
        print("hello")
        for row in deadline:
            print(row)

        # Define headers for the table
        headers = ['Name', 'Details', 'Date']
        # Set the number of rows and columns
        self.ui.prod_table.setRowCount(len(deadline))
        self.ui.prod_table.setColumnCount(len(headers))

        # Set the headers for the table
        self.ui.prod_table.setHorizontalHeaderLabels(headers)

        # Populate the table with fetched data
        for row_index, row_data in enumerate(deadline):
            for column_index, data in enumerate(row_data):
                item = QTableWidgetItem(str(data))
                self.ui.prod_table.setItem(row_index, column_index, item)
        # Set the edit triggers (disable editing)
        self.ui.prod_table.setEditTriggers(QTableWidget.NoEditTriggers)

        # Resize columns to fit content
        self.ui.prod_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.prod_table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

    def populate_history_DB(self):
        # Call the populate_deadline function from database module
        transacs = self.db_manager.populate_history_DB()
        print("hello")
        for row in transacs:
            print(row)

        # Define headers for the table
        headers = ['Client', 'Order']
        self.ui.history_DB.setRowCount(len(transacs))
        self.ui.history_DB.setColumnCount(len(headers))

        # Set the headers for the table
        self.ui.history_DB.setHorizontalHeaderLabels(headers)

        # Populate the table with fetched data
        for row_index, row_data in enumerate(transacs):
            for column_index, data in enumerate(row_data):
                item = QTableWidgetItem(str(data))
                self.ui.history_DB.setItem(row_index, column_index, item)
        # Set the edit triggers (disable editing)
        self.ui.history_DB.setEditTriggers(QTableWidget.NoEditTriggers)

        # Resize columns to fit content
        self.ui.history_DB.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.history_DB.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

    def save_added_deadline(self):

        reply = QMessageBox.question(self, 'Add Deadline',
                                     f'Are you sure you want to add this deadline?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        print(f"User reply: {reply}")
        if reply == QMessageBox.Yes:
            deadline_date = self.ui.add_deadline_date.date().toString("yyyy-MM-dd")
            deadline_name = self.ui.add_deadline_name.text()
            deadline_details = self.ui.add_deadline_details.toPlainText()
            print(deadline_name, deadline_details, deadline_date)
            self.db_manager.add_deadline(deadline_name, deadline_details, deadline_date)

            self.ui.add_deadline_date.setDate(QDate.currentDate())
            self.ui.add_deadline_name.setText("")
            self.ui.add_deadline_details.setText("")
            # self.ui.stackedWidget.setCurrentIndex(14)
            self.db_manager.connection.commit()
            self.show_scheduling()

            action = f"Added a new deadline on {deadline_date}."
            self.db_manager.add_user_log(self.username, self.username_id, action)
        else:
            print("User cancelled")
            # Handle cancellation logic

    def save_edited_deadline(self):
        reply = QMessageBox.question(self, 'Edit Deadline',
                                     f'Are you sure you want to edit this deadline?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        print(f"User reply: {reply}")
        if reply == QMessageBox.Yes:
            deadline_date = self.ui.edit_deadline_date.date().toString("yyyy-MM-dd")
            deadline_name = self.ui.edit_deadline_name.text()
            deadline_details = self.ui.edit_deadline_details.toPlainText()
            print(deadline_name, deadline_details, deadline_date)
            self.db_manager.set_deadline(deadline_name, deadline_details, deadline_date, self.data['name'], self.data['details'], self.data['date'])
            self.db_manager.connection.commit()
            self.show_scheduling()

            action = f"Edited {deadline_name} (deadline)."
            self.db_manager.add_user_log(self.username, self.username_id, action)
        else:
            print("User cancelled")
            # Handle cancellation logic

    def archive_deadline(self):
        print("Archive deadline function called")
        deadline_name = self.ui.edit_deadline_name.text()
        print(f"Deadline name: {deadline_name}")

        reply = QMessageBox.question(self, 'Cancel Deadline',
                                     f'Are you sure you want to cancel the deadline "{deadline_name}"?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        print(f"User reply: {reply}")

        if reply == QMessageBox.Yes:
            print("User confirmed")
            # Proceed with archiving logic
            self.db_manager.void_deadline(self.data['name'], self.data['details'], self.data['date'])
            self.db_manager.connection.commit()
            self.show_scheduling()
            action = f"Archived {deadline_name} (deadline)."
            self.db_manager.add_user_log(self.username, self.username_id, action)
        else:
            print("User cancelled")
            # Handle cancellation logic

        print("End of archive_deadline function")

    def cancel_add_dl(self):
        self.ui.stackedWidget.setCurrentIndex(12)

    def cancel_edit_dl(self):
        self.ui.stackedWidget.setCurrentIndex(12)

    def add_dl(self):
        self.ui.stackedWidget.setCurrentIndex(17)

    def populate_weekly_table(self):
        # Call the populate_deadline function from database module
        deadline_week = self.db_manager.populate_deadline_by_week()
        print("hello")
        for row in deadline_week:
            print(row)

        # Define headers for the table
        headers = ['Deadline Name', 'Deadline Details', 'Deadline Date', 'Edit']
        # Set the number of rows and columns
        self.ui.weekly_table.setRowCount(len(deadline_week))
        self.ui.weekly_table.setColumnCount(len(headers))

        # Set the headers for the table
        self.ui.weekly_table.setHorizontalHeaderLabels(headers)

        # Populate the table with fetched data
        for row_index, row_data in enumerate(deadline_week):
            for column_index, data in enumerate(row_data):
                item = QTableWidgetItem(str(data))
                self.ui.weekly_table.setItem(row_index, column_index, item)

            # Add edit button in the last column
            edit_button = QPushButton('Edit')
            edit_button.setProperty("row", row_index)

            edit_button.clicked.connect(lambda checked, row=row_index: self.handle_edit_deadline_weekly(row))
            self.ui.weekly_table.setCellWidget(row_index, len(headers) - 1, edit_button)

            #edit_button.clearFocus()

        # Set the edit triggers (disable editing)
        self.ui.weekly_table.setEditTriggers(QTableWidget.NoEditTriggers)

        # Resize columns to fit content
        self.ui.weekly_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.weekly_table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.ui.weekly_table.clearSelection()

    def handle_edit_deadline_weekly(self, row):
        # Get deadline name from table
        dl_name_item = self.ui.weekly_table.item(row, 0)
        if dl_name_item:
            dl_name = dl_name_item.text()
            self.ui.edit_deadline_name.setText(dl_name)
        else:
            print(f"Error: No data found in row {row}")

        dl_details_item = self.ui.weekly_table.item(row, 1)
        if dl_details_item:
            dl_details = dl_details_item.text()
            self.ui.edit_deadline_details.setText(dl_details)
        else:
            print(f"Error: No data found in row {row}")

        # Get deadline date from product_table's fourth column at specified row
        dl_date_item = self.ui.weekly_table.item(row, 2)  # Assuming deadline date is in the fourth column
        if dl_date_item:
            dl_str = dl_date_item.text()
            dl_date = QDateTime.fromString(dl_str,
                                                 "yyyy-MM-dd")  # Assuming the deadline format is "yyyy-MM-dd"
            self.ui.edit_deadline_date.setDate(dl_date.date())
        else:
            print(f"Error: No data found in row {row}")
        self.data = {
            'name': dl_name,
            'details': dl_details,
            'date': dl_date.date().toString("yyyy-MM-dd")
        }
        self.ui.stackedWidget.setCurrentIndex(18)

    def handle_edit_deadline_daily(self, row):
        # Get deadline name from table
        dl_name_item = self.ui.daily_table.item(row, 0)
        if dl_name_item:
            dl_name = dl_name_item.text()
            self.ui.edit_deadline_name.setText(dl_name)
        else:
            print(f"Error: No data found in row {row}")

        dl_details_item = self.ui.daily_table.item(row, 1)
        if dl_details_item:
            dl_details = dl_details_item.text()
            self.ui.edit_deadline_details.setText(dl_details)
        else:
            print(f"Error: No data found in row {row}")

        # Get deadline date from product_table's fourth column at specified row
        dl_date_item = self.ui.daily_table.item(row, 2)  # Assuming deadline date is in the fourth column
        if dl_date_item:
            dl_str = dl_date_item.text()
            dl_date = QDateTime.fromString(dl_str,
                                                 "yyyy-MM-dd")  # Assuming the deadline format is "yyyy-MM-dd"
            self.ui.edit_deadline_date.setDate(dl_date.date())
        else:
            print(f"Error: No data found in row {row}")
        self.data = {
            'name': dl_name,
            'details': dl_details,
            'date': dl_date.date().toString("yyyy-MM-dd")
        }
        self.ui.stackedWidget.setCurrentIndex(18)

    def populate_dashboard_weekly(self):
        # Call the populate_deadline function from database module
        dead_week = self.db_manager.populate_deadline()

        print("hello")
        for row in dead_week:
            print(row)

        # Define headers for the table
        headers = ['Deadline Name', 'Deadline Details', 'Deadline Date']
        # Set the number of rows and columns
        self.ui.dashboard_weekly.setRowCount(len(dead_week))
        self.ui.dashboard_weekly.setColumnCount(len(headers))

        # Set the headers for the table
        self.ui.dashboard_weekly.setHorizontalHeaderLabels(headers)

        # Populate the table with fetched data
        for row_index, row_data in enumerate(dead_week):
            for column_index, data in enumerate(row_data):
                item = QTableWidgetItem(str(data))
                self.ui.dashboard_weekly.setItem(row_index, column_index, item)
        # Set the edit triggers (disable editing)
        self.ui.dashboard_weekly.setEditTriggers(QTableWidget.NoEditTriggers)

        # Resize columns to fit content
        self.ui.dashboard_weekly.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.dashboard_weekly.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

    def populate_table_transac(self):
        # Call the populate_deadline function from database module
        transac = self.db_manager.populate_orders_transaction()
        print("hello")
        for row in transac:
            print(row)

        # Define headers for the table
        headers = ['Client', 'Order', 'Quantity', 'Order Created', 'Deadline']
        self.ui.table_transac.setRowCount(len(transac))
        self.ui.table_transac.setColumnCount(len(headers))

        # Set the headers for the table
        self.ui.table_transac.setHorizontalHeaderLabels(headers)

        # Populate the table with fetched data
        for row_index, row_data in enumerate(transac):
            for column_index, data in enumerate(row_data):
                item = QTableWidgetItem(str(data))
                self.ui.table_transac.setItem(row_index, column_index, item)
        # Set the edit triggers (disable editing)
        self.ui.table_transac.setEditTriggers(QTableWidget.NoEditTriggers)

        # Resize columns to fit content
        self.ui.table_transac.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.table_transac.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

    def save_plus_order(self):
        reply = QMessageBox.question(self, 'Edit Deadline',
                                     f'Save this addition to orders?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        print(f"User reply: {reply}")
        if reply == QMessageBox.Yes:
            deadline_date = self.ui.edit_deadline_date.date().toString("yyyy-MM-dd")
            deadline_name = self.ui.edit_deadline_name.text()
            deadline_details = self.ui.edit_deadline_details.toPlainText()
            print(deadline_name, deadline_details, deadline_date)
            self.db_manager.set_deadline(deadline_name, deadline_details, deadline_date, self.data['name'], self.data['details'], self.data['date'])
            self.db_manager.connection.commit()
            self.show_scheduling()

            action = f"Edited {deadline_name} (deadline)."
            self.db_manager.add_user_log(self.username, self.username_id, action)
        else:
            print("User cancelled")
            # Handle cancellation logic
    '''
    def populate_orders(self):
        # Call populate_orders from DatabaseManager to fetch orders data
        orders = self.db_manager.populate_orders()
        if orders:
            print(True)
        # Define headers for the table
        headers = ['Client Name', "Bag Type", "Order Quantity", "Deadline", 'Priority', "Edit", "Add"]

        # Set the number of rows and columns
        self.ui.product_table.setRowCount(len(orders))
        self.ui.product_table.setColumnCount(len(headers))

        # Set the headers for the table
        self.ui.product_table.setHorizontalHeaderLabels(headers)

        # Populate the table with fetched data
        for row_index, row_data in enumerate(orders):
            for column_index, data in enumerate(row_data):
                item = QTableWidgetItem(str(data))
                self.ui.product_table.setItem(row_index, column_index, item)
                # Add edit button in the last column
            edit_button = QPushButton('Edit')
            edit_button.setProperty("row", row_index)
            edit_button.clicked.connect(lambda checked, row=row_index: self.handle_edit_order(row))
            self.ui.product_table.setCellWidget(row_index, len(headers) - 2, edit_button)
            #edit_button.clearFocus()

            # Add add button in the last column
            plus_button = QPushButton('Add')
            plus_button.setProperty("row", row_index)
            plus_button.clicked.connect(lambda checked, row=row_index: self.handle_plus_order_inv(row))
            self.ui.product_inventory_table.setCellWidget(row_index, len(headers) - 1, plus_button)
            #plus_button.clearFocus()

        # Set the edit triggers (disable editing)
        self.ui.product_table.setEditTriggers(QTableWidget.NoEditTriggers)

        # Resize columns to fit content
        self.ui.product_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.product_table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
    '''



    def handle_edit_order(self, row):
        # Implement your edit logic here
        print(f"ako ang naclick {row}")

        client_id_item = self.ui.product_table.item(row, 0)
        client_id = client_id_item.text()
        # Get client name from product_table's first column at specified row
        client_name_item = self.ui.product_table.item(row, 1)  # Assuming client name is in the first column
        if client_name_item:
            client_name = client_name_item.text()
            self.ui.edit_client_name.setText(client_name)
        else:
            print(f"Error: No data found in row {row}")

        # Get bagtype name from product_table's first column at specified row
        bagtype = self.ui.product_table.item(row,2)  # Assuming client name is in the first column
        if bagtype:
            type_bag = bagtype.text()
            self.ui.edit_bag_type.setText(type_bag)
        else:
            print(f"Error: No data found in row {row}")

        order_quantity_item = self.ui.product_table.item(row, 3)  # Assuming order quantity is in the third column
        if order_quantity_item:
            order_quantity = int(order_quantity_item.text())
            self.ui.edit_order_quantity.setValue(order_quantity)
        else:
            print(f"Error: No data found in row {row}")

        # Get deadline date from product_table's fourth column at specified row
        deadline_item = self.ui.product_table.item(row, 4)  # Assuming deadline date is in the fourth column
        if deadline_item:
            deadline_str = deadline_item.text()
            deadline_date = QDateTime.fromString(deadline_str,
                                                 "yyyy-MM-dd")  # Assuming the deadline format is "yyyy-MM-dd"
            self.ui.edit_order_deadline.setDate(deadline_date.date())
        else:
            print(f"Error: No data found in row {row}")

        priority_item = self.ui.product_table.item(row, 5)  # Assuming order quantity is in the third column
        if priority_item:
            item_priority = int(priority_item.text())
            self.ui.edit_order_priority.setValue(item_priority)
        else:
            print(f"Error: No data found in row {row}")


        try:
            # Assuming db_manager is an instance of DatabaseManager
            # Initialize or get db_manager instance

            # Query the CLIENT table to get client_id
            cursor = self.db_manager.connection.cursor()
            encrypted_client_name = self.db_manager.cipher.encrypt(client_name)
            encrypted_bag_type = self.db_manager.cipher.encrypt(type_bag)
            print(encrypted_client_name,  order_quantity,encrypted_bag_type, item_priority )
            print(client_id)
            if not client_id:
                print(f"Error: Client '{client_name}' not found in database")
                return

            query = """
                SELECT 
                    D.deadline_details
                FROM 
                    CLIENT C
                JOIN 
                    ORDERS O ON C.client_id = O.client_id
                JOIN 
                    DEADLINE D ON C.deadline_id = D.deadline_id
                WHERE 
                    c.client_id =%s;
            """
            cursor.execute(query, (client_id,))
            rows = cursor.fetchone()[0]
            row = self.db_manager.cipher.decrypt(rows)
            print(f"details: {row}")
        except Exception as e: 
            print(f"Error executing database query: {e}")

        self.ui.edit_order_notes.setPlainText(row)
        # Switch to the desired index in stackedWidget

        self.data = {
            "name": client_name,
            "bag_type": type_bag,
            "order_quantity": order_quantity,
            "deadline_date": deadline_date,
            "priority": item_priority,
            "deadline_details": row
        }
        print(self.data)
        self.ui.stackedWidget.setCurrentIndex(11)

    def save_add_production_action(self):
        # Call save_add_production_action from DatabasecManager to fetch orders data
        print("add order action")
        client_name = self.ui.client_name_entry.text()
        order_quantity = self.ui.order_quantity_spinBox.value()
        bag_type = self.ui.bag_type_entry.text()
        deadline_date = self.ui.order_deadline_dateEdit.date().toString("yyyy-MM-dd")
        order_priority = self.ui.order_priority_spinBox.value()
        order_notes = self.ui.add_order_notes.toPlainText()
        exist = self.db_manager.get_order_exist(self.db_manager.cipher.encrypt(client_name), self.db_manager.cipher.encrypt(bag_type), order_quantity, deadline_date, order_priority)
        print(exist)
        if not exist:
            reply = QMessageBox.question(self, 'Add Order',
                                     f'Are you sure you want to add this order?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            print(f"User reply: {reply}")
            if reply == QMessageBox.Yes:
                
                self.db_manager.add_order(client_name, order_quantity, bag_type, deadline_date, order_priority, order_notes)
                print(self.ui.add_order_notes.toPlainText())
                self.ui.client_name_entry.setText("")
                self.ui.bag_type_entry.setText("")
                self.ui.order_quantity_spinBox.setValue(0)
                self.ui.order_deadline_dateEdit.setDate(QDate.currentDate())
                self.ui.order_priority_spinBox.setValue(0)
                self.db_manager.connection.commit()
                self.populate_orders()
                self.ui.stackedWidget.setCurrentIndex(9)

                action = f"Added an order."
                self.db_manager.add_user_log(self.username, self.username_id, action)
            else:
                print("User cancelled")
                # Handle cancellation logic
        else:
            QMessageBox.information(self, "The Order is duplicate", "The Order is duplicate")
            return


    def void_production(self):
        name = self.ui.edit_client_name.text()
        bag_type = self.ui.edit_bag_type.text()
        order_quantity = self.ui.edit_order_quantity.value()
        deadline_date = self.ui.edit_order_deadline.date().toString("yyyy-MM-dd")
        priority = self.ui.edit_order_priority.value()
        print(f"id {id}")
        deadline_details = self.ui.edit_order_notes.toPlainText()
        reply = QMessageBox.question(self, 'Void Order',
                                     f'Are you sure you want to void this order?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        print(f"User reply: {reply}")

        if reply == QMessageBox.Yes:

            client_name = self.ui.edit_client_name.text()
            client_id = self.db_manager.get_client_id(self.db_manager.cipher.encrypt(client_name), self.db_manager.cipher.encrypt(bag_type), order_quantity, deadline_date, priority)
            self.db_manager.void_client(client_id)
            self.db_manager.connection.commit()
            self.populate_orders()
            self.ui.stackedWidget.setCurrentIndex(9)
            action = f"Archived {client_name}'s order."
            self.db_manager.add_user_log(self.username, self.username_id, action)
        else:
            print("User cancelled")
            # Handle cancellation logic

    def save_add_finish_product_invent(self):

        bag_type = self.ui.inventory_bag_type.text()
        quantity = self.ui.add_inventory_product.value()
        defective = self.ui.add_inventory_defective.value()
        cost = self.ui.inventory_product_cost.value()
        price = self.ui.inventory_active_product.value()
        print(bag_type, quantity, defective, cost, price)

        reply = QMessageBox.question(self, 'Add Finished Product',
                                     f'Are you sure you want to add product to your inventory?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        print(f"User reply: {reply}")

        if reply == QMessageBox.Yes:
            self.db_manager.add_product(bag_type, quantity, defective, cost, price)
            self.db_manager.connection.commit()

            # User logs
            action = f"Added {quantity} {bag_type} (bag type) with {defective} defectives in the finished product inventory."
            self.db_manager.add_user_log(self.username, self.username_id, action)

            self.ui.inventory_bag_type.setText("")
            self.ui.add_inventory_product.setValue(0)
            self.ui.add_inventory_defective.setValue(0)
            self.ui.inventory_product_cost.setValue(0)
            self.ui.inventory_active_product.setValue(0)
            self.show_inventory()
        else:
            print("User cancelled")
            # Handle cancellation logic

        print("End of Add Finished Product to inventory function")

    def save_add_material_invent(self):
        reply = QMessageBox.question(self, 'Add Raw Material',
                                     f'Are you sure you want to add this raw material to the inventory?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        print(f"User reply: {reply}")

        if reply == QMessageBox.Yes:
            name = self.ui.add_inventory_Materiel.text()
            mat_type = self.ui.add_material_type.text()
            stock = self.ui.add_material_stock.value()
            cost = self.ui.add_material_cost.value()
            safety = self.ui.add_safety_stock.value()
            supplier = self.ui.add_material_supplier.text()
            print(name, mat_type, stock, cost, safety, supplier)
            self.db_manager.add_raw_material(name,mat_type, stock, cost, safety, supplier)
            self.db_manager.connection.commit()
            self.ui.add_inventory_Materiel.setText("")
            self.ui.add_material_type.setText("")
            self.ui.add_material_stock.setValue(0)
            self.ui.add_material_cost.setValue(0)
            self.ui.add_safety_stock.setValue(0)
            self.ui.add_material_supplier.setText("")

            self.show_inventory()

            action = f"Added {stock} {name} (material) in the raw materials inventory."
            self.db_manager.add_user_log(self.username, self.username_id, action)
        else:
            print("User cancelled")
            # Handle cancellation logic

    def void_material(self):
        reply = QMessageBox.question(self, 'Void Raw Material',
                                     f'Are you sure you want to void this raw material?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        print(f"User reply: {reply}")

        if reply == QMessageBox.Yes:
            name = self.ui.add_inventory_Materiel.text()

            self.db_manager.void_raw_material(self.data['name'], self.data['supplier'])
            self.db_manager.connection.commit()
            self.show_inventory()

            action = f"Archived {name} (material) from the raw materials inventory."
            self.db_manager.add_user_log(self.username, self.username_id, action)
        else:
            print("User cancelled")
            # Handle cancellation logic

    def populate_orders(self):
        # Call populate_orders from DatabaseManager to fetch orders data
        orders = self.db_manager.populate_orders()

        # Define headers for the table
        headers = ['ID','Client Name', "Bag Type", "Quantity", "Deadline", 'Priority', "Edit", "Add"]

        # Set the number of rows and columns
        self.ui.product_table.setRowCount(len(orders))
        self.ui.product_table.setColumnCount(len(headers))

        # Set the headers for the table
        self.ui.product_table.setHorizontalHeaderLabels(headers)

        # Populate the table with fetched data
        for row_index, row_data in enumerate(orders):
            for column_index, data in enumerate(row_data):
                item = QTableWidgetItem(str(data))
                self.ui.product_table.setItem(row_index, column_index, item)
            # Add edit button in the last column
            edit_button = QPushButton('Edit')
            edit_button.setProperty("row", row_index)

            # Properly connect the button click event
            edit_button.clicked.connect(lambda checked, row=row_index: self.handle_edit_order(row))
            self.ui.product_table.setCellWidget(row_index, len(headers) - 2, edit_button)
            #edit_button.clearFocus()

            # Add add button in the last column
            plus_button = QPushButton('Add')
            plus_button.setProperty("row", row_index)
            plus_button.clicked.connect(lambda checked, row=row_index: self.handle_plus_order_inv(row))
            self.ui.product_table.setCellWidget(row_index, len(headers) - 1, plus_button)
            #plus_button.clearFocus()

        # Set the edit triggers (disable editing)
        self.ui.product_table.setEditTriggers(QTableWidget.NoEditTriggers)

        # Resize columns to fit content
        self.ui.product_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.product_table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        # Clear the selection
        self.ui.product_table.clearSelection()
        self.ui.product_table.verticalHeader().setVisible(False)

    def handle_plus_order_inv(self, row):
        rows = 0
        client_id_item = int(self.ui.product_table.item(row, 0).text())
        # client_id = client_id_item.text()
        # Get client name from product_table's first column at specified row
        client_name_item = self.ui.product_table.item(row, 1)  # Assuming client name is in the first column
        if client_name_item:
            client_name = client_name_item.text()
            self.ui.client_order_plus.setText(client_name)
        else:
            print(f"Error: No data found in row {row}")

        # Get bagtype name from product_table's first column at specified row
        bagtype = self.ui.product_table.item(row, 2)  # Assuming client name is in the first column
        if bagtype:
            type_bag = bagtype.text()
            self.ui.typer_order_plus.setText(type_bag)
        else:
            print(f"Error: No data found in row {row}")


        # Get deadline date from product_table's fourth column at specified row
        deadline_item = self.ui.product_table.item(row, 4)  # Assuming deadline date is in the fourth column
        if deadline_item:
            deadline_str = deadline_item.text()
            deadline_date = QDateTime.fromString(deadline_str,
                                                 "yyyy-MM-dd")  # Assuming the deadline format is "yyyy-MM-dd"
            self.ui.deadline_order_plus.setDate(deadline_date.date())
        else:
            print(f"Error: No data found in row {row}")

        priority_item = self.ui.product_table.item(row, 5)  # Assuming order quantity is in the third column
        if priority_item:
            item_priority = int(priority_item.text())
            self.ui.priority_order_plus.setValue(item_priority)
        else:
            print(f"Error: No data found in row {row}")

        deadline_details = self.db_manager.get_order_details(client_name, type_bag,
                                                             deadline_date.toString("yyyy-MM-dd"), item_priority)

        if deadline_details:
            # Set the retrieved deadline details to UI element
            self.ui.notes_order_plus.setText(deadline_details)
        else:
            print(
                f"Error: Failed to retrieve deadline details for {client_name}, {type_bag}, {deadline_str}, {item_priority}")



        try:
            # Assuming db_manager is an instance of DatabaseManager
            # Initialize or get db_manager instance

            # Query the CLIENT table to get client_id
            cursor = self.db_manager.connection.cursor()
            if not client_id_item:
                print(f"Error: Client '{client_name}' not found in database")
                return

            query = """
                SELECT 
                    order_quantity
                FROM 
                    orders
                WHERE 
                    client_id =%s;
            """
            cursor.execute(query, (client_id_item,))
            rows = cursor.fetchone()[0]
        except Exception as e: 
            print(f"Error executing database query: {e}")

        # Switch to the desired index in stackedWidget

        self.data = {
            'client_id': client_id_item,
            "order_quantity": rows
        }
        print(self.data)


        self.ui.stackedWidget.setCurrentIndex(22)

    def save_order_plus_action(self):
        reply = QMessageBox.question(self, 'Edit Order',
                                     f'Are you sure you want to add on this order?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        print(f"User reply: {reply}")
        if reply == QMessageBox.Yes:
            print(self.data)
            id = self.data['client_id']
            quantity = self.ui.quantity_order_plus.value()
            cursor = self.db_manager.connection.cursor()
            cursor.execute("""

            UPDATE orders SET order_quantity = order_quantity + %s WHERE client_id = %s;
            """,(quantity, id))
            self.show_production()

            action = f"Edited {id}'s order."
            self.db_manager.add_user_log(self.username, self.username_id, action)
            self.ui.quantity_order_plus.setValue(0)
        else:
            print("User cancelled")
            # Handle cancellation logic
    
    def save_edit_order(self):

        reply = QMessageBox.question(self, 'Edit Order',
                                     f'Are you sure you want to edit this order?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        print(f"User reply: {reply}")
        if reply == QMessageBox.Yes:
            print(self.data)
            data_name = self.data['name']
            data_details = self.data['deadline_details']
            deadline_id = self.db_manager.get_deadline_id(data_name, data_details)
            deadline = self.db_manager.get_deadline_detail(data_name, data_details)
            id = self.db_manager.get_order_id(data_name, deadline_id, deadline)
            name = self.ui.edit_client_name.text()
            bag_type = self.ui.edit_bag_type.text()
            order_quantity = self.ui.edit_order_quantity.value()
            deadline_date = self.ui.edit_order_deadline.date().toString("yyyy-MM-dd")
            priority = self.ui.edit_order_priority.value()
            print(f"id {id}")
            deadline_details = self.ui.edit_order_notes.toPlainText()

            self.db_manager.set_order(id, order_quantity, bag_type)
            self.db_manager.set_deadline(name, deadline_details, deadline_date, deadline[0][0], deadline[0][1], deadline[0][2])
            self.db_manager.set_client_detail(deadline_id, priority, name)
            # self.db_manager.set_order(self.ui.client_name_entry.text(),
            # self.ui.order_quantity_spinBox.text(), self.ui.bag_type_entry.text(),
            # deadline_date, self.ui.order_priority_spinBox.text(), self.ui.add_order_notes.toPlainText())
            self.ui.client_name_entry.setText("")
            self.ui.edit_bag_type.setText("")
            self.ui.edit_order_quantity.setValue(0)
            self.ui.edit_order_deadline.setDate(QDate.currentDate())
            self.db_manager.connection.commit()
            self.show_production()

            action = f"Edited {name}'s order."
            self.db_manager.add_user_log(self.username, self.username_id, action)
        else:
            print("User cancelled")
            # Handle cancellation logic

    def populate_raw_invent(self):
        # Call populate_orders from DatabaseManager to fetch orders data
        raw = self.db_manager.populate_raw_materials()

        # Define headers for the table
        headers = [ 'Name', 'Stocks', 'Safety Stock', 'Cost','Type','Supplier','Edit', 'Add']
        # Set the number of rows and columns
        self.ui.raw_inventory_table.setRowCount(len(raw))
        self.ui.raw_inventory_table.setColumnCount(len(headers))

        # Set the headers for the table
        self.ui.raw_inventory_table.setHorizontalHeaderLabels(headers)

        # Populate the table with fetched data
        for row_index, row_data in enumerate(raw):
            for column_index, data in enumerate(row_data):
                item = QTableWidgetItem(str(data))
                self.ui.raw_inventory_table.setItem(row_index, column_index, item)
            stocks = int(row_data[1]) 
            safety_stock = int(row_data[2]) 
            if (stocks - safety_stock) <= 20:
                # Change the background color of the row to indicate critical stock level
                for column_index in range(len(headers)):
                    item = self.ui.raw_inventory_table.item(row_index, column_index)
                    if item:
                        color = QColor('red')
                        color.setAlpha(128)  # Set the alpha value (128 for 50% opacity)
                        item.setBackground(color)
            # Add edit button in the last column
            edit_button = QPushButton('Edit')
            edit_button.setProperty("row", row_index)
            edit_button.clicked.connect(lambda checked, row=row_index: self.handle_edit_prod_raw(row))
            self.ui.raw_inventory_table.setCellWidget(row_index, len(headers) - 2, edit_button)
            #edit_button.clearFocus()

            # Add add button in the last column
            plus_button = QPushButton('Add')
            plus_button.setProperty("row", row_index)
            plus_button.clicked.connect(lambda checked, row=row_index: self.handle_plus_raw_inv(row))
            self.ui.raw_inventory_table.setCellWidget(row_index, len(headers) - 1, plus_button)
            #plus_button.clearFocus()

        # Set the edit triggers (disable editing)
        self.ui.raw_inventory_table.setEditTriggers(QTableWidget.NoEditTriggers)

        # Resize columns to fit content
        self.ui.raw_inventory_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.raw_inventory_table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.ui.raw_inventory_table.clearSelection()

    def handle_plus_raw_inv(self, row):
        material_name = self.ui.raw_inventory_table.item(row, 0)
        if material_name:
            name = material_name.text()
            print(name)
            self.ui.raw_name_plus.setText(name)
        else:
            print(f"Error: No data found in row {row}")

        # Get bagtype name from product_table's first column at specified row
        material_type = self.ui.raw_inventory_table.item(row, 4)  # Assuming client name is in the first column
        if material_type:
            type_bag = material_type.text()
            self.ui.raw_type_plus.setText(type_bag)
        else:
            print(f"Error: No data found in row {row}")

        stock_item = self.ui.raw_inventory_table.item(row, 1)  # Assuming order quantity is in the third column
        if stock_item:
            stock = int(stock_item.text())
            self.ui.edit_material_stock.setValue(stock)
        else:
            print(f"Error: No stock found in row {row}")

        # Get deadline date from product_table's fourth column at specified row
        safety_item = self.ui.raw_inventory_table.item(row, 2)  # Assuming deadline date is in the fourth column
        if safety_item:
            safety = int(safety_item.text())
            self.ui.raw_safety_plus.setValue(safety)
        else:
            print(f"Error: No safety found in row {row}")

        cost_item = self.ui.raw_inventory_table.item(row, 3)  # Assuming order quantity is in the third column
        if cost_item:
            cost = int(cost_item.text())
            print(cost)
            self.ui.raw_cost_plus.setValue(cost)
        else:
            print(f"Error: No cost found in row {row}")

        supplier_item = self.ui.raw_inventory_table.item(row, 5)  # Assuming order quantity is in the third column
        if supplier_item:
            supplier = supplier_item.text()
            self.ui.raw_supplier_plus.setText(supplier)
        else:
            print(f"Error: No data found in row {row}")
        self.data = {
            "name": name,
            "material_type": type_bag,
            "cost": cost,
            "stock": stock,
            "safety_stock": safety,
            "supplier": supplier
        }
        self.ui.stackedWidget.setCurrentIndex(21)

    def save_plus_raw_inv_action(self):
        print(f"abra {self.data}")
        stock = self.ui.raw_stock_plus.value()
        print(stock)
        reply = QMessageBox.question(self, 'Save Edit Finished Product',
                                     f'Are you sure you want to edit this product in the inventory?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        print(f"User reply: {reply}")

        if reply == QMessageBox.Yes:


            cursor = self.db_manager.connection.cursor()
            cursor.execute("""
                SELECT material_id FROM raw_material
                WHERE material_name = %s AND material_type =%s
                AND material_cost = %s AND material_stock = %s
                AND material_safety_stock = %s;
            """, (self.db_manager.cipher.encrypt(self.data['name']), self.db_manager.cipher.encrypt(self.data['material_type']),self.data['cost'], self.data['stock'], self.data['safety_stock']))
            id = cursor.fetchone()
            id = id[0]
            cursor.execute("UPDATE raw_material SET material_stock = material_stock + %s WHERE material_id = %s"
                           ,(stock, id))
            self.db_manager.connection.commit()

            # User logs
            action = f"Edited {self.data['name']} (material) in the raw materials inventory."
            self.db_manager.add_user_log(self.username, self.username_id, action)

            self.show_inventory()
        else:
            print("User cancelled")
            # Handle cancellation logic

    def handle_edit_prod_raw(self, row):
        # Implement your edit logic here
        print(f"Editing order at row {row}")
        print(f"Tite")
        # Get client name from product_table's first column at specified row
        material_name = self.ui.raw_inventory_table.item(row, 0)
        if material_name:
            name = material_name.text()
            print(name)
            self.ui.Edit_inventory_Materiel.setText(name)
        else:
            print(f"Error: No data found in row {row}")

        # Get bagtype name from product_table's first column at specified row
        material_type = self.ui.raw_inventory_table.item(row, 4)  # Assuming client name is in the first column
        if material_type:
            type_bag = material_type.text()
            self.ui.Edit_material_type.setText(type_bag)
        else:
            print(f"Error: No data found in row {row}")

        stock_item = self.ui.raw_inventory_table.item(row, 1)  # Assuming order quantity is in the third column
        if stock_item:
            stock = int(stock_item.text())
            self.ui.edit_material_stock.setValue(stock)
        else:
            print(f"Error: No stock found in row {row}")

        # Get deadline date from product_table's fourth column at specified row
        safety_item = self.ui.raw_inventory_table.item(row, 2)  # Assuming deadline date is in the fourth column
        if safety_item:
            safety = int(safety_item.text())
            self.ui.edit_safety_stock.setValue(safety)
        else:
            print(f"Error: No safety found in row {row}")

        cost_item = self.ui.raw_inventory_table.item(row, 3)  # Assuming order quantity is in the third column
        if cost_item:
            cost = int(cost_item.text())
            print(cost)
            self.ui.edit_material_cost.setValue(cost)
        else:
            print(f"Error: No cost found in row {row}")

        supplier_item = self.ui.raw_inventory_table.item(row, 5)  # Assuming order quantity is in the third column
        if supplier_item:
            supplier = supplier_item.text()
            self.ui.edit_material_supplier.setText(supplier)
        else:
            print(f"Error: No data found in row {row}")

        self.data = {
            "name": name,
            "material_type": type_bag,
            "cost": cost,
            "stock": stock,
            "safety_stock": safety,
            "supplier": supplier

        }

        self.ui.stackedWidget.setCurrentIndex(5)

    def save_edit_material(self):

        reply = QMessageBox.question(self, 'Edit Raw Material',
                                     f'Are you sure you want to edit the material information?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        print(f"User reply: {reply}")

        if reply == QMessageBox.Yes:

            print(self.data)
            name = self.ui.Edit_inventory_Materiel.text()
            mat_type = self.ui.Edit_material_type.text()
            stock = self.ui.edit_material_stock.value()
            cost = self.ui.edit_material_cost.value()
            safety = self.ui.edit_safety_stock.value()
            supplier = self.ui.edit_material_supplier.text()

            print(name, mat_type, stock, cost, safety, supplier,  self.data['name'],
                  self.data['material_type'], self.data['stock'])

            self.db_manager.set_raw_material(name, stock, mat_type,safety, cost, supplier,
                                             self.data['name'], self.data['material_type'], self.data['stock'])

            self.ui.add_material_type.setText("")
            self.ui.add_material_stock.setValue(0)
            self.ui.add_material_cost.setValue(0)
            self.ui.add_safety_stock.setValue(0)
            self.ui.add_material_supplier.setText("")
            self.db_manager.connection.commit()
            self.show_inventory()
            action = f"Edited {name} (material) in the raw materials inventory."
            self.db_manager.add_user_log(self.username, self.username_id, action)
        else:
            print("User cancelled")
            # Handle cancellation logic

    def populate_product_invent(self):
        # Call populate_orders from DatabaseManager to fetch orders data
        prod = self.db_manager.populate_product()

        # Define headers for the table
        headers = ['Bag Type', 'Quantity', 'Defective', 'Cost', 'Price', 'Profit', 'Edit', 'Add']
        # Set the number of rows and columns
        self.ui.product_inventory_table.setRowCount(len(prod))
        self.ui.product_inventory_table.setColumnCount(len(headers))

        # Set the headers for the table
        self.ui.product_inventory_table.setHorizontalHeaderLabels(headers)

        # Populate the table with fetched data
        for row_index, row_data in enumerate(prod):
            for column_index, data in enumerate(row_data):
                item = QTableWidgetItem(str(data))
                self.ui.product_inventory_table.setItem(row_index, column_index, item)

            # Add edit button in the second-to-last column
            edit_button = QPushButton('Edit')
            edit_button.setProperty("row", row_index)
            edit_button.clicked.connect(lambda checked, row=row_index: self.handle_edit_prod_inv(row))
            self.ui.product_inventory_table.setCellWidget(row_index, len(headers) - 2, edit_button)
            #edit_button.clearFocus()

            # Add add button in the last column
            plus_button = QPushButton('Add')
            plus_button.setProperty("row", row_index)
            plus_button.clicked.connect(lambda checked, row=row_index: self.handle_plus_prod_inv(row))
            self.ui.product_inventory_table.setCellWidget(row_index, len(headers) - 1, plus_button)
            #plus_button.clearFocus()

        # Set the edit triggers (disable editing)
        self.ui.product_inventory_table.setEditTriggers(QTableWidget.NoEditTriggers)

        # Resize columns to fit content
        self.ui.product_inventory_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.product_inventory_table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.ui.product_inventory_table.clearSelection()
        

    def handle_plus_prod_inv(self, row):
        bag_type_item = self.ui.product_inventory_table.item(row, 0)  # Assuming client name is in the first column
        quantity_item = self.ui.product_inventory_table.item(row, 1)
        defective_item = self.ui.product_inventory_table.item(row, 2)
        cost_item = self.ui.product_inventory_table.item(row, 3)
        price_item = self.ui.product_inventory_table.item(row, 4)

        if bag_type_item and quantity_item and defective_item and cost_item and price_item:
            bag_type = bag_type_item.text()
            quantity = int(quantity_item.text())
            defective = int(defective_item.text())
            cost = int(cost_item.text())
            price = int(price_item.text())

            self.ui.bag_type_plus.setText(bag_type)

            self.ui.defect_plus.setValue(defective)
            self.ui.prod_cost_plus.setValue(cost)
            self.ui.price_plus.setValue(price)

        self.data = {
            "bag_type": bag_type,
            "quantity": quantity,
            "defective": defective,
                "cost": cost,
                "price": price,
        }
        self.ui.stackedWidget.setCurrentIndex(20)

    def save_prod_plus_action(self):
        print(self.data)
        quantity = self.ui.quantity_product_plus.value()

        reply = QMessageBox.question(self, 'Save Edit Finished Product',
                                     f'Are you sure you want to edit this product in the inventory?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        print(f"User reply: {reply}")

        if reply == QMessageBox.Yes:
            cursor = self.db_manager.connection.cursor()
            cursor.execute("""
                SELECT product_id FROM product
                WHERE bag_type = %s AND product_quantity =%s
                AND product_defectives = %s AND product_cost = %s
                AND product_price = %s;
            """, (self.db_manager.cipher.encrypt(self.data['bag_type']),self.data['quantity'], self.data['defective'], self.data['cost'], self.data['price'] ))
            id = cursor.fetchone()
            id = id[0]
            cursor.execute("UPDATE product SET product_quantity = product_quantity + %s WHERE product_id = %s"
                           ,(quantity, id))
            self.db_manager.connection.commit()

            # User logs
            action = f"Edited {self.data['bag_type']} (bag type) information in the finished product"
            self.db_manager.add_user_log(self.username, self.username_id, action)

            self.show_inventory()
        else:
            print("User cancelled")
            # Handle cancellation logic
    def handle_edit_prod_inv(self, row):
        # Implement your edit logic here
        print(f"Editing order at row {row}")
        print('pinindot mo ako')
        bag_type_item = self.ui.product_inventory_table.item(row, 0)  # Assuming client name is in the first column
        quantity_item = self.ui.product_inventory_table.item(row, 1)
        defective_item = self.ui.product_inventory_table.item(row, 2)
        cost_item = self.ui.product_inventory_table.item(row, 3)
        price_item = self.ui.product_inventory_table.item(row, 4)

        if bag_type_item and quantity_item and defective_item and cost_item and price_item:
            bag_type = bag_type_item.text()
            quantity = int(quantity_item.text())
            defective = int(defective_item.text())
            cost = int(cost_item.text())
            price = int(price_item.text())

            self.ui.Edit_inventory_bag_type.setText(bag_type)
            self.ui.Edit_inventory_product_2.setValue(quantity)
            self.ui.edit_inventory_defective_2.setValue(defective)
            self.ui.edit_product_cost_2.setValue(cost)
            self.ui.edit_inventory_active_product_2.setValue(price)

            print(bag_type)
        else:
            print(f"Error: No data found in row {row}")

        self.data = {
            "bag_type": bag_type,
            "quantity": quantity,
            "defective": defective,
                "cost": cost,
                "price": price,
        }

        self.ui.stackedWidget.setCurrentIndex(3)




    def save_edit_product(self):
        print(self.data)
        bag_type = self.ui.Edit_inventory_bag_type.text()
        quantity = self.ui.Edit_inventory_product_2.value()
        defective = self.ui.edit_inventory_defective_2.value()
        cost = self.ui.edit_product_cost_2.value()
        price = self.ui.edit_inventory_active_product_2.value()

        reply = QMessageBox.question(self, 'Save Edit Finished Product',
                                     f'Are you sure you want to edit this product in the inventory?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        print(f"User reply: {reply}")

        if reply == QMessageBox.Yes:

            self.db_manager.set_product(bag_type, quantity, defective, cost, price, self.data["bag_type"],
                                        self.data["quantity"], self.data["defective"],
                                        self.data["cost"], self.data["price"])

            self.db_manager.connection.commit()

            # User logs
            action = f"Edited {bag_type} (bag type) information in the finished product"
            self.db_manager.add_user_log(self.username, self.username_id, action)

            self.show_inventory()
        else:
            print("User cancelled")
            # Handle cancellation logic

    def void_product(self):

        reply = QMessageBox.question(self, 'Void Finished Product',
                                     f'Are you sure you want to void this finished product?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        print(f"User reply: {reply}")

        if reply == QMessageBox.Yes:
            bag_type = self.ui.Edit_inventory_bag_type.text()
            self.db_manager.void_product(self.data["bag_type"],self.data["quantity"], self.data["defective"],self.data["cost"], self.data["price"])
            self.db_manager.connection.commit()
            self.show_inventory()

            # User logs
            action = f"Voided  {bag_type} from the finished product inventory."
            self.db_manager.add_user_log(self.username, self.username_id, action)
        else:
            print("User cancelled")
            # Handle cancellation logic

    def ratcliff_obershelp_similarity(self, str1, str2):
        return difflib.SequenceMatcher(None, str1, str2).ratio()

    def search_in_table(self, search_term, table):
        search_term_lower = search_term.lower()
        first_exact_match = None
        matched_perfect = False
        matching = []

        # Reset the background and text colors for all items
        for row in range(table.rowCount()):
            for column in range(table.columnCount()):
                item = table.item(row, column)
                if item is not None:
                    item.setBackground(QBrush(Qt.transparent))
                    item.setForeground(QBrush(QColor(Qt.black)))

        # Search for the term in the table
        for row in range(table.rowCount()):
            for column in range(table.columnCount()):
                item = table.item(row, column)
                if item is not None:
                    item_text = item.text().lower()
                    if item_text == search_term_lower:
                        matched_perfect = True
                        matching.append(item)

        for row in range(table.rowCount()):
            for column in range(table.columnCount()):
                item = table.item(row, column)
                if item is not None:
                    item_text = item.text().lower()
                    if matched_perfect and item in matching:
                        highlight_color = QColor(255, 255, 255, 128)  # RGBA color with 50% opacity (128/255)
                        item.setBackground(QBrush(highlight_color))
                        item.setForeground(QBrush(QColor("black")))
                        if first_exact_match is None:
                            first_exact_match = table.model().index(row, column)
                    elif self.ratcliff_obershelp_similarity(item_text, search_term_lower) >= 0.45 and not matched_perfect:
                        highlight_color = QColor(255, 255, 255, 128)
                        item.setBackground(QBrush(highlight_color))
                        item.setForeground(QBrush(QColor("black")))
                        if first_exact_match is None:
                            first_exact_match = table.model().index(row, column)

        if first_exact_match is not None:
            table.scrollTo(first_exact_match, QTableWidget.PositionAtCenter)

    def perform_search(self):
        search_term = self.ui.search_bar.text()
        current_index = self.ui.stackedWidget.currentIndex()

        if current_index == 0:
            self.search_in_table(search_term, self.ui.prod_table)
            self.search_in_table(search_term, self.ui.dashboard_weekly)
            self.search_in_table(search_term, self.ui.history_DB)
        elif current_index == 1:
            self.search_in_table(search_term, self.ui.product_inventory_table)
            self.search_in_table(search_term, self.ui.raw_inventory_table)
        elif current_index == 6:
            self.search_in_table(search_term, self.ui.table_transac)
        elif current_index == 9:
            self.search_in_table(search_term, self.ui.product_table)
        elif current_index == 13:
            self.search_in_table(search_term, self.ui.weekly_table)
        elif current_index == 14:
            self.search_in_table(search_term, self.ui.daily_table)
        elif current_index == 19:
            self.search_in_table(search_term, self.ui.user_logs_table)
        # Add more conditions if there are more tables to search in

    def fetch_data(self, query):
        connection = self.db_manager.connection
        return pd.read_sql(query, connection)

    def specific_date(self, state):
        if state == 2:  # 2 corresponds to Qt.Checked
            self.ui.report_start.setEnabled(True)
            self.ui.report_end.setEnabled(True)
        elif state == 0:  # 0 corresponds to Qt.Unchecked
            self.ui.report_start.setEnabled(False)
            self.ui.report_end.setEnabled(False)

    def specific_user_logs(self, state):
        if state == 2:  # 2 corresponds to Qt.Checked
            self.ui.user_logs_start.setEnabled(True)
            self.ui.user_logs_end.setEnabled(True)
        elif state == 0:  # 0 corresponds to Qt.Unchecked
            self.ui.user_logs_start.setEnabled(False)
            self.ui.user_logs_end.setEnabled(False)

    def draw_header_footer(self, c, width, height):
        # Header
        c.setFont('Helvetica-Bold', 16)
        c.drawCentredString(width / 2, height - 50, "Rexie Maris Bag Enterprise")
        c.setFont('Helvetica', 12)
        c.drawCentredString(width / 2, height - 70, "58 Gen. Ordoñez St, Marikina, 1800 Metro Manila")
        c.drawCentredString(width / 2, height - 90, "0908 450 6694")

        # Date Created
        c.setFont('Helvetica', 12)
        c.drawRightString(width - 30, height - 30, "Generated on: " + pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S"))

        # Generated By
        c.setFont('Helvetica', 12)
        c.drawString(30, height - 30, f"Generated by: {self.username} / {self.username_id}")


    def generate_pdf(self, report_data_list, file_name):
        # Create reports directory if it doesn't exist
        reports_dir = 'reports'
        if not os.path.exists(reports_dir):
            os.makedirs(reports_dir)
        
        # Set the file name and path
        file_name = file_name.replace(" ", "_").replace(":", "-")
        full_file_name = os.path.join(reports_dir, f"{file_name}_{pd.Timestamp.now().strftime('%Y-%m-%d_%H-%M-%S')}.pdf")
        
        c = canvas.Canvas(full_file_name, pagesize=letter)
        width, height = letter

        # Constants for margins
        top_margin = height - 120
        bottom_margin = 60  # Adjust bottom margin to avoid overlap with "Generated by"
        available_height = top_margin - bottom_margin

        y_position = top_margin
        self.draw_header_footer(c, width, height)

        for report_data, report_title in report_data_list:
            # Type of Report
            c.setFont('Helvetica-Bold', 12)
            c.drawString(30, y_position, "Type of Report: " + report_title)
            y_position -= 15

            # Data Table
            data = report_data.values.tolist()
            colnames = report_data.columns.tolist()
            table_data = [colnames] + data

            while table_data:
                table = Table(table_data)
                table_style = TableStyle([
                    ('BACKGROUND', (0, 0), (-1, 0), colors.white),
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
                    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                    ('FONTNAME', (0, 0), (-1, 0), 'Times-Roman'),
                    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                    ('BACKGROUND', (0, 1), (-1, -1), colors.white),
                    ('GRID', (0, 0), (-1, -1), 1, colors.black),
                    ('FONTNAME', (0, 1), (-1, -1), 'Times-Roman'),
                ])
                table.setStyle(table_style)

                # Calculate the table height
                table_width, table_height = table.wrapOn(c, width, available_height)

                if table_height > available_height:
                    # If the table is too tall for the current page, split the data
                    split_idx = 1  # Start with the header
                    accumulated_height = 0

                    for i, row in enumerate(table_data[1:], start=1):
                        _, row_height = Table([row]).wrapOn(c, width, available_height)
                        accumulated_height += row_height
                        if accumulated_height > available_height:
                            split_idx = i
                            break

                    if split_idx == 1:
                        split_idx = len(table_data)

                    # Draw the part of the table that fits on the current page
                    table_part = Table(table_data[:split_idx])
                    table_part.setStyle(table_style)
                    table_part.wrapOn(c, width, available_height)
                    table_part.drawOn(c, 30, y_position - table_part._height)

                    table_data = [table_data[0]] + table_data[split_idx:]

                    c.showPage()
                    self.draw_header_footer(c, width, height)
                    y_position = top_margin
                else:
                    table.wrapOn(c, width, available_height)
                    table.drawOn(c, 30, y_position - table_height)
                    y_position -= table_height + 50
                    break

        c.save()
        self.open_report(full_file_name)
    def generate_product_pdf_clicked(self):
        start_date = self.ui.report_start.date().toString('yyyy-MM-dd')
        end_date = self.ui.report_end.date().toString('yyyy-MM-dd')
        print(not self.ui.specify_report_date.isChecked())
        # not checked
        if not self.ui.specify_report_date.isChecked():
            sql_script = """
            
            SELECT 
                c.client_name "Name" , 
                c.client_priority "Priority", 
                o.bag_type "Bag Type", 
                o.order_quantity "Order quantity", 
                d.deadline_date "Deadline date", 
                d.deadline_details "Deadline details" 
            FROM 
                ORDERS o 
            JOIN 
                CLIENT c ON o.client_id = c.client_id 
            JOIN 
                DEADLINE d ON c.deadline_id = d.deadline_id
            ORDER BY
                order_id DESC;
            """
        else:
            sql_script = """
            
            SELECT 
                c.client_name "Client Name", 
                o.bag_type "Bag Type", 
                o.order_quantity "Quantity", 
                d.deadline_date "Date", 
                d.deadline_details "Details", 
                c.client_priority "Priority" 
            FROM 
                ORDERS o 
            JOIN 
                CLIENT c ON o.client_id = c.client_id 
            JOIN 
                DEADLINE d ON c.deadline_id = d.deadline_id
            WHERE
                DATE(d.deadline_date) BETWEEN '{}' AND '{}'
            ORDER BY
                o.order_id DESC;
            """.format(start_date, end_date)
        # Fetch data
        df = self.fetch_data(sql_script)
        
        # Decrypt string columns
        df = df.map(lambda x: self.db_manager.cipher.decrypt(x) if isinstance(x, str) else x)

        reports = [
                (df, "Product Report")
            ]
        self.generate_pdf(reports, "production_report.pdf")
        action = f"Generated production report."
        self.db_manager.add_user_log(self.username, self.username_id, action)

    def generate_stock_pdf_clicked(self):
        start_date = self.ui.report_start.date().toString('yyyy-MM-dd')
        end_date = self.ui.report_end.date().toString('yyyy-MM-dd')
        if not self.ui.specify_report_date.isChecked():
            sql_script = """
                SELECT 
                    material_name "Name", 
                    material_type "Type",  
                    material_cost "Cost", 
                    material_stock "Stock", 
                    material_safety_stock "Safety Stock", 
                    created_at "Date"
                FROM 
                    RAW_MATERIAL
                WHERE 
                    raw_material_active = 1
                ORDER BY 
                    created_at DESC;
            """
        else:
            sql_script = """
           SELECT 
                    material_name "Name", 
                    material_type "Type",  
                    material_cost "Cost", 
                    material_stock "Stock", 
                    material_safety_stock "Safety Stock", 
                    created_at "Date"
                FROM 
                    RAW_MATERIAL
                WHERE 
                    raw_material_active = 1 and DATE(created_at) BETWEEN '{}' and '{}' 
                ORDER BY 
                    created_at DESC;
            """.format(start_date, end_date)
        # Fetch data
        df = self.fetch_data(sql_script)

        # Decrypt string columns
        df = df.applymap(lambda x: self.db_manager.cipher.decrypt(x) if isinstance(x, str) else x)

        reports = [
                (df, "Stock Report")
            ]
        self.generate_pdf(reports, "stock_report.pdf")
        action = f"Generated stocks report."
        self.db_manager.add_user_log(self.username, self.username_id, action)

    def generate_user_logs_pdf_clicked(self):
        start_date = self.ui.user_logs_start.date().toString('yyyy-MM-dd')
        end_date = self.ui.user_logs_end.date().toString('yyyy-MM-dd')
        if not self.ui.specify_user_logs_date.isChecked():
            sql_script = """
            SELECT 
                    a.username_id "ID", 
                    a.username "Username",  
                    u.action "Action",
                    u.timestamp "Date"
                FROM 
                    user_logs u
                JOIN accounts a ON u.account_id = a.account_id
                
                ORDER BY 
                    timestamp DESC;
            """
        else:
             sql_script = """
            SELECT 
                    a.username_id "ID", 
                    a.username "Username",  
                    u.action "Action",
                    u.timestamp "Date"
                FROM 
                    user_logs u
                JOIN accounts a ON u.account_id = a.account_id
                WHERE DATE(u.timestamp) BETWEEN '{}' AND '{}'
                ORDER BY 
                    timestamp DESC;
            """.format(start_date,end_date)
        # Fetch data
        df = self.fetch_data(sql_script)

        # Decrypt string columns
        df = df.applymap(lambda x: self.db_manager.cipher.decrypt(x) if isinstance(x, str) else x)

        reports = [
                (df, "User Logs Report")
            ]
        self.generate_pdf(reports, "user_logs_report.pdf")
        action = f"Generated user logs report."
        self.db_manager.add_user_log(self.username, self.username_id, action)

    def generate_inventory_pdf_clicked(self):
        start_date = self.ui.report_start.date().toString('yyyy-MM-dd')
        end_date = self.ui.report_end.date().toString('yyyy-MM-dd')
        if not self.ui.specify_report_date.isChecked():
            sql_script = """
            SELECT 
                    material_name "Name", 
                    material_type "Type",  
                    material_cost "Cost", 
                    material_stock "Stock", 
                    material_safety_stock "Safety Stock", 
                    created_at "Date"
                FROM 
                    RAW_MATERIAL
                ORDER BY 
                    created_at DESC;
            """
        else:
            sql_script = """
           SELECT 
                    material_name "Name", 
                    material_type "Type",  
                    material_cost "Cost", 
                    material_stock "Stock", 
                    material_safety_stock "Safety Stock", 
                    created_at "Date"
                FROM 
                    RAW_MATERIAL
                WHERE 
                    DATE(created_at) BETWEEN '{}' and '{}' 
                ORDER BY 
                    created_at DESC;
            """.format(start_date, end_date)
        # Fetch data
        df = self.fetch_data(sql_script)

        # Decrypt string columns
        df = df.applymap(lambda x: self.db_manager.cipher.decrypt(x) if isinstance(x, str) else x)

        reports = [
                (df, "Inventory Report")
            ]
        self.generate_pdf(reports, "inventory_report.pdf")
        action = f"Generated a inventory report."
        self.db_manager.add_user_log(self.username, self.username_id, action)

    def generate_sales_pdf_clicked(self):
        start_date = self.ui.report_start.date().toString('yyyy-MM-dd')
        end_date = self.ui.report_end.date().toString('yyyy-MM-dd')
        if not self.ui.specify_report_date.isChecked():
            total_bag_sql = """
            SELECT 
                    o.bag_type,
                    SUM(o.order_quantity) AS total_order_quantity
                FROM 
                    orders o
                JOIN 
                    client c ON o.client_id = c.client_id
                GROUP BY 
                    o.bag_type;

            """
            total_client_sql = '''
                SELECT
                    c.client_name,
                    SUM(p.product_quantity * p.product_price) AS total_sales
                FROM
                    CLIENT c
                JOIN
                    ORDERS o ON c.client_id = o.client_id
                JOIN
                    PRODUCT p ON o.order_id = p.order_id
                GROUP BY
                    c.client_name;
            '''
        else:
            total_bag_sql = """
                SELECT 
                    o.bag_type,
                    SUM(o.order_quantity) AS total_order_quantity
                FROM 
                    orders o
                JOIN 
                    client c ON o.client_id = c.client_id
                WHERE DATE(o.created_at) BETWEEN '{}' and '{}'
                GROUP BY 
                    o.bag_type;

            """.format(start_date, end_date)
             
            total_client_sql = '''
                SELECT
                    c.client_name,
                    SUM(p.product_quantity * p.product_price) AS total_sales
                FROM
                    CLIENT c
                JOIN
                    ORDERS o ON c.client_id = o.client_id
                JOIN
                    PRODUCT p ON o.order_id = p.order_id
                WHERE DATE(o.created_at) BETWEEN '{}' and '{}'
                GROUP BY
                    c.client_name;
            '''.format(start_date, end_date)
        reports = [
            (self.fetch_data(total_bag_sql), "Total Sales by Bag Type"),
            (self.fetch_data(total_client_sql), "Total Sales by Client")
            # (self.fetch_data(financial_summary), "Financial Summary")
        ]
        for i in range(len(reports)):
            reports[i] = (reports[i][0].applymap(lambda x: self.db_manager.cipher.decrypt(x) if isinstance(x, str) else x), reports[i][1])
        self.generate_pdf(reports,"sales_report.pdf")
        action = f"Generated sales report."
        self.db_manager.add_user_log(self.username, self.username_id, action)

    # calendar
    def date_clicked(self, date):
        # Handle the date clicked event
        clicked_date_str = date.toString(Qt.ISODate)  # Convert QDate to ISO date string (YYYY-MM-DD)
        print(f"Date clicked: {clicked_date_str}")

        # Fetch data from daily_table where date matches clicked date
        schedules = self.db_manager.populate_deadline_now(clicked_date_str)
        print("hello")
        for row in schedules:
            print(row)

        # Define headers for the table
        headers = ['Deadline Name', 'Deadline Details', 'Deadline Date', 'Edit']
        # Set the number of rows and columns
        self.ui.daily_table.setRowCount(len(schedules))
        self.ui.daily_table.setColumnCount(len(headers))

        # Set the headers for the table
        self.ui.daily_table.setHorizontalHeaderLabels(headers)

        # Populate the table with fetched data
        for row_index, row_data in enumerate(schedules):
            for column_index, data in enumerate(row_data):
                item = QTableWidgetItem(str(data))
                self.ui.daily_table.setItem(row_index, column_index, item)

            # Add edit button in the last column
            edit_button = QPushButton('Edit')
            edit_button.setProperty("row", row_index)

            edit_button.clicked.connect(lambda checked, row=row_index: self.handle_edit_deadline_daily(row))
            self.ui.daily_table.setCellWidget(row_index, len(headers) - 1, edit_button)

            #edit_button.clearFocus()
        # Set the edit triggers (disable editing)
        self.ui.daily_table.setEditTriggers(QTableWidget.NoEditTriggers)

        # Resize columns to fit content
        self.ui.daily_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.daily_table.clearSelection()

        # Navigate to index 14 in stackedWidget
        self.ui.stackedWidget.setCurrentIndex(14)

    def populate_today(self):
        print("Today populated")
        # Assuming current_date is a QDate object
        current_date = QDate.currentDate()

        # Converting QDate to string
        now = current_date.toString("yyyy-MM-dd")
        schedules = self.db_manager.populate_deadline_daily(now)
        print("hello")
        for row in schedules:
            print(row)

        # Define headers for the table
        headers = ['Deadline Name', 'Deadline Details', 'Deadline Date', 'Edit']
        # Set the number of rows and columns
        self.ui.daily_table.setRowCount(len(schedules))
        self.ui.daily_table.setColumnCount(len(headers))

        # Set the headers for the table
        self.ui.daily_table.setHorizontalHeaderLabels(headers)

        # Populate the table with fetched data
        for row_index, row_data in enumerate(schedules):
            for column_index, data in enumerate(row_data):
                item = QTableWidgetItem(str(data))
                self.ui.daily_table.setItem(row_index, column_index, item)

            # Add edit button in the last column
            edit_button = QPushButton('Edit')
            edit_button.setProperty("row", row_index)

            edit_button.clicked.connect(lambda checked, row=row_index: self.handle_edit_deadline_daily(row))
            self.ui.daily_table.setCellWidget(row_index, len(headers) - 1, edit_button)

            #edit_button.clearFocus()
        # Set the edit triggers (disable editing)
        self.ui.daily_table.setEditTriggers(QTableWidget.NoEditTriggers)

        # Resize columns to fit content
        self.ui.daily_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.daily_table.clearSelection()


'''
    def display_schedules(self, schedules):
        scheds = self.db_manager.populate_deadline_daily()
        headers = ['deadline_name', "deadline_details", " deadline_date"]
        model = QStandardItemModel(len(scheds), len(headers))
        model.setHorizontalHeaderLabels(headers)
        # Populate the model with fetched data
        for row_index, row_data in enumerate(scheds):
            for column_index, data in enumerate(row_data):
                item = QStandardItem(str(data))
                model.setItem(row_index, column_index, item)
                # Set the model to the product_table in UI
        self.ui.daily_table.setModel(model)
        self.ui.daily_table.setEditTriggers(QTableView.NoEditTriggers)
        # Resize columns to fit content
        self.ui.daily_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

'''


'''
orders = self.db_manager.populate_orders()

        # Define headers for the table
        headers = [ 'Client Name', "Bag Type"," Order Quantity", "Deadline", "Priority"]

        # Create a QStandardItemModel and set headers
        model = QStandardItemModel(len(orders), len(headers))
        model.setHorizontalHeaderLabels(headers)

        # Populate the model with fetched data
        for row_index, row_data in enumerate(orders):
            for column_index, data in enumerate(row_data):
                item = QStandardItem(str(data))
                model.setItem(row_index, column_index, item)


        # Set the model to the product_table in UI
        self.ui.product_table.setModel(model)
        self.ui.product_table.setEditTriggers(QTableView.NoEditTriggers)
        # Resize columns to fit content
        self.ui.product_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        
        '''


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    # Set the initial view to the dashboard after showing the window
    window.show_dashboard()
    sys.exit(app.exec())
