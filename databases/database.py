import mysql.connector
import re
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
                account_id INT NOT NULL,
                action VARCHAR(256) NOT NULL,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (account_id) REFERENCES accounts(account_id),
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
                ("Bitoy Supplier", "Pasay City", "09512949230"),
                ("Sweedny Silk Manufacturer", "Marikina", "09232592341"),
                ("Supplier C", "Location C", "09123784821"),
                ("Supplier D", "Location D", "09281283121"),
                ("Supplier E", "Location E", "Contact E")
            ]
            cursor.executemany("INSERT INTO SUPPLIER (supplier_name, supplier_loc, supplier_contact) VALUES (%s, %s, %s)", suppliers)

            # Insert dummy data for RAW_MATERIAL
            raw_materials = [
                ("Material A", 100, "Type A", "Color A", 50, 200, 20, 1),
                ("Material B", 200, "Type B", "Color B", 60, 300, 30, 2),
                ("Material C", 150, "Type C", "Color C", 70, 250, 25, 3),
                ("Material D", 180, "Type D", "Color D", 80, 280, 28, 4),
                ("Material E", 220, "Type E", "Color E", 90, 320, 32, 5)
            ]
            cursor.executemany("INSERT INTO RAW_MATERIAL (material_name, material_available, material_type, material_color, material_cost, material_stock, material_safety_stock, supplier_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", raw_materials)

            # Insert dummy data for DEADLINE
            deadlines = [
                ("Deadline A", "Details A", "2024-12-31"),
                ("Deadline B", "Details B", "2024-11-30"),
                ("Deadline C", "Details C", "2024-10-31"),
                ("Deadline D", "Details D", "2024-09-30"),
                ("Deadline E", "Details E", "2024-08-31")
            ]
            cursor.executemany("INSERT INTO DEADLINE (deadline_name, deadline_details, deadline_date) VALUES (%s, %s, %s)", deadlines)

            # Insert dummy data for CLIENT
            clients = [
                ("Client A", "Location A", "Contact A", 1, 1),
                ("Client B", "Location B", "Contact B", 2, 2),
                ("Client C", "Location C", "Contact C", 3, 3),
                ("Client D", "Location D", "Contact D", 4, 4),
                ("Client E", "Location E", "Contact E", 5, 5)
            ]
            cursor.executemany("INSERT INTO CLIENT (client_name, client_loc, client_contact, deadline_id, client_priority) VALUES (%s, %s, %s, %s, %s)", clients)

            # Insert dummy data for ORDERS
            orders = [
                (1, 100, 0, "Bag Type A"),
                (2, 200, 10, "Bag Type B"),
                (3, 150, 20, "Bag Type C"),
                (4, 180, 30, "Bag Type D"),
                (5, 220, 40, "Bag Type E")
            ]
            cursor.executemany("INSERT INTO ORDERS (client_id, order_quantity, order_progress, bag_type) VALUES (%s, %s, %s, %s)", orders)

            # Insert dummy data for BAG_COMPONENT
            bag_components = [
                ("Component A", "Labor A", "In Progress", "Bag Type A", 1),
                ("Component B", "Labor B", "Completed", "Bag Type B", 2),
                ("Component C", "Labor C", "Not Started", "Bag Type C", 3),
                ("Component D", "Labor D", "In Progress", "Bag Type D", 4),
                ("Component E", "Labor E", "Completed", "Bag Type E", 5)
            ]
            cursor.executemany("INSERT INTO BAG_COMPONENT (bag_component, labor_allocation, progress, bag_type, client_id) VALUES (%s, %s, %s, %s, %s)", bag_components)

            # Insert dummy data for PRODUCT
            products = [
                (1, 100, "Bag Type A", 0, 500, 700),
                (2, 200, "Bag Type B", 5, 600, 800),
                (3, 150, "Bag Type C", 10, 550, 750),
                (4, 180, "Bag Type D", 2, 580, 780),
                (5, 220, "Bag Type E", 3, 620, 820)
            ]
            cursor.executemany("INSERT INTO PRODUCT (order_id, product_quantity, bag_type, product_defectives, product_cost, product_price) VALUES (%s, %s, %s, %s, %s, %s)", products)

            # Insert dummy data for SUBCONTRACTOR
            subcontractors = [
                (1, 50, "Bag Type A"),
                (2, 60, "Bag Type B"),
                (3, 70, "Bag Type C"),
                (4, 80, "Bag Type D"),
                (5, 90, "Bag Type E")
            ]
            cursor.executemany("INSERT INTO SUBCONTRACTOR (order_id, order_quantity, bag_type) VALUES (%s, %s, %s)", subcontractors)

            # Insert dummy data for ACCOUNTS
            accounts = [
                ("user1", "username1", "password1", "Question 1", "Answer 1"),
                ("user2", "username2", "password2", "Question 2", "Answer 2"),
                ("user3", "username3", "password3", "Question 3", "Answer 3"),
                ("user4", "username4", "password4", "Question 4", "Answer 4"),
                ("user5", "username5", "password5", "Question 5", "Answer 5")
            ]
            cursor.executemany("INSERT INTO ACCOUNTS (username_id, username, password, secret_question, secret_answer) VALUES (%s, %s, %s, %s, %s)", accounts)

            # Insert dummy data for USER_LOGS
            user_logs = [
                (1, "Login"),
                (2, "Logout"),
                (3, "Login"),
                (4, "Logout"),
                (5, "Login")
            ]
            cursor.executemany("INSERT INTO USER_LOGS (account_id, action) VALUES (%s, %s)", user_logs)

            # Insert dummy data for TRANSACTION_HISTORY
            transaction_history = [
                (1, "Transaction A"),
                (2, "Transaction B"),
                (3, "Transaction C"),
                (4, "Transaction D"),
                (5, "Transaction E")
            ]
            cursor.executemany("INSERT INTO TRANSACTION_HISTORY (account_id, action) VALUES (%s, %s)", transaction_history)

            self.connection.commit()
            print("Dummy data inserted successfully.")
        except Error as e:
            print(f"Error: {e}")


    

    #validate login
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
                # decrypted_name = self.cipher.decrypt(encrypted_name)
                # decrypted_loc = self.cipher.decrypt(encrypted_loc)
                # decrypted_contact = self.cipher.decrypt(encrypted_contact)
                
                
                # Create a dictionary for better readability
                decrypted_row = {
                    'name': client_name,
                    'bag types': bag_types,
                    'deadline': deadline,
                    'progress': progress
                }
                
                # Print the decrypted row
                print(decrypted_row)
        except Error as e:
            print(f"Error: {e}")

    #EDIT CLIENT DETAILS
    def set_client_detail(self, client_id, name, loc,contact):
        if self.connection is None:
            print("No connection to the database.")
            return
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                SELECT client_id FROM client WHERE client_id = %s;
            ''',(client_id,))
            result = cursor.fetchone()
            print(result)
            if result:
                if  result[0] == client_id:
                    sql_script = "UPDATE CLIENT SET client_name=%s, client_loc=%s, client_contact=%s WHERE client_id = %s"
                    cursor.execute(sql_script, (name,loc,contact,client_id))
                    print("Details updated successfully.")
                else:
                    print("Invalid client_id.")
        except Error as e:
            print(f"Error: {e}")

    '''
        ADDITION OF CLIENT
    '''
    def add_client(self, name, loc, contact, deadline_id):
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
                deadline_id
                )
            VALUES 
            (%s,%s,%s,%s);
            '''
            ,(name, loc, contact, deadline_id))
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
                O.order_id,
                O.bag_type,
                O.order_progress
            FROM 
                ORDERS O
            '''
            )
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            return rows
        except Error as e:
            print(f"Error: {e}")
    ''' 
            UPDATE CLIENT ORDER
                                                    '''   
    def set_order(self, order_id, quantity, progress, bag_type):
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
                    cursor.execute("UPDATE ORDERs SET order_quantity=%s, order_progress =%s, bag_type =%s WHERE order_id = %s",
                                    (quantity,progress,bag_type,order_id))
                    print("Details updated successfully.")
                else:
                    print("Invalid order.")

        except Error as e:
            print(f"Error: {e}")

    def add_order(self, client_id, order_quantity, order_progress, bag_type):
        if self.connection is None:
            print("No connection to the database.")
            return
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                INSERT INTO ORDERS(
                client_id,
                order_quantity, 
                order_progress, 
                bag_type
                )
                VALUES (%s,%s,%s,%s)
            ''', (client_id, order_quantity, order_progress, bag_type))
        except Error as e:
            print(f"Error: {e}")

    '''
        POPULATE THE BAG COMPONENTS ACCORDING TO BAG TYPE
        O.bag_type is for testing purposes only -> can be excluded
    '''
    def populate_bag_components(self):
        if self.connection is None:
            print("No connection to the database.")
            return
        try:
            cursor = self.connection.cursor()
            cursor.execute(
            '''
            SELECT 
                B.bag_component,
                B.labor_allocation,
                B.progress,
                O.bag_type
            FROM 
                BAG_COMPONENT B
            JOIN 
                ORDERS O ON O.client_id = B.client_id
            WHERE
                O.bag_type = B.bag_type;
            '''
            )
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        except Error as e:
            print(f"Error: {e}")


    ''' 
            UPDATE BAG COMPONENT ORDER
                                                    '''   
    def set_bag_component(self,bag_component_id, bag_component, labor_allocation, progress, bag_type):
        if self.connection is None:
            print("No connection to the database.")
            return
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                SELECT bag_component_id FROM bag_component WHERE bag_component_id = %s
            ''', (bag_component_id,))
            result = cursor.fetchone()
            if result:
                if result[0] == bag_component_id:
                    cursor.execute("UPDATE bag_component SET bag_component =%s, labor_allocation =%s,progress =%s, bag_type =%s WHERE bag_component_id = %s",
                                    (bag_component,labor_allocation,progress,bag_type, bag_component_id ))
                    print("Details updated successfully.")
                else:
                    print("Invalid order.")

        except Error as e:
            print(f"Error: {e}")
    
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
                print(row)
        except Error as e:
            print(f"Error: {e}")

    #FOR EDITING THE DEADLINE NAME, DETAIL, DATE, STATUS

    def populate_deadline_by_week(self, start_date, end_date):
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
                deadline_date BETWEEN %s AND %s;
            ''',
            (start_date, end_date)
            )
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        except Error as e:
            print(f"Error: {e}")
    def populate_deadline(self) -> tuple:
        cursor = self.connection.cursor()
        cursor.execute("SELECT deadline_name, deadline_details, deadline_date FROM DEADLINE WHERE deadline_date >=CURDATE() ORDER BY deadline_date ASC")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        return rows
    def set_deadline(self, deadline_id, deadline_name, deadline_details, deadline_date,deadline_active):
        if self.connection is None:
            print("No connection to the database.")
            return
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                SELECT deadline_id FROM deadline WHERE deadline_id = %s
            ''', (deadline_id,))
            result = cursor.fetchone()
            if result:
                if result[0] == deadline_id:
                    cursor.execute("UPDATE deadline SET deadline_name =%s, deadline_details=%s,  deadline_date =%s, deadline_active=%s WHERE deadline_id =%s",
                                    (deadline_name, deadline_details, deadline_date, deadline_active, deadline_id))
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
            cursor.execute("INSERT INTO deadline(deadline_name, deadline_details, deadline_date) VALUES(%s,%s,%s)", (name,details,date))
        except Error as e:
            print(f"Error: {e}")
    '''
                    POPULATE raw material INVENTORY
                                                                '''
    def void_deadline(self, deadline_id):
        if self.connection is None:
            print("No connection to the database.")
            return
        try:
            cursor = self.connection.cursor()
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
                S.supplier_name,
                S.supplier_contact
            FROM 
                RAW_MATERIAL R
            JOIN 
                SUPPLIER S ON R.supplier_id = S.supplier_id;
            '''
            )
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        except Error as e:
            print(f"Error: {e}")

    def set_raw_material(self, material_id, name,stock, safety_stock, cost, supplier_name, supplier_contact):
        if self.connection is None:
            print("No connection to the database.")
            return
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                SELECT material_id FROM raw_material WHERE material_id = %s
            ''', (material_id,))
            result = cursor.fetchone()
            if result:
                if result[0] == material_id:
                    sql_script = '''
                    UPDATE RAW_MATERIAL SET
                        material_name = %s,
                        material_stock =%s,
                        material_safety_stock = %s,
                        material_cost = %s
                    WHERE material_id = %s;

                    '''
                    cursor.execute(sql_script, 
                    (name,stock,safety_stock,cost,material_id))
                    sql_script = '''
                    UPDATE SUPPLIER SET
                        supplier_name = %s,
                        supplier_contact =%s
                    WHERE supplier_id = (SELECT supplier_id FROM raw_material WHERE material_id = %s);
                    '''
                    cursor.execute(sql_script, (supplier_name,supplier_contact, material_id))
                    print("Details updated successfully.")
                else:
                    print("Invalid order.")

        except Error as e:
            print(f"Error: {e}")
    def add_raw_material(self, name,stock,available,materialtype, safety_stock, cost, supplier_id, color):
        if self.connection is None:
            print("No connection to the database.")
            return
        try:
            cursor = self.connection.cursor()
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
            (%s,%s,%s,%s,%s,%s,%s,%s);
            '''
            ,(name,available,materialtype, color, cost, stock, safety_stock,supplier_id))
        except Error as e:
            print(f"Error: {e}")
    
    def void_raw_material(self, material_id):
        if self.connection is None:
            print("No connection to the database.")
            return
        try:
            cursor = self.connection.cursor()
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
                    (product_price- product_cost) as profit
                FROM 
                    PRODUCT;
            '''
            )
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        except Error as e:
            print(f"Error: {e}")
    
    '''
                    UPDATE PRODUCT INVENTORY
                                                                '''
    def set_product(self, product_id, bag_type, quantity, defective, cost, price):
        if self.connection is None:
            print("No connection to the database.")
            return
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                SELECT product_id FROM product WHERE product_id = %s
            ''', (product_id,))
            result = cursor.fetchone()
            if result:
                if result[0] == product_id:
                    sql_script = '''
                    UPDATE product SET
                        bag_type = %s,
                        product_quantity= %s,
                        product_defectives= %s,
                        product_cost= %s,
                        product_price= %s
                    WHERE 
                        product_id = %s;

                    '''
                    cursor.execute(sql_script, (bag_type, quantity,defective,cost,price,product_id))
                    print("Details updated successfully.")
                else:
                    print("Invalid order.")

        except Error as e:
            print(f"Error: {e}")
    def add_product(self, order_id, product_quantity, bag_type,product_defectives,product_cost,product_price):
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
            ,(order_id, product_quantity, bag_type,product_defectives,product_cost,product_price))
        except Error as e:
            print(f"Error: {e}")
    
    def void_product(self, product_id):
        if self.connection is None:   
            print("No connection to the database.")
            return
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT  product_active FROM product WHERE product_id = %s", (product_id,))
            result = cursor.fetchone()
            if result is not None:
                material_active = result[0]  
                reversed_product_active = 0 if material_active == 1 else 1 
                sql_script = "UPDATE product SET  product_active = %s WHERE product_id = %s"
                cursor.execute(sql_script, (reversed_product_active, product_id))
        except Error as e:
            print(f"Error: {e}")

    def add_account(self, username, password, question, answer):
        if self.connection is None:
            print("No connection to the database.")
            return
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT RIGHT(MAX(username_id), LENGTH(MAX(username_id)) - 4) FROM ACCOUNTS")
            last_id = cursor.fetchone()[0]
            if last_id:
                new_id = "RXAC"+ str(int(last_id) + 1)
            else:
                new_id = "RXAC1"
            cursor.execute("SELECT username FROM ACCOUNTS WHERE username = %s", (username,))
            username_exist = cursor.fetchone()
            if username_exist is None:
                #r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]+$" -> to remove 8 char long
                if re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$", password):
                    cursor.execute("INSERT INTO ACCOUNTS (username_id, username, password, secret_question, secret_answer) VALUES (%s,%s, %s,%s,%s);", (new_id, username, password,question,answer))
                else:
                    print("wrong password")
        except Error as e:
            print(f"Error: {e}")
    
    
    def close_connection(self):
        if self.connection and self.connection.is_connected():
            self.connection.commit()
            self.connection.close()
            print("Database connection closed")
