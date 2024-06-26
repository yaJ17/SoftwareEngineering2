from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QMessageBox
from PySide6.QtCore import QDate
from PySide6.QtWidgets import QTableWidgetItem, QTableWidget, QHeaderView
import pandas as pd
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableView
from PySide6 import QtWidgets
from PySide6.QtGui import QStandardItemModel, QStandardItem, QColor, QBrush
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
from PySide6.QtCore import QDate, QDateTime
from register import RegisterWindow  # Adjust the import path as necessary
current_date = datetime.date.today()

class MainWindow(QMainWindow):
    def __init__(self, username):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(QSize(908, 463))  # Set the fixed size of the window

        self.current_date = datetime.date.today()
        self.ui.order_deadline_dateEdit.setDate(QDate(current_date.year, current_date.month, current_date.day))

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

        self.ui.weekly_calendar.clicked.connect(self.show_weekly_scheduling)
        self.ui.daily_calendar.clicked.connect(self.show_daily_scheduling)
        self.ui.return_calendar.clicked.connect(self.show_scheduling)
        self.ui.return_calendar_2.clicked.connect(self.show_scheduling)

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

        key = b'[Xd\xee[\\\x90\x8c\xc8t\xba\xe4\xe0\rR\x87\xe6\xbe\xce\x8a\x02lC6\xf7G\x15O\xca\x182\xd0'
        self.db_manager = DatabaseManager('localhost', 'root', 'admin', key)
        self.db_manager.connect_to_database()
        self.db_manager.create_schema_and_tables()
        #self.db_manager.add_dummy_data()
        self.ui.prod_button.clicked.connect(self.show_production)
        self.ui.search_bar.returnPressed.connect(self.perform_search)
        self.ui.edit_save_button.clicked.connect(self.save_edit_order)
        self.ui.update_edit_raw.clicked.connect(self.save_edit_material)
        self.ui.void_order.clicked.connect(self.void_production)
        self.ui.archive_raw.clicked.connect(self.void_material)

        # Populate the product table before showing the window
        self.populate_deadline_table()

        self.data = {}

        #calendar
        self.ui.calendarWidget.clicked.connect(self.date_clicked)
        self.schedules_table = QTableWidget(self)
        self.clicked_date = None

        # Show the window after populating the table
        self.show()
        self.ui.add_account.clicked.connect(self.show_register_window)

        self.ui.username_label.setText(username)
    def show_register_window(self):
        self.register_window = RegisterWindow()
        self.register_window.show()
    def show_dashboard(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.populate_deadline_table()

    def show_production(self):
        self.ui.stackedWidget.setCurrentIndex(9)
        self.populate_orders()

    def show_add_order(self):
        self.ui.stackedWidget.setCurrentIndex(10)


    def show_edit_order(self):
        self.ui.stackedWidget.setCurrentIndex(11)

    def show_scheduling(self):
        self.ui.stackedWidget.setCurrentIndex(12)

    def show_weekly_scheduling(self):
        self.ui.stackedWidget.setCurrentIndex(13)

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

    def show_help(self):
        self.ui.stackedWidget.setCurrentIndex(7)


    def show_about(self):
        self.ui.stackedWidget.setCurrentIndex(15)

    def show_maintenance(self):
        self.ui.stackedWidget.setCurrentIndex(8)

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
        # Call populate_orders from DatabaseManager to fetch orders data
        orders = self.db_manager.populate_orders()

        # Define headers for the table
        headers = ['Client Name', "Bag Type", "Order Quantity", "Deadline", 'Priority', "Edit"]

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
            self.ui.product_table.setCellWidget(row_index, len(headers) - 1, edit_button)

            edit_button.clearFocus()
        # Set the edit triggers (disable editing)
        self.ui.product_table.setEditTriggers(QTableWidget.NoEditTriggers)

        # Resize columns to fit content
        self.ui.product_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def handle_edit_order(self, row):
        # Implement your edit logic here
        print(f"Editing order at row {row}")

     
        # Get client name from product_table's first column at specified row
        client_name_item = self.ui.product_table.item(row, 0)  # Assuming client name is in the first column
        if client_name_item:
            client_name = client_name_item.text()
            self.ui.edit_client_name.setText(client_name)
        else:
            print(f"Error: No data found in row {row}")

        # Get bagtype name from product_table's first column at specified row
        bagtype = self.ui.product_table.item(row, 1)  # Assuming client name is in the first column
        if bagtype:
            type_bag = bagtype.text()
            self.ui.edit_bag_type.setText(type_bag)
        else:
            print(f"Error: No data found in row {row}")

        order_quantity_item = self.ui.product_table.item(row, 2)  # Assuming order quantity is in the third column
        if order_quantity_item:
            order_quantity = int(order_quantity_item.text())
            self.ui.edit_order_quantity.setValue(order_quantity)
        else:
            print(f"Error: No data found in row {row}")

        # Get deadline date from product_table's fourth column at specified row
        deadline_item = self.ui.product_table.item(row, 3)  # Assuming deadline date is in the fourth column
        if deadline_item:
            deadline_str = deadline_item.text()
            deadline_date = QDateTime.fromString(deadline_str,
                                                 "yyyy-MM-dd")  # Assuming the deadline format is "yyyy-MM-dd"
            self.ui.edit_order_deadline.setDate(deadline_date.date())
        else:
            print(f"Error: No data found in row {row}")

        priority_item = self.ui.product_table.item(row, 4)  # Assuming order quantity is in the third column
        if priority_item:
            item_priority = int(priority_item.text())
            self.ui.edit_order_priority.setValue(item_priority)
        else:
            print(f"Error: No data found in row {row}")


        #NOTES
        # Get client name and bag type from product_table
        client_name_item = self.ui.product_table.item(row, 0)  # Assuming client name is in the first column
        bag_type_item = self.ui.product_table.item(row, 1)  # Assuming bag type is in the second column


        client_name = client_name_item.text()
        bag_type = bag_type_item.text()

        try:
            # Assuming db_manager is an instance of DatabaseManager
            # Initialize or get db_manager instance


            # Query the CLIENT table to get client_id
            cursor = self.db_manager.connection.cursor()
            query_client_id = "SELECT client_id FROM CLIENT WHERE client_name = %s;"
            encrypted_client_name = self.db_manager.cipher.encrypt(client_name)
            cursor.execute(query_client_id, (encrypted_client_name,))
            client_id_row = cursor.fetchone()
            client_id = client_id_row[0] if client_id_row else None
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
                    C.client_name= %s;
            """
            cursor.execute(query, (encrypted_client_name,))
            row = self.db_manager.cipher.decrypt(cursor.fetchone()[0])
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
        deadline_date = self.ui.order_deadline_dateEdit.date().toString("yyyy-MM-dd")
        self.db_manager.add_order(self.ui.client_name_entry.text(), self.ui.order_quantity_spinBox.text(), self.ui.bag_type_entry.text(), deadline_date, self.ui.order_priority_spinBox.text(), self.ui.add_order_notes.toPlainText())
        print(self.ui.add_order_notes.toPlainText())
        self.ui.client_name_entry.setText("")
        self.ui.bag_type_entry.setText("")
        self.ui.order_quantity_spinBox.setValue(0)
        self.ui.order_deadline_dateEdit.setDate(QDate.currentDate())
        self.ui.order_priority_spinBox.setValue(0)
        self.populate_orders()
        self.ui.stackedWidget.setCurrentIndex(9)

    def void_production(self):
        client_id = self.db_manager.get_client_id(self.data["name"])
        self.db_manager.void_client(client_id)
        self.populate_orders()
        self.ui.stackedWidget.setCurrentIndex(9)
        
    # def save_add_finish_product_invent(self):
    #     # Call save_add_production_action from DatabasecManager to fetch orders data
    #     # data include bag type, quantity, no. of defectives, product cost, and product price
    #     self.db_manager.add_product(self.ui.bag_type_entry.text(), self.ui.product_quantity_spinBox.text(), self.ui.product_defective_spinBox.text(), self.ui.product_cost_spinBox.text(), self.ui.product_price_spinBox.text())
    #     self.ui.bag_type_entry.setText("")
    #     self.ui.product_quantity_spinBox.setValue(0)
    #     self.ui.product_defective_spinBox.setValue(0)
    #     self.ui.product_cost_spinBox.setValue(0)
    #     self.ui.product_price_spinBox.setValue(0)
    #     self.populate_product_invent()
    #     self.ui.stackedWidget.setCurrentIndex(1)

    def save_add_material_invent(self):
        # Call save_add_production_action from DatabasecManager to fetch orders data
        # data include material_name, material_type, materia_stock, material_cost, material_safety_stock, supplier_name
        name = self.ui.add_inventory_Materiel.text()
        mat_type = self.ui.add_material_type.text()
        stock = self.ui.add_material_stock.value()
        cost = self.ui.add_material_cost.value()
        safety = self.ui.add_safety_stock.value()
        supplier = self.ui.add_material_supplier.text()
        print(name, mat_type, stock, cost, safety, supplier)
        self.db_manager.add_raw_material(name,mat_type, stock, cost, safety, supplier)
        self.ui.add_inventory_Materiel.setText("")
        self.ui.add_material_type.setText("")
        self.ui.add_material_stock.setValue(0)
        self.ui.add_material_cost.setValue(0)
        self.ui.add_safety_stock.setValue(0)
        self.ui.add_material_supplier.setText("")
        self.show_inventory()

    def void_material(self):
        self.db_manager.void_raw_material(self.data['name'], self.data['supplier'])
        self.show_inventory()

    def populate_orders(self):
        # Call populate_orders from DatabaseManager to fetch orders data
        orders = self.db_manager.populate_orders()

        # Define headers for the table
        headers = ['Client Name', "Bag Type", "Order Quantity", "Deadline", 'Priority', "Edit"]

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
            self.ui.product_table.setCellWidget(row_index, len(headers) - 1, edit_button)

        # Set the edit triggers (disable editing)
        self.ui.product_table.setEditTriggers(QTableWidget.NoEditTriggers)

        # Resize columns to fit content
        self.ui.product_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Clear the selection
        self.ui.product_table.clearSelection()





    def handle_edit_prod_invent(self, row):
        # Implement your edit logic here
        print(f"Editing order at row {row}")
       
        self.ui.stackedWidget.setCurrentIndex(3)

    
    def save_edit_order(self):
        # Call save_add_production_action from DatabasecManager to fetch orders data
        print(self.data)
        data_name = self.data['name']
        data_details = self.data['deadline_details']
        id = self.db_manager.get_order_id(data_name)
        deadline_id = self.db_manager.get_deadline_id(data_name, data_details)
        name = self.ui.edit_client_name.text()
        bag_type = self.ui.edit_bag_type.text()
        order_quantity = self.ui.edit_order_quantity.value()
        deadline_date = self.ui.edit_order_deadline.date().toString("yyyy-MM-dd")
        priority = self.ui.edit_order_priority.value() 
        print(f"id {id}")
        deadline_details = self.ui.edit_order_notes.toPlainText()
        print(deadline_date)

        self.db_manager.set_order(id, order_quantity, bag_type)
        self.db_manager.set_deadline(deadline_id, name, deadline_details, deadline_date)
        self.db_manager.set_client_detail(deadline_id, priority, name)
        # self.db_manager.set_order(self.ui.client_name_entry.text(), self.ui.order_quantity_spinBox.text(), self.ui.bag_type_entry.text(), deadline_date, self.ui.order_priority_spinBox.text(), self.ui.add_order_notes.toPlainText())
        self.ui.client_name_entry.setText("")
        self.ui.bag_type_entry.setText("")
        self.ui.order_quantity_spinBox.setValue(0)
        self.ui.order_deadline_dateEdit.setDate(QDate.currentDate())
        self.db_manager.connection.commit()
        self.show_production()

    def populate_raw_invent(self):
        # Call populate_orders from DatabaseManager to fetch orders data
        raw = self.db_manager.populate_raw_materials()

        # Define headers for the table
        headers = [ 'Name', 'Stocks', 'Safety Stock', 'Cost','Type','Supplier','Edit']
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
                # Add edit button in the last column
            edit_button = QPushButton('Edit')
            edit_button.setProperty("row", row_index)

            edit_button.clicked.connect(lambda checked, row=row_index: self.handle_edit_prod_raw(row))
            self.ui.raw_inventory_table.setCellWidget(row_index, len(headers) - 1, edit_button)

        # Set the edit triggers (disable editing)
        self.ui.raw_inventory_table.setEditTriggers(QTableWidget.NoEditTriggers)

        # Resize columns to fit content
        self.ui.raw_inventory_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.raw_inventory_table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
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
        print(self.data)
        name = self.ui.Edit_inventory_Materiel.text()
        mat_type = self.ui.Edit_material_type.text()
        stock = self.ui.edit_material_stock.value()
        cost = self.ui.edit_material_cost.value()
        safety = self.ui.edit_safety_stock.value()
        supplier = self.ui.edit_material_supplier.text()
        print(name, mat_type, stock, cost, safety, supplier,  self.data['name'], self.data['material_type'], self.data['stock'])
        self.db_manager.set_raw_material(name, stock, mat_type,safety, cost, supplier, self.data['name'], self.data['material_type'], self.data['stock'])
        self.ui.add_material_type.setText("")
        self.ui.add_material_stock.setValue(0)
        self.ui.add_material_cost.setValue(0)
        self.ui.add_safety_stock.setValue(0)
        self.ui.add_material_supplier.setText("")
        self.db_manager.connection.commit()
        self.show_inventory()
        


    def populate_product_invent(self):
        # Call populate_orders from DatabaseManager to fetch orders data
        prod = self.db_manager.populate_product()

        # Define headers for the table
        headers = [ 'Bag Type', 'Quantity', 'Defective', 'Cost', 'Price' ,'Edit']
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
                # Add edit button in the last column
            edit_button = QPushButton('Edit')
            edit_button.setProperty("row", row_index)

            edit_button.clicked.connect(lambda checked, row=row_index: self.handle_edit_prod_inv(row))
            self.ui.product_inventory_table.setCellWidget(row_index, len(headers) - 1, edit_button)

        # Set the edit triggers (disable editing)
        self.ui.product_inventory_table.setEditTriggers(QTableWidget.NoEditTriggers)

        # Resize columns to fit content
        self.ui.product_inventory_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def handle_edit_prod_inv(self, row):
        # Implement your edit logic here
        print(f"Editing order at row {row}")
        print('pinindot mo ako')
        
        self.ui.stackedWidget.setCurrentIndex(5)


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
        elif current_index == 1:
            self.search_in_table(search_term, self.ui.product_inventory_table)
            self.search_in_table(search_term, self.ui.raw_inventory_table)
        elif current_index == 9:
            self.search_in_table(search_term, self.ui.product_table)
        elif current_index == 14:
            self.search_in_table(search_term, self.ui.daily_table)
        # Add more conditions if there are more tables to search in



    def fetch_data(self, query):
        return pd.read_sql(query, self.db_manager.connection)

    def generate_pdf(self, report_data_list, file_name):
        file_name = file_name.replace(" ", "_").replace(":", "-")
        full_file_name = f"{file_name}_{pd.Timestamp.now().strftime('%Y-%m-%d_%H-%M-%S')}.pdf"
        c = canvas.Canvas(full_file_name, pagesize=letter)
        width, height = letter

        # Header
        c.setFont('Helvetica-Bold', 16)
        c.drawCentredString(width / 2, height - 50, "Rexie Maris Bag Enterprise")
        c.setFont('Helvetica', 12)
        c.drawCentredString(width / 2, height - 70, "58 Gen. Ordoñez St, Marikina, 1800 Metro Manila")
        c.drawCentredString(width / 2, height - 90, "0908 450 6694")

        # Date Created
        c.setFont('Helvetica', 12)
        c.drawRightString(width - 30, height - 30, "Generated on: " + pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S"))

        y_position = height - 120
        for report_data, report_title in report_data_list:
            # Type of Report
            c.setFont('Helvetica-Bold', 12)
            c.drawString(30, y_position, "Type of Report: " + report_title)
            y_position -= 20

            # Data Table
            data = report_data.values.tolist()
            colnames = report_data.columns.tolist()

            table_data = [colnames] + data

            table = Table(table_data)
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ]))

            table_width, table_height = table.wrapOn(c, width, height)
            if table_width > width:
                table_width = width
            table.wrapOn(c, table_width, height)
            table.drawOn(c, (width - table_width) / 2, y_position - table_height - 10)

            y_position -= (table_height + 50)  # Space between tables

        c.save()

    def generate_product_pdf_clicked(self):
        sql_script = """
        SELECT  
                C.client_name "Name", 
                P.product_quantity "Quantity", 
                P.product_defectives "Defectives", 
                P.product_cost "Cost", 
                P.product_price "Price", 
                P.created_at "Date"
            FROM 
                PRODUCT P
            JOIN 
                ORDERS O ON P.order_id = O.order_id
            JOIN 
                CLIENT C ON O.client_id = C.client_id
            WHERE 
                P.product_active = 1
            ORDER BY 
                P.created_at DESC;
        """
        # Fetch data
        df = self.fetch_data(sql_script)

        # Decrypt string columns
        df = df.applymap(lambda x: self.db_manager.cipher.decrypt(x) if isinstance(x, str) else x)

        reports = [
                (df, "Product Report")
            ]
        self.generate_pdf(reports, "production_report.pdf")

    def generate_stock_pdf_clicked(self):
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
        # Fetch data
        df = self.fetch_data(sql_script)

        # Decrypt string columns
        df = df.applymap(lambda x: self.db_manager.cipher.decrypt(x) if isinstance(x, str) else x)

        reports = [
                (df, "Stock Report")
            ]
        self.generate_pdf(reports, "stock_report.pdf")

    def generate_inventory_pdf_clicked(self):
        sql = """
            SELECT 
                RM.material_name "Name", 
                RM.material_type "Type" ,  
                RM.material_cost "Cost", 
                RM.material_stock "Stock", 
                RM.material_safety_stock "Safety Stock", 
                S.supplier_name "Supplier",  
                RM.created_at "Date"
            FROM 
                RAW_MATERIAL RM
            JOIN 
                SUPPLIER S ON RM.supplier_id = S.supplier_id
            WHERE 
                RM.raw_material_active = 1
            ORDER BY 
                RM.created_at DESC;
        """
        # Fetch data
        df = self.fetch_data(sql)

        # Decrypt string columns
        df = df.applymap(lambda x: self.db_manager.cipher.decrypt(x) if isinstance(x, str) else x)

        reports = [
                (df, "Inventory Report")
            ]
        self.generate_pdf(reports, "inventory_report.pdf")

    def generate_sales_pdf_clicked(self):
        total_bag_sql = """
            SELECT
                p.bag_type,
                SUM(p.product_quantity * p.product_price) AS total_earnings
            FROM
                PRODUCT p
            GROUP BY
                p.bag_type;
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
        financial_summary = '''
            SELECT
                SUM(p.product_quantity * p.product_price) AS total_revenue,
                SUM(rm.material_cost * p.product_quantity) AS total_cost,
                SUM(p.product_quantity * p.product_price) - SUM(rm.material_cost * p.product_quantity) AS net_profit
            FROM
                PRODUCT p
            JOIN
                ORDERS o ON p.order_id = o.order_id
            JOIN
                RAW_MATERIAL rm ON o.material_id = rm.material_id;


        '''

        reports = [
            (self.fetch_data(total_bag_sql), "Total Sales by Bag Type"),
            (self.fetch_data(total_client_sql), "Total Sales by Client")
            # (self.fetch_data(financial_summary), "Financial Summary")
        ]
        for i in range(len(reports)):
            reports[i] = (reports[i][0].applymap(lambda x: self.db_manager.cipher.decrypt(x) if isinstance(x, str) else x), reports[i][1])
        self.generate_pdf(reports,"sales_report.pdf")



    #calendar
    def date_clicked(self, date):
        # Handle the date clicked event
        clicked_date_str = date.toString(Qt.ISODate)  # Convert QDate to ISO date string (YYYY-MM-DD)
        print(f"Date clicked: {clicked_date_str}")

        # Fetch data from daily_table where date matches clicked date
        schedules = self.db_manager.get_schedules_by_date(clicked_date_str)

        # Display fetched schedules in your QTableView (self.ui.daily_table)
        headers = ['deadline_name', "deadline_details", " deadline_date"]
        model = QStandardItemModel(len(schedules), len(headers))
        model.setHorizontalHeaderLabels(headers)
        # Populate the model with fetched data
        for row_index, row_data in enumerate(schedules):

            for column_index, data in enumerate(row_data):
                item = QStandardItem(str(data))
                model.setItem(row_index, column_index, item)
                # Set the model to the product_table in UI
        self.ui.daily_table.setModel(model)
        self.ui.daily_table.setEditTriggers(QTableView.NoEditTriggers)
        # Resize columns to fit content
        self.ui.daily_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        # Navigate to index 14 in stackedWidget
        self.ui.stackedWidget.setCurrentIndex(14)


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
