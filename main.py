from databases.connect import DatabaseManager
from logic.login_module import run_login
# Usage example
if __name__ == "__main__":
    db_manager = DatabaseManager('localhost', 'root', 'admin')
    db_manager.connect_to_database()
    db_manager.create_schema_and_tables()
    #db_manager.add_dummy_data()
    db_manager.check_account_login('admin', 'admin')
    db_manager.close_connection()
