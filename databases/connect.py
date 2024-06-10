import mysql.connector
from mysql.connector import Error
class DatabaseManager:
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.connection = None

    # CONNECTING TO THE DATABASE WITH OR WITHOUT THE GIVEN DATABASE NAME 
    def connect_to_database(self, database=None):
        try:
            if database:
                self.connection = mysql.connector.connect(
                    host=self.host,
                    database=database,
                    user=self.user,
                    password=self.password
                )
            else:
                self.connection = mysql.connector.connect(
                    host=self.host,
                    user=self.user,
                    password=self.password
                )
            if self.connection.is_connected():
                print("Connected to the database")
        except Error as e:
            print(f"Error: {e}")
            self.connection = None
    # CREATING SCHEMA IF NOT EXIST IT INCLUDES SCHEMA AND TABLES
    def create_schema_and_tables(self):
        if self.connection is None:
            print("No connection to the database.")
            return

        try:
            cursor = self.connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS rexie")
            cursor.execute("USE rexie")

            sql_script = '''
            CREATE TABLE IF NOT EXISTS SUPPLIER (
                supplier_id INT AUTO_INCREMENT PRIMARY KEY,
                supplier_name VARCHAR(100) NOT NULL,
                supplier_loc VARCHAR(100) NOT NULL,
                supplier_contact VARCHAR(100) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );

            CREATE TABLE IF NOT EXISTS RAW_MATERIAL (
                material_id INT AUTO_INCREMENT PRIMARY KEY,
                material_name VARCHAR(100) NOT NULL,
                material_available INT NOT NULL,
                material_type VARCHAR(100) NOT NULL,
                material_color VARCHAR(100) NOT NULL,
                material_cost INT NOT NULL,
                material_stock INT NOT NULL,
                material_safety_stock INT NOT NULL,
                supplier_id INT NOT NULL,
                FOREIGN KEY (supplier_id) REFERENCES SUPPLIER(supplier_id)
            );

            CREATE TABLE IF NOT EXISTS CLIENT (
                client_id INT AUTO_INCREMENT PRIMARY KEY,
                client_name VARCHAR(100) NOT NULL,
                client_loc VARCHAR(100) NOT NULL,
                client_contact VARCHAR(100) NOT NULL
            );

            CREATE TABLE IF NOT EXISTS DEADLINE (
                deadline_id INT AUTO_INCREMENT PRIMARY KEY,
                deadline_name VARCHAR(100) NOT NULL,
                deadline_details VARCHAR(100) NOT NULL,
                deadline_date DATE NOT NULL
            );

            CREATE TABLE IF NOT EXISTS ORDERS (
                order_id INT AUTO_INCREMENT PRIMARY KEY,
                client_id INT NOT NULL,
                deadline_id INT NOT NULL,
                order_quantity INT NOT NULL,
                order_progress INT NOT NULL,
                labor_allocation INT NOT NULL,
                order_style VARCHAR(100) NOT NULL,
                FOREIGN KEY (client_id) REFERENCES CLIENT(client_id),
                FOREIGN KEY (deadline_id) REFERENCES DEADLINE(deadline_id)
            );

            CREATE TABLE IF NOT EXISTS PRODUCT (
                product_id INT AUTO_INCREMENT PRIMARY KEY,
                order_id INT NOT NULL,
                product_quantity VARCHAR(100) NOT NULL,
                product_style VARCHAR(100) NOT NULL,
                product_defectives INT NOT NULL,
                product_cost INT NOT NULL,
                FOREIGN KEY (order_id) REFERENCES ORDERS(order_id)
            );

            CREATE TABLE IF NOT EXISTS SUBCONTRACTOR (
                subcon_id INT AUTO_INCREMENT PRIMARY KEY,
                order_id INT NOT NULL,
                order_quantity VARCHAR(100) NOT NULL,
                product_style VARCHAR(100) NOT NULL,
                FOREIGN KEY (order_id) REFERENCES ORDERS(order_id)
            );

            CREATE TABLE IF NOT EXISTS USER_LOGS (
                log_id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT NOT NULL,
                action VARCHAR(255) NOT NULL,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES CLIENT(client_id)
            );

            CREATE TABLE IF NOT EXISTS ACCOUNTS (
                account_id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(255) NOT NULL,
                password VARCHAR(255) NOT NULL
            );
            '''
            for statement in sql_script.split(';'):
                if statement.strip():
                    cursor.execute(statement)
            self.connection.commit()
            print("Schema created successfully.")
        except Error as e:
            print(f"Error: {e}")

    def add_dummy_data(self):
        if self.connection is None:
            print("No connection to the database.")
            return

        try:
            cursor = self.connection.cursor()
            
            # Insert into SUPPLIER
            supplier_sql = '''
            INSERT INTO SUPPLIER (supplier_name, supplier_loc, supplier_contact)
            VALUES
            ('Supplier A', 'Location A', 'Contact A'),
            ('Supplier B', 'Location B', 'Contact B');
            '''
            cursor.execute(supplier_sql)
            self.connection.commit()
            
            # Insert into RAW_MATERIAL
            raw_material_sql = '''
            INSERT INTO RAW_MATERIAL (material_name, material_available, material_type, material_color, material_cost, material_stock, material_safety_stock, supplier_id)
            VALUES
            ('Material A', 100, 'Type A', 'Color A', 50, 200, 20, 11),
            ('Material B', 200, 'Type B', 'Color B', 60, 300, 30, 2);
            '''
            cursor.execute(raw_material_sql)
            self.connection.commit()
            
            # Insert into CLIENT
            client_sql = '''
            INSERT INTO CLIENT (client_name, client_loc, client_contact)
            VALUES
            ('Client A', 'Location A', 'Contact A'),
            ('Client B', 'Location B', 'Contact B');
            '''
            cursor.execute(client_sql)
            self.connection.commit()
            
            # Insert into DEADLINE
            deadline_sql = '''
            INSERT INTO DEADLINE (deadline_name, deadline_details, deadline_date)
            VALUES
            ('Deadline A', 'Details A', '2024-12-31'),
            ('Deadline B', 'Details B', '2025-01-31');
            '''
            cursor.execute(deadline_sql)
            self.connection.commit()
            
            # Insert into ORDERS
            orders_sql = '''
            INSERT INTO ORDERS (client_id, deadline_id, order_quantity, order_progress, labor_allocation, order_style)
            VALUES
            (1, 1, 100, 0, 10, 'Style A'),
            (2, 2, 200, 50, 20, 'Style B');
            '''
            cursor.execute(orders_sql)
            self.connection.commit()
            
            # Insert into PRODUCT
            product_sql = '''
            INSERT INTO PRODUCT (order_id, product_quantity, product_style, product_defectives, product_cost)
            VALUES
            (1, '100', 'Style A', 5, 500),
            (2, '200', 'Style B', 10, 1000);
            '''
            cursor.execute(product_sql)
            self.connection.commit()
            
            # Insert into SUBCONTRACTOR
            subcontractor_sql = '''
            INSERT INTO SUBCONTRACTOR (order_id, order_quantity, product_style)
            VALUES
            (1, '100', 'Style A'),
            (2, '200', 'Style B');
            '''
            cursor.execute(subcontractor_sql)
            self.connection.commit()
            
            # Insert into USER_LOGS
            user_logs_sql = '''
            INSERT INTO USER_LOGS (user_id, action)
            VALUES
            (1, 'Created order'),
            (2, 'Updated product');
            '''
            cursor.execute(user_logs_sql)
            self.connection.commit()
            
            # Insert into ACCOUNTS
            accounts_sql = '''
            INSERT INTO ACCOUNTS (username, password)
            VALUES
            ('admin', 'admin');
            '''
            cursor.execute(accounts_sql)
            self.connection.commit()
            
            print("Dummy data added successfully.")
        except Error as e:
            print(f"Error: {e}")



    def print_accounts(self):
        if self.connection is None:
            print("No connection to the database.")
            return

        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM ACCOUNTS")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        except Error as e:
            print(f"Error: {e}")

    def check_account_login(self, username, password):
        if self.connection is None:
            print("No connection to the database.")
            return

        try:
            cursor = self.connection.cursor()
            sql_script = "SELECT username, password FROM ACCOUNTS WHERE username = %s AND password = %s"
            cursor.execute(sql_script, (username, password))
            result = cursor.fetchone()
            if result:
                print("Login successful")
            else:
                print("Invalid credentials")
        except Error as e:
            print(f"Error: {e}")

    def close_connection(self):
        if self.connection and self.connection.is_connected():
            self.connection.commit()
            self.connection.close()
            print("Database connection closed")
