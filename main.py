from databases.database import DatabaseManager
from logic.login_module import run_login
from Crypto.Random import get_random_bytes

# Usage example
if __name__ == "__main__":
    key = b'[Xd\xee[\\\x90\x8c\xc8t\xba\xe4\xe0\rR\x87\xe6\xbe\xce\x8a\x02lC6\xf7G\x15O\xca\x182\xd0'
    db_manager = DatabaseManager('localhost', 'root', 'admin', key)
    db_manager.connect_to_database()
    db_manager.create_schema_and_tables()
    db_manager.add_dummy_data()
    # db_manager.check_account_login('admin', 'password')
    #db_manager.populate_client()
    #db_manager.set_account_password('admin', 'password','newpass', 'newpass')
    db_manager.close_connection()
