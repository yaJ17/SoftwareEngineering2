from PySide6.QtWidgets import QApplication, QMainWindow, QGridLayout, QPushButton, QLabel, QWidget, QVBoxLayout, QDateEdit, QCalendarWidget, QTextEdit, QSizePolicy, QHeaderView, QTableWidget, QTableWidgetItem, QHBoxLayout, QComboBox, QStackedWidget
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt, QDate

import pandas as pd
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableView
from PySide6 import QtWidgets
from PySide6.QtGui import QStandardItemModel, QStandardItem, QColor, QBrush
import os
from PySide6.QtCore import Qt
from PySide6.QtCore import QSize
from ui_main import Ui_MainWindow  # Replace 'your_ui_file' with the actual filename of your UI code
from databases.database import DatabaseManager
import difflib
from PySide6.QtWidgets import QPushButton

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import Table, TableStyle

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

        self.ui.weekly_calendar.clicked.connect(self.show_weekly_scheduling)
        self.ui.daily_calendar.clicked.connect(self.show_daily_scheduling)
        self.ui.return_calendar.clicked.connect(self.show_scheduling)
        self.ui.return_calendar_2.clicked.connect(self.show_scheduling)

        self.ui.add_order_button.clicked.connect(self.show_add_order)
        self.ui.cancel_add_order.clicked.connect(self.show_production)

        self.ui.add_product_button.clicked.connect(self.show_add_finished_product)
        self.ui.add_inventory_button.clicked.connect(self.show_add_raw_material)
        self.ui.cancel_add_invProduct.clicked.connect(self.show_inventory)
        self.ui.cancel_add_raw.clicked.connect(self.show_inventory)


        self.ui.prod_report_btn.clicked.connect(self.generate_product_pdf_clicked)
        self.ui.stocks_report_btn.clicked.connect(self.generate_stock_pdf_clicked)
        self.ui.inventory_report_btn.clicked.connect(self.generate_inventory_pdf_clicked)
        self.ui.sales_report_btn.clicked.connect(self.generate_sales_pdf_clicked)

        self.ui.save_add_order.clicked.connect(self.save_add_production_action)
        key = b'[Xd\xee[\\\x90\x8c\xc8t\xba\xe4\xe0\rR\x87\xe6\xbe\xce\x8a\x02lC6\xf7G\x15O\xca\x182\xd0'
        self.db_manager = DatabaseManager('localhost', 'root', 'admin', key)
        self.db_manager.connect_to_database()
        self.db_manager.create_schema_and_tables()
        self.ui.prod_button.clicked.connect(self.show_production)
        self.ui.search_bar.returnPressed.connect(self.perform_search)
        # Populate the product table before showing the window
        self.populate_deadline_table()

        # Show the window after populating the table
        self.show()

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
        # Call populate_orders from DatabasecManager to fetch orders data
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

    def save_add_production_action(self):
        # Call save_add_production_action from DatabasecManager to fetch orders data
        deadline_date = self.ui.order_deadline_dateEdit.date().toString("yyyy-MM-dd")
        self.db_manager.add_order(self.ui.client_name_entry.text(), self.ui.order_quantity_spinBox.text(), self.ui.bag_type_entry.text(), deadline_date, self.ui.order_priority_spinBox.text())
        self.ui.client_name_entry.setText("")
        self.ui.bag_type_entry.setText("")
        self.ui.order_quantity_spinBox.setValue(0)
        self.ui.order_deadline_dateEdit.setDate(QDate.currentDate())
        self.ui.order_priority_spinBox.setValue(0)
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

    # def save_add_material_invent(self):
    #     # Call save_add_production_action from DatabasecManager to fetch orders data
    #     # data include material_name, material_type, materia_stock, material_cost, material_safety_stock, supplier_name
    #     self.db_manager.add_raw_material(self.ui.material_name_entry.text(), self.ui.material_type_entry.text(), self.ui.material_stock_spinBox.text(), self.ui.material_cost_spinBox.text(), self.ui.material_safety_stock_spinBox.text(), self.ui.supplier_name_entry.text())
    #     self.ui.mate  rial_name_entry.setText("")
    #     self.ui.material_type_entry.setText("")
    #     self.ui.material_stock_spinBox.setValue(0)
    #     self.ui.material_cost_spinBox.setValue(0)
    #     self.ui.material_safety_stock_spinBox.setValue(0)
    #     self.ui.supplier_name_entry.setText("")
    #     self.populate_raw_invent()
        
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


    def ratcliff_obershelp_similarity(self, str1, str2):
       return difflib.SequenceMatcher(None, str1, str2).ratio()



    def search_in_table(self, search_term, table):
        model = table.model()
        first_exact_match = None
        search_term_lower = search_term.lower()
        matched_perfect = False  # Convert search term to lowercase
        matching = []

        for row in range(model.rowCount()):
            for column in range(model.columnCount()):
                item = model.item(row, column)
                item.setBackground(QBrush(Qt.transparent))  # Reset background color
                item.setForeground(QBrush(QColor(Qt.white)))  # Reset text color

        for row in range(model.rowCount()):
            for column in range(model.columnCount()):
                item = model.item(row, column)
                item_text = item.text().lower()
                if  item_text == search_term_lower:
                    matched_perfect = True
                    matching.append(item)
        for row in range(model.rowCount()):
            for column in range(model.columnCount()):
                item = model.item(row, column)
                item_text = item.text().lower()  # Convert item text to lowercase for comparison
                if matched_perfect and item in matching:
                    print(f"Item Text: {item_text}: search term: {search_term_lower}")
                    highlight_color = QColor(255, 255, 255, 128)  # RGBA color with 50% opacity (128/255)
                    item.setBackground(QBrush(highlight_color))
                    item.setForeground(QBrush(QColor("black")))
                    if first_exact_match is None:
                        first_exact_match = table.model().index(row, column)
                elif self.ratcliff_obershelp_similarity(item_text, search_term_lower) >= 0.45 and matched_perfect is False:
                    print(f"ratio: {self.ratcliff_obershelp_similarity(item_text, search_term_lower)} item searched: {search_term_lower}, text: {item_text}")
                    highlight_color = QColor(255, 255, 255, 128)  # RGBA color with 50% opacity (128/255)
                    item.setBackground(QBrush(highlight_color))
                    item.setForeground(QBrush(QColor("black")))
                    if first_exact_match is None:
                        first_exact_match = table.model().index(row, column)
                else:
                    item.setBackground(QBrush(Qt.transparent))  # Retain original background color
                    item.setForeground(QBrush(QColor(Qt.black)))  # Retain original text color

            if first_exact_match is not None:
                # Scroll to the first exact match
                table.scrollTo(first_exact_match, QtWidgets.QAbstractItemView.PositionAtCenter)






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
        # Add more conditions if there are more tables to search in



    def fetch_data(self, query):
        return pd.read_sql(query, self.db_manager.connection)

    def generate_pdf(self, report_data, report_title, file_name):
        c = canvas.Canvas(file_name, pagesize=letter)
        width, height = letter

        # Header
        c.setFont('Helvetica-Bold', 16)
        c.drawCentredString(width / 2, height - 50, "Rexie Maris Bag Enterprise")
        c.setFont('Helvetica', 12)
        c.drawCentredString(width / 2, height - 70, "58 Gen. Ordoñez St, Marikina, 1800 Metro Manila")
        c.drawCentredString(width / 2, height - 90, "0908 450 6694")
        
        # Type of Report and Date Created
        c.setFont('Helvetica-Bold', 12)
        c.drawString(30, height - 120, "Type of Report: " + report_title)
        c.drawString(30, height - 140, "Generated on: " +  pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S"))
        
        
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
        table.drawOn(c, (width - table_width) / 2, height - 200 - table_height)

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
        production_data = self.fetch_data(sql_script)
        self.generate_pdf(production_data,"Production Report", "production_report.pdf")

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
        stock_data = self.fetch_data(sql_script)
        self.generate_pdf(stock_data,"Stock Report", "stock_report.pdf")

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
        invent_data = self.fetch_data(sql)
        self.generate_pdf(invent_data,"Invetory Report", "invetory_report.pdf")

    def generate_sales_pdf_clicked(self):
            sql = """
                SELECT 
                C.client_name "Client", 
                O.order_quantity "Order", 
                O.order_progress "Progress", 
                O.bag_type "Type", 
                O.created_at "Date"
            FROM 
                ORDERS O
            JOIN 
                CLIENT C ON O.client_id = C.client_id
            WHERE 
                O.orders_active = 1
            ORDER BY 
                O.created_at DESC;
            """
            sales_data = self.fetch_data(sql)
            self.generate_pdf(sales_data,"Sales Report", "sales_report.pdf")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    # Set the initial view to the dashboard after showing the window
    window.show_dashboard()
    sys.exit(app.exec())
