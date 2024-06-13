from databases.database import DatabaseManager
from logic.login_module import run_login
from Crypto.Random import get_random_bytes

# Usage example
if __name__ == "__main__":
    key = b'[Xd\xee[\\\x90\x8c\xc8t\xba\xe4\xe0\rR\x87\xe6\xbe\xce\x8a\x02lC6\xf7G\x15O\xca\x182\xd0'
    db_manager = DatabaseManager('localhost', 'root', 'admin', key)
    db_manager.connect_to_database()
    db_manager.create_schema_and_tables()
    #db_manager.add_dummy_data()
    # db_manager.check_account_login('admin', 'password')
    #db_manager.populate_accounts()
    #db_manager.set_account_password('user1', 'password1','newpass', 'newpass')
    #db_manager.set_deadline(1,'pogi','new details for deadline','2024-06-13',True)
    #db_manager.set_raw_material(2,'new mememe name', 10, 100, 50,'new 123123123supplier', 123213)
    #db_manager.populate_deadline_by_month()
    #db_manager.populate_raw_materials()
    db_manager.update_product(1,'D',5000,1000, 250, 350)
    db_manager.close_connection()
