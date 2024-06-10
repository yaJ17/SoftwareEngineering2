from databases.connect import DatabaseManager
from logic.login_module import run_login
# Usage example
if __name__ == "__main__":
    db_manager = DatabaseManager('localhost', 'root', 'admin')
    db_manager.connect_to_database()
    db_manager.create_schema()
    db_manager.add_dummy_data()
    db_manager.close_connection()
