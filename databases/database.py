import mysql.connector
import re
from mysql.connector import Error
from databases.encrypt import DatabaseAES
import pandas as pd
import numpy as np
import openpyxl
from PySide6.QtWidgets import QPushButton


class DatabaseManager:
    def __init__(self, host, user, password, encryption_key):
        self.host = host
        self.user = user
        self.password = password
        self.encryption_key = encryption_key
        self.cipher = DatabaseAES(encryption_key)
        self.connection = None

    def connect_to_database(self, database=None):
        try:
            if database:
                self.connection = mysql.connector.connect(
                    host=self.host,
                    database=database,
                    user=self.user,
                    password=self.password,
                    auth_plugin='mysql_native_password'
                )
            else:
                self.connection = mysql.connector.connect(
                    host=self.host,
                    user=self.user,
                    password=self.password,
                    auth_plugin='mysql_native_password'
                )
            if self.connection.is_connected():
                print("Connected to the database")
        except Error as e:
            print(f"Error: {e}")
            self.connection = None

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
                supplier_name VARCHAR(256) NOT NULL,
                supplier_loc VARCHAR(256) NOT NULL,
                supplier_contact VARCHAR(256) NOT NULL,
                supplier_active BOOL DEFAULT 1,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );

            CREATE TABLE IF NOT EXISTS RAW_MATERIAL (
                material_id INT AUTO_INCREMENT PRIMARY KEY,
                material_name VARCHAR(256) NOT NULL,
                material_available INT NOT NULL,
                material_type VARCHAR(256) NOT NULL,
                material_color VARCHAR(256) NOT NULL,
                material_cost INT NOT NULL,
                material_stock INT NOT NULL,
                material_safety_stock INT NOT NULL,
                supplier_id INT NOT NULL,
                FOREIGN KEY (supplier_id) REFERENCES SUPPLIER(supplier_id),
                raw_material_active BOOL DEFAULT 1,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );

            CREATE TABLE IF NOT EXISTS DEADLINE (
                deadline_id INT AUTO_INCREMENT PRIMARY KEY,
                deadline_name VARCHAR(256) NOT NULL,
                deadline_details VARCHAR(256) NOT NULL,
                deadline_date DATE NOT NULL,
                deadline_active BOOL DEFAULT 1,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );

            CREATE TABLE IF NOT EXISTS CLIENT (
                client_id INT AUTO_INCREMENT PRIMARY KEY,
                client_name VARCHAR(256) NOT NULL,
                client_loc VARCHAR(256) NOT NULL,
                client_contact VARCHAR(256) NOT NULL,
                deadline_id INT NOT NULL,
                client_priority INT NOT NULL,
                client_active BOOL DEFAULT 1,
                FOREIGN KEY (deadline_id) REFERENCES DEADLINE(deadline_id),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            CREATE TABLE IF NOT EXISTS ORDERS (
                order_id INT AUTO_INCREMENT PRIMARY KEY,
                client_id INT NOT NULL,
                order_quantity INT NOT NULL,
                order_progress INT NOT NULL,
                bag_type VARCHAR(256) NOT NULL,
                FOREIGN KEY (client_id) REFERENCES CLIENT(client_id),
                orders_active BOOL DEFAULT 1,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );

            CREATE TABLE IF NOT EXISTS BAG_COMPONENT (
                bag_component_id INT AUTO_INCREMENT PRIMARY KEY,
                bag_component VARCHAR(256) NOT NULL,
                labor_allocation VARCHAR(256) NOT NULL,
                progress VARCHAR(256) NOT NULL,
                bag_type VARCHAR(256) NOT NULL,
                client_id INT NOT NULL,
                FOREIGN KEY (client_id) REFERENCES CLIENT(client_id),
                bag_component_active BOOL DEFAULT 1,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );

            CREATE TABLE IF NOT EXISTS PRODUCT (
                product_id INT AUTO_INCREMENT PRIMARY KEY,
                order_id INT NOT NULL,
                product_quantity INT NOT NULL,
                bag_type VARCHAR(256) NOT NULL,
                product_defectives INT NOT NULL,
                product_cost INT NOT NULL,
                product_price INT NOT NULL,
                FOREIGN KEY (order_id) REFERENCES ORDERS(order_id),
                product_active BOOL DEFAULT 1,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );

            CREATE TABLE IF NOT EXISTS SUBCONTRACTOR (
                subcon_id INT AUTO_INCREMENT PRIMARY KEY,
                order_id INT NOT NULL,
                order_quantity INT NOT NULL,
                bag_type VARCHAR(256) NOT NULL,
                FOREIGN KEY (order_id) REFERENCES ORDERS(order_id),
                subcontractor_active BOOL DEFAULT 1,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );

            CREATE TABLE IF NOT EXISTS ACCOUNTS (
                account_id INT AUTO_INCREMENT PRIMARY KEY,
                username_id VARCHAR(256) NOT NULL,
                username VARCHAR(256) NOT NULL,
                password VARCHAR(256) NOT NULL,
                secret_question VARCHAR(256) NOT NULL,
                secret_answer VARCHAR(256) NOT NULL,
                accounts_active BOOL DEFAULT 1,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                UNIQUE KEY (username_id)
            );

            CREATE TABLE IF NOT EXISTS USER_LOGS (
                log_id INT AUTO_INCREMENT PRIMARY KEY,
                account_id INT NOT NULL,
                action VARCHAR(256) NOT NULL,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (account_id) REFERENCES accounts(account_id),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );


            CREATE TABLE IF NOT EXISTS TRANSACTION_HISTORY (
                transaction_id INT AUTO_INCREMENT PRIMARY KEY,
                account_id VARCHAR(256) NOT NULL,
                action VARCHAR(256) NOT NULL,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
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

            # Insert dummy data for SUPPLIER
            suppliers = [
                (self.cipher.encrypt("Bitoy Supplier"), self.cipher.encrypt("Pasay City"), self.cipher.encrypt("09512949230")),
                (self.cipher.encrypt("Sweedny Silk Manufacturer"), self.cipher.encrypt("Marikina"), self.cipher.encrypt("09232592341")),
                (self.cipher.encrypt("Kindey Manufacturer"), self.cipher.encrypt("Paranaque City"), self.cipher.encrypt("09123784821")),
                (self.cipher.encrypt("BigBoy Buttons"), self.cipher.encrypt("Makati"), self.cipher.encrypt("09281283121")),
                (self.cipher.encrypt("Angel's Zipper"), self.cipher.encrypt("Pasig"), self.cipher.encrypt("09234678231"))
            ]
            cursor.executemany("INSERT INTO SUPPLIER (supplier_name, supplier_loc, supplier_contact) VALUES (%s, %s, %s)", suppliers)

            # Insert dummy data for RAW_MATERIAL
            raw_materials = [
                (self.cipher.encrypt("Denim"), 100, self.cipher.encrypt("Type A"), self.cipher.encrypt("Black"), 50, 200, 20, 1),
                (self.cipher.encrypt("Denim"), 200, self.cipher.encrypt("Type B"), self.cipher.encrypt("White"), 60, 300, 30, 2),
                (self.cipher.encrypt("Mesh"), 150, self.cipher.encrypt("Type B"), self.cipher.encrypt("Black"), 70, 250, 25, 3),
                (self.cipher.encrypt("Mesh"), 180, self.cipher.encrypt("Type B"), self.cipher.encrypt("White"), 80, 280, 28, 4),
                (self.cipher.encrypt("Silk"), 220, self.cipher.encrypt("Type A"), self.cipher.encrypt("Black"), 90, 320, 32, 5)
            ]
            cursor.executemany("INSERT INTO RAW_MATERIAL (material_name, material_available, material_type, material_color, material_cost, material_stock, material_safety_stock, supplier_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", raw_materials)

            # Insert dummy data for DEADLINE
            deadlines = [
                (self.cipher.encrypt("Straightforward"), self.cipher.encrypt("Details A"), "2024-12-31"),
                (self.cipher.encrypt("Nikey"), self.cipher.encrypt("Details B"), "2024-11-30"),
                (self.cipher.encrypt("Adibas"), self.cipher.encrypt("Details C"), "2024-10-31"),
                (self.cipher.encrypt("Celline"), self.cipher.encrypt("Details D"), "2024-09-30"),
                (self.cipher.encrypt("Hermand"), self.cipher.encrypt("Details E"), "2024-08-31")
            ]
            cursor.executemany("INSERT INTO DEADLINE (deadline_name, deadline_details, deadline_date) VALUES (%s, %s, %s)", deadlines)

            # Insert dummy data for CLIENT
            clients = [
                (self.cipher.encrypt("Straightforward"), self.cipher.encrypt("Marikina"), self.cipher.encrypt("09313992912"), 1, 1),
                (self.cipher.encrypt("Nikey"), self.cipher.encrypt("Marikina"), self.cipher.encrypt("09237817271"), 2, 2),
                (self.cipher.encrypt("Adibas"), self.cipher.encrypt("Pasig"), self.cipher.encrypt("09381233458"), 3, 3),
                (self.cipher.encrypt("Celline"), self.cipher.encrypt("Pasay"), self.cipher.encrypt("09812877167"), 4, 4),
                (self.cipher.encrypt("Hermand"), self.cipher.encrypt("Quezon"), self.cipher.encrypt("09271827161"), 5, 5)
            ]
            cursor.executemany("INSERT INTO CLIENT (client_name, client_loc, client_contact, deadline_id, client_priority) VALUES (%s, %s, %s, %s, %s)", clients)

            # Insert dummy data for ORDERS
            orders = [
                (1, 100, 0, self.cipher.encrypt("Bag Type A")),
                (2, 200, 10, self.cipher.encrypt("Bag Type B")),
                (3, 150, 20, self.cipher.encrypt("Bag Type C")),
                (4, 180, 30, self.cipher.encrypt("Bag Type D")),
                (5, 220, 40, self.cipher.encrypt("Bag Type E"))
            ]
            cursor.executemany("INSERT INTO ORDERS (client_id, order_quantity, order_progress, bag_type) VALUES (%s, %s, %s, %s)", orders)

            # Insert dummy data for BAG_COMPONENT
            bag_components = [
                (self.cipher.encrypt("Component A"), self.cipher.encrypt("Labor A"), self.cipher.encrypt("In Progress"), self.cipher.encrypt("Bag Type A"), 1),
                (self.cipher.encrypt("Component B"), self.cipher.encrypt("Labor B"), self.cipher.encrypt("Completed"), self.cipher.encrypt("Bag Type B"), 2),
                (self.cipher.encrypt("Component C"), self.cipher.encrypt("Labor C"), self.cipher.encrypt("Not Started"), self.cipher.encrypt("Bag Type C"), 3),
                (self.cipher.encrypt("Component D"), self.cipher.encrypt("Labor D"), self.cipher.encrypt("In Progress"), self.cipher.encrypt("Bag Type D"), 4),
                (self.cipher.encrypt("Component E"), self.cipher.encrypt("Labor E"), self.cipher.encrypt("Completed"), self.cipher.encrypt("Bag Type E"), 5)
            ]
            cursor.executemany("INSERT INTO BAG_COMPONENT (bag_component, labor_allocation, progress, bag_type, client_id) VALUES (%s, %s, %s, %s, %s)", bag_components)

            # Insert dummy data for PRODUCT
            products = [
                (1, 100, self.cipher.encrypt("Bag Type A"), 0, 500, 700),
                (2, 200, self.cipher.encrypt("Bag Type B"), 5, 600, 800),
                (3, 150, self.cipher.encrypt("Bag Type C"), 10, 550, 750),
                (4, 180, self.cipher.encrypt("Bag Type D"), 2, 580, 780),
                (5, 220, self.cipher.encrypt("Bag Type E"), 3, 620, 820)
            ]
            cursor.executemany("INSERT INTO PRODUCT (order_id, product_quantity, bag_type, product_defectives, product_cost, product_price) VALUES (%s, %s, %s, %s, %s, %s)", products)

            # Insert dummy data for SUBCONTRACTOR
            subcontractors = [
                (1, 50, self.cipher.encrypt("Bag Type A")),
                (2, 60, self.cipher.encrypt("Bag Type B")),
                (3, 70, self.cipher.encrypt("Bag Type C")),
                (4, 80, self.cipher.encrypt("Bag Type D")),
                (5, 90, self.cipher.encrypt("Bag Type E"))
            ]
            cursor.executemany("INSERT INTO SUBCONTRACTOR (order_id, order_quantity, bag_type) VALUES (%s, %s, %s)", subcontractors)

            # Insert dummy data for ACCOUNTS
            accounts = [
                (self.cipher.encrypt("RXAC1"), self.cipher.encrypt("rexiemaris"), self.cipher.encrypt("Rexiemaris1!"), self.cipher.encrypt("What was the name of your first pet?"), self.cipher.encrypt("Mora"))
            ]
            cursor.executemany("INSERT INTO ACCOUNTS (username_id, username, password, secret_question, secret_answer) VALUES (%s, %s, %s, %s, %s)", accounts)

            # Insert dummy data for USER_LOGS
            user_logs = [
                (1, self.cipher.encrypt("Login")),
                (1, self.cipher.encrypt("Logout")),
                (1, self.cipher.encrypt("Login")),
                (1, self.cipher.encrypt("Logout")),
                (1, self.cipher.encrypt("Login"))
            ]
            cursor.executemany("INSERT INTO USER_LOGS (account_id, action) VALUES (%s, %s)", user_logs)

            # Insert dummy data for TRANSACTION_HISTORY
            transaction_history = [
                (self.cipher.encrypt("major"), self.cipher.encrypt("Added Raw Material")),
                (self.cipher.encrypt("majormina A"), self.cipher.encrypt("Added Daedline")),
                (self.cipher.encrypt("major A"), self.cipher.encrypt("Added Deadline")),
                (self.cipher.encrypt("major A"), self.cipher.encrypt("Added Deadline")),
                (self.cipher.encrypt("major A"), self.cipher.encrypt("Edit Deadline"))
            ]
            cursor.executemany("INSERT INTO TRANSACTION_HISTORY (account_id, action) VALUES (%s, %s)", transaction_history)

            self.connection.commit()
            print("Dummy data inserted successfully.")
        except Error as e:
            print(f"Error: {e}")


    def get_account_username(self):
        if self.connection is None:
            print("No connection to the database.")
            return
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT username_id, username FROM ACCOUNTs LIMIT 1;")
            rows = cursor.fetchall()
            
            decrypted_rows = []
            for row in rows:
                decrypted_row = []
                for value in row:
                    if isinstance(value, str):  # Decrypt only if the value is a string
                        decrypted_value = self.cipher.decrypt(value)
                    else:
                        decrypted_value = value
                    decrypted_row.append(decrypted_value)
                decrypted_rows.append(tuple(decrypted_row))
                
            return decrypted_rows[0][0], decrypted_rows[0][1]
        except Error as e:
            print(f"Error: {e}")



   

    def populate_accounts(self) -> None:
        if self.connection is None:
            print("No connection to the database.")
            return
        
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM ACCOUNTS")
            rows = cursor.fetchall()

            for row in rows:
                
                encrypted_username = row[1]
                encrypted_password = row[2]
                
                # Decrypt the encrypted columns
                decrypted_username = self.cipher.decrypt(encrypted_username)
                decrypted_password = self.cipher.decrypt(encrypted_password)
                
                # Create a dictionary for better readability
                decrypted_row = {
                    'username': decrypted_username,
                    'password': decrypted_password
                }
                
                # Print the decrypted row
                print(decrypted_row)
        except Error as e:
            print(f"Error: {e}")

    def set_account_password(self, username, password, new_password, confirm_password):
        if self.connection is None:
            print("No connection to the database.")
            return

        try:
            cursor = self.connection.cursor()
            enc_username = self.cipher.encrypt(username)
            enc_password = self.cipher.encrypt(password)
            cursor.execute("SELECT username FROM ACCOUNTS WHERE username = %s AND password = %s", (enc_username, enc_password))
            result = cursor.fetchone()
            print(result)
            if result:
                if new_password == confirm_password:
                    sql_script = "UPDATE ACCOUNTS SET password = %s WHERE username = %s"
                    cursor.execute(sql_script, (self.cipher.encrypt(new_password), enc_username))
                    print("Password updated successfully.")
                else:
                    print("Invalid credentials or passwords do not match.")
        except Error as e:
            print(e)
    
    #kulang pa to ng result
    def populate_client(self):
        if self.connection is None:
            print("No connection to the database.")
            return
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
           SELECT 
                C.client_name,
                GROUP_CONCAT(O.bag_type SEPARATOR ', ') AS all_bag_styles,
                D.deadline_date,
                AVG(O.order_progress) AS average_order_progress
            FROM 
                CLIENT C
            JOIN 
                ORDERS O ON C.client_id = O.client_id
            JOIN
                DEADLINE D ON C.deadline_id = D.deadline_id
            WHERE 
                C.client_active = 1
            GROUP BY 
                C.client_name, D.deadline_date;
              
            """)
            rows = cursor.fetchall()

            for row in rows:
                
                client_name = row[0]
                bag_types = row[1]
                deadline = row[2]
                progress = row[3]
                
                # Decrypt the encrypted columns
                decrypted_name = self.cipher.decrypt(client_name)
                # decrypted_loc = self.cipher.decrypt(encrypted_loc)
                # decrypted_contact = self.cipher.decrypt(encrypted_contact)
                
                
                # Create a dictionary for better readability
                decrypted_row = {
                    'name': decrypted_name,
                    'bag types': bag_types,
                    'deadline': deadline,
                    'progress': progress
                }
                
                # Print the decrypted row
                print(decrypted_row)
        except Error as e:
            print(f"Error: {e}")

    #EDIT CLIENT DETAILS
    def set_client_detail(self, deadline_id,priority, name, loc="",contact="", ):
        if self.connection is None:
            print("No connection to the database.")
            return
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                SELECT client_id FROM client WHERE deadline_id = %s;
            ''',(deadline_id,))
            result = cursor.fetchone()
            print(result)
            if result:
                result = result[0]
                remaining_rows = cursor.fetchall()
                cursor.close()
                if  result:
                    sql_script = "UPDATE CLIENT SET client_name=%s, client_loc=%s, client_contact=%s, client_priority=%s WHERE client_id = %s"
                    cursor = self.connection.cursor()
                    cursor.execute(sql_script, (self.cipher.encrypt(name),loc,contact, priority, result))
                    print("Details updated successfully.")
                else:
                    print("Invalid client_id.")
        except Error as e:
            print(f"Error: {e}")

    '''
        ADDITION OF CLIENT
    '''
    def add_client(self, name, loc, contact, deadline_id, client_priority):
        if self.connection is None:
            print("No connection to the database.")
            return
        try:
            cursor = self.connection.cursor()
            cursor.execute(
            '''
            INSERT INTO CLIENT(
                client_name,
                client_loc,
                client_contact,
                deadline_id,
                client_priority
                )
            VALUES 
            (%s,%s,%s,%s, %s);
            '''
            ,(self.cipher.encrypt(name), self.cipher.encrypt(loc) , self.cipher.encrypt(contact), deadline_id, client_priority))
        except Error as e:
            print(f"Error: {e}")
    

    '''
        DELETING CLIENTS OR RESTORE CLIENT
    '''
    def void_client(self, client_id):
        if self.connection is None:
            print("No connection to the database.")
            return
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT client_active FROM CLIENT WHERE client_id = %s", (client_id,))
            result = cursor.fetchone()
            if result is not None:
                client_active = result[0]  
                reversed_client_active = 0 if client_active == 1 else 1 
                sql_script = "UPDATE CLIENT SET client_active = %s WHERE client_id = %s"
                cursor.execute(sql_script, (reversed_client_active, client_id))
                self.connection.commit()
        except Error as e:
            print(f"Error: {e}")
    '''
    # POPULATING ORDER ID, BAG TYPE, AND COMPLETION FOR LABELS
    '''

    def populate_orders(self) -> tuple:
        if self.connection is None:
            print("No connection to the database.")
            return
        try:
            cursor = self.connection.cursor()
            cursor.execute(
            '''
            SELECT 
                c.client_id,
                c.client_name, 
                o.bag_type, 
                o.order_quantity, 
                d.deadline_date, 
                c.client_priority
            FROM 
                CLIENT c
			
            JOIN 
                ORDERS o ON c.client_id = o.client_id
            JOIN 
                DEADLINE d ON c.deadline_id = d.deadline_id
			WHERE 
				c.client_active = 1
            ORDER BY 
                c.client_priority ASC, 
                d.deadline_date ASC;
            '''
            )
            rows = cursor.fetchall()
            
            decrypted_rows = []
            for row in rows:
                decrypted_row = []
                for value in row:
                    if isinstance(value, str):  # Decrypt only if the value is a string
                        decrypted_value = self.cipher.decrypt(value)
                    else:
                        decrypted_value = value
                    decrypted_row.append(decrypted_value)
                decrypted_rows.append(tuple(decrypted_row))
                
            return decrypted_rows
        except Error as e:
            print(f"Error: {e}")

    def populate_orders_transaction(self) -> tuple:
        if self.connection is None:
            print("No connection to the database.")
            return
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                '''
                SELECT 
                    c.client_name, 
                    o.bag_type, 
                    o.order_quantity, 
                    o.created_at,
                    d.deadline_date 
                 
                FROM 
                    CLIENT c

                JOIN 
                    ORDERS o ON c.client_id = o.client_id
                JOIN 
                    DEADLINE d ON c.deadline_id = d.deadline_id
                WHERE 
                    c.client_active = 1
                ORDER BY 
          
                    o.created_at DESC;
                '''
            )
            rows = cursor.fetchall()

            decrypted_rows = []
            for row in rows:
                decrypted_row = []
                for value in row:
                    if isinstance(value, str):  # Decrypt only if the value is a string
                        decrypted_value = self.cipher.decrypt(value)
                    else:
                        decrypted_value = value
                    decrypted_row.append(decrypted_value)
                decrypted_rows.append(tuple(decrypted_row))

            return decrypted_rows
        except Error as e:
            print(f"Error: {e}")

    def populate_history_DB(self) -> tuple:
        if self.connection is None:
            print("No connection to the database.")
            return
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                '''
                SELECT 
                    c.client_name, 
                    o.created_at
                FROM 
                    CLIENT c

                JOIN 
                    ORDERS o ON c.client_id = o.client_id
                JOIN 
                    DEADLINE d ON c.deadline_id = d.deadline_id
                WHERE 
                    c.client_active = 1
                ORDER BY 
                    o.created_at DESC;
                '''
            )
            rows = cursor.fetchall()

            decrypted_rows = []
            for row in rows:
                decrypted_row = []
                for value in row:
                    if isinstance(value, str):  # Decrypt only if the value is a string
                        decrypted_value = self.cipher.decrypt(value)
                    else:
                        decrypted_value = value
                    decrypted_row.append(decrypted_value)
                decrypted_rows.append(tuple(decrypted_row))

            return decrypted_rows
        except Error as e:
            print(f"Error: {e}")

    def get_order_id(self, name, id, detail):
        cursor = self.connection.cursor()
        cursor.execute("SELECT order_id FROM ORDERS WHERE client_id = (SELECT client_id FROM client WHERE client_name= %s and deadline_id = %s)", (self.cipher.encrypt(name),id))
        result = cursor.fetchone()[0]
        return result
    
    ''' 
            UPDATE CLIENT ORDER
                                                    '''   
    def set_order(self, order_id, quantity, bag_type):
        if self.connection is None:
            print("No connection to the database.")
            return
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                SELECT order_id FROM orders WHERE order_id = %s
            ''', (order_id,))
            result = cursor.fetchone()
            if result:
                if result[0] == order_id:
                    cursor.execute("UPDATE ORDERs SET order_quantity=%s, bag_type =%s WHERE order_id = %s",
                                    (quantity,self.cipher.encrypt(bag_type),order_id))
                    print("Details updated successfully.")
                else:
                    print("Invalid order.")

        except Error as e:
            print(f"Error: {e}")

    def add_order(self, client_name, order_quantity, bag_type, deadline_date, client_priority, deadline_details):
        if self.connection is None:
            print("No connection to the database.")
            return

        try:
            cursor = self.connection.cursor()

            # Encrypt deadline_name before adding to the database
            deadline_name = client_name
            encrypted_deadline_name = self.cipher.encrypt(deadline_name)
            encrypted_deadline_details = self.cipher.encrypt(deadline_details)
            self.add_deadline(deadline_name, deadline_details, deadline_date)
            print(f"deadline details: {deadline_details}")
            print(self.cipher.decrypt(encrypted_deadline_name))
            # Fetch the deadline_id
            cursor.execute("SELECT deadline_id FROM deadline WHERE deadline_name = %s AND deadline_date = %s and deadline_details = %s",
                           (encrypted_deadline_name, deadline_date,encrypted_deadline_details))
            deadline_result = cursor.fetchone()

            if deadline_result is None:
                print("Deadline not found.")
                return

            deadline_id = deadline_result[0]  # Extract the first element from the tuple
            print(f"Deadline ID: {deadline_id}")

            # Insert into CLIENT table
            encrypted_client_name = self.cipher.encrypt(client_name)
            self.add_client(client_name, "", "", deadline_id, client_priority)
            self.connection.commit()

            print(f"Fetching client_id for encrypted_client_name: {encrypted_client_name}, deadline_id: {deadline_id}")
            cursor.execute("SELECT client_id FROM CLIENT WHERE client_name = %s AND deadline_id = %s",
                           (encrypted_client_name, deadline_id))
            client_result = cursor.fetchone()
            if client_result is None:
                print("Client not found.")
                return

            client_id = client_result[0]  # Extract the first element from the tuple
            print(f"Client ID: {client_id}")

            # Insert into ORDERS table
            bag_type = self.cipher.encrypt(bag_type)
            cursor.execute('''
                INSERT INTO ORDERS(
                    client_id,
                    order_quantity, 
                    order_progress, 
                    bag_type
                )
                VALUES (%s, %s, %s, %s)
            ''', (client_id, order_quantity, 0, bag_type))

            # Commit the transaction
            self.connection.commit()

        except Error as e:
            print(f"Error: {e}")
            self.connection.rollback()  # Rollback the transaction in case of error

        finally:
            cursor.close()  # Ensure the cursor is closed

    '''
    MONTH AND YEAR DEFAULT BY 2024 and January for testing purposes
    '''
    def populate_deadline_by_month(self, month=12, year=2024):
        if self.connection is None:
            print("No connection to the database.")
            return
        try:
            cursor = self.connection.cursor()
            cursor.execute(
            '''
            SELECT 
                deadline_name,
                deadline_date
            FROM
                deadline
            WHERE
                MONTH(deadline_date) = %s
                AND YEAR(deadline_date) = %s;
            ''',
            (month, year)
            )
            rows = cursor.fetchall()
            for row in rows:
                print(self.cipher.decrypt(row[0]))
        except Error as e:
            print(f"Error: {e}")

    #FOR EDITING THE DEADLINE NAME, DETAIL, DATE, STATUS

    def populate_deadline_by_week(self):
        if self.connection is None:
            print("No connection to the database.")
            return
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                '''
                SELECT
                    deadline_name,
                    deadline_details,
                    deadline_date
                FROM
                    DEADLINE
                WHERE
                    YEARWEEK(deadline_date, 1) = YEARWEEK(CURDATE(), 1) and
                    deadline_active = 1
                ORDER BY
                    deadline_date ASC,
                    deadline_id DESC
                '''
            )
            rows = cursor.fetchall()
            decrypted_rows = []
            for row in rows:
                decrypted_row = tuple(self.cipher.decrypt(value) if isinstance(value, str) else value for value in row)
                decrypted_rows.append(decrypted_row)
                print(decrypted_row)
            return decrypted_rows
        except Error as e:
            print(f"Error: {e}")

    def populate_deadline(self) -> tuple:
        cursor = self.connection.cursor()
        cursor.execute("SELECT deadline_name, deadline_details, deadline_date FROM DEADLINE WHERE deadline_date >=CURDATE() and deadline_active = 1 ORDER BY deadline_date ASC, deadline_id DESC")
        rows = cursor.fetchall()

        decrypted_rows = []
        for row in rows:
            decrypted_row = tuple(self.cipher.decrypt(value) if isinstance(value, str) else value for value in row)
            decrypted_rows.append(decrypted_row)
            print(decrypted_row)

        return decrypted_rows

    def populate_deadline_now(self, date) -> tuple:
        cursor = self.connection.cursor()
        cursor.execute("SELECT deadline_name, deadline_details, deadline_date FROM DEADLINE WHERE deadline_date =%s  and deadline_active = 1 ORDER BY deadline_date ASC,deadline_id DESC", (date,))
        rows = cursor.fetchall()

        decrypted_rows = []
        for row in rows:
            decrypted_row = tuple(self.cipher.decrypt(value) if isinstance(value, str) else value for value in row)
            decrypted_rows.append(decrypted_row)
            print(decrypted_row)

        return decrypted_rows

    def get_deadline_detail(self, deadline_name, deadline_details):
        cursor = self.connection.cursor()
        cursor.execute("SELECT deadline_name, deadline_details, deadline_date FROM DEADLINE WHERE deadline_name = %s AND deadline_details = %s",
                       (self.cipher.encrypt(deadline_name), self.cipher.encrypt(deadline_details)))
        result = cursor.fetchall()
        decrypted_rows = []
        for row in result:
            decrypted_row = tuple(self.cipher.decrypt(value) if isinstance(value, str) else value for value in row)
            decrypted_rows.append(decrypted_row)
            print(decrypted_row)

        return decrypted_rows
    def get_deadline_id(self, deadline_name, deadline_details):
        cursor = self.connection.cursor()
        cursor.execute("SELECT deadline_id FROM DEADLINE WHERE deadline_name = %s AND deadline_details = %s",
                       (self.cipher.encrypt(deadline_name), self.cipher.encrypt(deadline_details)))
        result = cursor.fetchone()[0]
        return result
    def set_deadline(self,deadline_name, deadline_details, deadline_date, olddeadline_name, olddeadline_details, olddeadline_date):
        if self.connection is None:
            print("No connection to the database.")
            return
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                SELECT deadline_id FROM deadline WHERE deadline_name = %s and deadline_details = %s and deadline_date = %s
            ''', (self.cipher.encrypt(olddeadline_name), self.cipher.encrypt(olddeadline_details), olddeadline_date))
            deadline_id = cursor.fetchone()
            if deadline_id:
                deadline_id = deadline_id[0]
                remaining_rows = cursor.fetchall()
                cursor.close()
                cursor = self.connection.cursor()  # Reopen cursor for update
                cursor.execute("UPDATE deadline SET deadline_name =%s, deadline_details=%s,  deadline_date =%s WHERE deadline_id =%s",
                                    (self.cipher.encrypt(deadline_name), self.cipher.encrypt(deadline_details), deadline_date, deadline_id))
                print("Details updated successfully.")
            else:
                print("Invalid order.")

        except Error as e:
            print(f"Error: {e}")
    '''
                    ADD DEADLINE
                                                                '''
    def add_deadline(self, name, details, date):
        if self.connection is None:
            print("No connection to database")
        try:
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO deadline(deadline_name, deadline_details, deadline_date) VALUES(%s,%s,%s)", (self.cipher.encrypt(name), self.cipher.encrypt(details), date))
        except Error as e:
            print(f"Error: {e}")
    '''
                    POPULATE raw material INVENTORY
                                                                '''
    def void_deadline(self, deadline_name, deadline_details, date):
        if self.connection is None:
            print("No connection to the database.")
            return
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT deadline_id FROM deadline WHERE deadline_name =%s and deadline_details =%s and deadline_date =%s", 
                           (self.cipher.encrypt(deadline_name), self.cipher.encrypt(deadline_details), date))
            deadline_id = cursor.fetchone()[0]
            print(deadline_id)
            cursor.execute("SELECT deadline_active FROM deadline WHERE deadline_id = %s", (deadline_id,))
            result = cursor.fetchone()
            if result is not None:
                deadline_active = result[0]  
                reversed_deadline_active = 0 if deadline_active == 1 else 1 
                sql_script = "UPDATE deadline SET deadline_active = %s WHERE deadline_id = %s"
                cursor.execute(sql_script, (reversed_deadline_active, deadline_id))
        except Error as e:
            print(f"Error: {e}")

    def populate_raw_materials(self):
        if self.connection is None:
            print("No connection to the database.")
            return
        try:
            cursor = self.connection.cursor()
            cursor.execute(
            '''
            SELECT
                R.material_name,
                R.material_stock,
                R.material_safety_stock,
                R.material_cost,
                R.material_type,
                S.supplier_name

            FROM 
                RAW_MATERIAL R
            JOIN 
                SUPPLIER S ON R.supplier_id = S.supplier_id
			WHERE 
                R.raw_material_active = 1
            ORDER BY
                material_id DESC;
            '''
            )
            rows = cursor.fetchall()

            decrypted_rows = []
            for row in rows:
                decrypted_row = tuple(self.cipher.decrypt(value) if isinstance(value, str) else value for value in row)
                decrypted_rows.append(decrypted_row)
            
            return decrypted_rows
        except Error as e:
            print(f"Error: {e}")


    def set_raw_material(self, name,stock, mattype,safety_stock, cost, supplier_name, oldname, oldtype, oldstock):
        if self.connection is None:
            print("No connection to the databasep.")
            return
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                SELECT material_id FROM raw_material WHERE material_name = %s and material_type = %s and  material_stock=%s
            ''', (self.cipher.encrypt(oldname), self.cipher.encrypt(oldtype), oldstock))
            result = cursor.fetchone()
            print(result)
            material_id = result[0]
            remaining_rows = cursor.fetchall()
            cursor.close()
            if result:
                if result:
                    sql_script = '''
                    UPDATE RAW_MATERIAL SET
                        material_name = %s,
                        material_stock =%s,
                        material_type = %s,
                        material_safety_stock = %s,
                        material_cost = %s
                    WHERE material_id = %s;
                    '''
                    cursor = self.connection.cursor()  # Reopen cursor for update
                    cursor.execute(sql_script, 
                    (self.cipher.encrypt(name),stock,self.cipher.encrypt(mattype),safety_stock,cost,material_id))
                    sql_script = '''
                    UPDATE SUPPLIER SET
                        supplier_name = %s,
                        supplier_contact =%s
                    WHERE supplier_id = (SELECT supplier_id FROM raw_material WHERE material_id = %s);
                    '''
                    cursor.execute(sql_script, (self.cipher.encrypt(supplier_name),"", material_id))
                    print("Details updated successfully.")
                else:
                    print("Invalid order.")

        except Error as e:
            print(f"Error: {e}")

    def add_raw_material(self, name, materialtype, stock, cost, safety_stock, supplier_name, color="", available=0):
        if self.connection is None:
            print("No connection to the database.")
            return
        try:
            cursor = self.connection.cursor()

            # Check if the supplier already exists to avoid duplicate entries
            cursor.execute("SELECT supplier_id FROM supplier WHERE supplier_name = %s", (self.cipher.encrypt(supplier_name), ))
            result = cursor.fetchone()
            if result is None:
                # Insert the supplier
                cursor.execute(
                    """
                    INSERT INTO supplier(
                        supplier_name, 
                        supplier_loc,
                        supplier_contact
                    )
                    VALUES(%s, %s, %s)
                    """, (self.cipher.encrypt(supplier_name), self.cipher.encrypt(""),self.cipher.encrypt(""))
                )
                # Fetch the supplier_id after insertion
                cursor.execute("SELECT supplier_id FROM supplier WHERE supplier_name = %s", (self.cipher.encrypt(supplier_name),))
                result = cursor.fetchone()
            
                if result is None:
                    print("Supplier not found after insertion.")
                    return
            supplier_id = result[0]
            # Insert the raw material
            cursor.execute(
                '''
                INSERT INTO raw_material(
                    material_name,
                    material_available,
                    material_type,
                    material_color,
                    material_cost,
                    material_stock,
                    material_safety_stock,
                    supplier_id
                )
                VALUES 
                (%s, %s, %s, %s, %s, %s, %s, %s)
                ''',
                (self.cipher.encrypt(name), 0, self.cipher.encrypt(materialtype), self.cipher.encrypt(""), cost, stock, safety_stock, supplier_id)
            )

            # Commit the transaction
            self.connection.commit()

        except Error as e:
            print(f"Error: {e}")

        finally:
            cursor.close()  # Ensure the cursor is closed


    def void_raw_material(self, name, matname):
        if self.connection is None:
            print("No connection to the database.")
            return
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT r.material_id from raw_material r WHERE r.material_name = %s ", (self.cipher.encrypt(name),))
            material_id = cursor.fetchone()[0]
            cursor.execute("SELECT  raw_material_active FROM raw_material WHERE material_id = %s", (material_id,))
            result = cursor.fetchone()
            if result is not None:
                material_active = result[0]  
                reversed_raw_material_active = 0 if material_active == 1 else 1 
                sql_script = "UPDATE RAW_MATERIAL SET  raw_material_active = %s WHERE material_id = %s"
                cursor.execute(sql_script, (reversed_raw_material_active, material_id))
        except Error as e:
            print(f"Error: {e}")

    '''
                    POPULATE PRODUCT INVENTORY
                                                                '''
    def populate_product(self):
        if self.connection is None:
            print("No connection to the database.")
            return
        try:
            cursor = self.connection.cursor()
            cursor.execute(
            '''
            SELECT
                bag_type,
                product_quantity,
                product_defectives,
                product_cost,
                product_price,
                (product_price - product_cost) as profit
            FROM 
                PRODUCT
            WHERE
                product_active = 1
            ORDER BY
                product_id DESC;
            '''
            )
            rows = cursor.fetchall()

            decrypted_rows = []
            for row in rows:
                decrypted_row = tuple(self.cipher.decrypt(value) if isinstance(value, str) else value for value in row)
                decrypted_rows.append(decrypted_row)
            
            return decrypted_rows
        except Error as e:
            print(f"Error: {e}")

    '''
                    UPDATE PRODUCT INVENTORY
                                                                '''
    def set_product(self, bag_type, quantity, defective, cost, price, oldbag_type, oldquantity, olddefective, oldcost, oldprice):
        if self.connection is None:
            print("No connection to the database.")
            return
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                SELECT product_id FROM product WHERE bag_type = %s and product_quantity = %s and product_defectives = %s and product_cost = %s and product_price = %s
            ''', (self.cipher.encrypt(oldbag_type), oldquantity, olddefective, oldcost, oldprice))
            product_id = cursor.fetchone()
            print(product_id)
            if product_id:
                product_id = product_id[0]  # Extract the product_id from the tuple

                # Fetch all remaining results and close the cursor
                remaining_rows = cursor.fetchall()
                cursor.close()
                encrypted_bag_type = self.cipher.encrypt(bag_type)
                old = self.cipher.encrypt(oldbag_type)
                print(old)
                print(encrypted_bag_type)
                sql_script = '''
                    UPDATE product SET 
                    bag_type = %s,
                    product_quantity=%s, 
                    product_defectives = %s,
                    product_cost= %s,
                    product_price = %s
                    WHERE product_id = %s;

                    '''
                cursor = self.connection.cursor()  # Reopen cursor for update
                cursor.execute(sql_script, (encrypted_bag_type, quantity,defective,cost,price,product_id))
                print("Details updated successfully.")
            else:
                print("Invalid order.")

        except Error as e:
            print(f"Error: {e}")

    def add_product(self, bag_type,product_quantity, product_defectives,product_cost,product_price, order_id=1):
        if self.connection is None:
            print("No connection to the database.")
            return
        try:
            cursor = self.connection.cursor()
            cursor.execute(
            '''
            INSERT INTO product(
            order_id, 
            product_quantity, 
            bag_type,
            product_defectives,
            product_cost,
            product_price
                )
            VALUES 
            (%s,%s,%s,%s,%s,%s);
            '''
            ,(order_id, product_quantity, self.cipher.encrypt(bag_type),product_defectives,product_cost,product_price))
        except Error as e:
            print(f"Error: {e}")
    
    def void_product(self, bag_type,product_quantity, product_defectives,product_cost,product_price):
        if self.connection is None:   
            print("No connection to the database.")
            return
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                SELECT product_id, product_active FROM product WHERE bag_type = %s and product_quantity = %s and product_defectives = %s and product_cost = %s and product_price = %s
            ''', (self.cipher.encrypt(bag_type), product_quantity, product_defectives, product_cost, product_price))
            result = cursor.fetchone()
            if result is not None:
                material_active = result[1] 
                product_id = result[0]
                reversed_product_active = 0 if material_active == 1 else 1 
                sql_script = "UPDATE product SET  product_active = %s WHERE product_id = %s"
                cursor.execute(sql_script, (reversed_product_active, product_id))
        except Error as e:
            print(f"Error: {e}")

    def get_client_id(self, name, bag_type, quantity, deadline_date, priority):
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT
                c.client_id, 
                o.bag_type, 
                o.order_quantity, 
                d.deadline_date, 
                c.client_priority
            FROM 
                CLIENT c
			
            JOIN 
                ORDERS o ON c.client_id = o.client_id
            JOIN 
                DEADLINE d ON c.deadline_id = d.deadline_id
			WHERE 
				c.client_name = %s AND o.bag_type = %s
                AND o.order_quantity = %s AND 
                d.deadline_date = %s AND c.client_priority = %s AND c.client_active = 1 ;
        """, (name, bag_type, quantity, deadline_date, priority))
        result = cursor.fetchone()[0]
        return result
    def get_table_creation_order(self):
        # Order the tables based on foreign key dependencies
        return [
            "supplier",
            "raw_material",
            "deadline",
            "client",
            "orders",
            "bag_component",
            "product",
            "subcontractor",
            "accounts",
            "user_logs",
            "transaction_history"
        ]


    def fetch_table_data(self, table_name):
        try:
            query = f"SELECT * FROM {table_name}"
            df = pd.read_sql(query, self.connection)
            return df
        except Error as e:
            print(f"Error fetching data from {table_name}: {e}")
            return None

    def backup_database_to_excel(self, output_file):
        if self.connection is None:
            print("No connection to the database.")
            return

        try:
            # Fetch all table names
            cursor = self.connection.cursor()
            cursor.execute("SHOW TABLES")
            tables = cursor.fetchall()
            cursor.close()

            # Create a writer object
            with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
                for (table_name,) in tables:
                    df = self.fetch_table_data(table_name)
                    if df is not None:
                        df.to_excel(writer, sheet_name=table_name, index=False)

            print(f"Database backup completed. Saved to {output_file}")

        except Error as e:
            print(f"Error during database backup: {e}")


    def get_sql_type(self, dtype):
        if pd.api.types.is_integer_dtype(dtype):
            return "INT"
        elif pd.api.types.is_float_dtype(dtype):
            return "FLOAT"
        elif pd.api.types.is_bool_dtype(dtype):
            return "BOOL"
        elif pd.api.types.is_datetime64_any_dtype(dtype):
            return "DATETIME"
        else:
            return "VARCHAR(255)"

    def restore_database_from_excel(self, input_file):
        if self.connection is None:
            print("No connection to the database.")
            return

        try:
            xls = pd.ExcelFile(input_file)
            cursor = self.connection.cursor()

            # List of table names in the order of insertion
            table_names = xls.sheet_names
            table_creation_order = self.get_table_creation_order()

            # Drop all tables
            for table_name in reversed(table_creation_order):
                cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
                print(f"Dropped table: {table_name}")

            # Create tables in the correct order
            for table_name in table_creation_order:
                if table_name in table_names:

                    df = pd.read_excel(xls, sheet_name=table_name)
                    print(df)
                    # Convert timestamps to strings
                    for col in df.columns:
                        print(col)
                        if np.issubdtype(df[col].dtype, np.datetime64):
                            df[col] = df[col].dt.strftime('%Y-%m-%d %H:%M:%S')


                    create_table_query = self.generate_create_table_query(table_name, df)
                    cursor.execute(create_table_query)
                    print(f"Created table: {table_name}")

            # Insert data in the correct order
            # Insert data in the correct order
            for table_name in table_creation_order:
                if table_name in table_names:
                    df = pd.read_excel(xls, sheet_name=table_name)

                    for row in df.itertuples(index=False, name=None):
                        placeholders = ', '.join(['%s'] * len(row))
                        columns = ', '.join(df.columns)

                        # Convert timestamp columns to MySQL-compatible format
                        row = list(row)
                        for i, value in enumerate(row):
                            if isinstance(value, pd.Timestamp):
                                row[i] = value.strftime('%Y-%m-%d %H:%M:%S')

                        insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
                        cursor.execute(insert_query, row)

            self.connection.commit()
            cursor.close()
            print(f"Database restored from {input_file}")

        except Error as e:
            print(f"Error during database restore: {e}")

    def overwrite_restore(self, input_file):
        try:
            xls = pd.ExcelFile(input_file)
            cursor = self.connection.cursor()

            # Drop all existing tables
            self.drop_existing_tables(cursor)

            # Create schema and tables
            self.create_schema_and_tables()

            # Populate tables from Excel file


            # Commit the changes

            print("Database overwritten successfully.")

        except Exception as e:
            print(f"An error occurred: {e}")
            self.connection.rollback()

    def drop_existing_tables(self, cursor):
        # Define table names to drop
        table_names = [
            'user_logs', 'transaction_history', 'supplier', 'subcontractor',
            'raw_material', 'product', 'orders', 'deadline',
            'client', 'bag_component', 'accounts'
        ]

        # Drop all tables in reverse order
        for table_name in reversed(table_names):
            # Disable foreign key checks temporarily for this session
            cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
            cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
            print(f"Dropped table: {table_name}")

        # Re-enable foreign key checks
        cursor.execute("SET FOREIGN_KEY_CHECKS = 1")



    def generate_create_table_query(self, table_name, df):
        columns = []
        for column_name, dtype in zip(df.columns, df.dtypes):
            sql_type = self.get_sql_type(dtype)
            columns.append(f"{column_name} {sql_type}")

        columns_query = ", ".join(columns)
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_query})"
        return create_table_query


 



    def add_transaction(self, account_id, action):
        if self.connection is None:
            print("No connection to the database.")
            return
        try:
            cursor = self.connection.cursor()
            cursor.execute(
            '''
            INSERT INTO TRANSACTION_HISTORY(
                account_id, 
                action
                )
            VALUES 
            (%s,%s);
            '''
            ,(account_id, action))
        except Error as e:
            print(f"Error: {e}")

    def populate_transaction(self) -> tuple:
        if self.connection is None:
            print("No connection to the database.")
            return
        try:
            cursor = self.connection.cursor()
            cursor.execute(
            '''
            SELECT account_id, action, timestamp FROM transaction_history order by timestamp desc;
            '''
            )
            rows = cursor.fetchall()
            decrypted_rows = []
            for row in rows:
                decrypted_row = []
                for value in row:
                    if isinstance(value, str):  # Decrypt only if the value is a string
                        decrypted_value = self.cipher.decrypt(value)
                    else:
                        decrypted_value = value
                    decrypted_row.append(decrypted_value)
                decrypted_rows.append(tuple(decrypted_row))

            return decrypted_rows
        except Error as e:
            print(f"Error: {e}")

    def generate_production_report(self):
        if self.connection is None:
            print("No connection to the database.")
            return
        try:
            cursor = self.connection.cursor()
            cursor.execute(
            '''
            SELECT 
                P.product_id, 
                P.order_id, 
                C.client_name,
                P.product_quantity, 
                P.product_defectives, 
                P.product_cost, 
                P.product_price, 
                P.created_at
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
            '''
            )
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        except mysql.connector.Error as e:
            print(f"Error: {e}")


    def generate_stock_report(self):
        if self.connection is None:
            print("No connection to the database.")
            return
        try:
            cursor = self.connection.cursor()
            cursor.execute(
            '''
            SELECT 
                material_id, 
                material_name, 
                material_available, 
                material_type, 
                material_color, 
                material_cost, 
                material_stock, 
                material_safety_stock, 
                created_at
            FROM 
                RAW_MATERIAL
            WHERE 
                raw_material_active = 1
            ORDER BY 
                created_at DESC;
            '''
            )
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        except mysql.connector.Error as e:
            print(f"Error: {e}")


    def generate_inventory_report(self):
        if self.connection is None:
            print("No connection to the database.")
            return
        try:
            cursor = self.connection.cursor()
            cursor.execute(
            '''
            SELECT 
                RM.material_id, 
                RM.material_name, 
                RM.material_available, 
                RM.material_type, 
                RM.material_color, 
                RM.material_cost, 
                RM.material_stock, 
                RM.material_safety_stock, 
                S.supplier_name, 
                S.supplier_loc, 
                RM.created_at
            FROM 
                RAW_MATERIAL RM
            JOIN 
                SUPPLIER S ON RM.supplier_id = S.supplier_id
            WHERE 
                RM.raw_material_active = 1
            ORDER BY 
                RM.created_at DESC;
            '''
            )
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        except mysql.connector.Error as e:
            print(f"Error: {e}")

    def generate_sales_report(self):
        if self.connection is None:
            print("No connection to the database.")
            return
        try:
            cursor = self.connection.cursor()
            cursor.execute(
            '''
            SELECT 
                O.order_id, 
                C.client_name, 
                O.order_quantity, 
                O.order_progress, 
                O.bag_type, 
                O.created_at
            FROM 
                ORDERS O
            JOIN 
                CLIENT C ON O.client_id = C.client_id
            WHERE 
                O.orders_active = 1
            ORDER BY 
                O.created_at DESC;
            '''
            )
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        except mysql.connector.Error as e:
            print(f"Error: {e}")

    def get_schedules_by_date(self, date):
        cursor = self.connection.cursor()
        query = "SELECT deadline_name, deadline_details, deadline_date FROM deadline WHERE deadline_date = %s"
        cursor.execute(query, (date,))
        schedules = cursor.fetchall()

        decrypted_rows = []
        for row in schedules:
            decrypted_row = tuple(self.cipher.decrypt(value) if isinstance(value, str) else value for value in row)
            decrypted_rows.append(decrypted_row)
            print(decrypted_row)

        return decrypted_rows

    def populate_deadline_daily(self, date) -> tuple:
        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT deadline_name, deadline_details, deadline_date FROM DEADLINE WHERE deadline_date =%s  and deadline_active = 1 ORDER BY deadline_date ASC,deadline_id DESC",
            (date,))
        rows = cursor.fetchall()

        decrypted_rows = []
        for row in rows:
            decrypted_row = tuple(self.cipher.decrypt(value) if isinstance(value, str) else value for value in row)
            decrypted_rows.append(decrypted_row)
            print(decrypted_row)

        return decrypted_rows



    def get_username_id(self, input_value):
        cursor = self.connection.cursor()

        # Check if input_value is username or username_id
        if input_value.isdigit():  # Assume it's username_id
            sql_query = "SELECT username, username_id FROM ACCOUNTS WHERE username_id = %s"
        else:  # Assume it's username
            sql_query = "SELECT username, username_id FROM ACCOUNTS WHERE username = %s"

        try:
            cursor.execute(sql_query, (input_value,))
            result = cursor.fetchone()
            if result:
                username = self.cipher.decrypt(result[0])
                username_id = self.cipher.decrypt(result[1])
                return username, username_id
            else:
                return None, None
        except Error as e:
            print(f"Error fetching username and username_id: {e}")
            return None, None

     #validate login
    def check_account_login(self, username, password) -> bool:
        if self.connection is None:
            print("No connection to the database.")
            return False

        try:
            cursor = self.connection.cursor()
            enc_username = self.cipher.encrypt(username)
            enc_password = self.cipher.encrypt(password)

            sql_script = "SELECT username, password FROM ACCOUNTS WHERE username = %s AND password = %s"

            cursor.execute(sql_script, (enc_username, enc_password))
            result = cursor.fetchone()
            if result:
                print("Login successful")
                return True
            else:
                print("Invalid credentials")
                return False
        except Error as e:
            print(f"Error: {e}")
            return False

    def check_account_login_by_id(self, username_id, password) -> bool:
        if self.connection is None:
            print("No connection to the database.")
            return False

        try:
            cursor = self.connection.cursor()
            enc_username_id = self.cipher.encrypt(username_id)
            enc_password = self.cipher.encrypt(password)

            sql_script = "SELECT username_id, password FROM ACCOUNTS WHERE username_id = %s AND password = %s"

            cursor.execute(sql_script, (enc_username_id, enc_password))
            result = cursor.fetchone()
            if result:
                print("Login successful")
                return True
            else:
                print("Invalid credentials")
                return False
        except Error as e:
            print(f"Error: {e}")
            return False

    def get_username_id(self, username, password):
        if self.connection is None:
            print("No connection to the database.")
            return None

        try:
            cursor = self.connection.cursor()

            # Encrypt username and password
            encrypted_username = self.cipher.encrypt(username)
            encrypted_password = self.cipher.encrypt(password)

            # Execute query to fetch username_id
            query = "SELECT username_id FROM ACCOUNTS WHERE username = %s AND password = %s"
            cursor.execute(query, (encrypted_username, encrypted_password))

            # Fetch the result
            result = cursor.fetchone()

            if result:
                # Decrypt and return username_id
                decrypted_username_id = self.cipher.decrypt(result[0])
                return decrypted_username_id
            else:
                print("Username and password combination not found.")
                return None

        except Error as e:
            print(f"Error while retrieving username_id: {e}")
            return None

    def get_username_by_id_and_password(self, username_id, password):
        if self.connection is None:
            print("No connection to the database.")
            return None

        try:
            cursor = self.connection.cursor()

            # Encrypt username_id and password
            encrypted_username_id = self.cipher.encrypt(username_id)
            encrypted_password = self.cipher.encrypt(password)

            # Execute query to fetch username
            query = "SELECT username FROM ACCOUNTS WHERE username_id = %s AND password = %s"
            cursor.execute(query, (encrypted_username_id, encrypted_password))

            # Fetch the result
            result = cursor.fetchone()

            if result:
                # Decrypt and return username
                decrypted_username = self.cipher.decrypt(result[0])
                return decrypted_username
            else:
                print("Username ID and password combination not found.")
                return None

        except Error as e:
            print(f"Error while retrieving username: {e}")
            return None

    def check_username_exists(self, username):
        if self.connection is None:
            print("No connection to the database.")
            return False

        try:
            cursor = self.connection.cursor()

            encrypted_username = self.cipher.encrypt(username)
            # Execute query to check if username exists
            query = "SELECT COUNT(*) FROM ACCOUNTS WHERE username = %s"
            cursor.execute(query, (encrypted_username,))

            # Fetch the result
            result = cursor.fetchone()[0]

            # Check if username count is greater than 0
            if result > 0:
                return True
            else:
                return False

        except Error as e:
            print(f"Error while checking username existence: {e}")
            return False

    def check_usernameid_exists(self, usernameid):
        if self.connection is None:
            print("No connection to the database.")
            return False

        try:
            cursor = self.connection.cursor()

            encrypted_usernameid = self.cipher.encrypt(usernameid)
            # Execute query to check if username_id exists
            query = "SELECT COUNT(*) FROM ACCOUNTS WHERE username_id = %s"
            cursor.execute(query, (encrypted_usernameid,))

            # Fetch the result
            result = cursor.fetchone()[0]

            # Check if username_id count is greater than 0
            if result > 0:
                return True
            else:
                return False

        except Error as e:
            print(f"Error while checking username_id existence: {e}")
            return False

    def add_account(self, username, password, question, answer):
        if self.connection is None:
            print("No connection to the database.")
            return
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT username_id FROM ACCOUNTS ORDER BY created_at DESC LIMIT 1")
            encrypted_last_id = cursor.fetchone()[0]
            last_id = self.cipher.decrypt(encrypted_last_id)
            print(last_id)
            if last_id and last_id.startswith('RXAC'):
                numeric_part = last_id[4:]
                if numeric_part.isdigit():
                    new_id = "RXAC" + str(int(numeric_part) + 1)
                else:
                    print(f"Unexpected format for username_id: {last_id}")
                    return
            else:
                new_id = "RXAC1"

            username_register = self.cipher.encrypt(username)

            cursor.execute("SELECT username FROM ACCOUNTS WHERE username = %s", (username_register,))
            username_exist = cursor.fetchone()
            if username_exist is None:
                # Validate password criteria
                 # Encrypt the data before insertion
                enc_id = self.cipher.encrypt(new_id)
                enc_password = self.cipher.encrypt(password)
                enc_question = self.cipher.encrypt(question)
                enc_answer = self.cipher.encrypt(answer)

                cursor.execute(
                    "INSERT INTO ACCOUNTS (username_id, username, password, secret_question, secret_answer) VALUES (%s,%s, %s,%s,%s);",
                    (enc_id, username_register, enc_password, enc_question, enc_answer))
                self.connection.commit()  # Don't forget to commit the transaction
                print("Account added successfully.")

            else:
                print("Username already exists.")
        except Error as e:
            print(f"Error: {e}")

    def validate_user_for_reset(self, username, question, answer):
        if self.connection is None:
            print("No connection to the database.")
            return False
        try:
            cursor = self.connection.cursor()
            enc_username = self.cipher.encrypt(username)
            cursor.execute("SELECT username, secret_question, secret_answer FROM ACCOUNTS WHERE username = %s",
                           (enc_username,))
            result = cursor.fetchone()
            if result:
                enc_question = self.cipher.encrypt(question)
                enc_answer = self.cipher.encrypt(answer)
                stored_question, stored_answer = result[1], result[2]
                if enc_question == stored_question and enc_answer == stored_answer:
                    return True
            return False
        except Error as e:
            print(f"Error: {e}")
            return False

    def update_password(self, username, new_password):
        if self.connection is None:
            print("No connection to the database.")
            return
        try:
            cursor = self.connection.cursor()
            enc_username = self.cipher.encrypt(username)
            enc_password = self.cipher.encrypt(new_password)
            cursor.execute("UPDATE ACCOUNTS SET password = %s WHERE username = %s", (enc_password, enc_username))
            self.connection.commit()
            print("Password updated successfully.")
        except Error as e:
            print(f"Error: {e}")
    def populate_user_logs(self):
        if self.connection is None:
            print("No connection to the database.")
            return
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
            SELECT 
                a.username_id,
                a.username,
                u.action,
                u.timestamp 
            FROM 
                USER_LOGS u JOIN accounts a ON u.account_id = a.account_id
            ORDER BY u.timestamp DESC
            LIMIT 50;;
            ''')
            result = cursor.fetchall()
            decrypted_rows = []
            for row in result:
                decrypted_row = tuple(self.cipher.decrypt(value) if isinstance(value, str) else value for value in row)
                decrypted_rows.append(decrypted_row)
            return decrypted_rows
        except Error as e:
            print(f"Error: {e}")
    def add_user_log(self, username, userid, action):
        if self.connection is None:
            print("No connection to the database.")
            return
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                INSERT INTO USER_LOGS 
	                (account_id ,
                    action
                    ) 
                VALUES 
                    ((SELECT account_id FROM accounts WHERE username = %s and username_id = %s), %s);
                """,
                (self.cipher.encrypt(username), self.cipher.encrypt(userid), self.cipher.encrypt(action)))
            self.connection.commit()
            print("User log added successfully.")
        except Error as e:
            print(f"Error: {e}")

    def has_schemas(self):
        if self.connection is None:
            print("No connection to the database.")
            return False

        try:
            cursor = self.connection.cursor()

            # Fetch table names
            cursor.execute("SHOW TABLES")
            tables = cursor.fetchall()

            # Check if all tables are empty
            all_empty = True
            for table in tables:
                table_name = table[0]
                cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
                row_count = cursor.fetchone()[0]
                if row_count > 0:
                    all_empty = False
                    break  # Exit loop early if any table has rows

            cursor.close()
            return all_empty

        except Error as e:
            print(f"Error checking schemas: {e}")
            return False

    def get_order_exist(self, name, bag_type, quantity, deadline_date, priority):
        try:
            cursor = self.connection.cursor()
            cursor.execute(
            '''
            SELECT 
                c.client_name, 
                o.bag_type, 
                o.order_quantity, 
                d.deadline_date, 
                c.client_priority
            FROM 
                CLIENT c
			
            JOIN 
                ORDERS o ON c.client_id = o.client_id
            JOIN 
                DEADLINE d ON c.deadline_id = d.deadline_id
			WHERE 
				c.client_name = %s AND o.bag_type = %s
                AND o.order_quantity = %s AND 
                d.deadline_date = %s AND c.client_priority = %s AND c.client_active = 1 ;
            '''
            , (name, bag_type, quantity, deadline_date, priority))
            result = cursor.fetchall()
            print(result)
            if result:
                return True
            else:
                return False
        except Error as e:
            print(f"Error: {e}")

    def get_order_details(self, client_name, bag_type, deadline_date, client_priority):
        if self.connection is None:
            print("No connection to the database.")
            return None

        try:
            cursor = self.connection.cursor()

            # Encrypt necessary fields
            encrypted_client_name = self.cipher.encrypt(client_name)
            encrypted_bag_type = self.cipher.encrypt(bag_type)

            # Fetch deadline details using a join with the deadline table
            query = """
                   SELECT d.deadline_details
                   FROM ORDERS o
                   JOIN CLIENT c ON o.client_id = c.client_id
                   JOIN DEADLINE d ON c.deadline_id = d.deadline_id
                   WHERE c.client_name = %s 
                     AND o.bag_type = %s
                     AND d.deadline_date = %s
                     AND c.client_priority = %s
               """
            cursor.execute(query, (encrypted_client_name, encrypted_bag_type, deadline_date, client_priority))

            deadline_details_result = cursor.fetchone()

            if deadline_details_result is None:
                print(f"Order not found for: {client_name}, {bag_type}, {deadline_date}, {client_priority}")
                return None

            encrypted_deadline_details = deadline_details_result[0]

            # Decrypt deadline details
            deadline_details = self.cipher.decrypt(encrypted_deadline_details)

            # Return deadline details
            return deadline_details

        except Exception as e:
            print(f"An error occurred while fetching order details: {e}")
            return None

    def close_connection(self):
        if self.connection and self.connection.is_connected():
            self.connection.commit()
            self.connection.close()
            print("Database connection closed")