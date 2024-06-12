import mysql.connector
from mysql.connector import Error
from databases.encrypt import DatabaseAES

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
                FOREIGN KEY (supplier_id) REFERENCES SUPPLIER(supplier_id)
            );

            CREATE TABLE IF NOT EXISTS CLIENT (
                client_id INT AUTO_INCREMENT PRIMARY KEY,
                client_name VARCHAR(256) NOT NULL,
                client_loc VARCHAR(256) NOT NULL,
                client_contact VARCHAR(256) NOT NULL
            );

            CREATE TABLE IF NOT EXISTS DEADLINE (
                deadline_id INT AUTO_INCREMENT PRIMARY KEY,
                deadline_name VARCHAR(256) NOT NULL,
                deadline_details VARCHAR(256) NOT NULL,
                deadline_date DATE NOT NULL
            );

            CREATE TABLE IF NOT EXISTS ORDERS (
                order_id INT AUTO_INCREMENT PRIMARY KEY,
                client_id INT NOT NULL,
                deadline_id INT NOT NULL,
                order_quantity INT NOT NULL,
                order_progress INT NOT NULL,
                labor_allocation INT NOT NULL,
                order_style VARCHAR(256) NOT NULL,
                FOREIGN KEY (client_id) REFERENCES CLIENT(client_id),
                FOREIGN KEY (deadline_id) REFERENCES DEADLINE(deadline_id)
            );

            CREATE TABLE IF NOT EXISTS PRODUCT (
                product_id INT AUTO_INCREMENT PRIMARY KEY,
                order_id INT NOT NULL,
                product_quantity INT NOT NULL,
                product_style VARCHAR(256) NOT NULL,
                product_defectives INT NOT NULL,
                product_cost INT NOT NULL,
                FOREIGN KEY (order_id) REFERENCES ORDERS(order_id)
            );

            CREATE TABLE IF NOT EXISTS SUBCONTRACTOR (
                subcon_id INT AUTO_INCREMENT PRIMARY KEY,
                order_id INT NOT NULL,
                order_quantity INT NOT NULL,
                product_style VARCHAR(256) NOT NULL,
                FOREIGN KEY (order_id) REFERENCES ORDERS(order_id)
            );

            CREATE TABLE IF NOT EXISTS USER_LOGS (
                log_id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT NOT NULL,
                action VARCHAR(256) NOT NULL,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES CLIENT(client_id)
            );

            CREATE TABLE IF NOT EXISTS ACCOUNTS (
                account_id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(256) NOT NULL,
                password VARCHAR(256) NOT NULL
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

            # Encrypting the data before insertion
            encrypted_supplier_name_1 = self.cipher.encrypt('Supplier A')
            encrypted_supplier_name_2 = self.cipher.encrypt('Supplier B')
            encrypted_supplier_loc_1 = self.cipher.encrypt('Location A')
            encrypted_supplier_loc_2 = self.cipher.encrypt('Location B')
            encrypted_supplier_contact_1 = self.cipher.encrypt('Contact A')
            encrypted_supplier_contact_2 = self.cipher.encrypt('Contact B')

            encrypted_material_name_1 = self.cipher.encrypt('Material A')
            encrypted_material_name_2 = self.cipher.encrypt('Material B')
            encrypted_material_type_1 = self.cipher.encrypt('Type A')
            encrypted_material_type_2 = self.cipher.encrypt('Type B')
            encrypted_material_color_1 = self.cipher.encrypt('Color A')
            encrypted_material_color_2 = self.cipher.encrypt('Color B')

            encrypted_client_name_1 = self.cipher.encrypt('Client A')
            encrypted_client_name_2 = self.cipher.encrypt('Client B')
            encrypted_client_loc_1 = self.cipher.encrypt('Client Location A')
            encrypted_client_loc_2 = self.cipher.encrypt('Client Location B')
            encrypted_client_contact_1 = self.cipher.encrypt('Client Contact A')
            encrypted_client_contact_2 = self.cipher.encrypt('Client Contact B')

            encrypted_deadline_name_1 = self.cipher.encrypt('Deadline A')
            encrypted_deadline_name_2 = self.cipher.encrypt('Deadline B')
            encrypted_deadline_details_1 = self.cipher.encrypt('Details A')
            encrypted_deadline_details_2 = self.cipher.encrypt('Details B')

            encrypted_order_style_1 = self.cipher.encrypt('Style A')
            encrypted_order_style_2 = self.cipher.encrypt('Style B')

            encrypted_product_quantity_1 = self.cipher.encrypt('100')
            encrypted_product_quantity_2 = self.cipher.encrypt('200')
            encrypted_product_style_1 = self.cipher.encrypt('Product Style A')
            encrypted_product_style_2 = self.cipher.encrypt('Product Style B')

            encrypted_order_quantity_1 = self.cipher.encrypt('Order Quantity A')
            encrypted_order_quantity_2 = self.cipher.encrypt('Order Quantity B')

            encrypted_user_action_1 = self.cipher.encrypt('Created order')
            encrypted_user_action_2 = self.cipher.encrypt('Updated product')

            encrypted_username = self.cipher.encrypt('admin')
            encrypted_password = self.cipher.encrypt('password')
            encrypted_username1 = self.cipher.encrypt('admin1')
            encrypted_password1 = self.cipher.encrypt('password1')
            # Insert into SUPPLIER
            supplier_sql = '''
            INSERT INTO SUPPLIER (supplier_name, supplier_loc, supplier_contact)
            VALUES (%s, %s, %s), (%s, %s, %s);
            '''
            cursor.execute(supplier_sql, (encrypted_supplier_name_1, encrypted_supplier_loc_1, encrypted_supplier_contact_1, encrypted_supplier_name_2, encrypted_supplier_loc_2, encrypted_supplier_contact_2))

            # Insert into RAW_MATERIAL
            raw_material_sql = '''
            INSERT INTO RAW_MATERIAL (material_name, material_available, material_type, material_color, material_cost, material_stock, material_safety_stock, supplier_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s), (%s, %s, %s, %s, %s, %s, %s, %s);
            '''
            cursor.execute(raw_material_sql, (encrypted_material_name_1, 100, encrypted_material_type_1, encrypted_material_color_1, 50, 200, 20, 1, encrypted_material_name_2, 200, encrypted_material_type_2, encrypted_material_color_2, 60, 300, 30, 2))

            # Insert into CLIENT
            client_sql = '''
            INSERT INTO CLIENT (client_name, client_loc, client_contact)
            VALUES (%s, %s, %s), (%s, %s, %s);
            '''
            cursor.execute(client_sql, (encrypted_client_name_1, encrypted_client_loc_1, encrypted_client_contact_1, encrypted_client_name_2, encrypted_client_loc_2, encrypted_client_contact_2))

            # Insert into DEADLINE
            deadline_sql = '''
            INSERT INTO DEADLINE (deadline_name, deadline_details, deadline_date)
            VALUES (%s, %s, %s), (%s, %s, %s);
            '''
            cursor.execute(deadline_sql, (encrypted_deadline_name_1, encrypted_deadline_details_1, '2024-12-31', encrypted_deadline_name_2, encrypted_deadline_details_2, '2025-01-31'))

            # Insert into ORDERS
            orders_sql = '''
            INSERT INTO ORDERS (client_id, deadline_id, order_quantity, order_progress, labor_allocation, order_style)
            VALUES (%s, %s, %s, %s, %s, %s), (%s, %s, %s, %s, %s, %s);
            '''
            cursor.execute(orders_sql, (1, 1, 10, 0, 10, encrypted_order_style_1, 2, 2, 5, 50, 20, encrypted_order_style_2))

            # Insert into PRODUCT
            product_sql = '''
            INSERT INTO PRODUCT (order_id, product_quantity, product_style, product_defectives, product_cost)
            VALUES (%s, %s, %s, %s, %s), (%s, %s, %s, %s, %s);
            '''
            cursor.execute(product_sql, (1, 5, encrypted_product_style_1, 5, 500, 2, 5, encrypted_product_style_2, 10, 1000))

            # Insert into SUBCONTRACTOR
            subcontractor_sql = '''
            INSERT INTO SUBCONTRACTOR (order_id, order_quantity, product_style)
            VALUES (%s, %s, %s), (%s, %s, %s);
            '''
            cursor.execute(subcontractor_sql, (1, 1, encrypted_product_style_1, 2,1, encrypted_product_style_2))

            # Insert into USER_LOGS
            user_logs_sql = '''
            INSERT INTO USER_LOGS (user_id, action)
            VALUES (%s, %s), (%s, %s);
            '''
            cursor.execute(user_logs_sql, (1, encrypted_user_action_1, 2, encrypted_user_action_2))

            # Insert into ACCOUNTS
            accounts_sql = '''
            INSERT INTO ACCOUNTS (username, password)
            VALUES (%s, %s), (%s, %s);
            '''
            cursor.execute(accounts_sql, (encrypted_username, encrypted_password, encrypted_username1, encrypted_password1))

            self.connection.commit()
            print("Dummy data added successfully.")
        except Error as e:
            print(f"Error: {e}")


    def check_account_login(self, username, password) -> bool:
        if self.connection is None:
            print("No connection to the database.")
            return False

        try:
            cursor = self.connection.cursor()
            enc_username = self.cipher.encrypt(username)
            enc_password = self.cipher.encrypt(password)
            print(enc_username)
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
            if result and new_password == confirm_password:
                sql_script = "UPDATE ACCOUNTS SET password = %s WHERE username = %s"
                cursor.execute(sql_script, (self.cipher.encrypt(new_password), enc_username))
                self.connection.commit()
                print("Password updated successfully.")
            else:
                print("Invalid credentials or passwords do not match.")
        except Error as e:
            print(e)
    
    def populate_client(self):
        if self.connection is None:
            print("No connection to the database.")
            return
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM CLIENT")
            rows = cursor.fetchall()

            for row in rows:
                
                encrypted_name = row[1]
                encrypted_loc = row[2]
                encrypted_contact = row[3]
                
                # Decrypt the encrypted columns
                decrypted_name = self.cipher.decrypt(encrypted_name)
                decrypted_loc = self.cipher.decrypt(encrypted_loc)
                decrypted_contact = self.cipher.decrypt(encrypted_contact)
                
                
                # Create a dictionary for better readability
                decrypted_row = {
                    'name': decrypted_name,
                    'location': decrypted_loc,
                    'contact': decrypted_contact
                }
                
                # Print the decrypted row
                print(decrypted_row)
        except Error as e:
            print(f"Error: {e}")
    def close_connection(self):
        if self.connection and self.connection.is_connected():
            self.connection.commit()
            self.connection.close()
            print("Database connection closed")
