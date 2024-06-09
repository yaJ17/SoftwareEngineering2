import mysql.connector
from mysql.connector import Error

class DatabaseManager:
    def __init__(self, host, user, password):
        
        self.host = host
        self.user = user
        self.password = password
        self.connection = None

    def connect_to_database(self, database=None):
        #Connect to MySQL database and set the connection object
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

    def create_schema(self):
        #Create a schema and insert dummy data
        if self.connection is None:
            print("No connection to the database.")
            return

        try:
            cursor = self.connection.cursor()
            # cursor.execute("DROP DATABASE IF EXISTS rexie")
            #cursor.execute("CREATE DATABASE rexie")
            cursor.execute("USE rexie")

            # SQL script to create schema
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
        except Error as e:
            print(f"Error: {e}")
    def add_dummy_data(self):
        cursor = self.connection.cursor()
        
        sql_script = '''
        INSERT INTO SUPPLIER (supplier_name, supplier_loc, supplier_contact)
            VALUES
            ('Supplier A', 'Location A', 'Contact A'),
            ('Supplier B', 'Location B', 'Contact B');

            INSERT INTO RAW_MATERIAL (material_name, material_available, material_type, material_color, material_cost, material_stock, material_safety_stock, supplier_id)
            VALUES
            ('Material A', 100, 'Type A', 'Color A', 50, 200, 20, 1),
            ('Material B', 200, 'Type B', 'Color B', 60, 300, 30, 2);

            INSERT INTO CLIENT (client_name, client_loc, client_contact)
            VALUES
            ('Client A', 'Location A', 'Contact A'),
            ('Client B', 'Location B', 'Contact B');

            INSERT INTO DEADLINE (deadline_name, deadline_details, deadline_date)
            VALUES
            ('Deadline A', 'Details A', '2024-12-31'),
            ('Deadline B', 'Details B', '2025-01-31');

            INSERT INTO ORDERS (client_id, deadline_id, order_quantity, order_progress, labor_allocation, order_style)
            VALUES
            (1, 1, 100, 0, 10, 'Style A'),
            (2, 2, 200, 50, 20, 'Style B');

            INSERT INTO PRODUCT (order_id, product_quantity, product_style, product_defectives, product_cost)
            VALUES
            (1, '100', 'Style A', 5, 500),
            (2, '200', 'Style B', 10, 1000);

            INSERT INTO SUBCONTRACTOR (order_id, order_quantity, product_style)
            VALUES
            (1, '100', 'Style A'),
            (2, '200', 'Style B');

            INSERT INTO USER_LOGS (user_id, action)
            VALUES
            (1, 'Created order'),
            (2, 'Updated product');


            INSERT INTO ACCOUNTS (username, password)
            VALUES
            (admin,admin)
            
        '''
        cursor.execute(sql_script)
    def print(self):
        table = "ACCOUNTS"
        if self.connection is None:
            print("No connection")
            return
        try:
            cursor = self.connection.cursor()
            sql_script1 = f'''
            SELECT * FROM {table}
            '''
            sql_script2= '''
            
            INSERT INTO ACCOUNTS (username, password)
            VALUES
            ("admin","admin")
            '''
            cursor.execute(sql_script2)
            self.connection.commit()
            cursor.execute(sql_script1)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        except Error as e:
            print(e)
    def close_connection(self):
        """Close the database connection."""
        if self.connection.is_connected():
            self.connection.close()
            print("Database connection closed")

